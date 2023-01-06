from flask import Flask
import logging
import requests
from pytrends.request import TrendReq
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import base64
import time
from collections import Counter

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

@app.route('/trends', methods=["GET"])

def trends():
    print("start")
    pytrends = TrendReq(hl='en-US', tz=360)
    kw_list = ["/m/0bk1p", "/m/07c0j", "/m/04xrx"]
    pytrends.build_payload(kw_list, cat=0, timeframe='today 3-m', geo='FR', gprop='')
    print("pytrended")
    df = pytrends.interest_over_time() #does not work anymore from there, it seems...
    print("dfed")
    df.rename(columns={"/m/0bk1p":"Queen", "/m/07c0j":"Beatles", "/m/04xrx":"Mariah"}, inplace=True)
    print("df done")
    #fig = plt.figure(figsize=(10,5))
    #plt.plot(df["date"], df["Queen"])
    #plt.plot(df["date"], df["Beatles"])
    #plt.plot(df["date"], df["Mariah"])
    #Saving the plot as an image
    #plt.savefig('/tmp/line_plot.jpg', bbox_inches='tight', dpi=150)

    #with open("/tmp/line_plot.jpg", "rb") as img_file:
    #    my_string = base64.b64encode(img_file.read())
    #print(my_string)

    return df.to_json() #+ "\n" + my_string

@app.route('/time', methods=["GET"])

def timeLog():
    def log_execution_time(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"Execution time of {func.__name__}: {execution_time} seconds")
            x.append(execution_time)
            return result
        return wrapper

    def count_count(text, word_counter):
        word_counter.update(text)
        return (word_counter)

    def dict_count(text, word_count):
        # Split the text into words
        words = text.split()

        # Iterate over the list of words
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        return (word_count)

    global x
    x = []
    @log_execution_time
    def compute_count():
        with(open("sh.txt") as f):
            data = f.readlines()
        prevOutput=Counter()
        for sentence in data:
            countOutput = count_count(sentence, prevOutput)
            prevOutput = countOutput
        return countOutput

    @log_execution_time
    def compute_dict():
        with(open("sh.txt") as f):
            data = f.readlines()
        prevOutput = {}
        for sentence in data:
            dictOutput = dict_count(sentence, prevOutput)
            prevOutput = dictOutput
        return dictOutput


    for i in range(100):
        countResult=compute_count()
        dictResult = compute_dict()

    counts=x[::2]
    dicts=x[1::2]
    outString = "count mean: "
    outString += str(np.mean(counts))
    outString += "\ncount variance: "
    outString += str(np.std(counts)**2)
    outString += "\ndict mean: "
    outString += str(np.mean(dicts))
    outString += "\ndict variance: "
    outString += str(np.std(dicts)**2)
    return outString

if __name__ == '__main__':
    app.run()