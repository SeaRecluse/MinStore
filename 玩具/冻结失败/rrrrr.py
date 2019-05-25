import os
import sys
import numpy as np
import tensorflow as tf
from tensorflow.python.framework import graph_util
from tensorflow.python.platform import gfile

def saveModel(): 
    with tf.Session(graph=tf.Graph()) as sess:
        x = tf.placeholder(tf.string, name='x')#x
        y= tf.add(x,"", name='y')

        sess.run(tf.global_variables_initializer())
     
        # convert_variables_to_constants 需要指定output_node_names，list()，可以多个

        constant_graph = graph_util.convert_variables_to_constants(\
            sess, sess.graph_def, ['y'])
        # 测试 OP
        feed_dict = {x: "oooooooooooooo"}
        print(sess.run(y, feed_dict))
     
        # 写入序列化的 PB 文件
        with tf.gfile.FastGFile('model.pb', mode='wb') as f:
            f.write(constant_graph.SerializeToString())   

def loadModel():
    sess = tf.Session()
    with gfile.FastGFile('model.pb', 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        sess.graph.as_default()
        tf.import_graph_def(graph_def, name='') # 导入计算图

    # tensor_node_list = [tensor for tensor in tf.get_default_graph().as_graph_def().node]
    # for tensor_node in tensor_node_list:
    #      print(tensor_node.name)
    #      print(tensor_node.op,"\n")
     
    # 需要有一个初始化的过程    
    sess.run(tf.global_variables_initializer())
     
    input_x = sess.graph.get_tensor_by_name('x:0')
    output_y = sess.graph.get_tensor_by_name('y:0')
    test_op_1 = sess.run(output_y,  feed_dict={input_x:"999999999999"})   
    print(test_op_1)

    test_op_1 = sess.run(output_y,  feed_dict={input_x:"777777777777777"})   
    print(test_op_1)


#------------------------------------------------------------------------------
if __name__ == "__main__":
    saveModel()
    loadModel()

