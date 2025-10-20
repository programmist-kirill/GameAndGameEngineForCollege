import os
import time

def main():
    DIRECTORY_TO_SCENE = "/home/kirill/NOT_DELETE_FOLDER/game_for_college/scene"
    
    # Создаем файл, если его нет
    if not os.path.exists(DIRECTORY_TO_SCENE):
        with open(DIRECTORY_TO_SCENE, "w") as f:
            f.write("")
    
    last_content = ""
    
    while True:
        try:
            if os.path.exists(DIRECTORY_TO_SCENE):
                with open(DIRECTORY_TO_SCENE, "r") as file:
                    scene_content = file.read()
                
                # Обновляем экран только если контент изменился
                if scene_content != last_content:
                    os.system("clear")  # Всегда очищаем экран перед новым выводом
                    if scene_content:  # Выводим только если есть содержание
                        print(scene_content)
                    last_content = scene_content
            
            time.sleep(0.05)  # Чаще проверяем обновления
            
        except (IOError, PermissionError):
            # Файл может быть временно заблокирован для записи
            time.sleep(0.05)
            continue

if __name__ == "__main__":
    main()