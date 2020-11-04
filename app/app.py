from flask import Flask, render_template
from flask import jsonify
from flask import request
from flask_mysqldb import MySQL

app = Flask(__name__)

# MY SQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'dns'

mysql = MySQL(app)

# Open connection with sql to query the domain
def query_domain(name):
    cur = mysql.connection.cursor()
    sql_query = "SELECT * FROM records WHERE domain='" + name + "';"
    print("SQL Query: " + sql_query)
    cur.execute(sql_query)
    results = cur.fetchall()
    cur.close()

    # Change the format
    formatted_results = []
    for record in results:
        formatted_results.append({
            "domain": record[0],
            "ip": record[1]
        })

    return formatted_results

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dnsconfig")
def dnsconfig():
    return render_template("dnsconfig.html")

# /dnsconfig/search?query=something
@app.route("/dnsconfig/search")
def search():
    query = request.args.get('query') or ""
    print("This is your query: " +  query)
    results = query_domain(query)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
