import yfinance as yf
from datetime import date

class StockProfitCalculator: 
    def getProceeds(self, allotment: int, finalPrice: int) -> int: 
        return allotment * finalPrice

    def getCost(self, allotment: int, initialPrice: int, finalPrice: int, buyCommission: int, sellCommission:int, taxRate: int) -> int: 
        # Total purchase price
        totalPurchasePrice = allotment * initialPrice

        # Capital gain after tax
        diffPrice = finalPrice - initialPrice
        profit = diffPrice * allotment - buyCommission - sellCommission
        capitalGainTax =  profit * (taxRate / 100)

        return round(totalPurchasePrice + capitalGainTax + buyCommission + sellCommission, 2)

    def getNetProfit(self, proceeds: int, cost: int) -> int: 
        return proceeds - cost

    def getInvestmentReturn(self, netProfit: int, cost: int) -> int: 
        return round((netProfit / cost) * 100, 2)

    def getBreakEven(self, allotment: int, buyCommission: int, sellCommission: int, initialPrice: int) -> int: 
        diffPrice = (buyCommission + sellCommission) / allotment
        finalPrice = diffPrice + initialPrice
        return finalPrice

    def calculateStockProfit(self, stockSymbol: str, allotment: int, finalPrice: int, sellCommission: int, 
        initialPrice: int, buyCommission: int, taxRate: int) -> [int]: 

        # Return an array of proceeds, cost, net profit, return on investment, break even price
        profit_report = [None] * 5

        profit_report[0] = self.getProceeds(allotment, finalPrice)
        profit_report[1] = self.getCost(allotment, initialPrice, finalPrice, buyCommission, sellCommission, taxRate)
        profit_report[2] = self.getNetProfit(profit_report[0], profit_report[1])
        profit_report[3] = self.getInvestmentReturn(profit_report[2], profit_report[1])
        profit_report[4] = self.getBreakEven(allotment, buyCommission, sellCommission, initialPrice)

        # Print expense report 
        print("====== Report Expense for ", stockSymbol, " =====\n")
        print("Proceeds: ", profit_report[0])
        print("Cost: ", profit_report[1])
        print("Net Profit: ", profit_report[2])
        print("Return on Investment: ", profit_report[3])
        print("To break even, you should have a final share price of ", profit_report[4])

    def stockAPI(self, stockCode: str):
        try: 
            code = yf.Ticker(stockCode)
            info = code.info
            print('\n')
            print(date.today().strftime("%a %b %d %I:%M:%S %Z%Y"))
            print("{} ({})".format(info['longName'],stockCode.upper()))
            price = info['regularMarketPrice']
            valueChange = info['regularMarketPrice'] - info['previousClose']
            percentChange = valueChange / info['previousClose'] * 100
            print(f'{price} {valueChange:.2f} ({percentChange:.2f}%)')

        except KeyError: 
            print("Connection error!")

        except Exception:
            print("Invalid stock code, please try again.")

        
if __name__ == "__main__": 
    tickerSymbol = "ADBE"
    allotment = 100
    initialPrice = 25
    finalPrice = 110
    buyCommission = 10
    sellCommission = 15
    taxRate = 15

    c = StockProfitCalculator()
    # hw 1
    # c.calculateStockProfit(tickerSymbol, allotment, finalPrice, sellCommission, initialPrice, buyCommission, taxRate)

    # hw 2
    c.stockAPI("ADBE")
    c.stockAPI("MSFT")
    c.stockAPI("AAPL")