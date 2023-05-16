from flask import Flask, render_template, request
import pyqrcode
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    link_name = request.form['link_name']
    link = request.form['link']
    file_name = link_name + ".png"
    url = pyqrcode.create(link)
    url.png(file_name, scale=8)
    image = Image.open(file_name)
    image_data = io.BytesIO()
    image.save(image_data, 'PNG')
    image_data.seek(0)
    return image_data, 200, {'Content-Type': 'image/png'}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)