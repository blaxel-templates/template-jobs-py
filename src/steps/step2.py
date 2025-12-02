from time import sleep
from opentelemetry import trace
import logging

logger = logging.getLogger(__name__)
tracer = trace.get_tracer("blaxel")

def step2(name: str) -> None:
    with tracer.start_as_current_span(name="step2"):
        logger.info(f"Step 2 {name}")
        step2_a(name)
        step2_b(name)
        logger.info(f"Step 2 {name} - End")


def step2_a(name: str) -> None:
    with tracer.start_as_current_span(name="step2_a"):
        logger.info(f"Step 2.a {name}")
        sleep(2)
        logger.info(f"Step 2.a {name} - End")


def step2_b(name: str) -> None:
    with tracer.start_as_current_span(name="step2_b"):
        logger.info(f"Step 2.b {name}")
        sleep(2)
        logger.info(f"Step 2.b {name} - End")
