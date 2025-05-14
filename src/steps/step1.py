from time import sleep
from opentelemetry import trace
import logging

logger = logging.getLogger(__name__)
tracer = trace.get_tracer(__name__)


def step1() -> None:
    start_span = tracer.start_span(name="step1")
    logger.info("Step 1")
    sleep(10)
    logger.info("Step 1 - End")
    start_span.end()