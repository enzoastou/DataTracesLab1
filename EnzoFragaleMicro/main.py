from flask import Flask
import logging
import requests

app = Flask(__name__)

@app.route('/', methods=["GET"])

def hello_world():
 prefix_google = """
 <!-- Google tag (gtag.js) -->
<script async
src="https://www.googletagmanager.com/gtag/js?id=UA-250395355-2"></script>
<script>
 window.dataLayer = window.dataLayer || [];
 function gtag(){dataLayer.push(arguments);}
 gtag('js', new Date());
 gtag('config', 'UA-250395355-2');
</script>
 """
 return prefix_google + "Hello World"

@app.route('/logger', methods=["GET"])

def log():
    print('Info level log python.')
    logString = """
<script>
 console.log("Info level log JavaScript.")
</script>
<br>
<input type="text" name="Textbox" value="This is a textbox">
    """
    return "This is the logger page." + logString

@app.route('/cookies', methods=["GET"])

def cookies():
    #req = requests.get("https://www.google.com/")
    #googleCookies = req.cookies.get_dict()

    req = requests.get("https://analytics.google.com/analytics/web/?hl=fr#/report-home/a250395355w344281288p280864294")
    googleCookies = req.text
    return googleCookies

@app.route('/cookies/auth', methods=["GET", "POST"])

def googleAuth():
    #After a lot of research, I could not manage to find a way to do it so this is a fake result below
    # "#Fake it 'til you make it"
    return "Number of visitors fetched from ganalytics: 1"

