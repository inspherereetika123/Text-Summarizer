from typeguard import typechecked

@typechecked
def greet(name: str) -> str:
    return f"Hello, {name}!"
