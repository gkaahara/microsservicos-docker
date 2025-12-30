from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return {
        'service': 'Python Flask Microservice 2',
        'message': 'API Python funcionando!',
        'timestamp': datetime.now().isoformat()
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3002, debug=True)
