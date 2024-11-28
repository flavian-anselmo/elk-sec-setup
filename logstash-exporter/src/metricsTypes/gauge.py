from prometheus_client import Gauge

# Events metrics
events_input = Gauge('logstash_events_input_total', 'Total input events')
events_filtered = Gauge('logstash_events_filtered_total', 'Total filtered events')
events_output = Gauge('logstash_events_output_total', 'Total output events')
events_duration_ms = Gauge('logstash_events_duration_ms', 'Event processing duration')

# jvm 
# JVM Thread Metrics
jvm_threads_count = Gauge('logstash_jvm_threads_count', 'JVM Thread Count')
jvm_threads_peak_count = Gauge('logstash_jvm_threads_peak_count', 'JVM Peak Thread Count')

# JVM Pool Metrics
jvm_pool_young_used_bytes = Gauge('logstash_jvm_pool_young_used_bytes', 'JVM Young Generation Pool Used in Bytes')
jvm_pool_young_max_bytes = Gauge('logstash_jvm_pool_young_max_bytes', 'JVM Young Generation Pool Max in Bytes')
jvm_pool_young_peak_used_bytes = Gauge('logstash_jvm_pool_young_peak_used_bytes', 'JVM Young Generation Pool Peak Used in Bytes')
jvm_pool_young_peak_max_bytes = Gauge('logstash_jvm_pool_young_peak_max_bytes', 'JVM Young Generation Pool Peak Max in Bytes')
jvm_pool_old_used_bytes = Gauge('logstash_jvm_pool_old_used_bytes', 'JVM Old Generation Pool Used in Bytes')
jvm_pool_old_max_bytes = Gauge('logstash_jvm_pool_old_max_bytes', 'JVM Old Generation Pool Max in Bytes')
jvm_pool_old_peak_used_bytes = Gauge('logstash_jvm_pool_old_peak_used_bytes', 'JVM Old Generation Pool Peak Used in Bytes')
jvm_pool_old_peak_max_bytes = Gauge('logstash_jvm_pool_old_peak_max_bytes', 'JVM Old Generation Pool Peak Max in Bytes')
jvm_pool_survivor_used_bytes = Gauge('logstash_jvm_pool_survivor_used_bytes', 'JVM Survivor Pool Used in Bytes')
jvm_pool_survivor_max_bytes = Gauge('logstash_jvm_pool_survivor_max_bytes', 'JVM Survivor Pool Max in Bytes')
jvm_pool_survivor_peak_used_bytes = Gauge('logstash_jvm_pool_survivor_peak_used_bytes', 'JVM Survivor Pool Peak Used in Bytes')
jvm_pool_survivor_peak_max_bytes = Gauge('logstash_jvm_pool_survivor_peak_max_bytes', 'JVM Survivor Pool Peak Max in Bytes')

 # JVM GC Metrics
jvm_gc_young_collection_count = Gauge('logstash_jvm_gc_young_collection_count', 'Young Generation Garbage Collection Count')
jvm_gc_young_collection_time_millis = Gauge('logstash_jvm_gc_young_collection_time_millis', 'Young Generation Garbage Collection Time in Milliseconds')
jvm_gc_old_collection_count = Gauge('logstash_jvm_gc_old_collection_count', 'Old Generation Garbage Collection Count')
jvm_gc_old_collection_time_millis = Gauge('logstash_jvm_gc_old_collection_time_millis', 'Old Generation Garbage Collection Time in Milliseconds')


jvm_heap_used_bytes = Gauge('logstash_jvm_heap_used_in_bytes','Current JVM heap memory used by Logstash process in bytes')
jvm_heap_max_bytes = Gauge('logstash_jvm_heap_max_in_bytes','Maximum JVM heap memory available to Logstash process in bytes')
jvm_heap_used_percent = Gauge('logstash_jvm_heap_used_percent','Percentage of JVM heap memory currently in use by Logstash')

# JVM Uptime
jvm_uptime_millis = Gauge('logstash_jvm_uptime_millis', 'JVM Uptime in Milliseconds')

# Node status
node_status = Gauge('logstash_node_status', '1 for Healthy (GREEN), 0 for Unhealthy(RED), 2 for unknown, 3 for Functionality degraded (YELLOW)')