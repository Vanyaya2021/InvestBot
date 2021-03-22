from DB.Queries.userQuery import getUserAssets

def assetsMessage(userAssets):
    message = ""
    lastDayAssetsPrice = 0
    for asset in userAssets:
        ticker_name = asset[1]
        name = asset[2]
        tickerAmount = int(asset[5])
        actualPrice = float(asset[7])
        lastDayPrice = float(asset[8])

        tickerChangePrice = round(actualPrice - lastDayPrice,3)
        percentTickerChange = round((tickerChangePrice/lastDayPrice)*100,3)

        if tickerChangePrice > 0:
            tickerChangePrice = "+" + str(tickerChangePrice)
            percentTickerChange = str(percentTickerChange)
        else:
            tickerChangePrice = "-" + str(tickerChangePrice).replace('-', '')
            percentTickerChange = str(percentTickerChange).replace('-', '')
        lastDayAssetsPrice = lastDayAssetsPrice + tickerAmount * lastDayPrice
        message = message + "*{0} ({1})* {2}шт, цена {3}₽. " \
                            "Изменение за сегодня {4}₽({5}%)\n".format(name,ticker_name,tickerAmount,actualPrice,tickerChangePrice,percentTickerChange)
    return message

def generalMessageAboutUsersAssets(chatId):
    userAllAssets = getUserAssets(chatId,page = 0)
    assetsPrice = 0
    balancedValue = 0
    lastDayAssetsPrice = 0
    for asset in userAllAssets:
        tickerAmount = int(asset[5])
        bookValue = float(asset[6])
        actualPrice = float(asset[7])
        lastDayPrice = float(asset[8])

        assetsPrice = assetsPrice + tickerAmount * actualPrice
        balancedValue = balancedValue + tickerAmount * bookValue
        lastDayAssetsPrice = lastDayAssetsPrice + tickerAmount * lastDayPrice

    changePerDay = round(assetsPrice - lastDayAssetsPrice, 3)
    changePerTime = round(assetsPrice - balancedValue, 3)
    if changePerDay > 0:
        changePerDay = "+" + str(changePerDay)
    else:
        changePerDay = "-" + str(changePerDay).replace('-', '')

    if changePerTime > 0:
        changePerTime = "+" + str(changePerTime)
    else:
        changePerTime = "-" + str(changePerTime).replace('-', '')

    message = "*Рыночная стоимость активов:* {0}₽\n" \
                  "*Изменение за день:* {1}₽\n" \
                  "*Изменение за все время:* {2}₽\n\n".format(str(round(assetsPrice,3)), changePerDay, changePerTime)
    return message