# grafana_postgresql_workshop

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
