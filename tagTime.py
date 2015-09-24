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
	TagTime()
print 'Current path:',os.getcwd()
Comeon(os.getcwd())
