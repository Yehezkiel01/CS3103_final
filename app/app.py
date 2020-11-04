from flask import Flask, render_template
from flask import jsonify
from flask import request
from flask import current_app

import sqlite3
from flask import g

app = Flask(__name__)

def get_database_path():
    return current_app.root_path + '/database/dns.db'

# Reference: https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/
# Get the current db or created a new connection if there is no db yet
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        print("[LOG] The database path: " + get_database_path())
        db = g._database = sqlite3.connect(get_database_path())
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Open connection with sql to query the domain
def query_domain(name):
    cur = get_db().cursor()
    sql_query = "SELECT * FROM records WHERE domain='" + name + "';"
    print("[LOG] SQL Query: " + sql_query)
    cur.execute(sql_query)
    results = cur.fetchall()
    print("[LOG] Raw Resulst: " + str(results))
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
