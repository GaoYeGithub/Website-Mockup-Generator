from flask import Flask, render_template, request, send_from_directory, redirect, url_for
import os
import urllib.request
from datetime import datetime

app = Flask(__name__)

MOCKUP_DIR = 'static/Mockup'
os.makedirs(MOCKUP_DIR, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_mockup', methods=['POST'])
def generate_mockup():
    website_address = request.form.get('websiteAddress')
    bg_color = request.form.get('bgColor')

    mockup_url = f"https://2s9e3bif52.execute-api.eu-central-1.amazonaws.com/production/screenshot?url={website_address}&color={bg_color}"

    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    mockup_filename = f'mockup_{timestamp}.png'
    mockup_path = os.path.join(MOCKUP_DIR, mockup_filename)

    urllib.request.urlretrieve(mockup_url, mockup_path)

    return redirect(url_for('index', mockup=mockup_filename))

@app.route('/mockups')
def view_mockups():
    mockups = os.listdir(MOCKUP_DIR)
    return render_template('mockups.html', mockups=mockups)

@app.route('/mockup/<filename>')
def mockup(filename):
    return send_from_directory(MOCKUP_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True)
