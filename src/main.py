from blaxel.jobs import bl_start_job
import logging
from steps.step1 import step1
from steps.step2 import step2
from steps.step3 import step3

logger = logging.getLogger(__name__)

def my_job(lastname: str = None, firstname: str = None) -> None:
    logger.info(f"Hello, world {firstname} {lastname}!")
    step1()
    step2()
    step3()

bl_start_job.start(my_job)