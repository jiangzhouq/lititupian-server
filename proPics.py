import imghdr
import os
import Image

pics_path = "/home/qjizho/mode"
#imgType = imghdr.what(imageFile)

for lists in os.listdir(pics_path):
	path = os.path.join(pics_path, lists)
	typeName = imghdr.what(path)
	if('jpeg' == typeName):
		try:
			img = Image.open(path)
			w,h = img.size
			if w > 600 or h > 600:
				print 'ok'
			else:
				os.remove(path)
				print'remove w:',w,'h:',h
		except:
			os.remove(path)
			print 'remove because exception'
	else:
		os.remove(path)
