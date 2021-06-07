# Binance Alert

Binance Alert is a demo program built in Python and QT, to request via API the price of cryptocurrencies in Binance Platform. This demo program send a request every 5 seconds and triggers a voice alert if the recovered price is out of range.

For demo purposes, this program can handle at most 4 cryptocurrencies price request


## Dependencies

![](https://img.shields.io/badge/dependencies-python-red) 

![](https://img.shields.io/badge/dependencies-QTDesigner-red)

![](https://img.shields.io/badge/dependencies-PYQT5-blue)

![](https://img.shields.io/badge/dependencies-PYPIWIN32-blue)


## Usage
Setup parameters in **appsetting.json** file

For each currency to request price, you must define the following information

```json
{
    "currency": [
        {
            "disable":"False",
            "currencyName":"ETC/USDT",
            "minRange": 60,
            "maxRange": 80,
            "binanceEndpoint":"https://api3.binance.com/api/v3/ticker/price"
        },
        {
            "disable":"False",
            "currencyName":"BTC/USDT",
            "minRange": 35000,
            "maxRange": 37000,
            "binanceEndpoint":"https://api3.binance.com/api/v3/ticker/price"
        },
        {
            "disable":"False",
            "currencyName":"ETH/USDT",
            "minRange": 2600,
            "maxRange": 2850,
            "binanceEndpoint":"https://api3.binance.com/api/v3/ticker/price"
        },
        {
            "disable":"True",
            "currencyName":"",
            "minRange": 0,
            "maxRange": 0,
            "binanceEndpoint":""
        }
    ]

}
```


## License

MIT License

Copyright (c)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.