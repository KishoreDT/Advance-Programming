import mysql.connector
import os
import platform
#import pandas as pd 
"""
create database rail;
use rail
create table traindetail(TName char(50),TNum int primary key,AC1 int,AC2 int,AC3 int,Sleeper int);
create table passengers(PName char(50),Age int,TrainNo int,NoofPas int,Class char(3),Amount int,Status char(20),PNR int);

"""
pnr=1024
host=input("Enter Host Address of MySQL : ")
user=input("Enter User Name of MySQL    : ")
passwd=input("Enter Password of User Name : ")
database=input("Enter Database Name         : ")
mydb=mysql.connector.connect(host=host,user=user,passwd=passwd,database=database);
if (mydb.is_connected()):
    # Carry out normal procedure
    print("\nConnection successful\n")
else:
    # Terminate
    print("Connection unsuccessful")
mycursor=mydb.cursor()
def railresmenu():
    print("Railway Reservation ")
    print("1. Train Detail")
    print("2. Reservation of Ticket")
    print("3. Cancellation of Ticket")
    print("4. Display PNR Status")
    print("5. Quit")
    n=int(input("\nEnter your choice : "))
    if(n==1):
        traindetail()
    elif(n==2):
        reservation()
    elif(n==3):
        cancel()
    elif(n==4):
        displayPNR()
    elif(n==5):
        exit(0)
    else:
        print("Wrong Choice")

def traindetail():
    print("Train Details")
    ch='y'
    while (ch=='y'):
        l=[]
        name=input("Enter train name : ")
        l.append(name)
        tnum=int(input("Enter train number : "))
        l.append(tnum)
        ac1=int(input("Enter number of AC 1 class seats : "))
        l.append(ac1)
        ac2=int(input("Enter number of AC 2 class seats : "))
        l.append(ac2)
        ac3=int(input("Enter number of AC 3 class seats : "))
        l.append(ac3)
        slp=int(input("Enter number of sleeper class seats : "))
        l.append(slp)
        train=(l)
        sql="insert into traindetail(TName,TNum,AC1,AC2,AC3,Sleeper)values(%s,%s,%s,%s,%s,%s)"
        mycursor.execute(sql,train)
        mydb.commit()
        print("Insertion Completed")
        print("Do you want to insert more train Detail")
        ch=input("Enter Yes/No :")
        print("/n")
    print('\n' *5)
    
    print("===================================================================")
    railresmenu()

def reservation():
    global pnr
    l1=[]
    pname=input("Enter passenger name : ")
    l1.append(pname)
    age=input("Enter age of passenger : ")
    l1.append(age)
    trainno=input("Enter train number : ")
    l1.append(trainno)
    np=int(input("Enter number of passanger : "))
    l1.append(np)
    print("select a class you would like to travel in")
    print("1. AC FIRST CLASS")
    print("2. AC SECOND CLASS")
    print("3. AC THIRD CLASS")
    print("4. SLEEPER CLASS")
    cp=int(input("Enter your choice : "))
    if(cp==1):
        amount=np*1000
        cls='AC1'
    elif(cp==2):
        amount=np*800
        cls='AC2'
    elif(cp==3):
        amount=np*500
        cls='AC3'
    else:
        amount=np*350
        cls='SLP'
    l1.append(cls)           
    print("Total amount to be paid:",amount)
    l1.append(amount)
    pnr=pnr+1
    print("PNR Number : ",pnr)
    print("Status: Confirmed")
    sts='Confirmed'
    l1.append(sts)
    l1.append(pnr)
    train1=(l1)
    sql="insert into passengers(PName,Age,TrainNo,NoofPas,Class,Amount,Status,PNR)values(%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,train1)
    mydb.commit()
    print("Insertion Completed")
    print("Go back to menu")
    print('\n' *5)

    print("===================================================================")
    railresmenu()

def cancel():
    print("Ticket Cancel Window")
    pnr=input("Enter PNR for cancellation of Ticket : ")
    pn=(pnr,)
    sql="update passengers set Status='Cancelled' where PNR=%s"
    mycursor.execute(sql,pn)
    mydb.commit()
    print("Deletion Completed")
    print("Go back to menu")
    print('\n' *5)

    print("===================================================================")
    railresmenu()

def displayPNR():
    print("PNR STATUS Window")
    pnr=input("Enter PNR NUMBER : ")
    pn=(pnr,) 
    sql="select * from passengers where PNR=%s"
    mycursor.execute(sql,pn)
    res=mycursor.fetchall() 
    #mydb.commit()
    print("PNR STATUS are as follows : ")
    print("(PName,Age,TrainNo, NoofPas,Cls,Amt,Status,PNR)")
    for x in res:
        print(x)   
    #print("Deletion completed")
    print("Go back to menu")
    print('\n' *5)

    print("===================================================================")
    railresmenu()

railresmenu()
