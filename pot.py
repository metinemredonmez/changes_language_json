import polib
from deep_translator import GoogleTranslator

def translate_pot_file(input_file_path, output_file_path, source_lang='en', target_lang='tr'):
    # .pot dosyasını oku
    pot = polib.pofile(input_file_path)
    
    # Çevirmen nesnesi oluştur
    translator = GoogleTranslator(source=source_lang, target=target_lang)

    # Her çeviri için
    for entry in pot:
        if entry.msgid and not entry.msgstr:
            # Metni çevir ve çeviriyi ayarla
            translated_text = translator.translate(entry.msgid)
            entry.msgstr = translated_text

    # Çeviriyi kaydet
    pot.save(output_file_path)

def main():
    input_file = 'template.pot'  # Giriş dosyası yolu
    output_file = 'translated.po'  # Çıkış dosyası yolu

    translate_pot_file(input_file, output_file)

    print(f"Çeviri tamamlandı ve '{output_file}' olarak kaydedildi.")

if __name__ == "__main__":
    main()
