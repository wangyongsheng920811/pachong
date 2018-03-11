# _*_ coding=utf-8 _*_
#猫眼电影 TOP100 榜的电影名称、时间、评分、图片等信息
import requests
import re
import os

def getPage(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
	res = requests.get(url,headers=headers).text
	return res

def saveInfo(infos):
	os.chdir(r'C:\Users\wangyongsheng\Desktop\pachong')
	for i in range(10):
		name = '第' + infos[1][i] + '名：' + infos[0][i]
		os.mkdir(name)
		with open(name+'/'+name+'.txt','w+') as f:
			f.write('排名：%s\n电影名：%s\n上映时间：%s\n分数：%s\n'%(infos[1][i],infos[0][i],infos[2][i],infos[3][i]+infos[4][i]))
		with open(name+'/'+name+'.jpg','wb') as p:
			p.write(requests.get(infos[6][i]).content)

	os.listdir()
def getMovieInfo(res):
	names = re.findall('<a href=.*title=.*data-act=".*>(.*)</a>',res)
	releasetimes = re.findall('<.*class="releasetime">上映时间：(.*).*</p>',res)
	scores1 = re.findall('<i class="integer">(.*)</i><i.*</i>',res)
	scores2 = re.findall('<i class="fraction">(.*)</i>',res)
	imgTitles = re.findall('<img data-src=".*" alt="(.*)" class="board-img" />',res)
	imgAddrs = re.findall('<img data-src="(.*)" alt=".*" class="board-img" />',res)
	places = re.findall('<i class="board-index.*">(.*)</i>',res)
	# for i in range(10):
	# 	print('第%s名：%s，上映时间:%s，分数%s%s'%(places[i],names[i],releasetimes[i],scores1[i],scores2[i]))
	return names,places,releasetimes,scores1,scores2,imgTitles,imgAddrs

if __name__ == '__main__':
	url = 'http://maoyan.com/board/4'
	for i in range(10):
		page = '?offset=' + str(i*10)
		res = getPage(url+page)
		infos = getMovieInfo(res)
		saveInfo(infos)
	#diyiqiehttp://maoyan.com/board/4?offset=0
	# http://maoyan.com/board/4?offset=10
	# http://maoyan.com/board/4?offset=90
