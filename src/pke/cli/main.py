import argparse

from pke.version import VERSION


def main():

    parser = argparse.ArgumentParser(
        prog="pke",
        description="Project Knowledge Engine"
    )

    parser.add_argument(
        "--version",
        action="store_true",
        help="Show version"
    )


    args = parser.parse_args()


    if args.version:
        print(
            f"PKE {VERSION}"
        )
        return


    parser.print_help()


if __name__ == "__main__":
    main()