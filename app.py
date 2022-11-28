from flask import Flask

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def startfunc():
    return "what do you want now ?"

if __name__ == "__main__":
    app.run(debug=True)