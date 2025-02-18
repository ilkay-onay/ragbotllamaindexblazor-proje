from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
from llama_index.core import SimpleDirectoryReader
from llama_index.core import Document

uygulama = Flask(__name__)
yukleme_klasoru = 'yuklemeler'
os.makedirs(yukleme_klasoru, exist_ok=True)

@uygulama.route('/yukle', methods=['POST'])
def pdf_yukle():
    if 'dosya' not in request.files:
        return jsonify({'hata': 'Dosya yuklenmedi'}), 400

    dosya = request.files['dosya']
    if dosya.filename == '':
        return jsonify({'hata': 'Dosya secilmedi'}), 400

    dosya_adi = secure_filename(dosya.filename)
    dosya_yolu = os.path.join(yukleme_klasoru, dosya_adi)
    dosya.save(dosya_yolu)

    belgeler = SimpleDirectoryReader(yukleme_klasoru).load_data()
    belge_metinleri = [belge.text for belge in belgeler]
    return jsonify({
        'mesaj': 'PDF basariyla islendi',
        'belgeler': belge_metinleri
    })

if __name__ == '__main__':
    uygulama.run(port=5001)