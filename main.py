import requests
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

def run_etl():
    # 1. Extract (ดึงข้อมูล)
    print("Extracting data...")
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&per_page=5"
    response = requests.get(url)
    data = response.json()

    # 2. Transform (แปลงข้อมูล)
    print("Transforming data...")
    df = pd.DataFrame(data)
    df = df[['id', 'symbol', 'current_price', 'market_cap']] # เลือกเฉพาะที่จำเป็น
    df['extracted_at'] = datetime.now() # เพิ่มเวลาที่ดึงข้อมูล

    # 3. Load (เก็บลง Database)
    # หมายเหตุ: ในเครื่องจริงต้องเปลี่ยน URL เป็นของฐานข้อมูลคุณ
    print("Data sample:")
    print(df.head())
    print("\nETL Process finished successfully!")

if __name__ == "__main__":
    run_etl()
