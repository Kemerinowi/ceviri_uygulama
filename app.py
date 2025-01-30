from flask import Flask, render_template, request, jsonify
from googletrans import Translator

app = Flask(__name__)

# Desteklenen diller ve kodları
SUPPORTED_LANGUAGES = {
    'en': 'İngilizce',
    'tr': 'Türkçe',
    'es': 'İspanyolca',
    'fr': 'Fransızca',
    'de': 'Almanca',
    'ar': 'Arapça',
    'ru': 'Rusça',
   }

translator = Translator()

@app.route('/')
def home():
    return render_template('index.html', languages=SUPPORTED_LANGUAGES)

@app.route('/translate', methods=['POST'])
def translate():
    try:
        # Frontend'den gelen JSON verilerini al
        text = request.json['text']
        source_lang = request.json['source_lang']
        target_lang = request.json['target_lang']
        
        # Debugging: Gelen değerleri kontrol et
        print(f"Source: {source_lang}, Target: {target_lang}, Text: {text}")
        
        # Çeviri işlemini yap
        translated = translator.translate(text, src=source_lang, dest=target_lang)
        
        # Çeviri sonucunu geri döndür
        return jsonify({'translated_text': translated.text})
    except Exception as e:
        # Hata durumunda hata mesajını döndür
        print(f"Hata: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
