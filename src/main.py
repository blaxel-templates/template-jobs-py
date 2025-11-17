import logging

from blaxel.core.jobs import bl_start_job
from opentelemetry import trace

from steps.step1 import step1
from steps.step2 import step2
from steps.step3 import step3

logger = logging.getLogger(__name__)
tracer = trace.get_tracer(__name__)


def my_job(name: str) -> None:
    with tracer.start_as_current_span(name="myjob"):
        logger.info(f"Hello, {name}")
        step1()
        step2()
        step3()


bl_start_job.start(my_job)
