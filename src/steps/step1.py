from time import sleep
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

def step1() -> None:
    start_span = tracer.start_span(name="step1")
    print("Step 1")
    sleep(1)
    print("Step 1 - End")
    start_span.end()