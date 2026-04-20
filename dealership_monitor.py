import psycopg2
import random
import time
from datetime import datetime, timezone

# Connection details
DB_SETTINGS = {
    "host": "localhost",
    "database": "racing_data", # We can use the same DB, just a new table
    "user": "admin",
    "password": "password123",
    "port": "5432"
}

# Ford Data for simulation
MODELS = ["F-150", "Mustang Mach-E", "Explorer", "Bronco", "Maverick", "Ranger"]
TRIMS = ["XL", "XLT", "Lariat", "King Ranch", "Platinum", "Raptor"]
COLORS = ["Iconic Silver", "Rapid Red", "Carbonized Gray", "Antimatter Blue", "Oxford White"]
PAYMENT_TYPES = ["Finance", "Lease", "Cash"]

def run_dealership_sim():
    try:
        conn = psycopg2.connect(**DB_SETTINGS)
        cur = conn.cursor()
        
        # 1. Create the Sales Table
        cur.execute("DROP TABLE IF EXISTS dealership_sales;")
        cur.execute("""
            CREATE TABLE dealership_sales (
                sale_time TIMESTAMP,
                model TEXT,
                trim TEXT,
                color TEXT,
                sale_price INTEGER,
                profit INTEGER,
                payment_method TEXT
            );
        """)
        conn.commit()
        print("Dealership Sales System Online!")

        while True:
            now = datetime.now(timezone.utc)
            model = random.choice(MODELS)
            trim = random.choice(TRIMS)
            color = random.choice(COLORS)
            payment = random.choice(PAYMENT_TYPES)
            
            # Generate realistic pricing/profit
            base_price = random.randint(35000, 85000)
            profit = int(base_price * random.uniform(0.05, 0.12)) # 5-12% profit
            
            cur.execute(
                """INSERT INTO dealership_sales 
                   (sale_time, model, trim, color, sale_price, profit, payment_method) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                (now, model, trim, color, base_price, profit, payment)
            )
            conn.commit()
            
            print(f"[{now.strftime('%H:%M:%S')}] SOLD: {color} {model} {trim} for ${base_price:,}")
            time.sleep(random.randint(2, 5)) # Sales happen every 2-5 seconds

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    run_dealership_sim()
