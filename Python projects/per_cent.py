per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите желаемую сумму (в рублях): "))
n = {key: value / 100 * money for key, value in per_cent.items()}
deposit = list(map(round, list(n.values())))
print("deposit =", deposit)
print("Максимальная сумма, которую вы можете заработать — deposit", [max(deposit)])



