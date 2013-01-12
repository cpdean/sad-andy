from flask import Flask, render_template, request, redirect
from urlparse import urlparse
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.debug = True


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/go/")
def go():
    q = request.args.get('url')
    content = requests.get(q).text
    s = BeautifulSoup(content)
    if "ycombinator" in q:
        td = s.find_all("td", class_="title")[0]
        link = td.find("a").get("href")
    elif "reddit" in q:
        return "{0} ?? lollololololol reddit lololol".format(q)
    else:
        return "{0} ?? lollololololol".format(q)
    return redirect(link)

if __name__ == '__main__':
    app.run()
