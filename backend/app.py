import mysql.connector
from flask import Flask, send_from_directory
app = Flask(__name__, static_folder='frontend/build', static_url_path='')

# Run pip install -r requirements.txt to install all necessary
# libraries and dependencies

def get_db_connection():
    return mysql.connector.connect(
        host="db",  # This is the service name in Docker Compose
        user="user",
        password="password",
        database="dbname"
    )

@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:5000/"]
  interval: 30s
  timeout: 10s
  retries: 5

if __name__ == "__main__":
    app.run(debug=True)

