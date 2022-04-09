from argparse import ArgumentParser


def talk_about_conference(conference_name: str, year: int = 2022):
    """Talks about a conference.

    Args:
        conference_name: Name of the conference
        year: Year of the conference
    """
    print(f"{conference_name} {year} is the best conference ever!")


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('conference_name', type=str, help='Name of the conference')
    parser.add_argument('--year', type=int, default=2022, help='Year of the conference')
    args = parser.parse_args()
    talk_about_conference(args.conference_name, args.year)
