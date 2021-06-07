import requests
import json

class currency:
    currencyName : str
    minRange : float
    maxRange : float
    currentPrice : float
    binanceEndpoint : str
    disable : bool



class readCurrenciesFile:
    
    objCurrencyListing = []

    def __init__(self) -> None:

        #READ APPSETTING.JSON
        objFile = open("appsetting.json")

        data = json.load(objFile)

        for objData in data["currency"]:

            node = currency()
            node.disable = objData["disable"]
            node.currencyName = objData["currencyName"]
            node.minRange = objData["minRange"]
            node.maxRange = objData["maxRange"]
            node.binanceEndpoint = objData["binanceEndpoint"]

            #ADD CURRENCY LISTING
            self.objCurrencyListing.append(node)

    def getCurrencyListing(self):

        return self.objCurrencyListing
        
    

class BinanceApiRequest:
    
    def requestApi(self, objCurrency):

        requestURL = objCurrency.binanceEndpoint + "?symbol=" + objCurrency.currencyName.replace('/', '') 

        responseObject = requests.get(requestURL)
        
        result = responseObject.json()
        
        currentPrice = float(result["price"])
        
        return currentPrice