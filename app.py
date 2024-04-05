from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

logs = []

def register_info():
    logs.append({
        "endereco": request.remote_addr,
        "metodo": request.method,
        "hora": datetime.now()
    })

@app.route('/ping', methods=['GET'])
def ping():
    register_info('/ping')
    return jsonify({'resposta': 'pong'})

@app.route('/echo', methods=['POST'])
def echo():
    register_info('/echo')
    input_data = request.json.get('dados')
    return jsonify({'resposta': input_data})

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/dash')
def dash():
    return render_template('dash.html', itens=logs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)