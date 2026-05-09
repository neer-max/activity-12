#part1

s1 = {2, 3, 1}
s2 = {'b', 'a', 'c'}
s3 = list(zip(s1, s2))
print(s3, "\n")

#part2
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list1[::-1]):
    print(x, y)

#part3
stocks = ['reliance', 'infosys', 'tcs']
prices = [2175, 1127, 2750]

new_dict = {stocks: prices for stocks,
            prices in zip(stocks, prices)}
print('\n{}'.format(new_dict))

