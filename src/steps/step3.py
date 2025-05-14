from time import sleep
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

def step3() -> None:
    start_span = tracer.start_span(name="step3")
    print("Step 3")
    sleep(1)
    print("Step 3 - End")
    start_span.end()