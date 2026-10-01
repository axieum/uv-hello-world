from uv_hello_world_api import add


def main() -> None:
    """The main entrypoint to the application."""

    print(f"Hello, world! 6 + 7 is {add(6, 7)}")


if __name__ == "__main__":
    main()
