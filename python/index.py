#!C:\Users\KIM\AppData\Local\Programs\Python\Python38\python.exe
print("content-type: text/html; charset=utf-8\n")

import cgi,os,view

form=cgi.FieldStorage()

if 'id' in form:
  pageId=form["id"].value
  description=open("data/"+pageId,"r").read()
  description=description.replace("<","&lt;")
  description=description.replace(">","&gt;")
  update_link="<a href='update.py?id={}'>update</a>".format(pageId)
  delete_action="""<form action="process_delete.py"method="post">
    <input type="hidden"name="pageId"value="{}">
    <input type="submit"value="delete">
  </form>""".format(pageId)
else:
  pageId="welcome"
  description=open("WEB","r").read()
  update_link=""
  delete_action=""

print("""<!DOCTYPE html>
<html lang="ko" dir="ltr">
  <head>
    <title>WEB1 - welcome</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <link rel="stylesheet" href="style.css">
    <script src="color.js"></script>
  </head>
  <body>
    <h1><a href="index.py">WEB</a></h1>
    <input id="nightday"type="button"value="night"onclick="
      nightdayhandeler(this);">
    <div id="grid">
      <ol>
        {liststr}<br>
        <a href="create.py">create</a>
        {update_link}<pre>
</pre>
        {delete_action}
      </ol>
      <div id="article">
        <h2>{title}</h2>
        <p>{desc}</p>
      </div>
    </div>
  </body>
</html>
<!DOCTYPE html>
""".format(title=pageId,desc=description,liststr=view.getlist(),update_link=update_link,delete_action=delete_action))