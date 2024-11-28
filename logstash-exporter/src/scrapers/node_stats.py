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

                #  queue event count
                queue = stats.get('queue',{})
                gauge.queue_events_count.set(queue.get('events_count',0))

                # pipelines (overall)
                pipeline = stats.get('pipeline',{})
                gauge.pipeline_batch_delay.set(pipeline.get('workers',0))
                gauge.pipeline_batch_size.set(pipeline.get('batch_size',0))
                gauge.pipeline_workers.set(pipeline.get('batch_delay',0))

                # pipeline realods (overall)
                reloads = stats.get('reloads',{})
                gauge.reload_failures.set(reloads.get('failures',0))
                gauge.reload_successes.set(reloads.get('successes',0))

                # JVM Heap metrics
                jvm = stats.get('jvm', {})
                mem = jvm.get('mem', {})
                threads = jvm.get('threads',{})
                pool = mem.get('pool',{})
                young = pool.get('young',{})
                old = pool.get('old',{})
                survivor = pool.get('survivor',{})
                gc = jvm.get('gc',{})
                gc_old = gc.get('old',{})
                gc_young = gc.get('young',{})

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

                # gc collectors (young & old)
                gauge.jvm_gc_young_collection_count.set(gc_young.get('collection_count',0))
                gauge.jvm_gc_young_collection_time_millis.set(gc_young.get('collection_time_in_millis',0))
                gauge.jvm_gc_old_collection_count.set(gc_old.get('collection_count',0))
                gauge.jvm_gc_old_collection_time_millis.set(gc_old.get('collection_time_in_millis',0))

                # processes
                process = stats.get('process', {})
                process_mem = process.get('mem',{})
                process_cpu = process.get('cpu',{})
                process_cpu_load_avg = process_cpu.get('load_average',{})
                gauge.process_open_file_descriptors.set(process.get('open_file_descriptors',0))
                gauge.process_peak_open_file_descriptors.set(process.get('peak_open_file_descriptors',0))
                gauge.process_max_file_descriptors.set(process.get('max_file_descriptors',0))
                gauge.process_mem_total_virtual_bytes.set(process_mem.get('total_virtual_in_bytes',0))
                gauge.process_cpu_percent.set(process_cpu.get('total_in_millis',0))
                gauge.process_cpu_total_millis.set(process_cpu.get('percent',0))
                gauge.process_cpu_load_average_1m.set(process_cpu_load_avg.get('1m',0))
                gauge.process_cpu_load_average_5m.set(process_cpu_load_avg.get('5m',0))
                gauge.process_cpu_load_average_15m.set(process_cpu_load_avg.get('15m',0))

            




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
            logger.error(f"NodeStatsCollectionError: {err}")


