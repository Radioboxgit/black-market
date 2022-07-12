# Black-Market 
# Python #requests  #beautifulsoup #pandas
Repo for Naira to dollar,euro,pounds parallel market scraped from
[This link](https://nairablackmarket.com/page/Black-market-exchange%20rates)

The project returns the tickers as well as the source of the exchange 

Sample output:

```
{'Date': '12/07/2022', 'Morning': [{'ticker': 'USD', 'buyRates': '618', 'sellRates': '621.88', 'source': 'P2P'}, {'ticker': 'EUR', 'buyRates': '624.24', 'sellRates': '628.16', 'source': 'P2P'}, {'ticker': 'GBP', 'buyRates': '735.71', 'sellRates': '740.33', 'source': 'P2P'}, {'ticker': 'USD', 'buyRates': '616', 'sellRates': '620', 'source': 'Aboki Rate'}, {'ticker': 'EUR', 'buyRates': '616', 'sellRates': '625', 'source': 'Aboki Rate'}, {'ticker': 'GBP', 'buyRates': '750', 'sellRates': '763', 'source': 'Aboki Rate'}, {'ticker': 'USD', 'buyRates': '616', 'sellRates': '621', 'source': 'BDC_Inflow_Bank_Transfer_Rates'}, {'ticker': 'EUR', 'buyRates': '615', 'sellRates': '635', 
'source': 'BDC_Inflow_Bank_Transfer_Rates'}, {'ticker': 'GBP', 'buyRates': '750', 'sellRates': '760', 'source': 'BDC_Inflow_Bank_Transfer_Rates'}], 'Afternoon': [{'ticker': 'USD', 'buyRates': '618', 'sellRates': '621.88', 'source': 'P2P'}, {'ticker': 'EUR', 'buyRates': '624.24', 'sellRates': '628.16', 'source': 'P2P'}, {'ticker': 'GBP', 'buyRates': '735.71', 'sellRates': '740.33', 'source': 'P2P'}, {'ticker': 'USD', 'buyRates': '616', 'sellRates': '620', 'source': 'Aboki Rate'}, {'ticker': 'EUR', 'buyRates': '616', 'sellRates': '625', 'source': 'Aboki Rate'}, {'ticker': 'GBP', 'buyRates': '750', 'sellRates': '763', 'source': 'Aboki Rate'}, {'ticker': 'USD', 'buyRates': '616', 'sellRates': '621', 'source': 'Inflow/Bank TransferRates'}, {'ticker': 'EUR', 'buyRates': '615', 'sellRates': '635', 'source': 'Inflow/Bank TransferRates'}, {'ticker': 'GBP', 'buyRates': '750', 'sellRates': '760', 'source': 'Inflow/Bank TransferRates'}], 'Evening': [{'ticker': 'USD', 'buyRates': '618', 'sellRates': '621.88', 'source': 'P2P'}, {'ticker': 'EUR', 'buyRates': '624.24', 'sellRates': '628.16', 'source': 'P2P'}, {'ticker': 'GBP', 'buyRates': '735.71', 'sellRates': '740.33', 'source': 'P2P'}, {'ticker': 'USD', 'buyRates': '616', 'sellRates': '620', 'source': 'Aboki Rate'}, {'ticker': 'EUR', 'buyRates': '616', 'sellRates': '625', 'source': 'Aboki Rate'}, {'ticker': 'GBP', 'buyRates': '750', 'sellRates': '763', 'source': 'Aboki Rate'}, {'ticker': 'USD', 'buyRates': '616', 'sellRates': '621', 'source': 'BDC_Inflow_Bank_Transfer_Rates'}, {'ticker': 'EUR', 'buyRates': '615', 'sellRates': '635', 'source': 'BDC_Inflow_Bank_Transfer_Rates'}, {'ticker': 'GBP', 'buyRates': '750', 'sellRates': '760', 'source': 'BDC_Inflow_Bank_Transfer_Rates'}]}

```


