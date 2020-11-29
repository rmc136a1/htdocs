#!C:\Users\KIM\AppData\Local\Programs\Python\Python38\python.exe
import cgi
form=cgi.FieldStorage()
title=form["title"].value
description=form["description"].value
opened_file=open("data/"+title,"w")
opened_file.write(description)
print("Location: index.py?id="+title+"\n")