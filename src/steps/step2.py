from time import sleep
from opentelemetry import trace
import logging

logger = logging.getLogger(__name__)
tracer = trace.get_tracer("blaxel")

def step2() -> None:
    with tracer.start_as_current_span(name="step2"):
        logger.info("Step 2")
        step2_a()
        step2_b()
        logger.info("Step 2 - End")


def step2_a() -> None:
    with tracer.start_as_current_span(name="step2_a"):
        logger.info("Step 2.a")
        sleep(2)
        logger.info("Step 2.a - End")


def step2_b() -> None:
    with tracer.start_as_current_span(name="step2_b"):
        logger.info("Step 2.b")
        sleep(2)
        logger.info("Step 2.b - End")
