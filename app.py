from flask import Flask, render_template, flash, request, redirect, url_for, session
from werkzeug.utils import secure_filename
import numpy as np
import os
from flask_session import Session
import tensorflow as tf
from keras.utils import load_img, img_to_array

# Nama file model TFLite
TFLITE_MODEL = 'models/model__v1.tflite'

# Memuat model TFLite
interpreter = tf.lite.Interpreter(model_path=TFLITE_MODEL)
interpreter.allocate_tensors()

# Mendapatkan detail input dan output
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

print('@@ Model loaded. Check http://127.0.0.1:8080/')

def predict(img_path, interpreter):
    # Sesuaikan ukuran gambar sesuai dengan ukuran input model
    test_image = load_img(img_path, target_size=(120, 120))
    print('@@ Got Image for prediction')

    test_image = img_to_array(test_image) / 255.0
    test_image = np.expand_dims(test_image, axis=0)
    
    print("Test image shape:", test_image.shape)
    
    # Set input tensor
    interpreter.set_tensor(input_details[0]['index'], test_image)

    # Lakukan inferensi
    interpreter.invoke()

    # Ambil hasil prediksi
    output_data = interpreter.get_tensor(output_details[0]['index'])
    print("Output data shape:", output_data.shape)
    print(output_data[0])

    # Prediksi kelas
    probability = output_data[0][0]
    classes = 0 if probability <= 0.5 else 1
    return classes

app = Flask(__name__, template_folder='templates')
app.secret_key = 'algo908%jejeneverdiesiapajejesayagatau'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Ubah kondisi menjadi kelas malaria
KONDISI = ['Parasitized', 'Uninfected']
TIPS1 = [
    'Deteksi parasit malaria. Disarankan segera berkonsultasi dengan dokter.',
    'Tidak terdeteksi adanya infeksi malaria. Tetap jaga kesehatan dan lingkungan.'
]
TIPS2 = [
    'Pastikan untuk mengikuti saran medis dan segera lakukan pengobatan jika diperlukan.',
    'Jaga kebersihan dan hindari gigitan nyamuk untuk mencegah infeksi malaria.'
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            classes = predict(filepath, interpreter)
            session['classes'] = str(classes)
            session['filepath'] = filepath
            return redirect(url_for('hasil'))

@app.route('/dokumentasi')
def dokumentasi():
    return render_template('dokumentasi.html')

@app.route('/tentang')
def tentang():
    return render_template('tentang.html')

@app.route('/hasil')
def hasil():
    classes = int(session.get('classes'))
    filepath = session.get('filepath')
    return render_template('hasil.html',
                            penyakit=KONDISI[classes],
                            imagepath=filepath,
                            tips1=TIPS1[classes],
                            tips2=TIPS2[classes])

@app.route('/upload')
def proses():
    return render_template('proses.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
