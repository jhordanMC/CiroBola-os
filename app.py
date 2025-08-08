from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Ruta raíz para verificar que el contenedor está activo
@app.route('/')
def home():
    return "✅ Proxy activo en Railway"

# Ruta proxy que reenvía a tu VM en GCP
@app.route('/proxy', methods=['GET', 'POST'])
def proxy():
    target_url = "http://35.225.198.236:5000/endpoint"  # Ajusta si tu VM usa otra ruta

    try:
        if request.method == 'GET':
            print("🔄 Reenviando GET a:", target_url)
            response = requests.get(target_url, params=request.args)
        else:
            payload = request.get_json()
            print("📦 Reenviando POST a:", target_url)
            print("➡️ Payload:", payload)
            response = requests.post(target_url, json=payload)

        print("✅ Respuesta desde VM:", response.text)
        return jsonify(response.json()), response.status_code

    except Exception as e:
        import traceback
        traceback.print_exc()
        print("❌ Error al reenviar:", str(e))
        return jsonify({"error": str(e)}), 500

# Inicia el servidor en el puerto que Railway espera
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
