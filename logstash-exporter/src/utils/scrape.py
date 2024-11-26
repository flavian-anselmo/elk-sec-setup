import logging
from src.scrapers.event_stats  import EventStats

logger = logging.getLogger(__name__)

class ScrapeMetrics:
    @staticmethod
    async def collect_metrics(logstash_url:str, LOGSTASH_PORT:str):
        try:
            EventStats.event_stats(logstash_url=logstash_url, LOGSTASH_PORT=LOGSTASH_PORT)
        except Exception as err:
            logger.error(f'Error: {err}')


              
              
      