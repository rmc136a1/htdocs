import os
def getlist():
    files=os.listdir("data")
    liststr=""
    for item in files:
        liststr=liststr+"<li><a href='index.py?id={name}'>{name}</a></li>".format(name=item)
    return liststr