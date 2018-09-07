#-*- coding:utf-8 -*-

#将文件夹内的文件名保存到excel中
#@author : star
#@date : 2018-8-27
#---------------------

import os
import xlwt
import sys

#当前路径
curpath = os.path.dirname(os.path.abspath(sys.argv[0]))

'''	param1:dir_path,文件夹路径
	param2:exort_path,导出excel路径
'''

def fileName2xls(dir_path,export_path):
	#打开excel
	f = xlwt.Workbook(encoding='utf-8')
	worksheet = f.add_sheet('图片路径')

	#当前行和列
	row = 0
	col_path = 0
	col_filename = 1
	col_ch = 2
	col_backup = 3
	#写入表头
	worksheet.write(row,col_path,"目录")
	worksheet.write(row,col_filename,'文件名')
	worksheet.write(row,col_ch,'繁体')
	worksheet.write(row,col_backup,'备注说明')
	row = row+1

	#将文件路径，文件名遍历写入xls中
	for root,dirs,files in os.walk(dir_path):
		#写入当前图片所在文件夹
		worksheet.write(row,col_path,root)
		worksheet.write(row,col_filename,os.path.basename(root))
		row = row+1

		for name in files:			
			worksheet.write(row,col_path,root)
			worksheet.write(row,col_filename,name)
			row = row+1


	#保存excel
	f.save(export_path)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('python writeFileName2xls.py <dirpath> <output_path>')
        exit(1)

    fileName2xls(os.path.join(curpath,sys.argv[1]),os.path.join(curpath,sys.argv[2]))
