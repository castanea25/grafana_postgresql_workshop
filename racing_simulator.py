import psycopg2
import random
import time
from datetime import datetime, timezone

# Connection details
DB_SETTINGS = {
    "host": "localhost",
    "database": "racing_data",
    "user": "admin",
    "password": "password123",
    "port": "5432"
}

def run_generator():
    fuel = 100.0 # Start with a full tank
    
    try:
        conn = psycopg2.connect(**DB_SETTINGS)
        cur = conn.cursor()
        print("Connected! Upgrading telemetry suite...")

        # 1. Drop the old table and create the new one with more columns
        cur.execute("DROP TABLE IF EXISTS car_telemetry;")
        cur.execute("""
            CREATE TABLE car_telemetry (
                time TIMESTAMP,
                car_id TEXT,
                speed_mph INTEGER,
                engine_temp_c FLOAT,
                rpm INTEGER,
                fuel_percent FLOAT,
                tire_pressure_psi FLOAT,
                battery_voltage FLOAT
            );
        """)
        conn.commit()

        print("Sending expanded telemetry... (Ctrl+C to stop)")
        while True:
            now = datetime.now(timezone.utc)
            
            # Logic for new data
            speed = random.randint(70, 150)
            rpm = (speed * 40) + random.randint(-200, 200) # RPM scales with speed
            fuel -= 0.05 # Fuel drops slowly
            if fuel < 0: fuel = 100 # Refuel!
            
            temp = random.uniform(85.0, 105.0)
            tire_psi = random.uniform(30.0, 34.0)
            battery = random.uniform(13.2, 14.2)
            
            cur.execute(
                """INSERT INTO car_telemetry 
                   (time, car_id, speed_mph, engine_temp_c, rpm, fuel_percent, tire_pressure_psi, battery_voltage) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                (now, "Ford-GT-01", speed, temp, rpm, fuel, tire_psi, battery)
            )
            conn.commit()
            
            print(f"[{now.strftime('%H:%M:%S')}] Speed: {speed} | RPM: {rpm} | Fuel: {fuel:.1f}%")
            time.sleep(1)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    run_generator()
