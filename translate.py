from deep_translator import GoogleTranslator
import json

# JSON dosyasını yükleme fonksiyonu
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# JSON dosyasını çevirme fonksiyonu
def translate_json(json_data, source_lang='en', target_lang='tr'):
    translated_data = {}
    translator = GoogleTranslator(source=source_lang, target=target_lang)
    for key, value in json_data.items():
        if isinstance(value, str):
            translated_data[key] = translator.translate(value)
        elif isinstance(value, dict):
            translated_data[key] = translate_json(value, source_lang, target_lang)
        else:
            translated_data[key] = value  # Diğer veri tipleri için çeviri yapılmaz
    return translated_data

# Ana fonksiyon
def main():
    input_file = 'streamit-extensions.po'  # Giriş dosyası yolu
    output_file = 'translated.po'  # Çıkış dosyası yolu

    # JSON dosyasını yükle
    data = load_json(input_file)

    # JSON dosyasını çevir
    translated_data = translate_json(data)

    # Çevrilen veriyi kaydet
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(translated_data, file, ensure_ascii=False, indent=4)

    print(f"Çeviri tamamlandı ve '{output_file}' olarak kaydedildi.")

if __name__ == "__main__":
    main()
