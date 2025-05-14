from time import sleep
from opentelemetry import trace
import logging

logger = logging.getLogger(__name__)
tracer = trace.get_tracer(__name__)

def step3() -> None:
    start_span = tracer.start_span(name="step3")
    logger.info("Step 3")
    sleep(10)
    logger.info("Step 3 - End")
    start_span.end()