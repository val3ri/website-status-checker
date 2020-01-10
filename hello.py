from flask import Flask, render_template

from flask_table import Table, Col

import logging

import json
import checking

app = Flask(__name__)


@app.route("/")
def hello():
    checking.main()

    json_file = open("updated_db.json", "r")
    json_data = json.load(json_file)

    print(json_data)

    # return str(json_data)
    return render_template('for-loop.html')
    # return """
    # Hello world!
    # This is my web app!
    # """ + """
    # """ + json_data[0]["url"] + """
    # """

# Declare your table
class ItemTable(Table):
    name = Col('Name')
    description = Col('Description')

# Or, equivalently, some dicts
items = [dict(name='Name1', description='Description1'),
         dict(name='Name2', description='Description2'),
         dict(name='Name3', description='Description3')]

# Populate the table
table = ItemTable(items)


@app.route("/hello")
def hello1():
    return render_template('home.html', table=table, name="valeri")

@app.route("/test_table")
def test_table():
    return render_template('table.html')

if __name__ == "__main__":
    # app.run()
    app.run(debug=True, use_reloader=True)


