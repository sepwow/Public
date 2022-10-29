row = list(map(int, input("Введите числа через пробел:\n").split()))
random_n = int(input("Введите любое число:\n"))

def bubble_sort(row): #Ранжировка по возрастанию
    for run in range (len(row) - 1):
        for i in range (len(row) - 1 - run):
            if row[i] > row[i+1]:
                row[i], row[i+1] = row[i+1], row [i]
    return row
print(bubble_sort(row))

def binary_search(row, random_n): # Поиск рандомного числа в списке
    low = 0
    high = len(row) - 1
    search_res = False

    while low <= high and not search_res:
        middle = (low + high) // 2
        guess = row[middle]
        if guess == random_n:
            search_res = True
            return search_res
        if guess > random_n:
            high = middle - 1
        else:
            low = middle + 1
    return search_res

result = binary_search(row, random_n)
if result:
    print("Ваше число",random_n,"уже есть в списке и его индекс :",
          row.index(random_n))
    print("Индекс предыдущего числа",row[row.index(random_n) - 1],":",
          row.index(random_n) - 1)
else:
    row.append(random_n)
    bubble_sort(row)
    print("Ваше число отутствует в списке, индексы рядом стоящих чисел",
          row[row.index(random_n) - 1],"и",
          row[row.index(random_n) + 1],":",
          row.index(random_n) - 1,",",
          row.index(random_n) + 1)