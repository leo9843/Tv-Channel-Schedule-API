import requests
import json

def getCategories():
	with open('sch/categories.json','r') as f:
		data=json.loads(f.read())
	data_json={"categories":list(data["categories"].keys()),"languages":list(data["languages"].keys())}
	return data_json# jsonify before sending it

def searchChannel(lang=False,cate=False):
	with open('sch/categories.json','r') as f:
		data=json.loads(f.read())
		categories,languages=data["categories"],data["languages"]
	
	try:
		if (lang):
				lang=languages[lang]
	except Exception:
		return "invalid language search /getCategories"
	try:
		if (cate):
			cate=categories[cate]
	except Exception:
		return "invalid categories search /getCategories"
	with open('sch/channel.json','r') as f:
		data=json.loads(f.read())
	data.pop("Updated-on")
	data_json=[]
	if (lang&cate):
		for i in data:
			if (data[i]['lang']==lang)&(data[i]['cate']==cate):
				data_json.append(i)
	elif (lang):
		for i in data:
			if (data[i]['lang']==lang):
				data_json.append(i)
	elif (cate):
		for i in data:
			if (data[i]['cate']==cate):
				data_json.append(i)
	return data_json

def TodaySchedule(channel=False):
	with open('sch/channel.json','r') as f:
		data=json.loads(f.read())
	try:
		channel=data[channel]['id']
	except Exception:
		return "invalid categories search /searchChannel"
	res=requests.get("http://shdbdecdnems04.cdnsrv.jio.com/jiotv.data.cdn.jio.com/apis/v1.3/getepg/get?offset=0&channel_id="+str(channel)+"&langId=6").json()
	data_json={}
	for i in res['epg']:
		data_json[i["showtime"]]={"name":i["showname"],"type":i["showCategory"],"other-details":i["description"]}
	return data_json

