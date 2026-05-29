from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

DB_CONFIG = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT")
}

@app.route("/")
def home():
    return "Flask + PostgreSQL running. Jenkins pipeline feature is added.Yay!"

@app.route("/db-check")
def db_check():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        cur.execute("SELECT version();")
        version = cur.fetchone()

        cur.close()
        conn.close()

        return jsonify({
            "database_status": "connected",
            "postgres_version": version[0]
        })

    except Exception as e:
        return jsonify({
            "database_status": "failed",
            "error": str(e)
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
