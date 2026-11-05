# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
with open("test_file/task_3.txt", "r", encoding="utf-8") as f:
    text = f.read()
purchases = text.split("\n\n")
purchase_sums = []
for p in purchases:
    p = p.strip()
    if p == "":
        continue
    lines = p.splitlines()
    total = 0
    for line in lines:
        price = int(line.strip())
        total += price
    purchase_sums.append(total)

sorted_sums = sorted(purchase_sums, reverse=True)
top_three = sorted_sums[:3]
three_most_expensive_purchases = sum(top_three)
print(three_most_expensive_purchases)

assert three_most_expensive_purchases == 202346
