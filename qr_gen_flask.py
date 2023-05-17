from flask import Flask, render_template, request
import pyqrcode
from PIL import Image
import io
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

# Define the QRCodeForm class
class QRCodeForm(FlaskForm):
    link_name = StringField('Link Name', validators=[DataRequired()])
    link = StringField('Link URL', validators=[DataRequired()])
    submit = SubmitField('Generate QR Code')

@app.route('/')
def index():
    form = QRCodeForm()
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    form = QRCodeForm(request.form)
    if form.validate_on_submit():
        link_name = form.link_name.data
        link = form.link.data
        file_name = link_name + ".png"
        url = pyqrcode.create(link)
        url.png(file_name, scale=8)
        image = Image.open(file_name)
        image_data = io.BytesIO()
        image.save(image_data, 'PNG')
        image_data.seek(0)
        return image_data, 200, {'Content-Type': 'image/png'}
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)