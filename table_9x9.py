#! /usr/bin/python
# Filename : table_9x9.py
# Author : zhangjie
# Date : 20150728

print '\n9x9 Table\n'

for i in range(1,10) :
    for j in range(1,i+1) :
        print j, 'x', i, '=', j*i, '\t',
        # print '%d x %d = %d\t' %(j, i, j*i)
    print '\n'
print '\nDone!'
