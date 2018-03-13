#-*- coding:utf-8 -*-

'xlrd test'
__author__ = 'star'

import xlrd
import os

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


fileOutput = open('xlrd.lua','w')

writedate = '--@author:star\n\n\n'

workbook = xlrd.open_workbook('test.xlsx')
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
        keywords.append(sheet.cell(0,col).value)
    print keywords


    #通过行数和列数，取得单元格cell的value
    for row in xrange(rows):
        if row == 0:
            #row(行)为0，特殊处理，表示keys
            continue

        writedate = writedate + '\t' + '{\n'

        for col in xrange(cols):
            cell_val = sheet.cell(row,col).value
            #print cell_val

            writedate = writedate + '\t\t' + '["' + keywords[col] + '"]=' + str(cell_val) +',\n' 

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
