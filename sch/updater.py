import requests
import json
import time
import os

try:
	os.environ['TZ']='Asia/Kolkata'
	time.tzset()
except Exception as e:
	pass

def RefreshJson():
	res=requests.get("http://shdbdcdnems02.cdnsrv.jio.com/jiotv.data.cdn.jio.com/apis/v1.3/getMobileChannelList/get/?langId=6&os=android&devicetype=phone&usergroup=tvYR7NSNn7rymo3F&version=6.0.0").json()
	chnl={}
	for i in res['result']:
		chnl[i["channel_name"].replace("+"," ")]={"id":i["channel_id"],"lang":i["channelLanguageId"],"cate":i["channelCategoryId"]}
	chnl["Updated-on"]=time.strftime("%D-%T")
	with open("channel.json","w") as f:
		f.write(json.dumps(chnl))
	res=requests.get("http://shdbdecdnems05.cdnsrv.jio.com/jiotv.data.cdn.jio.com/apis/v1.3/dictionary/dictionary.json?langId=6").json()
	chnlCate={}
	for i in res['channelCategoryMapping']:
		chnlCate[res['channelCategoryMapping'][i]]=int(i)
	chnlLang={}
	for i in res['languageIdMapping']:
		chnlLang[res['languageIdMapping'][i]]=int(i)
	with open("categories.json","w") as f:
		f.write(json.dumps({"categories":chnlCate,"languages":chnlLang}))

RefreshJson()


