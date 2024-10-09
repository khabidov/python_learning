# Домашнее задание:
# 1. Улучшить интернет-магазин
# должна присутствовать корзина
# замена товаров в корзине
# удаление товаров
# доп.библиотеки не требуются
# 2. Сделать мини-ролик о том, что прошел и что узнал)
# 3. Пройти тест на скорость печатания

busket={'item1':'iPhone 15','item2':'iPhone 15 Plus','item3':'iPhone 15 Pro'}  #создание корзины
print(busket)
busket.update({'item1':'iPhone16'}) #замена товара 1 с iPhone 15 на iPhone 16
print(busket)
x=busket.values()
print(x)
y=busket.keys()
print(y)
z=busket.items()
print(z)
busket.pop('item2')  #удаление товара 2
print(busket)
busket.popitem()  #удаление последнего товара
print(busket)
