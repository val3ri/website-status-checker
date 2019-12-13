from flask import Flask, render_template

import logging

import json
import checking

app = Flask(__name__)


@app.route("/")
def hello():
    checking.main()

    json_file = open("updated_db.json", "r")
    json_data = json.load(json_file)
    # console.log(json_file)

    # return str(json_data)
    return render_template('for-loop.html')
    # return """
    # Hello world!
    # This is my web app!
    # """ + """ 
    # """ + json_data[0]["url"] + """ 
    # """


if __name__ == "__main__":
    # app.run()
    app.run(debug=True, use_reloader=True)
