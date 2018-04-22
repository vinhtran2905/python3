from urllib import request

url = 'https://query1.finance.yahoo.com/v7/finance/download/TSLA?period1=1521654485&period2=1524332885&interval=1d&events=history&crumb=o5Eu4tetf/L'

def download_stock_data(csv_url):
    response = request.urlopen(csv_url)

    csv = response.read()
    csv_str = str(csv)

    lines = csv_str.split("\\n")
    print(lines)
    '''
    dest_url = r'goog.csv'

    fw = open(dest_url,'w')
    for line in lines:
        fw.write(line + "\n")
    fw.close()

'''
download_stock_data(url)

