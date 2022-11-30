from flask import Flask
import gunicorn
from housing.logger import logging
from housing.exception import HousingException
import sys
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def startfunc():
    try:
        raise Exception("yoo testing exception yooo")
    except Exception as e:
        custom_ex = HousingException.get_detailed_error_message(e,sys) 
        logging.info(custom_ex)
        logging.info("hello i'm from info :) ")
    return "what do you want now ?"

if __name__ == "__main__":
    app.run(debug=True)