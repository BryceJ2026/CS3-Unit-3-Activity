from flask import Flask, render_template, requests
import json

 # Create instance of Flask
 app = Flask(__name__)

#Homepage route
@app.route("/")
def index():
   #Open a JSON data file in ead mode
   with open('static/data.json', 'r') as file:
      data_dictionary = json.load(file)
   return render_template("index.html", data=data_dictionary)

# RUN THE APP (or type flask run in terminal)
if __name__ == "__main__": 

    app.run(host='0.0.0.0', port=5000, debug=True)