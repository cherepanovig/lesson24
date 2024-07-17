# Домашняя работа по уроку "Различие атрибутов класса и экземпляра."

class House:
    houses_history = []  # Создаем атрибут, который будет хранить названия созданных объектов

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])  # Добавляем наименование объекта в список
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name  # Инициализация атрибута name
        self.number_of_floors = number_of_floors  # Инициализация атрибута number_of_floors

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


    # def __str__(self):
    #     return self.name


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
#del h1
del h2
del h3

print(House.houses_history)
