import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
import requests
import re
import json

# 🔗 Ask local LLM (LLaMA3 via Ollama)
def ask_llm(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3", "prompt": prompt, "stream": False}
    )
    return response.json()["response"]

# 🧠 Extract ticker & period
def extract_query_info(user_input):
    prompt = (
        f"You are an AI that extracts stock information. "
        f"Only reply with a JSON object like this: {{\"ticker\": \"AAPL\", \"period\": \"1mo\"}}. "
        f"Do not include any explanation.\n\nUser input: '{user_input}'"
    )
    reply = ask_llm(prompt)

    try:
        match = re.search(r'\{[^{}]+\}', reply)
        if match:
            json_obj = json.loads(match.group())

            if json_obj["period"].lower() in ["last", "latest", "recent", "now"]:
                json_obj["period"] = "1d"

            return json_obj
        else:
            st.error("❌ Couldn't find a JSON object in LLM reply.")
            return None
    except Exception as e:
        st.error(f"❌ Failed to parse JSON from LLM: {e}")
        return None

# 🎨 Custom plot
def plot_stock_chart(df, ticker):
    is_up = df["Close"].iloc[-1] >= df["Close"].iloc[0]
    st.write(f"📈 {ticker.upper()} is {'up' if is_up else 'down'} today!")
    line_color = "#16c784" if is_up else "#ea3943"
    fill_color = "rgba(22,199,132,0.15)" if is_up else "rgba(234,57,67,0.15)"

    # Calculate y-axis range with padding
    y_min = df["Close"].min()
    y_max = df["Close"].max()
    y_range = y_max - y_min
    pad = y_range * 0.15 if y_range > 0 else 1  # 15% padding or 1 if flat
    yaxis_range = [y_min - pad, y_max + pad]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df.index,
        y=df["Close"],
        mode="lines",
        name=f"{ticker.upper()} Close Price",
        line=dict(color=line_color, width=3, shape="spline"),
        fill="tozeroy",
        fillcolor=fill_color,
        hovertemplate="<b>Date:</b> %{x|%b %d, %Y}<br><b>Close:</b> $%{y:.2f}<extra></extra>"
    ))

    fig.update_layout(
        showlegend=False,
        plot_bgcolor="#181a20",
        paper_bgcolor="#181a20",
        font=dict(color="#f5f6fa", family="Inter, Arial, sans-serif", size=16),
        margin=dict(l=0, r=0, t=0, b=0),
        xaxis=dict(
            showgrid=False,
            showline=False,
            zeroline=False,
            tickfont=dict(color="#888", size=13),
            ticks="outside",
            tickcolor="#222",
            ticklen=8,
            tickwidth=2,
            tickformat="%b %d",
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1D", step="day", stepmode="backward"),
                    dict(count=5, label="5D", step="day", stepmode="backward"),
                    dict(count=1, label="1M", step="month", stepmode="backward"),
                    dict(count=6, label="6M", step="month", stepmode="backward"),
                    dict(step="all", label="MAX")
                ]),
                bgcolor="#232323",
                activecolor=line_color,
                x=0.5,
                y=1.15,
                font=dict(color="#fff", size=13)
            ),
            type="date"
        ),
        yaxis=dict(
            showgrid=False,
            showline=False,
            zeroline=False,
            tickfont=dict(color="#888", size=13),
            range=yaxis_range  # <-- Set the padded y-axis range here
        ),
        hovermode="x unified"
    )

    return fig



# 🏁 App Start
st.set_page_config(page_title="Stock Bot", page_icon="📊")
st.title("📈 Stock Price Bot using LLM")

# 📝 User query input
user_input = st.text_input("Ask something like: 'Apple stock for the last 10 days'")

# 🧠 If user typed something
if user_input:
    query = extract_query_info(user_input)
    if query:
        ticker = query["ticker"]
        period = query["period"]


        stock = yf.Ticker(ticker)
        hist = stock.history(period=period)

        if hist.empty:
            st.error("⚠️ No data available for this ticker or date range.")
        else:
            current_price = hist["Close"].iloc[-1]
            prev_price = hist["Close"].iloc[0]
            pct_change = ((current_price - prev_price) / prev_price) * 100
            tgt_price = stock.info.get("targetMeanPrice", "N/A")
            target_price_str = f"${tgt_price:.2f}" if tgt_price != "N/A" else "N/A"
            st.write(f"📊 Current Price: ${current_price:.2f} |  🎯 Target Price: {target_price_str}")
            #metric_delta_color = "normal" if pct_change >= 0 else "inverse"
            #st.write(f"color: {metric_delta_color}")
            st.metric(f"{ticker.upper()} Current Price", f"${current_price:.2f}", delta=f"{pct_change:.2f}%")
            fig = plot_stock_chart(hist, ticker)
            st.plotly_chart(fig, use_container_width=True, config={
        "displayModeBar": False  # Hides the entire modebar (zoom, pan, save, etc.)
    })
    else:
        st.error("Sorry, I couldn't understand your request.")
