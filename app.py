from flask import Flask, jsonify, request#, make_response
from flask_cors import cross_origin
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd

app = Flask(__name__)

@app.route("/")
@cross_origin()
def index():
    return jsonify({'Pie': 'Payment'})

@app.route("/Pie")
@cross_origin()
def Pie():
    fig = go.Figure()
    try:
        col = request.args.get('names', default = 'City', type = str)
        goal = request.args.get('values', default = 'Total', type = str)
        df = pd.read_csv('./data/supermarket_sales - Sheet1.csv')
        fig = px.pie(df[[col, goal]], values=goal, names=col)
    except Exception as ex:
        print("%s: %s" % (type(ex).__name__, str(ex)))
        return jsonify({type(ex).__name__: str(ex)})
    return fig.to_html()

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=4988)