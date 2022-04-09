from jsonargparse import CLI


def talk_about_conference(conference_name: str, year: int = 2022):
    """Talks about a conference.

    Args:
        conference_name: Name of the conference
        year: Year of the conference
    """
    print(f"{conference_name} {year} is the best conference ever!")


if __name__ == '__main__':
    CLI(env_prefix="PYCON", default_env=True)
