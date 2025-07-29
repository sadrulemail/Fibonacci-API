# 🚀 Fibonacci Sequence API

A production-ready REST API to compute Fibonacci numbers. Deploys with Docker + CI/CD.

## ▶️ Quick Start

```bash
# 1. Clone repo
git clone https://github.com/yourusername/fibonacci-api.git
cd fibonacci-api

# 2. Run with Docker (recommended)
docker build -t fib-api .
docker run -p 5000:5000 fib-api

# 3. Test API
curl "http://localhost:5000/fibonacci?n=10"
# {"input":10,"result":55}