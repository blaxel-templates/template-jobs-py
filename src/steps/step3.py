from time import sleep
from opentelemetry import trace
import logging

logger = logging.getLogger(__name__)
tracer = trace.get_tracer("blaxel")

def step3() -> None:
    with tracer.start_as_current_span(name="step3"):
        logger.info("Step 3")
        sleep(2)
        logger.info("Step 3 - End")
