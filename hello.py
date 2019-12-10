from flask import Flask
import json
import checking

app = Flask(__name__)


@app.route("/")
def hello():
    checking.main()

    json_file = open("updated_db.json", "r")
    json_data = json.load(json_file)
    # console.log(json_file)

    return str(json_data)


if __name__ == "__main__":
    app.run()
