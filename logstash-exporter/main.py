from prometheus_client import make_asgi_app
from hypercorn.asyncio import serve
import asyncio
import logging
from hypercorn.config import Config
from src.utils.scrape import ScrapeMetrics

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def collect():
    await ScrapeMetrics.collect_metrics('logstash','9600')
    
async def metrics_app(scope,receive, send):
    if scope['type'] == 'http' and scope['path'] == f'/metrics':
        await collect()
    app = make_asgi_app()
    await app(scope, receive, send)

async def main():
    hypercon_config = Config()
    hypercon_config.bind = [f"0.0.0.0:9124"]
    await serve(metrics_app, hypercon_config)

if __name__ == '__main__':
    asyncio.run(main())