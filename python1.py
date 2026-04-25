import argparse


def parse_args():
    p = argparse.ArgumentParser(
        description="Count Rally PortfolioItem/Feature created in the last N days for each project in a workspace; also outputs summary grouped by parent project"
    )
   return p.parse_args()

