import subprocess
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Bienvenido a mi aplicación Flask en Docker con Ansible.'

@app.route('/ejecutar-playbook', methods=['GET'])
def ejecutar_playbook():
    playbook_path = '/etc/ansible/docker3/playbook.yml'
    try:
        resultado = subprocess.run(['ansible-playbook', '-i', '/etc/ansible/docker3/hosts.ini', playbook_path], capture_output=True, text=True)
        output = resultado.stdout
        return jsonify({'status': 'success', 'output': output}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

