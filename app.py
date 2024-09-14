from flask import Flask

app = Flask(__name__)

# Run pip install -r requirements.txt to install all necessary
# libraries and dependencies

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
