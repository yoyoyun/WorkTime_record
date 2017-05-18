#用于创建新excel文件并执行写操作
import xlwt
#用于读excel文件
import xlrd
#用于复制excel并执行写操作
from xlutils.copy import copy

#8:36
arriveTime = raw_input("ArriveTime: ")
#18:30
leaveTime = raw_input("LeaveTime: ")   

aT = arriveTime.split(':')
lT = leaveTime.split(':')

#17 - 8 + (30+60-36)/60 -1 保留两位小数
workHour = '%.2f' % (int(lT[0])-1 - int(aT[0]) + ( float(lT[1])+60 - float(aT[1]) ) / 60  -1)

#根据文件名打开文件，读
data = xlrd.open_workbook('WorkTime.xls')
#获取表
table = data.sheet_by_name(u'My WorkTime')
#统计当前行数
row = table.nrows
#复制文件
newdata = copy(data)
#获得对应的表
newtable = newdata.get_sheet(0)
#在最后一行下面添加数据
newtable.write(row,0,workHour)
#保存文件
newdata.save('WorkTime.xls')




