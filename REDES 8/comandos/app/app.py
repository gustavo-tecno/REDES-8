from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute_command', methods=['POST'])
def execute_command():
    if request.method == 'POST':
        command = request.form['command']
        try:
            result = subprocess.run(command, capture_output=True, text=True, shell=True)
            return render_template('index.html', command=command, result=result.stdout)
        except Exception as e:
            return render_template('index.html', command=command, error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
