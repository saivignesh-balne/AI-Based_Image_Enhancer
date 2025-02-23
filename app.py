from flask import Flask, render_template, request, send_file
import os
from PIL import Image
from real_esrgan import setup_real_esrgan, enhance_image

app = Flask(__name__)

# Set up the Real-ESRGAN model
upsampler = setup_real_esrgan()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return 'No file part'
    file = request.files['image']
    if file.filename == '':
        return 'No selected file'
    if file:
        temp_image_path = os.path.join('static', 'temp_input_image.png')
        file.save(temp_image_path)

        # Enhance the image
        enhanced_image_path = enhance_image(temp_image_path, upsampler)

        return render_template('result.html', original_image_path='temp_input_image.png', enhanced_image_path=enhanced_image_path)

@app.route('/download/<filename>')
def download(filename):
    return send_file(os.path.join('static', filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
