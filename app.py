from flask import Flask, render_template, request, send_file
import os
from PIL import Image
from real_esrgan import setup_real_esrgan, enhance_image

app = Flask(__name__, template_folder='templates')

# Set up the Real-ESRGAN model
upsampler = setup_real_esrgan()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload')
def upload_page():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    try:
        if 'image' not in request.files:
            return 'No file part'
        file = request.files['image']
        if file.filename == '':
            return 'No selected file'
        if file:
            static_dir = os.path.join(app.root_path, 'static')
            if not os.path.exists(static_dir):
                os.makedirs(static_dir)
            image_path = os.path.join(static_dir, 'temp_input_image.png')
            file.save(image_path)

            # Enhance the image
            enhanced_image_path = enhance_image(image_path, upsampler)

            return render_template('upload.html', original_image_path='temp_input_image.png', enhanced_image_path=enhanced_image_path)
    except Exception as e:
        return str(e)

@app.route('/download/<filename>')
def download(filename):
    try:
        file_path = os.path.join('static', filename)
        response = send_file(file_path, as_attachment=True)

        return response
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
