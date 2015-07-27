#!/usr/bin/env python
#Author:ryt
#Function:去除html文件中的特殊符号
#Date:2015-7-22
import html
filename = input("Input the filename:")
fin = open(filename,'r')
data = fin.read()
fin.close()
fout = open(filename,'w')
fout.write(html.escape(data))
fout.close()
