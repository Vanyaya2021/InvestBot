
def assetsMessage(userAssets):
    message = ""
    assetsPrice = 0
    balancedValue = 0
    lastDayAssetsPrice = 0
    index = 0
    for asset in userAssets:
        index +=1
        ticker_name = asset[1]
        name = asset[2]
        type = asset[3]
        tickerAmount = int(asset[5])
        bookValue = float(asset[6])
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


        assetsPrice = assetsPrice + tickerAmount * actualPrice
        balancedValue = balancedValue + tickerAmount * bookValue
        lastDayAssetsPrice = lastDayAssetsPrice + tickerAmount * lastDayPrice
        message = message + "*{0}. {1} ({2})* {3}шт, цена {4}₽. " \
                            "Изменение за сегодня {5}₽({6}%)\n".format(index,name,ticker_name,tickerAmount,actualPrice,tickerChangePrice,percentTickerChange)


    changePerDay = round(assetsPrice - lastDayAssetsPrice,3)
    changePerTime = round(assetsPrice - balancedValue,3)
    if changePerDay > 0:
        changePerDay = "+"+str(changePerDay)
    else:
        changePerDay = "-"+str(changePerDay).replace('-','')

    if changePerTime > 0:
        changePerTime = "+"+str(changePerTime)
    else:
        changePerTime = "-"+str(changePerTime).replace('-','')

    pre_message = "*Рыночная стоимость:* {0}₽\n" \
              "*Изменение за день:* {1}₽\n" \
              "*Изменение за все время:* {2}₽\n\n".format(str(assetsPrice),changePerDay,changePerTime)

    message = pre_message + message


    return message