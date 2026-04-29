# Ford Dealership Executive Suite

## Exercises
1. Create a **Stat** panel titled "Total Dealer Profit" that shows the sum of all profit.​
2. Modify `exercise.py` to include a `color` column in the data table to track which paint colors are selling.​
3. Create a **Table** panel titled "Recent Sales Activity" to see the 10 most recent sales. In the table, include the columns `sale_time`, `model`, `trim`, `color`, and `sale_price`.
4. (Challenge) Create a **Bar Gauge** panel titled "Sales by Model" to show the total quantity sold for model, sorted to highlight the #1 selling model.​

## Setup
1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/). Make sure engine is running
2. In the terminal, run `docker-compose up -d`
3. Open `localhost:3000` and ensure it is open to Grafana
4. In Grafana, go to `Connections` &rarr; `Data Sources` &rarr; `Add Data Source`
5. Search and select `PostgreSQL`
6. Enter these settings
     - Host: `host.docker.internal:5432`
     - Database: `car_data`
     - User: `admin`
     - Password: `password123`
     - TLS/SSL Mode: `disable`
     - Click `Save`
7. In the terminal, run the following
     - `python3 -m venv venv`
     - `source venv/bin/activate`
     - `pip install psycopg2-binary`
     - `python3 dealership_monitor.py`
8. The terminal should now be printing something like `SOLD: Antimatter Blue Bronco King Ranch for $74,769` continuously
9. Under Dashboard, press `New` and click import
10. Import `starter_dashboard.json` and `dashboard_key.json`
11. Set the dashboards to the Last 5 minutes and to refresh every 5s

## To stop running
In the terminal, run the following commands:
1. `Ctrl` + `C`
2. `deactivate`
3. `docker-compose down`

## To start running (after setup has already been done)
In the terminal, run the following commands:
1. `docker-compose up -d`
2. `source venv/bin/activate`
3. `python3 dealership_monitor.py`
