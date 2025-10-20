import time
import os

SCENE_FILE = "/home/kirill/NOT_DELETE_FOLDER/game_for_college/scene"

def clear_screen():
    """Очищает экран через файл сцены"""
    with open(SCENE_FILE, "w") as fp:
        fp.write("")  # Пустая строка для очистки

def display_text_gradually(text, delay=0.2):
    """Постепенно отображает текст по одному символу"""
    current_text = ""
    for char in text:
        current_text += char
        with open(SCENE_FILE, "w") as fp:
            fp.write(current_text)
        time.sleep(delay)

def menu():
    clear_screen()
    time.sleep(0.5)
    scene = "    П ᴏ ᴄ ᴧ ᴇ д н и й   К ᴧ ю ч\n\n\n\tн̲ᴀ̲ч̲ᴀ̲т̲ь̲ н̲о̲в̲ʏ̲ю̲ и̲r̲ᴘ̲ʏ̲\n\n\tНᴀᴄᴛᴩᴏйᴋи\n\n\tВыхᴏд"
    with open(SCENE_FILE, "w") as fp:
        fp.write(scene)
    time.sleep(2)

def plot_beginning_of_the_game():
    clear_screen()
    string = 'Меня зовут "Каин" , и мне оставил головоломку мой предок. И спустя 2 года я нашел дом . В котором была только одна комната , и там я узнаю разгадку к головоломке.'
    display_text_gradually(string, 0.1)

def after_lifting_the_key():
    clear_screen()
    string = "Я поднял пыльный ключ с пола , замечая на нем гравировку фамильного герба . Я думаю это от той двери."
    display_text_gradually(string, 0.1)

def before_opening_the_door():
    clear_screen()
    string = "Я начал прислушиваться к тишине за дверью , затем резко вставил ключ . Рука дрожит - и я чувствую холодное сопротивление механизма."
    display_text_gradually(string, 0.1)

def after_opening_the_door():
    clear_screen()
    string = "Я делаю шаг внутрь , оборачиваюсь и вижу что дверь исчезла , словно её никогда и не было . В центре комнаты стоял пыльный гроб."
    display_text_gradually(string, 0.1)

def creating_doors(): 
    clear_screen()
    string = "Прежде чем я успел осознать ужас происходящего , позади меня материализуется такая же дверь , но наглухо закрытая."
    display_text_gradually(string, 0.1)

def ending():
    clear_screen()
    string = 'Я слышу скрип - крышка гроба сама приоткрывается , и оттуда доносится шёпот предка: "ты не жертва. Ты - ключ к вечности рода".'
    display_text_gradually(string, 0.1)

def main_loop():
    """Анимация подхода к ключу"""
    clear_screen()


    positions = [
        "━━━━━━━━━━━━━━━━━━━━━━━\n🔑         🧍        🚪\n━━━━━━━━━━━━━━━━━━━━━━━",
        "━━━━━━━━━━━━━━━━━━━━━━━\n🔑        🧍         🚪\n━━━━━━━━━━━━━━━━━━━━━━━",
        "━━━━━━━━━━━━━━━━━━━━━━━\n🔑       🧍          🚪\n━━━━━━━━━━━━━━━━━━━━━━━",
        "━━━━━━━━━━━━━━━━━━━━━━━\n🔑      🧍           🚪\n━━━━━━━━━━━━━━━━━━━━━━━",
        "━━━━━━━━━━━━━━━━━━━━━━━\n🔑     🧍            🚪\n━━━━━━━━━━━━━━━━━━━━━━━",
        "━━━━━━━━━━━━━━━━━━━━━━━\n🔑    🧍             🚪\n━━━━━━━━━━━━━━━━━━━━━━━",
        "━━━━━━━━━━━━━━━━━━━━━━━\n🔑   🧍              🚪\n━━━━━━━━━━━━━━━━━━━━━━━",
        "━━━━━━━━━━━━━━━━━━━━━━━\n🔑  🧍               🚪\n━━━━━━━━━━━━━━━━━━━━━━━",
        "━━━━━━━━━━━━━━━━━━━━━━━\n🔑 🧍                🚪\n━━━━━━━━━━━━━━━━━━━━━━━",
        "━━━━━━━━━━━━━━━━━━━━━━━\n🔑🧍                 🚪\n━━━━━━━━━━━━━━━━━━━━━━━",
        "━━━━━━━━━━━━━━━━━━━━━━━\n🧍                   🚪\n━━━━━━━━━━━━━━━━━━━━━━━"
    ]
    
    for position in positions:
        with open(SCENE_FILE, "w") as fp:
            fp.write(position)
        time.sleep(0.2)



def raised_key():
    """Анимация подхода к двери"""
    clear_screen()
    positions = [
        "━━━━━━━━━━━━━━━━━━━━━━━\n 🧍                  🚪\n━━━━━━━━━━━━━━━━━━━━━━━",
        "━━━━━━━━━━━━━━━━━━━━━━━\n  🧍                 🚪\n━━━━━━━━━━━━━━━━━━━━━━━",
        "━━━━━━━━━━━━━━━━━━━━━━━\n   🧍                🚪\n━━━━━━━━━━━━━━━━━━━━━━━",
        "━━━━━━━━━━━━━━━━━━━━━━━\n    🧍               🚪\n━━━━━━━━━━━━━━━━━━━━━━━",
        "━━━━━━━━━━━━━━━━━━━━━━━\n     🧍              🚪\n━━━━━━━━━━━━━━━━━━━━━━━",
        "━━━━━━━━━━━━━━━━━━━━━━━\n       🧍            🚪\n━━━━━━━━━━━━━━━━━━━━━━━",
        "━━━━━━━━━━━━━━━━━━━━━━━\n        🧍           🚪\n━━━━━━━━━━━━━━━━━━━━━━━",
        "━━━━━━━━━━━━━━━━━━━━━━━\n         🧍          🚪\n━━━━━━━━━━━━━━━━━━━━━━━",
        "━━━━━━━━━━━━━━━━━━━━━━━\n          🧍         🚪\n━━━━━━━━━━━━━━━━━━━━━━━",
        "━━━━━━━━━━━━━━━━━━━━━━━\n           🧍        🚪\n━━━━━━━━━━━━━━━━━━━━━━━",
        "━━━━━━━━━━━━━━━━━━━━━━━\n            🧍       🚪\n━━━━━━━━━━━━━━━━━━━━━━━",
        "━━━━━━━━━━━━━━━━━━━━━━━\n             🧍      🚪\n━━━━━━━━━━━━━━━━━━━━━━━",
        "━━━━━━━━━━━━━━━━━━━━━━━\n              🧍     🚪\n━━━━━━━━━━━━━━━━━━━━━━━",
        "━━━━━━━━━━━━━━━━━━━━━━━\n               🧍    🚪\n━━━━━━━━━━━━━━━━━━━━━━━",
        "━━━━━━━━━━━━━━━━━━━━━━━\n                🧍   🚪\n━━━━━━━━━━━━━━━━━━━━━━━",
        "━━━━━━━━━━━━━━━━━━━━━━━\n                 🧍  🚪\n━━━━━━━━━━━━━━━━━━━━━━━",
        "━━━━━━━━━━━━━━━━━━━━━━━\n                  🧍 🚪\n━━━━━━━━━━━━━━━━━━━━━━━",
        "━━━━━━━━━━━━━━━━━━━━━━━\n                   🧍🚪\n━━━━━━━━━━━━━━━━━━━━━━━"
    ]
    
    for position in positions:
        with open(SCENE_FILE, "w") as fp:
            fp.write(position)
        time.sleep(0.2)


def scene_with_a_coffin():
    clear_screen()
    coffin = "⚰️"
    player = "🧍"
    scene = "━━━━━━━━━━━━━━━━━━━━━━━\n" + " " + player + "      " + coffin + "\n━━━━━━━━━━━━━━━━━━━━━━━"
    with open(SCENE_FILE, "w") as fp:
        fp.write(scene)
    time.sleep(1)

def main():
    # Убедимся, что файл существует
    if not os.path.exists(SCENE_FILE):
        with open(SCENE_FILE, "w") as f:
            f.write("")
    
    menu()
    time.sleep(1)
    
    plot_beginning_of_the_game()
    time.sleep(1)
    
    main_loop()
    time.sleep(1)
    
    after_lifting_the_key()
    time.sleep(1)
    
    raised_key()
    time.sleep(1)
    
    before_opening_the_door()
    time.sleep(1)
    
    after_opening_the_door()
    time.sleep(1)
    
    scene_with_a_coffin()
    time.sleep(1)
    
    creating_doors()
    time.sleep(1)
    
    ending()
    time.sleep(2)

    menu()

if __name__ == "__main__":
    main()
