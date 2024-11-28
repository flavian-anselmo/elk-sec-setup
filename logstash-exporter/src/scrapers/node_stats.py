import requests
import logging
from src.metricsTypes import gauge

logger = logging.getLogger(__name__)


class NodeStats:
    @staticmethod
    def node_stats(logstash_url: str, LOGSTASH_PORT:str):
        '''
        node stats
        '''
        try:
            headers = {"Content-Type": "application/json"}
            response = requests.get(f'http://{logstash_url}:{LOGSTASH_PORT}/_node/stats',headers=headers)
            if response.status_code == 200:
                stats = response.json()
                # events
                events = stats.get('events', {})
                gauge.events_input.set(events.get('in', 0))
                gauge.events_filtered.set(events.get('filtered', 0))
                gauge.events_output.set(events.get('out', 0))
                gauge.events_duration_ms.set(events.get('duration_in_millis', 0))

                # JVM Heap metrics
                jvm = stats.get('jvm', {})
                mem = jvm.get('mem', {})
                threads = jvm.get('threads',{})
                pool = mem.get('pool',{})
                young = pool.get('young',{})
                old = pool.get('old',{})
                survivor = pool.get('survivor',{})
                gc_young = jvm.get('gc',{}).get('young',{})
                gc_old = jvm.get('gc',{}).get('old',{})

                # JVM Threads Metrics
                gauge.jvm_threads_count.set(threads.get('count', 0))
                gauge.jvm_threads_peak_count.set(threads.get('peak_count', 0))
                gauge.jvm_heap_used_bytes.set(mem.get('heap_used_in_bytes', 0))
                gauge.jvm_heap_max_bytes.set(mem.get('heap_max_in_bytes', 0))
                gauge.jvm_heap_used_percent.set(mem.get('heap_used_percent', 0))
                gauge.jvm_uptime_millis.set(mem.get('uptime_in_millis',0))

                # jvm pools (old)
                gauge.jvm_pool_old_max_bytes.set(old.get('max_in_bytes',0))
                gauge.jvm_pool_old_peak_used_bytes.set(old.get('peak_used_in_bytes',0))
                gauge.jvm_pool_old_peak_max_bytes.set(old.get('peak_max_in_bytes',0))
                gauge.jvm_pool_old_used_bytes.set(old.get('used_in_bytes',0))

                # jvm pools (young)
                gauge.jvm_pool_young_max_bytes.set(young.get('max_in_bytes',0))
                gauge.jvm_pool_young_peak_used_bytes.set(young.get('peak_used_in_bytes',0))
                gauge.jvm_pool_young_peak_max_bytes.set(young.get('peak_max_in_bytes',0))
                gauge.jvm_pool_young_used_bytes.set(young.get('used_in_bytes',0))

                # jvm pools (survivor)
                gauge.jvm_pool_young_max_bytes.set(survivor.get('max_in_bytes',0))
                gauge.jvm_pool_young_peak_used_bytes.set(survivor.get('peak_used_in_bytes',0))
                gauge.jvm_pool_young_peak_max_bytes.set(survivor.get('peak_max_in_bytes',0))
                gauge.jvm_pool_young_used_bytes.set(survivor.get('used_in_bytes',0))

                # gc collectors
                gauge.jvm_gc_young_collection_count.set(gc_young.set('collection_count',0))
                gauge.jvm_gc_young_collection_time_millis.set(gc_young.set('collection_time_in_millis',0))
                gauge.jvm_gc_old_collection_count.set(gc_old.set('collection_count',0))
                gauge.jvm_gc_old_collection_time_millis.set(gc_old.set('collection_time_in_millis',0))

                # Node stats
                node_status = stats.get('status',{})
                if node_status == 'green':
                  gauge.node_status.set(1)
                if node_status == 'red':
                  gauge.node_status.set(0)
                if node_status == 'unkown':
                  gauge.node_status.set(2)
                if node_status == 'yellow':
                  gauge.node_status.set(3)

        
        except Exception as err:
            logger.error(f"Error fetching events stats: {err}")


