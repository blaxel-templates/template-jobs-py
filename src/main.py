from blaxel.jobs import bl_start_job
import logging

logger = logging.getLogger(__name__)

def my_job(lastname: str = None, firstname: str = None) -> None:
    logger.info(f"Hello, world {firstname} {lastname}!")

bl_start_job.start(my_job)