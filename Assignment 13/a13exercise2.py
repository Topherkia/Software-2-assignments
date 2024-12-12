import json
from flask import Flask, jsonify
import mysql.connector
from mysql.connector import connection

app = Flask(__name__)

@app.route('/airport/<icao_code>', methods=['GET'])
def get_airport_data(icao_code):
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{icao_code}'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            name = row[0]
            municipality = row[1]
    if cursor.rowcount > 0:
        result = {
            "ICAO": icao_code,
            "Name": name,
            "Location": municipality
        }
    else:
        result = {"error": "Airport not found"}
    return jsonify(result)


connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        database='course_db',
        user='user',
        password='pass',
        autocommit=True,
        charset="utf8mb4",
        collation="utf8mb4_general_ci"
    )

if __name__ == '__main__':
    app.run(debug=True)