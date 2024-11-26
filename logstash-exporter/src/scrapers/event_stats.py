import requests
from src.metricsTypes import gauge

class EventStats:
    @staticmethod
    def event_stats(logstash_url: str, LOGSTASH_PORT:str):
        '''
        event stats
        '''
        try:
            response = requests.get(f'http://{logstash_url}:{LOGSTASH_PORT}/_node/stats')
            if response.status_code == 200:
                stats = response.json()
                events = stats.get('events', {})
                gauge.events_input.set(events.get('in', 0))
                gauge.events_filtered.set(events.get('filtered', 0))
                gauge.events_output.set(events.get('out', 0))
                gauge.events_duration_ms.set(events.get('duration_in_millis', 0))
        except Exception as e:
            print(f"Error fetching events stats: {e}")