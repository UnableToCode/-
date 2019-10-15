import json
import string
import re
import collections # 词频统计库
f=open("stackoverflow.json",'r',encoding="utf-8")
data=json.load(f)
f.close()
for i in range(len(data)):
    data[i]["questions"]=data[i]["questions"][0].lower()
    data[i]["questions"]=re.sub("/"," ",data[i]["questions"])
    data[i]["questions"] = re.sub(r"[^a-z]", " ", data[i]["questions"])
    data[i]["questions"]=data[i]["questions"].translate(str.maketrans('', '', string.punctuation))
    data[i]["questions"] = data[i]["questions"].translate(str.maketrans('', '', string.punctuation))
article=[data[i]["questions"].split() for i in range(len(data))]
print(article[10])
word_list=[]
remove_words = ["in","out","below","above","on","with","of","not","a","to","i","is","are","for","the","and","can","an","do","there","from","or","closed","using","when"]
for sentence in article:
    for word in sentence:
        if word not in remove_words:
            word_list.append(word)
word_counts = collections.Counter(word_list) # 对分词做词频统计
word_counts_top10 = word_counts.most_common(20) # 获取前10最高频的词
print (word_counts_top10) # 输出检查

