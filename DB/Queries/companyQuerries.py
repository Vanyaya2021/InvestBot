from DB.Queries import dbConnection as db

def getSectors():
    getSectorLst = []
    rec = db.query('SELECT DISTINCT sector FROM botdb.public.company_t')
    for i in range(0, len(rec)):
        getSectorLst.append(rec[i][0])
    return(getSectorLst)


