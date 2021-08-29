#coding:utf-8
import jieba
from collections import Counter # 次數統計
from PIL import Image # 圖片轉array陣列
import matplotlib.pyplot as plt
import numpy
from wordcloud import STOPWORDS,WordCloud


news ="""
今天新增的13例本土病例有6例男性、7例女性，年齡介於未滿5歲至50多歲，發病日介於今(2021)年8/16日至8/28日。個案分布為新北市11例、台北市2例；而新北市三峽家庭群聚總共10人感染，感染源為確診的大遠百員工，其中9例為已知感染源，皆為居隔期檢出的陽性者，陳時中說明，這10人都是同住家人，在居住上比較擁擠，所以整個家庭都受感染，共有一個小孩沒被感染，其它從2歲到4、50歲的人都遭感染。另有4例關聯不明，將持續進行疫情調查。
"""

# 設定分詞資料庫
# https://raw.githubusercontent.com/fxsjy/jieba/master/extra_dict/dict.txt.big 右鍵另存放目錄下
jieba.set_dictionary('sample/intel.txt')

# 將自己常用的詞加入字典
# jieba.load_userdict('finance_dict.txt')

# 新增及刪除常用詞
jieba.add_word('英特爾') # 加入英特爾
jieba.add_word('美元') # 加入英特爾
jieba.del_word('元') # 刪除電風扇

# 斷句方式
# # 用jieba.lcut(text, cut_all=False)直接返回list
# segs = jieba.cut(news, cut_all=True) # 全切模式 切的很碎
# segs = jieba.cut(news, cut_all=False) # 預設模式
seg_list = jieba.lcut(news, cut_all=False) # lcut直接返回list

# 統計分詞出現次數
dictionary = Counter(seg_list)

# 移除停用詞
stopword = [' ', '，', '（', '）', '...', '。', '「', '」']  # 定義停用詞
[dictionary.pop(x, None) for x in stopword] # 存字典裡刪除停用詞

# 產生文字雲

# 格式設定
font_path = 'font/HanyiSentyBubbleTea.ttf' # 設定字體格式
mask = numpy.array(Image.open('picture/alice_mask.png')) # 遮罩
# mask=(mask==0)*255 # 把舉證等於0的地方變成255 原本有數字的地方變0


stopwords = set(STOPWORDS)
stopwords.add("said")
wc = WordCloud(background_color="white", max_words=2000,mask=mask,
font_path=font_path,stopwords=stopwords, contour_width=3, contour_color='steelblue')

# wc = wordcloud.WordCloud(background_color='white',
#                          margin=2, # 文字間距
#                          mask=mask, # 遮罩 有用的話則無視設定長寬
#                          font_path=font_path, # 設定字體
#                          max_words=200, # 取多少文字在裡面
#                          width=1080, height=720, # 長寬解析度
#                          relative_scaling=0.5 # 詞頻與詞大小關聯性
#                          )
# 生成文字雲
wc.generate_from_frequencies(dictionary) # 吃入次數字典資料

# 輸出
wc.to_file('my_wordcloud.png')

# 顯示文字雲
plt.imshow(wc)