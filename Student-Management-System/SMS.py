from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import socket
import requests
import bs4
#****************************************************************************************************************
#code to main window

root=Tk()
root.title("S.M.S")
root.geometry("650x400+400+100")

try:
	city='Mumbai'
	socket.create_connection(("www.google.com", 80))
	a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"#link
	a2 ="&q=" + city#city data
	a3 = "&appid=c6e315d09197cec231495138183954bd"#userid
	api_address= a1+a2+a3
	res1 = requests.get(api_address)
	print(res1)

	data=res1.json()
	main=data['main']
	temp=main['temp']
	print("temp ",temp)

except OSError:
	print("check connection")

#res=requests.get("http://www.brainyquote.com/quotes_of_the_day.html")
#soup=bs4.BeautifulSoup(res,'lxml')
#quote=soup.find('img',{"class":"p-qotd"})
#text=quote['alt']
#print(text)


def f1():
	root.withdraw()
	addStud.deiconify()
def f2():
	root.withdraw()
	viewStud.deiconify()
	import cx_Oracle
	con = None
	cursor = None
	try:
		con = cx_Oracle.connect("system/abc123")
		cursor = con.cursor()
		sql="select sid, sname, smarks from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		data.sort()
		print(data)
		mdata=""
		for d in data:
			mdata = mdata + str(d[0])+ " " + d[1] + "\n"
		stData.insert(INSERT, mdata)
	except cx_Oracle.DatabaseError as e:
		print("issue",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()

def f3():
	root.withdraw()
	updStud.deiconify()

def f4():
	root.withdraw()
	studDel.deiconify()

def f5():
	root.withdraw()
	studgraph.deiconify()

btnAdd=Button(root,text="Add",width=10,font=("arial",16,"bold"),command=f1)
btnView=Button(root,text="View",width=10,font=("arial",16,"bold"),command=f2)
btnUpdate=Button(root,text="Update",width=10,font=("arial",16,"bold"),command=f3)
btnDelete=Button(root,text="Delete",width=10,font=("arial",16,"bold"),command=f4)
btnGraph=Button(root,text="Graph",width=10,font=("arial",16,"bold"),command=f5)
lblweather=Label(root,text=("Temperature",temp),width=18,font=("arial",16,"bold"))
#lblQuote=Label(root,text=("Quote",text),width=150,font=("arial",9,"bold"))

btnAdd.pack(pady=10)
btnView.pack(pady=10)
btnUpdate.pack(pady=10)
btnDelete.pack(pady=10)
btnGraph.pack(pady=10)
lblweather.pack(pady=10)
#lblQuote.pack(pady=10)
#******************************************************************************************************************************
#code to add Student


addStud=Toplevel(root)
addStud.title("Add Student")
addStud.geometry("400x500+400+100")

def f6():
	addStud.withdraw()
	root.deiconify()

def f9():
	try:
		import xlwt 
		from xlwt import Workbook 
		import cx_Oracle
		con = None
		cursor = None
		con = cx_Oracle.connect("system/abc123")
		cursor = con.cursor()
		print("hello")
		try:	
			print("h")
			n=0
			sid=entsid.get()
			sname=entsname.get()
			smarks=float(entsmarks.get())
			print(sid)
			count=0
			sql="select sid from student"
			cursor.execute(sql)
			data1 = cursor.fetchall()
			print(data1)
			

			for d in data1:
				if(sid==d[0]):
					count=count+1

			if(count>=1):
				msg = "ID No. "+str(sid)+" is already Present"
				messagebox.showwarning("Incorret ID",msg)
				n=n+1
			if len(sname)<2:
				msg = sname+" is Incorrect"
				messagebox.showwarning("Incorrect Name",msg)
				n=n+1
			if smarks > 100 or smarks < 0:
				msg = str(smarks)+" is Incorrect"
				messagebox.showwarning("Invalid",msg)
				n=n+1
			if(sname.isdigit()):
				msg = "No Digit"
				messagebox.showwarning("Invalid",msg)
				n=n+1
			if(sid.isalpha()):
				messagebox.showwarning("Invalid",'Id should be Integer')
				n=n+1
			if(n>0):
				print(n)
			else:
				sid=int(sid)
				sql="insert into student values ('%d','%s','%d')"
				args =(sid,sname,smarks)
				cursor.execute(sql % args)
				sql="select sid, sname, smarks from student"
				cursor.execute(sql)
				data = cursor.fetchall()
				data.sort()
				print(data)

				import csv
				with open('sdata.csv','w+',newline='') as newFile:
					newFileWriter = csv.writer(newFile)
					newFileWriter.writerow(['Id','Name','Marks'])
					
					for d in data:
						newFileWriter.writerow([d[0],d[1],d[2]])

				msg = str(cursor.rowcount)+" record inserted" 
				messagebox.showinfo("Success",msg)
		

		except Exception:
			messagebox.showwarning("Invalid","No Input")			
	

		con.commit()

	except cx_Oracle.DatabaseError as e:
		print("issue",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()


lblsid=Label(addStud,text="Enter Student Id",width=18,font=("arial",16,"bold"))
entsid=Entry(addStud,bd=5,width=10,font=("arial",16,"bold"))
lblsname=Label(addStud,text="Enter Student Name",width=18,font=("arial",16,"bold"))
entsname=Entry(addStud,bd=5,width=10,font=("arial",16,"bold"))
lblsmarks=Label(addStud,text="Enter Student Marks",width=18,font=("arial",16,"bold"))
entsmarks=Entry(addStud,bd=5,width=10,font=("arial",16,"bold"))
btnAddsave=Button(addStud,text="Add",width=10,font=("arial",16,"bold"),command=f9)
btnAddback=Button(addStud,text="Back",width=10,font=("arial",16,"bold"),command=f6)

lblsid.pack(pady=10)
entsid.pack(pady=10)
lblsname.pack(pady=10)
entsname.pack(pady=10)
lblsmarks.pack(pady=10)
entsmarks.pack(pady=10)
btnAddsave.pack(pady=10)
btnAddback.pack(pady=10)

addStud.withdraw()

#code to view

viewStud=Toplevel(root)
viewStud.title("View Student")
viewStud.geometry("400x400+400+100")

def f7():
	viewStud.withdraw()
	root.deiconify()
	stData.delete(1.0,END)

stData= scrolledtext.ScrolledText(viewStud, width=40, height=20)
btnviewback=Button(viewStud,text="Back",width=10,font=("arial",16,"bold"),command=f7)

stData.pack()
btnviewback.pack(pady=10)

viewStud.withdraw()
#****************************************************************************************************************
#code to update

updStud=Toplevel(root)
updStud.title("update Student")
updStud.geometry("400x500+400+100")

def f8():
	updStud.withdraw()
	root.deiconify()

def f10():
	try:	
		import cx_Oracle
		con = None
		cursor = None
		con = cx_Oracle.connect("system/abc123")
		cursor = con.cursor()
		print("h")


		try:	
			n=0
			count=0
			nsid=int(entusid.get())
			nsname=entusname.get()
			nsmarks=int(entusmarks.get())

			sql="select sid from student"

			cursor.execute(sql)
			data0=cursor.fetchall()
			for d in data0:
				if(nsid==d[0]):
					count=count+1
			print(count)
			if(count==0):
				messagebox.showwarning('',"No Id Present")
				n=n+1

			if len(nsname)<2:
				msg = nsname+" is Incorrect"
				messagebox.showwarning("Incorrect Name",msg)
				n=n+1
			if nsmarks > 100 or nsmarks < 0:
				msg = str(nsmarks)+" is Incorrect"
				messagebox.showwarning("Invalid",msg)
				n=n+1
			if(nsname.isdigit()):
				msg = "No Digit"
				messagebox.showwarning("Invalid",msg)
				n=n+1

			if(n>0):
				print(n)

			else:
				sql="update student set sname='%s',smarks='%d' where sid='%d'"
				args =(nsname,nsmarks,nsid)
		

				cursor.execute(sql % args)
				msg = str(cursor.rowcount)+"record updated"
				messagebox.showinfo("Success",msg)


				sql="select sid, sname, smarks from student"
				cursor.execute(sql)
				data = cursor.fetchall()

				import csv
				with open('sdata.csv','w+',newline='') as newFile:
					newFileWriter = csv.writer(newFile)
					newFileWriter.writerow(['Id','Name','Marks'])
					
					for d in data:
						newFileWriter.writerow([d[0],d[1],d[2]])


		
		except Exception:
			messagebox.showwarning('',"No Input")

		
		con.commit()

	except cx_Oracle.DatabaseError as e:
		print("issue",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()

lblusid=Label(updStud,text="Enter Student Id",width=18,font=("arial",16,"bold"))
entusid=Entry(updStud,bd=5,width=10,font=("arial",16,"bold"))
lblusname=Label(updStud,text="Enter Student Name",width=18,font=("arial",16,"bold"))
entusname=Entry(updStud,bd=5,width=10,font=("arial",16,"bold"))
lblusmarks=Label(updStud,text="Enter Student Marks",width=18,font=("arial",16,"bold"))
entusmarks=Entry(updStud,bd=5,width=10,font=("arial",16,"bold"))
btnupdsave=Button(updStud,text="Add",width=10,font=("arial",16,"bold"),command=f10)
btnupdback=Button(updStud,text="Back",width=10,font=("arial",16,"bold"),command=f8)

lblusid.pack(pady=10)
entusid.pack(pady=10)
lblusname.pack(pady=10)
entusname.pack(pady=10)
lblusmarks.pack(pady=10)
entusmarks.pack(pady=10)
btnupdsave.pack(pady=10)
btnupdback.pack(pady=10)

updStud.withdraw()
#*****************************************************************************************************************************************
#code to delete

studDel=Toplevel(root)
studDel.title("Delete Student")
studDel.geometry("400x400+400+100")

def f11():
	root.deiconify()
	studDel.withdraw()

def f12():
	try:
		import xlwt 
		from xlwt import Workbook 
		import cx_Oracle
		con = None
		cursor = None
		con = cx_Oracle.connect("system/abc123")
		cursor = con.cursor()
		try: 
			count=0
			dsid=int(entdsid.get())
			sql="select sid from student"
			cursor.execute(sql)
			data0=cursor.fetchall()
			for d in data0:
				if(dsid==d[0]):
					count=count+1
			if(count==0):
				messagebox.showwarning("Invalid","Wrong Id")
			else:
				sql="delete from student where sid='%d'"

				args =(dsid)
				cursor.execute(sql % args)
				sql="select sid, sname, smarks from student"
				cursor.execute(sql)
				data = cursor.fetchall()
				import csv
				with open('sdata.csv','w+',newline='') as newFile:
					newFileWriter = csv.writer(newFile)
					newFileWriter.writerow(['Id','Name','Marks'])
					
					for d in data:
						newFileWriter.writerow([d[0],d[1],d[2]])
				msg = "record deleted" 
				messagebox.showinfo("Success",msg)
		except Exception:
			print("nnnnnn")

		con.commit()

	except cx_Oracle.DatabaseError as e:
		print("issue",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()

lbldsid=Label(studDel,text="Enter Student Id",width=18,font=('arial',16,'bold'))
entdsid=Entry(studDel,bd=5,width=10,font=("arial",16,"bold"))
btnDel=Button(studDel,text="Delete",width=10,font=('arial',16,'bold'),command=f12)
btnDelback=Button(studDel,text="Back",width=10,font=('arial',16,'bold'),command=f11)

lbldsid.pack(pady=10)
entdsid.pack(pady=10)
btnDel.pack(pady=10)
btnDelback.pack(pady=10)

studDel.withdraw()
#*****************************************************************************************************************************
#student graph

studgraph=Toplevel(root)
studgraph.title("Students Graph")
studgraph.geometry("400x400+400+100")

def f13():
	import csv
	import numpy as np 
	import pandas as pd
	import matplotlib.pyplot as plt
	import cx_Oracle
	con = None
	cursor = None
	con = cx_Oracle.connect("system/abc123")
	cursor = con.cursor()

	sql="select sid from student"
	count=0
	cursor.execute(sql)
	data0=cursor.fetchall()
	for d in data0:
		count=count+1
	con.commit()

	data=pd.read_csv("sdata.csv")
	Id=data['Id'].tolist()
	marks=data['Marks'].tolist()


	plt.bar(Id,marks,label='marks')
	


	plt.xlabel("Id")
	plt.ylabel("Marks")
	plt.title("Student Marks")
	plt.grid()
	plt.legend(shadow=True)
	plt.xticks(np.arange(1,count+1, 1)) 

	plt.show()
	

def f14():

	import csv
	import numpy as np 
	import pandas as pd
	import matplotlib.pyplot as plt
	import cx_Oracle
	con = None
	cursor = None
	con = cx_Oracle.connect("system/abc123")
	cursor = con.cursor()

	sql="select sid from student"
	count=0
	cursor.execute(sql)
	data0=cursor.fetchall()
	for d in data0:
		count=count+1
	con.commit()

	data=pd.read_csv("sdata.csv")
	Id=data['Id'].tolist()
	marks=data['Marks'].tolist()


	plt.plot(Id,marks,marker='o',label='marks')
	


	plt.xlabel("Id")
	plt.ylabel("Marks")
	plt.title("Student Marks")
	plt.grid()
	plt.legend(shadow=True)
	plt.xticks(np.arange(1,count+2, 1)) 

	plt.show()
def f15():
	studgraph.withdraw()
	root.deiconify()

btnbar=Button(studgraph,text="Bar",width=10,font=('arial',16,'bold'),command=f13)
btnline=Button(studgraph,text="Line",width=10,font=('arial',16,'bold'),command=f14)
btngraphback=Button(studgraph,text="Back",width=10,font=("arial",16,"bold"),command=f15)

btnbar.pack(pady=10)
btnline.pack(pady=10)
btngraphback.pack(pady=10)

studgraph.withdraw()



root.mainloop()

 