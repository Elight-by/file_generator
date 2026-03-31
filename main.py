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


def settings():
    settings_loaded = load_settings()
    print("Select setting:\n1. Unit of measurement of information (Bytes, kilobytes, etc.)\n2. File name and other ")
    setting_get = input("1/2 ")
    if setting_get == "1":
        print("Select unit of measurement:\n1. Bytes\n2. Kilobytes (1024 bytes)\n3. Megabytes (1024 kilobytes)\n4. Gigabytes (1024 megabytes) ")
        uomoi = int(input("1/2/3/4 "))
        if uomoi not in (1, 2, 3, 4):
            print("Incorrectly entered value! 1/2/3/4")
        else:
            settings_loaded["settings"]["uomoi"] = uomoi
            save_settings(settings_loaded)
    elif setting_get == "2":
        print("Enter the file name with the type after the dot, for example: generated.data ")
        file_name = input()
        settings_loaded["settings"]["file_name"] = file_name
        save_settings(settings_loaded)


def main():
    settings_loaded = load_settings()
    file_name=settings_loaded["settings"]["file_name"]
    path_generate = os.path.join(current_directory, file_name)
    if settings_loaded["settings"]["uomoi"] == 1:
        one = 1
        size_uomoi = "bytes"
    elif settings_loaded["settings"]["uomoi"] == 2:
        one = 1024
        size_uomoi = "kilobytes"
    elif settings_loaded["settings"]["uomoi"] == 3:
        one = 1048576
        size_uomoi = "megabytes"
    elif settings_loaded["settings"]["uomoi"] == 4:
        one = 1073741824
        size_uomoi = "gigabytes"
    print(f"Enter the file size in {size_uomoi}:")
    file_hg = int(input())
    file_hg = file_hg * one
    with open(path_generate, 'w', encoding='utf-8') as file:
        print("Starting...")
        for i in range(0, file_hg):
            file.write("1")
    print("File generated successfully")

def start():
    start_choice = input("1. Generate file\n2. Settings ")
    if start_choice == "1":
        main()
    elif start_choice == "2":
        settings()

while True:
    settings_loaded = load_settings()
    start()
