# Класс для стримера
class Streamer:
    def __init__(self, nick, subscribers):
        self.nick = nick
        self.donates = []  # список для донатов
        self.subscribers = subscribers

    def add_donate(self, amount):
        # Добавляем донат в список
        self.donates.append(amount)

    def total_donates(self):
        # Считаем сумму всех донатов циклом for
        total = 0
        for d in self.donates:
            total += d
        return total

    def average_donate(self):
        # Считаем средний донат (сумма / количество)
        if len(self.donates) == 0:
            return 0
        return self.total_donates() / len(self.donates)

# Функции вне класса
def print_stats(streamer):
    total = streamer.total_donates()
    avg = streamer.average_donate()
    # Округляем до 1 знака после запятой, чтобы красиво выводилось 133.3
    print(f"Стример: {streamer.nick}")
    print(f"Донатов: {len(streamer.donates)}, сумма: {total}, средний: {round(avg, 1)}")
    print(f"Подписчиков: {streamer.subscribers}")

def is_popular(streamer):
    # Возвращает True, если подписчиков больше 1000
    if streamer.subscribers > 1000:
        return True
    else:
        return False

# Главная часть программы
if __name__ == "__main__":
    s = Streamer("ShadowStorm", 1500)
    s.add_donate(100)
    s.add_donate(250)
    s.add_donate(50)
    
    print_stats(s)
    print("Популярен:", is_popular(s))