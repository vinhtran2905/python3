item = ['December 23, 2015', 'Bread gloves', 8.51]
date = item[0]
print(date)


date, name, price  = ['December 23, 2015', 'Bread gloves', 8.51]
print(date)
print(name)
print(price)


def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(first)
    print(last)
    print(avg)

drop_first_last([3,4,5,6,7,7,8,9])



