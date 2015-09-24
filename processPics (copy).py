# -*- coding: utf-8 -*- 
import os 
import MySQLdb
import time
import shutil
import time
#
first_page_folder = "/page/"
pics_folder = "/mode/"
new_floder = "/new/"

def SearchFirstPages(first_page_url):
	print 'drop page collection'
	page_collection.drop()
	print 'start to search first pages. Path:',first_page_url
	list_dirs = os.walk(first_page_url) 
	for root, dirs, files in list_dirs:
		for f in files:
			print os.path.join(root,f)
			post = {"name":f,"url":os.path.join(root,f),"ctime":os.path.getctime(os.path.join(root,f))}
			page_collection.insert(post)
	print 'over'	
	
def SearchPics(rootDir):
	list_dirs = os.walk(rootDir + new_floder)
	values=[]
	for root, dirs, files in list_dirs:
		for f in files:
	#		absPath = os.path.join(root,f)
	#		relPathSGroup = absPath.replace(rootDir + pics_folder , "").split('/')
	#		post = {"mode":"红蓝","category":relPathSGroup[0],"name":relPathSGroup[1],"url":absPath}
		#	pic_collection.insert(post)
			values.append((str(f),"","",""))
			shutil.move(rootDir + new_floder + str(f),rootDir + pics_folder)
	conn=MySQLdb.connect(host='localhost',user='root',passwd='biu1biu2biu3',port=3306)
    	cur=conn.cursor()
    	#cur.execute('create database if not exists tdp')
    	conn.select_db('tdp')
    	#cur.execute('create table pics(name varchar(128),mode varchar(128),category varchar(128),tag varchar(256))')
	cur.executemany('insert into pics(name,mode,category,tag) values(%s,%s,%s,%s)',values)
	conn.commit()
	cur.close()
	conn.close()
	print 'over'

def TagTime():
	conn=MySQLdb.connect(host='localhost',user='root',passwd='biu1biu2biu3',port=3306)
    	cur=conn.cursor()
    	conn.select_db('tdp')
	value = [time.time()]
	cur.execute('delete from time')
	cur.execute('insert into time(time) values(%s)',value)
	conn.commit()
	cur.close()
	conn.close()

def Comeon(rootDir): 
	#SearchFirstPages(rootDir + first_page_folder)
#	SearchPics(rootDir)
	TagTime()
print 'Current path:',os.getcwd()
Comeon(os.getcwd())
