from  flask import Flask

app=Flask(__name__)

@app.route("/")
def hello():
    return "HI world"

if __name__ == "__main__":
    app.run(debug=True, port=800)