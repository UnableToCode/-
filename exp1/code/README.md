# 爬虫代码
爬虫代码使用scrapy为爬虫框架，基于scrapy给予爬虫名和网址生成基础代码，然后通过对网页h5源码的分析找到需要的信息编写识别和提取代码，编写item类，并通过setting进行相关设置后使用scrapy crawl stackoverflow -o stackoverflow.json指令执行爬虫并将结果以json格式保存在文件中。

对Stack Overflow tag为IDE的页面进行爬虫获取所有问题的标题和tag  
爬虫网址为  
“https://stackoverflow.com/questions/tagged/ide?tab=newest&page={page}&pagesize=50".format(page=page) for page in range(1, 187)  
（每页50条回答共有187页）  
结果保存为json格式存储于stackoverflow.json中，共有9299条记录  

# 词频分析
词频分析代码在文件word_stat.py中，直接运行即可，通过对所有question的单词提取统计数量并去除一些常见连词副词如"in"、"to"、"a"等后，经过筛选，排名前10的单词如下：  
('ide', 2491)('how', 1860)('eclipse', 1198)('studio', 1111)('code', 835)
('visual', 798)('c', 657)('project', 608)('intellij', 529)('java', 468)('android', 466)
