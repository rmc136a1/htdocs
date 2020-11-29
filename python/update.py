#!C:\Users\KIM\AppData\Local\Programs\Python\Python38\python.exe
print("content-type: text/html; charset=utf-8\n")

import cgi,os,view

form=cgi.FieldStorage()

if 'id' in form:
  pageId=form["id"].value
  description=open("data/"+pageId,"r").read()
else:
  pageId="welcome"
  description=open("WEB","r").read()

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
      </ol>
      <div id="article">
      <form action="process_update.py"method="post">
        <input type="hidden"name="pageId"value="{form_default_title}"
        <p><input type="text"name="title"placeholder="title"value="{form_default_title}"></p>
        <p><textarea rows="15"name="description"placeholder="description"style="width:1000px;">{form_default_description}</textarea></p>
        <p><input type="submit"></p>
      </form>
      </div>
    </div>
  </body>
</html>
<!DOCTYPE html>
""".format(title=pageId,desc=description,liststr=view.getlist(),form_default_title=pageId,form_default_description=description))