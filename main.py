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

byte = "bytes"
kilo_byte = "kilobytes"
mega_byte = "megabytes"
giga_byte = "gigabytes"
settings_first = "Select setting:\n1. Unit of measurement of information (Bytes, kilobytes, etc.)\n2. File name and other "
settings_uomoi = "Select unit of measurement:\n1. Bytes\n2. Kilobytes (1024 bytes)\n3. Megabytes (1024 kilobytes)\n4. Gigabytes (1024 megabytes) "
settings_uomoi_incorrect = "Incorrectly entered value! 1/2/3/4"
settings_file_name = "Enter the file name with the type after the dot, for example: generated.data "
generate = "Enter the file size in "
succesfylly_generate = "File generated successfully"
start_code = "1. Generate file\n2. Settings "


def settings():
    settings_loaded = load_settings()
    print(settings_first)
    setting_get = input("1/2 ")
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

def start():
    start_choice = input(start_code)
    if start_choice == "1":
        main()
    elif start_choice == "2":
        settings()

while True:
    settings_loaded = load_settings()
    start()
