import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title("Minh's Portfolio Tracker")

watch_list = {}

tickers = {"NVDA": 15.41, "LLY": 10.87, "META": 5.32, "VOO": 20, "GOOGL": 8}

for stock, shares in tickers.items():
    ticker_obj = yf.Ticker(stock)
    data = ticker_obj.history(period="2d")
    close_price = round(data['Close'].iloc[1], 2)
    previous_close_price = round(data['Close'].iloc[0], 2)
    percent_change = round(((close_price - previous_close_price) / previous_close_price) * 100, 2)
    watch_list[stock] = {
        "Price": close_price,
        "Previous_Close": previous_close_price,
        "Day_Change": round(close_price - previous_close_price, 2),
        "Percent_Change": percent_change,
        "Shares": shares,
        "Total_Value": round(close_price * shares, 2)
    }

portfolio_value = 0
for stock in watch_list:
    portfolio_value += watch_list[stock]["Total_Value"]
for stock in watch_list:
    allocation_percentage = (watch_list[stock]["Total_Value"] / portfolio_value) * 100
    watch_list[stock]["Allocation_%"] = round(allocation_percentage, 2)

portfolio_change = 0
for stock in watch_list:
    portfolio_change += watch_list[stock]["Day_Change"] * watch_list[stock]["Shares"]

#print(f"Portfolio Value: ${round(portfolio_value, 2)}")
st.metric(label="Portfolio Value", value=round(portfolio_value, 2), delta=round(portfolio_change, 2))
#print(f"Portfolio Change: ${round(portfolio_change, 2)}")

for stock in watch_list:
    print(f"{stock}: $ Tdy: ({watch_list[stock]['Day_Change']}) % Tdy: ({watch_list[stock]['Percent_Change']}%) Price: ${watch_list[stock]['Price']}, Allocation Percentage: {watch_list[stock]['Allocation_%']}%")

stocks = list(watch_list.keys())
stock_values = [watch_list[stock]["Total_Value"] for stock in stocks]

plt.pie(stock_values, labels=stocks, autopct='%1.1f%%')
plt.title('InvestmentPortfolio')
fig, ax = plt.subplots()
fig.patch.set_alpha(0)
ax.pie(stock_values, labels=stocks, autopct='%1.1f%%', textprops={'color': 'white'}, colors=['darkgreen', 'darkred', 'darkblue', 'darkgray', 'darkviolet'])


df = pd.DataFrame(watch_list).T
st.dataframe(df, column_config={
    "Price": st.column_config.NumberColumn(format="$%.2f"),
    "Previous_Close": st.column_config.NumberColumn(format="$%.2f"),
    "Day_Change": st.column_config.NumberColumn(format="%.2f"),
    "Percent_Change": st.column_config.NumberColumn(format="%.2f%%"),
    "Total_Value": st.column_config.NumberColumn(format="$%.2f"),
    "Allocation_%": st.column_config.NumberColumn(format="%.2f%%")
})
st.pyplot(fig)