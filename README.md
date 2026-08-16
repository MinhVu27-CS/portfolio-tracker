# Portfolio Tracker

A live financial dashboard tracking a multi-stock portfolio — real-time prices, allocation breakdown, and daily performance, built with Python and deployed as an interactive Streamlit app.

## What it does

Tracks 5 holdings (NVDA, LLY, META, VOO, GOOGL) and, using live market data, calculates:
- Current price and total value per stock
- Portfolio allocation percentage per holding
- Day-over-day dollar and percent change, per stock and portfolio-wide

## Features

- **Live price data** — pulled directly from Yahoo Finance via the `yfinance` API, no manual data entry
- **Portfolio metrics** — total value and total day change displayed with Streamlit's `st.metric`, including a colored up/down delta indicator
- **Formatted data table** — every holding's price, previous close, day change, shares, total value, and allocation %, displayed as an interactive table with proper `$`/`%` formatting via `column_config`
- **Allocation pie chart** — custom-colored, theme-matched (transparent background, white text) to fit the dashboard's dark mode

## How to run

```bash
uv venv
uv pip install yfinance pandas matplotlib streamlit
.venv\Scripts\python.exe -m streamlit run main.py
```

## What I learned

- Working with a real financial API (`yfinance`) and structuring live data into nested dictionaries
- Pandas fundamentals — DataFrames, `.between_time()`, boolean masking, aggregation (`.max()`, `.min()`)
- Building and interpreting financial calculations (allocation %, day change) from raw price data
- Data visualization with Matplotlib, including the `fig`/`ax` pattern needed for embedding in Streamlit and customizing chart theming (transparency, custom colors, text styling)
- Streamlit fundamentals — `st.metric`, `st.dataframe` with `column_config`, `st.pyplot`, and Streamlit's "rerun the whole script" execution model
- Real environment debugging — Windows PATH issues, `uv` virtual environments, and pointing VS Code at the correct interpreter

## Status

Working prototype, single-file (`main.py`), hardcoded share counts. Planned next steps (see roadmap): a SQLite database to track historical prices and performance over time, wrapping the logic in a Flask/FastAPI backend, and deploying it live on the web.
