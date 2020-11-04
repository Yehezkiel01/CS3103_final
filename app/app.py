from flask import Flask, render_template
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dnsconfig")
def dnsconfig():
    return render_template("dnsconfig.html")

# /dnsconfig/search?query=something
@app.route("/dnsconfig/search")
def search():
    query = request.args.get('query')
    print("This is your query: " +  query)
    return jsonify(query)

if __name__ == "__main__":
    app.run(debug=True)