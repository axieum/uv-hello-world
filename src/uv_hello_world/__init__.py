from uv_hello_world_api import add


def main() -> None:
    """The main entrypoint to the application."""

    print(f"Hello, world! 7 + 8 is {add(7, 8)}")


if __name__ == "__main__":
    main()
