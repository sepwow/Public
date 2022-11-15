row = list(map(int, input("Enter numbers separated by spaces:\n").split()))
random_n = int(input("Enter any number:\n"))

def bubble_sort(row): #ascending
    for run in range (len(row) - 1):
        for i in range (len(row) - 1 - run):
            if row[i] > row[i+1]:
                row[i], row[i+1] = row[i+1], row [i]
    return row
print(bubble_sort(row))

def binary_search(row, random_n): #seeking the random number
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
    print("Your number",random_n,"is already in the list and its index is :",
          row.index(random_n))
    print("Previous number index",row[row.index(random_n) - 1],":",
          row.index(random_n) - 1)
else:
    row.append(random_n)
    bubble_sort(row)
    print("Your number is not in the list, the closest numbers indexes are :",
          row[row.index(random_n) - 1],"и",
          row[row.index(random_n) + 1],":",
          row.index(random_n) - 1,",",
          row.index(random_n) + 1)