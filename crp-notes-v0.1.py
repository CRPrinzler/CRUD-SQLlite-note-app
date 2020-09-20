#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 22:35:46 2020

@author: toxic
"""

import sqlite3
import os
from prettytable import from_db_cursor
import clipboard





#lets clear everything
os.system('clear')

def newnote():

    print('--------------------------')
    heading = input("Heading:\n")
    newnote = input("New NOTE:\n")
    db=sqlite3.connect('noter')
    qry="insert into notes (heading,note) values (?,?);"
    try:
        cur=db.cursor()
        data_tuple= (heading,newnote)
        cur.execute(qry, data_tuple)
        db.commit()
        print ("one record added successfully")
    except:
        print ("error in operation")
        db.rollback()
    db.close()

def editnote():
    db=sqlite3.connect('noter')
    sql="SELECT * from notes;"
    cur=db.cursor()
    cur.execute(sql)
    x = from_db_cursor(cur)
    print (x)
    db.close()
    print('--------------------------')
    pick=input('Choose ID:')
    int(pick)

    db=sqlite3.connect('noter')
    sql=("SELECT note from notes where id="+(pick))
    #print(sql)
    cur=db.cursor()
    cur.execute(sql)
    print('--------------------------')
    #escape if pick is not found

    myresult = cur.fetchall()
    for x in myresult:
        print(x[0])

        #push var into OS clipboard

        clipboard.copy(x[0])
        print('-------------------------------------')
        print('USE CTRL + V to access the note data.')
        print('-------------------------------------')
        editnote = input("EDIT NOTE:\n")
    db=sqlite3.connect('noter')
    qry=("update notes set note='"+editnote+"' where id="+pick+";")
    try:
        cur=db.cursor()

        cur.execute(qry)
        db.commit()
        print ("one record updated successfully")
    except:
        print ("error in operation")
        db.rollback()
    db.close()

def deletenote():
    print('----------DELETE----------------')
    db=sqlite3.connect('noter')
    sql="SELECT * from notes;"
    cur=db.cursor()
    cur.execute(sql)
    x = from_db_cursor(cur)
    print (x)
    db.close()
    pick=input('Choose ID:')
    int(pick)
    db=sqlite3.connect('noter')
    sql=("DELETE FROM notes where id="+(pick))
    print(sql)
    cur=db.cursor()
    cur.execute(sql)
    print('--------------------------')

    try:

        db.commit()
        print ("one record updated successfully")
    except:
        print ("error in operation")
        db.rollback()
    db.close()


def main():
    pick = '99'
    while pick != '0':
        db=sqlite3.connect('noter')
        sql="SELECT * from notes;"
        cur=db.cursor()
        cur.execute(sql)
        x = from_db_cursor(cur)
        print (x)
        db.close()
        print(' NEW NOTE: 1 || EDIT NOTE: 2 || DELETE NOTE: 3')
        print('----------------------------------------------')
        print('Press 0 to quit')
        print('----------------------------------------------')
        pick=input('Task? : ')

        if pick == '1':
            os.system('clear')
            newnote()
     
            os.system('clear')

        if pick == '2':
            os.system('clear')
            editnote()
     
            os.system('clear')

        if pick == '3':
            os.system('clear')
            deletenote()
     
            os.system('clear')



    if pick == 0:
            return
main()

