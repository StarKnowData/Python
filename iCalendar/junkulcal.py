from icalendar import Calendar,Event,vDatetime
from datetime import datetime

print('v0.1.0功能：一次只能编辑一个日程，重复写日程操作会覆盖原有日程')
while True:
	n=input('请输入你想使用的功能号：1.写日程；2.查看日程；3.退出程序\n')
	if n=='1':
		#设置ics文件头参数
		cal=Calendar()
		cal.add('prodid','-//JunKul`s calenadr product//')
		cal.add('version','2.0')
		#获取当前日期信息
		today = datetime.today()

		#设置实践主体参数
		event=Event()
		summary=input('请输入活动内容:\n')
		event.add('summary',summary)
		event.add('dtend',today)
		event.add('dtstart',today)
		#event.add('dtstamp', datetime(2005,4,4,0,10,0,tzinfo=UTC))
		event['uid']='junkulmadein201901091422'
		#整合数据
		cal.add_component(event)
		#写入文件
		f=open('junkul.ics','wb')
		f.write(cal.to_ical())
		f.close()
	elif n=='2':
		try:
			#打开日程文件
			j=open('junkul.ics','rb')
			jcal=Calendar.from_ical(j.read())
			#输出关键信息
			for comp in jcal.walk():
				if comp.name=='VEVENT':
					print('内容：',comp.get('summary'))
					dts=comp.get('dtstart').to_ical()
					dts1=vDatetime.from_ical(dts)
					print('起始：',dts1)
					dte=comp.get('dtend').to_ical()
					dte1=vDatetime.from_ical(dte)
					print('结束：',dte1)
			j.close()
		except FileNotFoundError:
			print('请先制作日程！')
	elif n=='3':
		break;
	else:
		#简单的错误处理
		print('错误指令！此功能尚未开发！')
