#爬取StackOverflow IDE tag分析需求
使用scrapy爬虫框架对Stack Overflow tag为IDE的页面进行爬虫获取所有问题的标题和tag
爬虫网址为\n
“https://stackoverflow.com/questions/tagged/ide?tab=newest&page={page}&pagesize=50".format(page=page) for page in range(1, 187)\n
（每页50条回答共有187页）
结果保存为json格式存储于stackoverflow.json中，共有9299条记录

