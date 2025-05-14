# ENG22DS0004

Stock Microservice Description
This project consists of creating a microservice with FastAPI that retrieves real-time stock prices via the Twelve Data API. The microservice is comprised of:
A root endpoint (/) for serving a simple message indicating the service has started.
A stock price endpoint (/stock/{symbol}) that retrieves the real-time stock price of any symbol (e.g., AAPL) by querying the Twelve Data API.
Error handling for invalid stock symbols or problems with the API.

Important Features
FastAPI Framework: Deployed to create a high-performance API with less effort.
Asynchronous HTTP Requests: The application utilizes httpx to asynchronously retrieve data from the Twelve Data API, avoiding non-blocking I/O operations.
API Integration: Retrieves stock prices by making API calls to a third-party API (Twelve Data).

Basic Error Handling: When the API fails or the stock symbol is invalid, the user gets a suitable error message.

API Key Configuration: Implemented a free API key from Twelve Data to retrieve stock information.

Project Flow
Setup: Installed FastAPI and its dependencies (httpx, uvicorn) to host the server.
Developed API: Implemented endpoints to retrieve stock prices by symbol and return errors as appropriate.
Local Testing: Run the service locally at http://127.0.0.1:8000.
