import argparse


def parse_args():
    p = argparse.ArgumentParser(
        description="Count Rally PortfolioItem/Feature created in the last N days for each project in a workspace; also outputs summary grouped by parent project"
    )
   return p.parse_args()

def main() -> int:
    args = parse_args()
    print("Example Content.)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
