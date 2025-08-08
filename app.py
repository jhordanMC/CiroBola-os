from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/proxy', methods=['GET', 'POST'])
def proxy():
    target_url = "http://35.225.198.236:5000/endpoint"  # Ajusta si tu ruta es distinta
    if request.method == 'GET':
        response = requests.get(target_url, params=request.args)
    else:
        response = requests.post(target_url, json=request.get_json())
    return jsonify(response.json())

if __name__ == '__main__':
    app.run()