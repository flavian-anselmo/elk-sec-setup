from prometheus_client import Gauge

# Events metrics
events_input = Gauge('logstash_events_input_total', 'Total input events')
events_filtered = Gauge('logstash_events_filtered_total', 'Total filtered events')
events_output = Gauge('logstash_events_output_total', 'Total output events')
events_duration_ms = Gauge('logstash_events_duration_ms', 'Event processing duration')