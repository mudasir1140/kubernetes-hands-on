# Exercise 6: Real-Time Operations Monitoring and Alerting

## Project Overview

This exercise simulates real-time delivery operations for ZAPPTTO using Python, Prometheus, and Grafana. It monitors delivery metrics and defines alert rules for high pending deliveries and increased average delivery time.

## Technologies Used

- Python
- Prometheus
- Grafana
- Docker
- PromQL

## Project Structure

```text
Exercise-6/
├── delivery_metrics.py
├── prometheus.yml
├── alert_rules.yml
└── README.md
```

## Monitored Metrics

| Metric | Description |
|---|---|
| `total_deliveries` | Total simulated deliveries |
| `pending_deliveries` | Deliveries waiting to be processed |
| `on_the_way_deliveries` | Deliveries currently in transit |
| `average_delivery_time_seconds` | Simulated average delivery time in seconds |

The Python script updates these simulated metrics every five seconds and exposes them on port 8000.

## Setup and Execution

### 1. Start the Python metrics application

From the Exercise-6 directory, activate the existing Python environment and start the application:

```bash
source ../Exercise-5/.venv/bin/activate
python delivery_metrics.py
```

Keep this terminal running.

### 2. Start Prometheus

Open another terminal in the Exercise-6 directory:

```bash
docker run -d \
  --name prometheus \
  --add-host=host.docker.internal:host-gateway \
  -p 9090:9090 \
  -v "$PWD/prometheus.yml:/etc/prometheus/prometheus.yml:ro" \
  -v "$PWD/alert_rules.yml:/etc/prometheus/alert_rules.yml:ro" \
  prom/prometheus
```

Prometheus interface: http://localhost:9090

Targets page: http://localhost:9090/targets

### 3. Start Grafana

```bash
docker run -d \
  --name grafana \
  -p 3000:3000 \
  grafana/grafana
```

Grafana interface: http://localhost:3000

Configure Prometheus as the Grafana data source using:

```text
http://host.docker.internal:9090
```

Use the dashboard to visualize the four delivery metrics.

## Grafana Dashboard Panels

1. Total Deliveries — `total_deliveries`
2. Pending Deliveries — `pending_deliveries`
3. Deliveries On the Way — `on_the_way_deliveries`
4. Average Delivery Time — `average_delivery_time_seconds`

## Alert Rules

| Alert | Condition | Severity |
|---|---|---|
| HighPendingDeliveries | `pending_deliveries > 10` for 15 seconds | Warning |
| HighAverageDeliveryTime | `average_delivery_time_seconds > 30` for 15 seconds | Critical |

Prometheus evaluates these rules according to the configuration in `alert_rules.yml`.

## Verification

- Confirm that the Prometheus and delivery-service targets are UP.
- Check the delivery metrics in the Prometheus expression browser.
- Verify that the Grafana dashboard panels display metric values.
- Check the Prometheus Alerts page to observe alert states.

## Notes

This exercise uses randomly generated simulated delivery data. The metrics do not represent real delivery operations.

The Python application and Docker containers must be running for live monitoring. Jenkins pipeline integration can be documented separately if required by the lab instructions.
CI polling test: Jenkins checks this repository for new commits.
