NAME,DATE,OPEN,MAX,MIN,CLOSE,VOLUME = 0,1,2,3,4,5,6

def main():
    lst = loadStockFile("nasdaq.csv")
    # Show just first and last tuples:
    print("first:", lst[1])
    print("last:", lst[-1])
    
    print("a) totVol=", totalVolume(lst))

    print("b) maxVal=", maxValorization(lst))
    
    stocksDic = stocksByDateByName(lst)
    print("c) CSCO@11:", stocksDic['2020-10-12']['CSCO'])
    print("c) AMZN@22:", stocksDic['2020-10-22']['AMZN'])

    port = {'NFLX': 100, 'CSCO': 80}
    print("d) portfolio@01:", portfolioValue(stocksDic, port, "2020-10-01"))
    print("d) portfolio@30:", portfolioValue(stocksDic, port, "2020-10-30"))

def loadStockFile(filename):
    lst = []
    with open(filename) as f:
        for line in f:
            parts = line.strip().split('\t')
            name = parts[NAME]
            date = parts[DATE]
            tup = (name, date, float(parts[OPEN]), float(parts[MAX]),
                float(parts[MIN]), float(parts[CLOSE]), int(parts[VOLUME]))
            lst.append(tup)
    return lst

def totalVolume(lst):
    totVol = {}
    for i in lst:
        empresa = i[0]
        volume = i[6]
        if empresa not in totVol:
            totVol[empresa] = volume 
        else:
            totVol[empresa] += volume
    return totVol

def maxValorization(lst):
    vMax = {}
    for i in lst:
        data = i[1]
        empresa = i[0]
        fecho = i[5]
        abertura = i[2]
        valorização = (fecho/abertura - 100)
        if data not in vMax:
            vMax[data] = (empresa, valorização)
        else:
            if valorização > vMax[data][1]:
                vMax[data] = (empresa, valorização)
    return vMax

def stocksByDateByName(lst):
    dic = {}
    for i in lst:
        data = i[0]
        empresa = i[1]
        info = i[2:]
        if data not in dic:
            dic[data] = {}   #criação de um novo dicionário para adicionar as empresas e as duas infos
        dic[data][empresa] = info  #adição da info ao dicionário de cada data dentro do dicionário dic
    return dic

def portfolioValue(stocks, portfolio, date):
    assert date in stocks
    val = 0.0
    for stock, quantidade in portfolio:
        if stock in stocks[date]:
            fecho = stocks[date][stock][3]
            val += fecho * quantidade
    return val

if __name__ == "__main__":
    main()
