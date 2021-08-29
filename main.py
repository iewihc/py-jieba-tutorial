import jieba

samples = ["今天下雨我騎車差點摔倒了好在我一把把把住了","吃檸檬吧檸檬熟了酸爆"]

print("---精準模式")
for sentence in samples:
    seg_list = jieba.cut(sentence)
    print('/'.join(seg_list))
print("---")

print("---全模式")
for sentence in samples:
    seg_list = jieba.cut(sentence,cut_all=True)
    print('/'.join(seg_list))
print("---")


print("---搜尋引擎模式")
for sentence in samples:
    seg_list = jieba.cut_for_search(sentence)
    print('/'.join(seg_list))
print("---")

# 預期"陳其邁"，但被切分為"陳/其邁"了
news ="感謝陳其邁副院長費心督導，對於年假期間各防疫機關人員的堅守崗位，也表示肯定與感謝。"
seg_list = jieba.cut(news)
print('/'.join(seg_list))
# 感謝/陳/其邁/副/院長/費心督導/，/對/於/年/假期/間/各/防疫/機關/人員/的/堅守崗位/，/也/表示/肯定/與/感謝/。

# 載入字典
jieba.load_userdict('sample/userdict.txt')
seg_list = jieba.cut(news)
print('/'.join(seg_list))
# 感謝/陳其邁/副/院長/費心督導/，/對/於/年/假期/間/各/防疫/機關/人員/的/堅守崗位/，/也/表示/肯定/與/感謝/。


