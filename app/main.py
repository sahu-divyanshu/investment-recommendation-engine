from app import create_app
from flask import jsonify

app = create_app()

@app.route('/')
def index():
    return jsonify({
        'message': 'Investment Recommendation Engine API',
        'version': '1.0.0',
        'status': 'running'
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)