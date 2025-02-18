from flask import Flask, request, jsonify
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.core import Document

uygulama = Flask(__name__)
indeks = None

@uygulama.route('/isle', methods=['POST'])
def belgeleri_isle():
    global indeks
    belge_metinleri = request.json.get('belgeler')
    if not belge_metinleri:
        return jsonify({'hata': 'Belge yok'}), 400

    belgeler = [Document(text=metin) for metin in belge_metinleri]

    indeks = VectorStoreIndex.from_documents(belgeler)
    return jsonify({'mesaj': 'Belgeler indekslendi'})

@uygulama.route('/sor', methods=['POST'])
def soru_sor():
    veri = request.json
    soru = veri.get('soru')

    if not indeks:
        return jsonify({'hata': 'Belgeler henuz islenmedi'}), 400

    sorgu_motoru = indeks.as_query_engine()
    yanit = sorgu_motoru.query(soru)
    return jsonify({'cevap': str(yanit)})

if __name__ == '__main__':
    uygulama.run(port=5002)