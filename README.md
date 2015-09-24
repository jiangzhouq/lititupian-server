立体图片后台服务器搭建
1,数据库建立
按照createdb.txt的说明新建数据库
2,图片数据整理导入
processPics.py	把new文件夹的图片信息添加进数据库,并移动图片到mode文件夹
tagTime.py	写入当前修改日期(app运行时会检查)
3,图片筛选,分类和tag的整理
PicManager.rar 源代码
PicManager_exe.rar 可运行文件
4,服务运行
qigz.py

附:app文件夹为二维码下载服务相关文件
