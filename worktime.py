import xlwt
import xlrd
from xlutils.copy import copy


arriveTime = raw_input("ArriveTime: ") 
leaveTime = raw_input("LeaveTime: ")   

aT = arriveTime.split(':')
lT = leaveTime.split(':')

workHour = '%.2f' % (int(lT[0])-1 - int(aT[0]) + ( float(lT[1])+60 - float(aT[1]) ) / 60  -1)
#print workHour

data = xlrd.open_workbook('WorkTime.xls')
table = data.sheet_by_name(u'My WorkTime')
#print table.nrows
row = table.nrows
newdata = copy(data)
newtable = newdata.get_sheet(0)
newtable.write(row,0,workHour)
newdata.save('WorkTime.xls')

#f = xlwt.Workbook()
#sheet1 = f.add_sheet(r'sheet1',cell_overwrite_ok=True)
#sheet1.write(0,0,value)


