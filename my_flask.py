from flask import Flask, render_template
import csv



app = Flask(__name__)

@app.route('/')
def render_card(title=None, names=None, pic1=None):
    names=[]
    with open('fruits.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    for i in range(0,len(data)-3,4):
        names.append([data[i],data[i+1],data[i+2],data[i+3]])

    return render_template('card.html', title="Fruit", names=names)    
