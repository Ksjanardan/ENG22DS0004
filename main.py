from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Stock Microservice is running."}

@app.get("/stock/{symbol}")
async def get_stock_price(symbol: str):
    # Replace with your actual API key
    api_key = "dbd077361d974545baaf4d68ccdab1b0"
    url = f"https://api.twelvedata.com/price?symbol={symbol}&apikey={api_key}"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
            "symbol": symbol.upper(),
            "price": data.get("price")
        }
    else:
        return {
            "error": "Failed to fetch stock data",
            "details": response.json()
        }
