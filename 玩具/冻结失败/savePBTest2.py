import tensorflow as tf
import os
from tensorflow.python.framework import graph_util
import shutil

pb_file_path = "./"
saved_model_dir = './savemodel/'

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
        constant_graph = graph_util.convert_variables_to_constants(sess, sess.graph_def, ['op_to_store'])
     
        # 测试 OP
        feed_dict = {x: 10, y: 3}
        print(sess.run(op, feed_dict))
     
        # 写入序列化的 PB 文件
        with tf.gfile.FastGFile(pb_file_path+'model.pb', mode='wb') as f:
            f.write(constant_graph.SerializeToString())
     
        # INFO:tensorflow:Froze 1 variables.
        # Converted 1 variables to const ops.
        # 31
        
        
        # 官网有误，写成了 saved_model_builder
        if os.path.exists(pb_file_path+'savemodel'): 
            shutil.rmtree(pb_file_path+'savemodel') 
        builder = tf.saved_model.builder.SavedModelBuilder(pb_file_path+'savemodel')
        # 构造模型保存的内容，指定要保存的 session，特定的 tag, 
        # 输入输出信息字典，额外的信息
        builder.add_meta_graph_and_variables(sess,
                                           ['cpu_server_1'])
     
     
    # 添加第二个 MetaGraphDef 
    #with tf.Session(graph=tf.Graph()) as sess:
    #  ...
    #  builder.add_meta_graph([tag_constants.SERVING])
    #...
     
    builder.save()  # 保存 PB 模型

def loadModel():
    with tf.Session(graph=tf.Graph()) as sess:
        tf.saved_model.loader.load(sess, ['cpu_server_1'], pb_file_path+'savemodel')
        sess.run(tf.global_variables_initializer())
     
        input_x = sess.graph.get_tensor_by_name('x:0')
        input_y = sess.graph.get_tensor_by_name('y:0')
     
        op = sess.graph.get_tensor_by_name('op_to_store:0')
     
        ret = sess.run(op,  feed_dict={input_x: 5, input_y: 5})
        print(ret)
# 只需要指定要恢复模型的 session，模型的 tag，模型的保存路径即可,使用起来更加简单


def saveModel2():
    builder = tf.saved_model.builder.SavedModelBuilder(saved_model_dir)
    # x 为输入tensor, keep_prob为dropout的prob tensor 
    inputs = {'input_x': tf.saved_model.utils.build_tensor_info(x), 
                'keep_prob': tf.saved_model.utils.build_tensor_info(keep_prob)}

    # y 为最终需要的输出结果tensor 
    outputs = {'output' : tf.saved_model.utils.build_tensor_info(y)}

    signature = tf.saved_model.signature_def_utils.build_signature_def(inputs, outputs, 'test_sig_name')

    builder.add_meta_graph_and_variables(sess, ['test_saved_model'], {'test_signature':signature})
    builder.save()

def  loadModel2():
    signature_key = 'test_signature'
    input_key = 'input_x'
    output_key = 'output'

    meta_graph_def = tf.saved_model.loader.load(sess, ['test_saved_model'], saved_model_dir)
    # 从meta_graph_def中取出SignatureDef对象
    signature = meta_graph_def.signature_def

    # 从signature中找出具体输入输出的tensor name 
    x_tensor_name = signature[signature_key].inputs[input_key].name
    y_tensor_name = signature[signature_key].outputs[output_key].name

    # 获取tensor 并inference
    x = sess.graph.get_tensor_by_name(x_tensor_name)
    y = sess.graph.get_tensor_by_name(y_tensor_name)

    # _x 实际输入待inference的data
    sess.run(y, feed_dict={x:_x})


if __name__ == "__main__":
    saveModel()
    loadModel()

    # saveModel2()
    # loadModel2()