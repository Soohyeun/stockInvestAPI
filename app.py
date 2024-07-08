from flask import Flask, make_response
from predictive_model.train import get_ten_days_predicton

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/predictions/<string:stockname>", methods=['GET'])
def get_prediction(stockname):
    try:
        predictions = get_ten_days_predicton(stockname)
        response = make_response(predictions, 200)
        return response
    except:
        response = make_response("No Stock name", 400)
        return response


if __name__=='__main__':
    app.run(debug=True, port=5000)