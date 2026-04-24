import psycopg2
import random
import time
from datetime import datetime, timezone

""" --- STEP 1: CREATE THE TABLE --- """
def create_table(cur):
    create_query = """
    CREATE TABLE dealership_sales (
        sale_time TIMESTAMP,
        model TEXT,
        trim TEXT,
        sale_price INTEGER,
        profit INTEGER,
        payment_method TEXT,
        color TEXT
    );
    """
    # Executes the query to create the table (do not modify)
    cur.execute(create_query)

""" --- STEP 2: INSERT DATA INTO DATABASE --- """
def insert_sale_into_database(cur, sale_data):
    """
    Example of what sale_data looks like:
    {
        "sale_time": 2026-05-01 14:15:49.544191,
        "model": "F-150",
        "trim": "Lariat",
        "sale_price": 45000,
        "profit": 5000,
        "payment_method": "Finance",
        "color": "Iconic Silver"
    }
    """
    insert_query = """
    INSERT INTO dealership_sales (
        sale_time,
        model,
        trim,
        sale_price,
        profit,
        payment_method,
        color
    )
    VALUES (
        %(sale_time)s,
        %(model)s,
        %(trim)s,
        %(sale_price)s,
        %(profit)s,
        %(payment_method)s,
        %(color)s
    )
    """
    # Executes the query to insert the data (do not modify)
    cur.execute(insert_query, sale_data)

""" --- DB CONFIGURATION --- (do not modify) """
DB_SETTINGS = {
    "host": "localhost",
    "database": "car_data",
    "user": "admin",
    "password": "password123",
    "port": "5432"
}

""" --- MAIN PROGRAM --- (do not modify) """
def run_monitor():
    conn = psycopg2.connect(**DB_SETTINGS)
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS dealership_sales;")

    create_table(cur)
    conn.commit()
    print("Dealership Sales System Online!")

    try:
        while True:
            MODELS = ["F-150", "Mustang Mach-E", "Explorer", "Bronco", "Maverick", "Ranger"]
            TRIMS = ["XL", "XLT", "Lariat", "King Ranch", "Platinum", "Raptor"]
            PAYMENT_TYPES = ["Finance", "Lease", "Cash"]
            COLORS = ["Iconic Silver", "Rapid Red", "Carbonized Gray", "Antimatter Blue", "Oxford White"]

            now = datetime.now(timezone.utc)
            model = random.choice(MODELS)
            trim = random.choice(TRIMS)
            sale_price = random.randint(35000, 85000)
            profit = int(sale_price * random.uniform(0.05, 0.12))
            payment_method = random.choice(PAYMENT_TYPES)
            color = random.choice(COLORS)

            sale_data = {
            "sale_time": now,
            "model": model,
            "trim": trim,
            "sale_price": sale_price,
            "profit": profit,
            "payment_method": payment_method,
            "color": color
            }

            insert_sale_into_database(cur, sale_data)

            conn.commit()
            print(f"[{now.strftime('%H:%M:%S')}] SOLD: {color} {model} {trim} for ${sale_price:,}")
            time.sleep(5)

    except KeyboardInterrupt:
        print("Monitoring stopped.")
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    run_monitor()


