from flask import Flask, render_template, request
app = Flask(__name__)

css_styles = "<link rel='stylesheet' href='static/css/normalize.css'><link rel='stylesheet' href='static/css/skeleton.css'>"

@app.route("/")
def run():
    return "Hello World!"

@app.route("/getitems")
def getitems():
    header = "<html><head>" + css_styles + "</head><body><div class='container'><h2>Somelist</h2>"
    somelist = ['a1', 'b2', 'c3']
    list1 = "<ol>"
    for i in somelist:
        list1 = list1 + ("<li>" + (str(i)) + "</li>")
    list1 = list1 + ("</ol>")
    footer = "</div></body></html>"
    return header + list1 + footer

@app.route("/start")
def start():
    somelist = ['a1', 'b2', 'c3']
    out = render_template("start.html", name="Juergen", liste1=somelist)   # sinnvoller ist Übergabe einer Klasse oder eines Dictionaries an die View
    #print(out)
    return out

@app.route("/page1")
def page1():
    return render_template("page1.html")

@app.route("/about")
def about():
    name = request.args.get("name")
    age = request.args.get("age")
    return render_template("about.html", name=name, age=age)   # sinnvoller ist Übergabe einer Klasse oder eines Dictionaries an die View
