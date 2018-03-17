#-*- coding:utf-8 -*-

'xlrd test 2'
__author__ = 'star'

import xlrd
import os

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


fileOutput = open('xlrd2.lua','w')

writedate = '--@author:star\n\n\n'

workbook = xlrd.open_workbook('test02.xls')
print "Excel sheels num = %s" % workbook.nsheets

#先获取所有的sheet
sheet_num = workbook.nsheets

for sheet_idx in range(0,sheet_num):
    #获得当前sheet
    sheet = workbook.sheet_by_index(sheet_idx)
    writedate = writedate + sheet.name + ' = {\n'

    #获得行数
    rows = sheet.nrows
    #获得列数
    cols = sheet.ncols

    #获取关键词字段keyword
    keywords = []
    for col in xrange(cols):
        keywords.append(str(sheet.cell(1,col).value))
    print keywords

    #判断关键词id的唯一性
    excel_id_dic = {}
    for k in xrange(3,rows):
        cell_id = int(sheet.cell(k,0).value)
        if cell_id in excel_id_dic:
            print '[warning] duplicated data id: %d, all previous value will be ignored!~' % (cell_id)
        excel_id_dic[cell_id] = 0


    #通过行数和列数，取得单元格cell的value
    for row in xrange(rows):
        if row <= 2:
            #row(行)为0，特殊处理，表示keys
            continue

        writedate = writedate + '\t' + '{\n'

        for col in xrange(cols):

            #如果第二行为空，则表示这格子是注释。
            if not any(sheet.cell(1,col).value):
                continue
            #如果字段以_开头，表示这列是策划用的，无需编译
            if str(keywords[col]).startswith('_'):
                continue
            
            cellType = sheet.cell(2,col).value
            cell = sheet.cell(row,col)
            cell_val = cell.value

            writedate = writedate + '\t\t' + '["' + keywords[col] + '"] = '

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

            # if cellType == 'int':
            #      writedate = writedate + str(int(cell_val)) + ',\n'
            # elif cellType == 'string':
            #     writedate = writedate + str(cell_val) + ',\n'

            # if col == 0:
            #     #writedate = writedate + '\t' + '["' + cell_val + '"]' + ' = ' + '{'
            #     writedate = writedate + '["' + keywords[col] + '"]' + '='

            # writedate = writedate + str(cell_val) + ',\n'
           # else:              
              #  writedate = writedate + '["' + str(sheet.cell(row,col).value) + '"]' + ','

        writedate = writedate + '\n' + '\t},\n'
    else:
        writedate = writedate + '}\n\n\n'

fileOutput.write(writedate)
fileOutput.close()
