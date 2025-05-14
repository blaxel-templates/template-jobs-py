from time import sleep
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

def step2() -> None:
    start_span = tracer.start_span(name="step2")
    print("Step 2")
    step2_a()
    step2_b()
    print("Step 2 - End")
    start_span.end()

def step2_a() -> None:
    start_span = tracer.start_span(name="step2_a")
    print("Step 2.a")
    sleep(1)
    print("Step 2.a - End")
    start_span.end()

def step2_b() -> None:
    start_span = tracer.start_span(name="step2_b")
    print("Step 2.b")
    sleep(1)
    print("Step 2.b - End")
    start_span.end()