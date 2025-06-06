import requests
import os
import json

def extract_stocks_data_from_yahoo_finance_using_requests():
    current_dir = os.path.dirname(os.path.abspath(__file__))

    reports = [
        "MOST_ACTIVES",
        "DAY_GAINERS",
        "DAY_LOSERS",
        "FIFTY_TWO_WK_GAINERS",
        "FIFTY_TWO_WK_LOSERS"
    ]

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    output = []
    print(f"Data for report trending...")
    print(f"Fetch page 1")

    url = "https://query1.finance.yahoo.com/v1/finance/trending/US?count=25&fields=logoUrl%2ClongName%2CshortName%2CregularMarketChange%2CregularMarketChangePercent%2CregularMarketPrice%2Cticker%2Csymbol%2ClongName%2Csparkline%2CshortName%2CregularMarketPrice%2CregularMarketChange%2CregularMarketChangePercent%2CregularMarketVolume%2CaverageDailyVolume3Month%2CmarketCap%2CtrailingPE%2CfiftyTwoWeekChangePercent%2CfiftyTwoWeekRange%2CregularMarketOpen&format=true&useQuotes=true&quoteType=equity&lang=en-US&region=US&crumb=EvdmtZGpKMt"



    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        for quote in response.json()["finance"]["result"][0]["quotes"]:
            output.append(quote)
    
    except requests.RequestException as e:
        print("Request failed: ", e)
        print("Response: ", response.text)
    
    with open(f"{current_dir}/../data/processed/yahoo_finance_quotes_trending.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(output, indent=4))
    

    for report in reports:
        print(f"data: {report}")
        output = []
        start = 0
        page = 1
        while page < 22:
            print(f"Fetching page {page}...")
            url = f"https://query1.finance.yahoo.com/v1/finance/screener/predefined/saved?count=25&formatted=true&scrIds={report}&sortField=&sortType=&start={start}&useRecordsResponse=false&fields=ticker%2Csymbol%2ClongName%2Csparkline%2CshortName%2CregularMarketPrice%2CregularMarketChange%2CregularMarketChangePercent%2CregularMarketVolume%2CaverageDailyVolume3Month%2CmarketCap%2CtrailingPE%2CfiftyTwoWeekChangePercent%2CfiftyTwoWeekRange%2CregularMarketOpen&lang=en-US&region=US"

            try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()
                
                for quote in response.json()["finance"]["result"][0]["quotes"]:
                    output.append(quote)
            
            except requests.RequestException as e:
                print("Request failed:", e)
                print("Response Content:", response.text)
            
            start += 25
            page += 1

        with open(f"{current_dir}/../data/processed/yahoo_finance_quotes_{report.lower()}.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(output, indent=4))

    
if __name__ == "__main__":
    extract_stocks_data_from_yahoo_finance_using_requests()