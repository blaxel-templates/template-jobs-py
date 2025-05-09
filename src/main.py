from blaxel.jobs import bl_job

def my_job(name: str) -> None:
    print(f"Hello, world {name}!")

bl_job.start(my_job)