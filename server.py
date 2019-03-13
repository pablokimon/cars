from flask import Flask, render_template, request, jsonify, Response
import pickle

#create the app object that will route our calls
app = Flask(__name__)
@app.route('/',methods = ['GET'])
def home():
    return render_template('home.html')
@app.route('/mpg',methods = ['GET'])
def mpg():
    return render_template('mpg.html')

if __name__=='__main__':
    app.run(host='0.0.0.0',port=3333,debug=True)

