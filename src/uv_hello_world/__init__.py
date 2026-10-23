from uv_hello_world_api import add


def main() -> None:
    """The main entrypoint to the application."""

    print(f"Hello, world! 9 + 10 is {add(9, 10)}")


if __name__ == "__main__":
    main()
