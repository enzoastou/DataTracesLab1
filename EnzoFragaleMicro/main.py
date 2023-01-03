from flask import Flask
import logging

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
    """
    return logString + "This is the logger page."

