from blaxel.jobs import bl_job

def my_job(lastname: str = None, firstname: str = None) -> None:
    print(f"Hello, world {firstname} {lastname}!")

bl_job.start(my_job)