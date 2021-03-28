from DB.Queries.userQuery import getUserAssets

def assetsMessage(userAssets):
    message = ""
    lastDayAssetsPrice = 0
    for asset in userAssets:
        ticker_name = asset[1]
        name = asset[2]
        tickerAmount = int(asset[5]) if asset[5] != None else 0
        actualPrice = float(asset[7])
        lastDayPrice = float(asset[8])
        isFavorite = bool(asset[9])

        tickerChangePrice = round(actualPrice - lastDayPrice,3)
        percentTickerChange = round((tickerChangePrice/lastDayPrice)*100,3)

        sign = "+" if tickerChangePrice > 0 else "-"
        favorite = "🌟" if isFavorite == True else ""

        tickerChangePrice = sign + str(tickerChangePrice).replace('-', '')
        percentTickerChange = sign + str(percentTickerChange).replace('-', '')

        lastDayAssetsPrice = lastDayAssetsPrice + tickerAmount * lastDayPrice
        message = message + "{0}*{1} *(/{2}) {3}шт, цена {4}₽. " \
                            "Изменение за сегодня {5}₽({6}%)\n".format(favorite,name,ticker_name,tickerAmount,actualPrice,tickerChangePrice,percentTickerChange)
    return message

def generalMessageAboutUsersAssets(chatId):
    userAllAssets,allPages = getUserAssets(chatId, page = 0)
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

    signPerDay = "+" if changePerDay > 0 else "-"
    signPerTime = "+" if changePerTime > 0 else "-"

    changePerDay = signPerDay + str(changePerDay).replace('-', '')
    changePerTime = signPerTime + str(changePerTime).replace('-', '')

    message = "*Рыночная стоимость активов:* {0}₽\n" \
                  "*Изменение за день:* {1}₽\n" \
                  "*Изменение за все время:* {2}₽\n\n".format(str(round(assetsPrice,3)), changePerDay, changePerTime)
    return message