mydict = {'first':'vinh'}

print(mydict['first'])

stocks = {
    'GOOG': 520.343,
    'YHoo': 34.44,
    'AMZn': 343,
    'AAPL': 443

}


#min, max ,sort by values
zip(stocks.values(),stocks.keys())



min(zip(stocks.values(),stocks.keys()))

print(min(zip(stocks.values(),stocks.keys())))

print(max(zip(stocks.values(),stocks.keys())))
print(sorted(zip(stocks.values(),stocks.keys())))