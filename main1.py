# main.py
# Лабораторная работа № 10. Вариант 1 — «Стример»


class Streamer:
    """Класс, описывающий стримера и его донаты."""

    def __init__(self, nick, followers):
        # ник стримера
        self.nick = nick
        # список сумм донатов
        self.donates = []
        # количество подписчиков
        self.followers = followers

    def add_donate(self, amount):
        """Добавить сумму доната в список."""
        self.donates.append(amount)

    def total_donates(self):
        """Вернуть общую сумму всех донатов."""
        return sum(self.donates)

    def average_donate(self):
        """Вернуть средний донат (0, если донатов нет)."""
        if len(self.donates) == 0:
            return 0
        return sum(self.donates) / len(self.donates)


def print_stats(streamer):
    """Вывести статистику стримера в консоль."""
    print("=== Статистика стримера ===")
    print("Ник:", streamer.nick)
    print("Подписчики:", streamer.followers)
    print("Всего донатов:", streamer.total_donates())
    print("Средний донат:", streamer.average_donate())


# --- Демонстрация работы ---
if __name__ == "__main__":
    streamer = Streamer("GolubKin", 1200)
    streamer.add_donate(500)
    streamer.add_donate(150)
    print_stats(streamer)