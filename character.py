# Класс для персонажа игры
class Character:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.health = 100
        self.inventory = []

    def take_damage(self, damage):
        # Уменьшаем здоровье, но не ниже 0
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def heal(self, amount):
        # Увеличиваем здоровье
        self.health += amount

    def add_item(self, item):
        # Добавляем предмет в инвентарь
        self.inventory.append(item)

# Функции вне класса
def print_character(hero):
    # Печатаем карточку персонажа
    print(f"Персонаж: {hero.name}")
    print(f"Уровень: {hero.level}, здоровье: {hero.health}")
    print(f"Инвентарь: {', '.join(hero.inventory)}")

def is_alive(hero):
    # Возвращает True, если здоровье больше 0
    return hero.health > 0

# Главная часть программы
if __name__ == "__main__":
    hero = Character("Genshin_Hero", 42)
    hero.add_item("Меч дождя")
    hero.add_item("Крылышки ветра")
    hero.take_damage(30)
    hero.heal(10)
    
    print_character(hero)
    print("Жив:", is_alive(hero))