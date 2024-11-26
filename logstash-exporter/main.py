import requests
from prometheus_client import start_http_server, Gauge
import time

class LogstashEventsExporter:
    def __init__(self, logstash_url, metrics_port=9124, collect_interval=15):
        self.logstash_url = logstash_url
        self.metrics_port = metrics_port
        self.collect_interval = collect_interval
        
        # Events metrics
        self.events_input = Gauge('logstash_events_input_total', 'Total input events')
        self.events_filtered = Gauge('logstash_events_filtered_total', 'Total filtered events')
        self.events_output = Gauge('logstash_events_output_total', 'Total output events')
        self.events_duration_ms = Gauge('logstash_events_duration_ms', 'Event processing duration')
        
    def fetch_events_stats(self):
        try:
            response = requests.get(f'{self.logstash_url}/_node/stats')
            if response.status_code == 200:
                stats = response.json()
                events = stats.get('events', {})
                
                self.events_input.set(events.get('in', 0))
                self.events_filtered.set(events.get('filtered', 0))
                self.events_output.set(events.get('out', 0))
                self.events_duration_ms.set(events.get('duration_in_millis', 0))
        except Exception as e:
            print(f"Error fetching events stats: {e}")
    
    def collect_metrics(self):
        while True:
            self.fetch_events_stats()
            time.sleep(self.collect_interval)
    
    def start(self):
        start_http_server(self.metrics_port)
        self.collect_metrics()

def main():
    LOGSTASH_URL = 'http://logstash:9600'
    exporter = LogstashEventsExporter(LOGSTASH_URL)
    exporter.start()

if __name__ == '__main__':
    main()