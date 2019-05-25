import os
import sys
import numpy as np
import tensorflow as tf
from tensorflow.python.framework import graph_util
from tensorflow.python.platform import gfile

pb_file_path = "./ "
logdir='./'

#------------------------------------------------------------------------------
def saveModel(): 
    with tf.Session(graph=tf.Graph()) as sess:
        x = tf.placeholder(tf.int32, name='x')
        y = tf.placeholder(tf.int32, name='y')
        b = tf.Variable(1, name='b')
        xy = tf.multiply(x, y)
        # 这里的输出需要加上name属性
        op = tf.add(xy, b, name='op_to_store')
     
        sess.run(tf.global_variables_initializer())
     
        # convert_variables_to_constants 需要指定output_node_names，list()，可以多个
        constant_graph = graph_util.convert_variables_to_constants(\
            sess, sess.graph_def, ['op_to_store'])
     
        # 测试 OP
        feed_dict = {x: 10, y: 3}
        print(sess.run(op, feed_dict))
     
        # 写入序列化的 PB 文件
        with tf.gfile.FastGFile(pb_file_path+'model.pb', mode='wb') as f:
            f.write(constant_graph.SerializeToString())   

def loadModel():
    sess = tf.Session()
    with gfile.FastGFile(pb_file_path+'model.pb', 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        sess.graph.as_default()
        tf.import_graph_def(graph_def, name='') # 导入计算图
     
    # 需要有一个初始化的过程    
    sess.run(tf.global_variables_initializer())
     
    # 需要先复原变量
    print(sess.run('b:0'))
     
    # 输入
    input_x = sess.graph.get_tensor_by_name('x:0')
    input_y = sess.graph.get_tensor_by_name('y:0')
     
    op = sess.graph.get_tensor_by_name('op_to_store:0')
     
    ret = sess.run(op,  feed_dict={input_x: 5, input_y: 5})
    print(ret)

#------------------------------------------------------------------------------
def saveModel2():
    with tf.variable_scope('conv'):
        w=tf.get_variable('w',[2,2],tf.float32,initializer=tf.random_normal_initializer)
        b=tf.get_variable('b',[2],tf.float32,initializer=tf.random_normal_initializer)

    sess=tf.InteractiveSession()

    tf.global_variables_initializer().run() # 初始化所有变量

    # tf.train.write_graph(tf.get_default_graph(),logdir,'expert-graph.pb',False)

    constant_graph = graph_util.convert_variables_to_constants(sess, sess.graph_def, ["conv/w"])
    with tf.gfile.FastGFile(logdir+'expert-graph.pb', mode='wb') as f:
        f.write(constant_graph.SerializeToString())


    sess.close()

def loadModel2():
    output_graph_path = logdir+'expert-graph.pb'
    with tf.Session() as sess:
        # with tf.gfile.FastGFile(output_graph_path, 'rb') as f:
        #     graph_def = tf.GraphDef()
        #     graph_def.ParseFromString(f.read())
        #     sess.graph.as_default()
        #     tf.import_graph_def(graph_def, name='')
        tf.global_variables_initializer().run()
        output_graph_def = tf.GraphDef()
        with open(output_graph_path, "rb") as f:
            output_graph_def.ParseFromString(f.read())
            _ = tf.import_graph_def(output_graph_def, name="")

        input_x = sess.graph.get_tensor_by_name("conv/w:0")
        print(input_x.eval())

        output = sess.graph.get_tensor_by_name("conv/b:0")
        print(output.eval())

#------------------------------------------------------------------------------
def saveModel3():
    placeholder = tf.placeholder(name='input', dtype=tf.float32,
                                 shape=[None, 28* 28* 1])
    # tf.train.write_graph(tf.get_default_graph(),logdir,'expert-graph.pb',False)
    # constant_graph = graph_util.convert_variables_to_constants(sess, sess.graph_def, ["conv/w"])   
    constant_graph = tf.get_default_graph().as_graph_def()
    with tf.gfile.FastGFile(logdir+'expert-graph.pb', mode='wb') as f:
        f.write(constant_graph.SerializeToString())

def loadModel3():
    output_graph_path = logdir+ "expert-graph.pb"
    with tf.Session() as sess:
        # with tf.gfile.FastGFile(output_graph_path, 'rb') as f:
        #     graph_def = tf.GraphDef()
        #     graph_def.ParseFromString(f.read())
        #     sess.graph.as_default()
        #     tf.import_graph_def(graph_def, name='')
        tf.global_variables_initializer().run()
        output_graph_def = tf.GraphDef()
        with open(output_graph_path, "rb") as f:
            output_graph_def.ParseFromString(f.read())
            _ = tf.import_graph_def(output_graph_def, name="")

        input_x = sess.graph.get_tensor_by_name("input:0")
        print(input_x)
        y=input_x

        out=sess.run(y,{input_x:np.random.random([1,28*28])})
        print(out[:10])

#------------------------------------------------------------------------------
if __name__ == "__main__":
    # saveModel()
    # loadModel()

    saveModel2()
    loadModel2()

    saveModel3()
    loadModel3()

