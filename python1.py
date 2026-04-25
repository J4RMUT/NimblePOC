import argparse


def parse_args():
    p = argparse.ArgumentParser(
        description="Example of python file with argparser."
    )
   return p.parse_args()

def main() -> int:
    args = parse_args()
    print("Example Content.)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
