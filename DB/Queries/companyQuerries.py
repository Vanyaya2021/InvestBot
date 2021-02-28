from DB.Queries import dbConnection as db

def getSectors(type): # Аргумент type передаёт значение фильтра для поиска отраслей
    getSectorLst = []
    rec = db.query(f'SELECT DISTINCT sector FROM botdb.public.company_t WHERE stock_type={type}')
    for i in range(0, len(rec)):
        getSectorLst.append(rec[i][0])
    return(getSectorLst)


def getCompanies(sector):
    getCompaniesLst = []
    rec = db.query(f'SELECT DISTINCT name FROM botdb.public.company_t WHERE sector={sector}')
    for i in range(0, len(rec)):
        getCompaniesLst.append(rec[i][0])
    return(getCompaniesLst)

    ### Добавить вывод сообщения с компаниями из листа в f строке