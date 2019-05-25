import os
from os import path
from wordcloud import WordCloud
import jieba
from scipy.misc import imread
import matplotlib.image as mpimg # mpimg 用于读取图片
import matplotlib.pyplot as plt

fontPath = "./fort/simfang.ttf"

def jiebaclearText(text):
    mywordlist = []
    seg_list = jieba.cut(text, cut_all=False)
    liststr="/ ".join(seg_list)
    f_stop = open("stopwords1893.txt","rb")
    try:
        f_stop_text = str(f_stop.read(),encoding="utf-8")

        #f_stop_text=unicode(f_stop_text,'gbk')
    finally:
        f_stop.close( )
    f_stop_seg_list=f_stop_text.split('\n')
    for myword in liststr.split('/'):
        if not(myword.strip() in f_stop_seg_list) and len(myword.strip())>1:
            mywordlist.append(myword)
    return ''.join(mywordlist)
 

# Read the whole text.
text = str(open('test.txt',"rb").read(),encoding="utf-8")
# back_coloring = imread("123.png")# 设置背景图片

# # Generate a word cloud image
# wordcloud = WordCloud(font_path=fontPath,  # 设置字体
#                background_color="white",  # 背景颜色
#                max_words=1000,  # 词云显示的最大词数
#                mask=back_coloring,  # 设置背景图片
#                max_font_size=80,  # 字体最大值
#                random_state=40,
#                width=1000, height=860, margin=2,# 设置图片默认的大小,但是如果使用背景图片的话,那么保存的图片大小将会按照其大小保存,margin为词语边缘距离
#                ).generate(text)

# # Display the generated image:
# # the matplotlib way:

# plt.rcParams['savefig.dpi'] = 500 #图片像素
# plt.rcParams['figure.dpi'] = 500 #分辨率
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.savefig("1.png",dpi = 300)

text = jiebaclearText(text)
back_coloring = imread("appleCut.png")
wordcloud = WordCloud(font_path=fontPath,  # 设置字体
               background_color="rgba(255, 255, 204, 0)",  # 背景颜色
               max_words=5000,  # 词云显示的最大词数
               mask=back_coloring,  # 设置背景图片
               max_font_size=40,  # 字体最大值
               random_state=60,
               width=960, height=540, margin=2,# 设置图片默认的大小,但是如果使用背景图片的话,那么保存的图片大小将会按照其大小保存,margin为词语边缘距离
               ).generate(text)
# lower max_font_size
#wordcloud = WordCloud(max_font_size=40).generate(text)
# tmp = mpimg.imread('1.jpg')
# plt.imshow(tmp)
plt.rcParams['savefig.dpi'] = 500 #图片像素
plt.rcParams['figure.dpi'] = 500 #分辨率
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.gca().xaxis.set_major_locator(plt.NullLocator()) 
plt.gca().yaxis.set_major_locator(plt.NullLocator()) 
plt.subplots_adjust(top=1,bottom=0,left=0,right=1,hspace=0,wspace=0) 
plt.margins(0,0)
plt.savefig("2.png",dpi = 500)
plt.show()

# The pil way (if you don't have matplotlib)
# image = wordcloud.to_image()
# image.show()