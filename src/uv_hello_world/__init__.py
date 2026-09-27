from uv_hello_world_api import add


def main() -> None:
    """The main entrypoint to the application."""

    print(f"Hello, world! 5 + 9 is {add(5, 9)}")


if __name__ == "__main__":
    main()
