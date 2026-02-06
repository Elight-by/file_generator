import os
import json

current_directory = os.path.dirname(os.path.abspath(__file__))
path_settings = os.path.join(current_directory, "settings.json")


def load_settings():
    try:
        with open(path_settings, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


settings_loaded = load_settings()
file_name=settings_loaded["settings"]["file_name"]
path_generate = os.path.join(current_directory, file_name)


def save_settings(new_data):
    with open(path_settings, 'w', encoding='utf-8') as f:
        json.dump(new_data, f, indent=4, ensure_ascii=False)

settings_loaded = load_settings()
if settings_loaded["settings"]["lang"] == "en":
    byte = "bytes"
    kilo_byte = "kilobytes"
    mega_byte = "megabytes"
    giga_byte = "gigabytes"
    settings_first = "Select setting:\n1. Unit of measurement of information (Bytes, kilobytes, etc.)\n2. File name and other\n3. Language "
    settings_uomoi = "Select unit of measurement:\n1. Bytes\n2. Kilobytes (1024 bytes)\n3. Megabytes (1024 kilobytes)\n4. Gigabytes (1024 megabytes) "
    settings_uomoi_incorrect = "Incorrectly entered value! 1/2/3/4"
    settings_file_name = "Enter the file name with the type after the dot, for example: generated.data "
    settings_lang = "Select language:\n1. English\n2. Russian "
    generate = "Enter the file size in "
    succesfylly_generate = "File generated successfully"
    start_code = "1. Generate file\n2. Settings "
elif settings_loaded["settings"]["lang"] == "ru":
    byte = "байты"
    kilo_byte = "килобайты"
    mega_byte = "мегабайты"
    giga_byte = "гигабайты"
    settings_first = "Выберите настройку:\n1. Единица измерения информации (Байты, килобайты и т.д.) текущая:\n2. Название файла и другое\n3. Язык "
    settings_uomoi = "Выберите единицу измерения:\n1. Байты\n2. Килобайты (1024 байта)\n3. Мегабайты (1024 килобайта)\n4. Гигабайты (1024 мегабайта) "
    settings_uomoi_incorrect = "Неправильно введенное значение! 1/2/3/4"
    settings_file_name = "Введите название файла с типом после точки например: generated.data "
    settings_lang = "Выберите язык:\n1. Английский\n2. Русский "
    generate = "Введите размер файла в "
    succesfylly_generate = "Файл успешно сгенерирован"
    start_code = "1. Сгенерировать файл\n2. Настройки "
else:
    None


def settings():
    settings_loaded = load_settings()
    print(settings_first)
    setting_get = input("1/2/3 ")
    if setting_get == "1":
        print(settings_uomoi)
        uomoi = int(input("1/2/3/4 "))
        if uomoi not in (1, 2, 3, 4):
            print(settings_uomoi_incorrect)
        else:
            settings_loaded["settings"]["uomoi"] = uomoi
            save_settings(settings_loaded)
    elif setting_get == "2":
        print(settings_file_name)
        file_name = input()
        settings_loaded["settings"]["file_name"] = file_name
        save_settings(settings_loaded)
    elif setting_get == "3":
        lang = input(settings_lang)
        if lang == "1":
            settings_loaded["settings"]["lang"] = "en"
            save_settings(settings_loaded)
        elif lang == "2":
            settings_loaded["settings"]["lang"] = "ru"
            save_settings(settings_loaded)


def main():
    now = 0
    percent = 0
    settings_loaded = load_settings()
    file_name=settings_loaded["settings"]["file_name"]
    path_generate = os.path.join(current_directory, file_name)
    if settings_loaded["settings"]["uomoi"] == 1:
        one = 1
        size_uomoi = byte
    elif settings_loaded["settings"]["uomoi"] == 2:
        one = 1024
        size_uomoi = kilo_byte
    elif settings_loaded["settings"]["uomoi"] == 3:
        one = 1048576
        size_uomoi = mega_byte
    elif settings_loaded["settings"]["uomoi"] == 4:
        one = 1073741824
        size_uomoi = giga_byte
    print(f"{generate} {size_uomoi}:")
    file_hg = int(input())
    file_hg = file_hg * one
    one_percent = file_hg/100
    with open(path_generate, 'w', encoding='utf-8') as file:
        for i in range(0, file_hg):
            now = now + 1
            file.write("1")
            if now >= one_percent:
                percent = percent + 1
                now = 0
                print(f"{percent}%")
        print(succesfylly_generate)


def first_start():
    settings_loaded = load_settings()
    print("Thanks for downloading!")
    lang = input("Select language: \n1. English\n2. Russian\n")
    try:
        if lang == "1":
            settings_loaded["settings"]["lang"] = "en"
            save_settings(settings_loaded)
            start()
        elif lang == "2":
            settings_loaded["settings"]["lang"] = "ru"
            save_settings(settings_loaded)
            start()
    except:
        print("✅")
    else:
        print("Incorrect input")
        first_start()

def start():
    start_choice = input(start_code)
    if start_choice == "1":
        main()
    elif start_choice == "2":
        settings()

settings_loaded = load_settings()
if settings_loaded["settings"]["lang"] == "none":
    first_start()

while True:
    settings_loaded = load_settings()
    if settings_loaded["settings"]["lang"] == "en":
        byte = "bytes"
        kilo_byte = "kilobytes"
        mega_byte = "megabytes"
        giga_byte = "gigabytes"
        settings_first = "Select setting:\n1. Unit of measurement of information (Bytes, kilobytes, etc.)\n2. File name and other\n3. Language "
        settings_uomoi = "Select unit of measurement:\n1. Bytes\n2. Kilobytes (1024 bytes)\n3. Megabytes (1024 kilobytes)\n4. Gigabytes (1024 megabytes) "
        settings_uomoi_incorrect = "Incorrectly entered value! 1/2/3/4"
        settings_file_name = "Enter the file name with the type after the dot, for example: generated.data "
        settings_lang = "Select language:\n1. English\n2. Russian "
        generate = "Enter the file size in "
        succesfylly_generate = "File generated successfully"
        start_code = "1. Generate file\n2. Settings "
    elif settings_loaded["settings"]["lang"] == "ru":
        byte = "байты"
        kilo_byte = "килобайты"
        mega_byte = "мегабайты"
        giga_byte = "гигабайты"
        settings_first = "Выберите настройку:\n1. Единица измерения информации (Байты, килобайты и т.д.) текущая:\n2. Название файла и другое\n3. Язык "
        settings_uomoi = "Выберите единицу измерения:\n1. Байты\n2. Килобайты (1024 байта)\n3. Мегабайты (1024 килобайта)\n4. Гигабайты (1024 мегабайта) "
        settings_uomoi_incorrect = "Неправильно введенное значение! 1/2/3/4"
        settings_file_name = "Введите название файла с типом после точки например: generated.data "
        settings_lang = "Выберите язык:\n1. Английский\n2. Русский "
        generate = "Введите размер файла в "
        succesfylly_generate = "Файл успешно сгенерирован"
        start_code = "1. Сгенерировать файл\n2. Настройки "
    else:
        None
    start()