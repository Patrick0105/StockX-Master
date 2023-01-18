import json
import requests
#========

def jsonget(query):
    global productmsg,stockxTitle
    
    headers = {
            'accept': 'application/json',
            'accept-encoding': 'utf-8',
            'accept-language': 'zh-tw,tw;q=0.9',
            'app-platform': 'Iron',
            'referer': 'https://stockx.com/zh-tw',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }

    url = f'https://stockx.com/api/browse?_search={query}'
    html = requests.get(url=f'http://api.scrape.do?token=<token>&url={url}', headers=headers)

    output = json.loads(html.text)

    stockxItem = output['Products'][0]
    stockxUrlKey = stockxItem['urlKey']

    stockxTitle = stockxItem['title']   #產品標題
    stockxImg = stockxItem['media']['imageUrl'] #產品圖片
    stockxColourway = stockxItem['colorway']    #產品規格
    stockxStyleID = stockxItem['styleId']   #產品ID
    stockxGender = stockxItem['gender'] #產品性別
    stockxRetailPrice = stockxItem['retailPrice']   #產品發行價
    stockxUrl = 'https://stockx.com/zh-tw/' + stockxItem['urlKey']  #產品連結

    pUrl = f'https://stockx.com/api/products/{stockxUrlKey}?includes=market'
    pHtml = requests.get(url=f'http://api.scrape.do?token=<token>&url={pUrl}', headers=headers)

    pOutput = json.loads(pHtml.text)

    stockxProductItem = pOutput['Product']
    stockxHighestBid = stockxProductItem['market']['highestBid']   #最高委買價(出價出到最高的)

    stockxSalesLast72Hours = stockxProductItem['market']['salesLast72Hours']   #近三日總成交量

    stockxDeadstockSold = stockxProductItem['market']['deadstockSold']   #近一年成交量
    stockAverageDeadstockPrice = stockxProductItem['market']['averageDeadstockPrice'] #成交均價
    stockChangeValue = stockxProductItem['market']['changeValue'] #漲跌
    stockChangePercentage = stockxProductItem['market']['changePercentage'] #漲幅

    stockxSortInfo = {}
    for i in range(len(stockxProductItem['children'])):
        stockxSizeIndex = list(stockxProductItem['children'])[i]
        stockxSortInfo[stockxProductItem['children'][stockxSizeIndex]['shoeSize']] = {'上次成交價':f"{stockxProductItem['children'][stockxSizeIndex]['market']['lastSale']}",'上次成交日期':f"{stockxProductItem['children'][stockxSizeIndex]['market']['lastSaleDate']}",'預估發行淨利潤':f"{stockxProductItem['children'][stockxSizeIndex]['market']['lastSale']*0.87 - stockxRetailPrice}",'近三日成交量':f"{stockxProductItem['children'][stockxSizeIndex]['market']['salesLast72Hours']}"}

    #=========
    SizeMen = {
        '2':'21 cm',
        '2.5':'21.5 cm',
        '3':'22 cm',
        '3.5':'22.5 cm',
        '4':'23 cm',
        '4.5':'23.5 cm',
        '5':'23.5 cm',
        '5.5':'24 cm',
        '6':'24 cm',
        '6.5':'24.5 cm',
        '7':'25 cm',
        '7.5':'25.5 cm',
        '8':'26 cm',
        '8.5':'26.5 cm',
        '9':'27 cm',
        '9.5':'27.5 cm',
        '10':'28 cm',
        '10.5':'28.5 cm',
        '11':'29 cm',
        '11.5':'29.5 cm',
        '12':'30 cm',
        '12.5':'30.5 cm',
        '13':'31 cm',
        '14':'32 cm',
        '15':'33 cm',
        '16':'34 cm',
        '17':'35 cm',
        '18':'36 cm',
        '19':'37 cm',
        '20':'38 cm',
        'M 2':'21 cm',
        'M 2.5':'21.5 cm',
        'M 3':'22 cm',
        'M 3.5':'22.5 cm',
        'M 4':'23 cm',
        'M 4.5':'23.5 cm',
        'M 5':'23.5 cm',
        'M 5.5':'24 cm',
        'M 6':'24 cm',
        'M 6.5':'24.5 cm',
        'M 7':'25 cm',
        'M 7.5':'25.5 cm',
        'M 8':'26 cm',
        'M 8.5':'26.5 cm',
        'M 9':'27 cm',
        'M 9.5':'27.5 cm',
        'M 10':'28 cm',
        'M 10.5':'28.5 cm',
        'M 11':'29 cm',
        'M 11.5':'29.5 cm',
        'M 12':'30 cm',
        'M 12.5':'30.5 cm',
        'M 13':'31 cm',
        'M 14':'32 cm',
        'M 15':'33 cm',
        'M 16':'34 cm',
        'M 17':'35 cm',
        'M 18':'36 cm',
        'M 19':'37 cm',
        'M 20':'38 cm'
    }

    SizeWomen = {
        '2':'19 cm',
        '2.5':'19.5cm',
        '3':'20 cm',
        '3.5':'20.5 cm',
        '4':'21 cm',
        '4.5':'21.5 cm',
        '5':'22 cm',
        '5.5':'22.5 cm',
        '6':'23 cm',
        '6.5':'23.5 cm',
        '7':'24 cm',
        '7.5':'24.5 cm',
        '8':'25 cm',
        '8.5':'25.5 cm',
        '9':'26 cm',
        '9.5':'26.5 cm',
        '10':'27 cm',
        '10.5':'27.5 cm',
        '11':'28 cm',
        '11.5':'28.5 cm',
        '12':'29 cm',
        '12.5':'30 cm',
        '13':'31 cm',
        '14':'32 cm',
        '15':'33 cm',
        '16':'34 cm',
        '17':'35 cm',
        '18':'36 cm',
        '19':'37 cm',
        '20':'38 cm',
        '2W':'19 cm',
        '2.5W':'19.5cm',
        '3W':'20 cm',
        '3.5W':'20.5 cm',
        '4W':'21 cm',
        '4.5W':'21.5 cm',
        '5W':'22 cm',
        '5.5W':'22.5 cm',
        '6W':'23 cm',
        '6.5W':'23.5 cm',
        '7W':'24 cm',
        '7.5W':'24.5 cm',
        '8W':'25 cm',
        '8.5W':'25.5 cm',
        '9W':'26 cm',
        '9.5W':'26.5 cm',
        '10W':'27 cm',
        '10.5W':'27.5 cm',
        '11W':'28 cm',
        '11.5W':'28.5 cm',
        '12W':'29 cm',
        '12.5W':'30 cm',
        '13W':'31 cm',
        '14W':'32 cm',
        '15W':'33 cm',
        '16W':'34 cm',
        '17W':'35 cm',
        '18W':'36 cm',
        '19W':'37 cm',
        '20W':'38 cm'
    }

    #=========
    productmsg = {
    "type": "bubble",
    "hero": {
        "type": "image",
        "url": stockxImg,
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
        "type": "uri",
        "uri": stockxUrl
        }
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": stockxTitle,
            "weight": "bold",
            "size": "xl"
        },
        {
            "type": "box",
            "layout": "baseline",
            "margin": "md",
            "contents": [
            {
                "type": "text",
                "text": "最高出價：",
                "size": "sm",
                "color": "#999999",
                "margin": "md",
                "flex": 0
            },
            {
                "type": "text",
                "text": str(stockxHighestBid),
                "color": "#d9cb62"
            }
            ]
        },
        {
            "type": "box",
            "layout": "vertical",
            "margin": "lg",
            "spacing": "sm",
            "contents": [
            {
                "type": "separator"
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "尺碼",
                        "size": "12px",
                        "align": "center"
                    }
                    ]
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "預估淨利潤",
                        "size": "12px",
                        "align": "center"
                    }
                    ]
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "成交價",
                        "size": "12px",
                        "align": "center"
                    }
                    ]
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "三日成交量",
                        "size": "12px",
                        "align": "center"
                    }
                    ]
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "成交日期",
                        "size": "12px",
                        "align": "center"
                    }
                    ]
                }
                ]
            },
            {
                "type": "separator"
            }
            ]
        },
        {
            "type": "box",
            "layout": "horizontal",
            "contents": [
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "規格",
                    "margin": "md",
                    "size": "sm",
                    "color": "#999999",
                    "align": "center"
                },
                {
                    "type": "text",
                    "text": "產品ID",
                    "margin": "md",
                    "size": "sm",
                    "color": "#999999",
                    "align": "center"
                },
                {
                    "type": "text",
                    "text": "發行價",
                    "margin": "md",
                    "size": "sm",
                    "color": "#999999",
                    "align": "center"
                },
                {
                    "type": "text",
                    "text": "性別",
                    "margin": "md",
                    "size": "sm",
                    "color": "#999999",
                    "align": "center"
                },
                {
                    "type": "text",
                    "text": "三日成交量",
                    "margin": "md",
                    "size": "sm",
                    "color": "#999999",
                    "align": "center"
                },
                {
                    "type": "text",
                    "text": "一年成交量",
                    "margin": "md",
                    "size": "sm",
                    "color": "#999999",
                    "align": "center"
                },
                {
                    "type": "text",
                    "text": "一年成交均價",
                    "margin": "md",
                    "size": "sm",
                    "color": "#999999",
                    "align": "center"
                },
                {
                    "type": "text",
                    "text": "漲跌",
                    "margin": "md",
                    "size": "sm",
                    "color": "#999999",
                    "align": "center"
                },
                {
                    "type": "text",
                    "text": "漲幅",
                    "margin": "md",
                    "size": "sm",
                    "color": "#999999",
                    "align": "center"
                }
                ]
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": str(stockxColourway),
                    "size": "sm",
                    "color": "#999999",
                    "margin": "md"
                },
                {
                    "type": "text",
                    "text": str(stockxStyleID),
                    "size": "sm",
                    "margin": "md",
                    "color": "#999999"
                },
                {
                    "type": "text",
                    "text": str(stockxRetailPrice),
                    "size": "sm",
                    "margin": "md",
                    "color": "#999999"
                },
                {
                    "type": "text",
                    "text": str(stockxGender),
                    "size": "sm",
                    "margin": "md",
                    "color": "#999999"
                },
                {
                    "type": "text",
                    "text": str(stockxSalesLast72Hours),
                    "size": "sm",
                    "margin": "md",
                    "color": "#999999"
                },
                {
                    "type": "text",
                    "text": str(stockxDeadstockSold), 
                    "size": "sm",
                    "margin": "md",
                    "color": "#999999"
                },
                {
                    "type": "text",
                    "text": str(stockAverageDeadstockPrice), 
                    "size": "sm",
                    "margin": "md",
                    "color": "#999999"
                },
                {
                    "type": "text",
                    "text": str(stockChangeValue), 
                    "size": "sm",
                    "margin": "md",
                    "color": "#999999"
                },
                {
                    "type": "text",
                    "text": f"{round(stockChangePercentage*100)}%", 
                    "size": "sm",
                    "margin": "md",
                    "color": "#999999"
                }
                ]
            }
            ]
        }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "uri",
            "label": "StockX",
            "uri": stockxUrl
            }
        },
        {
            "type": "box",
            "layout": "vertical",
            "contents": [],
            "margin": "sm"
        }
        ],
        "flex": 0
    },
    "size": "giga"
    }

    for i in range(len(stockxSortInfo)):
        appendSize = {'type': 'text', 'text': list(stockxSortInfo)[i], 'size': '12px', 'align': 'center', 'color': '#969690'}
        appendProfitR = {'type': 'text', 'text': str(round(float((stockxSortInfo[list(stockxSortInfo)[i]]['預估發行淨利潤'])))*30), 'size': '12px', 'align': 'center', 'color': '#b5336d'}
        appendProfitG = {'type': 'text', 'text': str(round(float((stockxSortInfo[list(stockxSortInfo)[i]]['預估發行淨利潤'])))*30), 'size': '12px', 'align': 'center', 'color': '#33b540'}
        appendLastPrice = {'type': 'text', 'text': str(stockxSortInfo[list(stockxSortInfo)[i]]['上次成交價']), 'size': '12px', 'align': 'center', 'color': '#969690'}
        appendLastVolume = {'type': 'text', 'text': str(stockxSortInfo[list(stockxSortInfo)[i]]['近三日成交量']), 'size': '12px', 'align': 'center', 'color': '#969690'}
        appendLastDate = {'type': 'text', 'text': str(stockxSortInfo[list(stockxSortInfo)[i]]['上次成交日期'][2:10]), 'size': '12px', 'align': 'center', 'color': '#969690'}

        productmsg["body"]["contents"][2]["contents"][1]["contents"][0]["contents"].append(appendSize)
        productmsg["body"]["contents"][2]["contents"][1]["contents"][2]["contents"].append(appendLastPrice)
        productmsg["body"]["contents"][2]["contents"][1]["contents"][3]["contents"].append(appendLastVolume)
        productmsg["body"]["contents"][2]["contents"][1]["contents"][4]["contents"].append(appendLastDate)
        if round(float((stockxSortInfo[list(stockxSortInfo)[i]]['預估發行淨利潤']))) > 0:
            productmsg["body"]["contents"][2]["contents"][1]["contents"][1]["contents"].append(appendProfitG)
        elif round(float((stockxSortInfo[list(stockxSortInfo)[i]]['預估發行淨利潤']))) <= 0:
            productmsg["body"]["contents"][2]["contents"][1]["contents"][1]["contents"].append(appendProfitR)
        SizeChange = productmsg["body"]["contents"][2]["contents"][1]["contents"][0]["contents"][i+1]["text"]
        try:
            if stockxGender == 'men':
                    productmsg["body"]["contents"][2]["contents"][1]["contents"][0]["contents"][i+1].update({"text":SizeMen[SizeChange]})
            elif stockxGender == 'women':
                    productmsg["body"]["contents"][2]["contents"][1]["contents"][0]["contents"][i+1].update({"text":SizeWomen[SizeChange]})
        except:
            continue
    return productmsg,stockxTitle