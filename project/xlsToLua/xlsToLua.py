#-*- coding:utf-8 -*-

#将Excel转成lua脚本文件
#@author : star
#@date : 2018-3-16
#---------------------

import xlrd
import os

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#关键词在第三行（根据不同需求，行数也不一样）
key_row = 2


curpath = os.path.dirname(os.path.abspath(sys.argv[0]))
print 'current dir path : ' + curpath

def excel2lua(src_excel_path,tar_lua_path):

    fileOutput = open(tar_lua_path,'w')

    writedate = '--@author:star\n\n\n'
    writedate = writedate + 'local root=\n{\n'
    workbook = xlrd.open_workbook(src_excel_path)

    #先获取所有的sheet
    sheet_num = workbook.nsheets

    for sheet_idx in range(0,sheet_num):
        #获得当前sheet
        sheet = workbook.sheet_by_index(sheet_idx)
        writedate = writedate + '\t' + '[\"%s\"]' %(str(sheet.cell(0,1).value)) + ' = {\n'

        #获得行数
        rows = sheet.nrows
        #获得列数
        cols = sheet.ncols

        #获取关键词字段keyword
        keywords = []
        for col in xrange(cols):
            keywords.append(str(sheet.cell(key_row,col).value))

        #判断关键词id的唯一性
        excel_id_dic = {}
        for k in xrange(key_row+2,rows):
            cell_id = int(sheet.cell(k,0).value)
            if cell_id in excel_id_dic:
                print '[warning] duplicated data id: %d, all previous value will be ignored!~' % (cell_id)
            excel_id_dic[cell_id] = 0


        #通过行数和列数，取得单元格cell的value
        for row in xrange(rows):
            if row <= key_row+1:
                #row(行)为0，特殊处理，表示keys
                continue

            writedate = writedate + '\t\t' + '{\n'

            for col in xrange(cols):

                #如果第二行为空，则表示这格子是注释。
                if not any(sheet.cell(key_row,col).value):
                    continue
                #如果字段以_开头，表示这列是策划用的，无需编译
                if str(keywords[col]).startswith('_'):
                    continue
                
                cellType = sheet.cell(key_row+1,col).value
                cell = sheet.cell(row,col)
                cell_val = cell.value

                writedate = writedate + '\t\t\t' + '["' + keywords[col] + '"] = '

                #根据字段类型去调整数值 如果为空值 依据字段类型 填上默认值
                v = 0
                if cellType == 'string':
                    if cell.ctype == 0:
                        v = '\'\''
                    else:
                        v = '\'%s\'' %(cell_val)
                if cellType == 'int':
                    if cell.ctype == 0:
                        v = -1
                    else:
                        v = int(cell_val)
                if cellType == 'float':
                    if cell.ctype == 0:
                        v = -1
                    else:
                        v = float(cell_val)
                if cellType == 'table':
                    if cell.ctype == 0:
                        v = {}
                    else:
                        v = cell_val

                writedate = writedate + str(v) + ',\n'

            writedate = writedate + '\n' + '\t\t},\n'
        else:
            writedate = writedate + '\t},\n\n\n'

    writedate = writedate + '}\n' + 'return root'

    fileOutput.write(writedate)
    fileOutput.close()

#输入
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('python excel2lua.py <excel_input_path> <lua_output_path>')
        exit(1)

    excel2lua(os.path.join(curpath,sys.argv[1]),os.path.join(curpath,sys.argv[2]))

