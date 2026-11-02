import re
import sys


def main():
    print(parse(input("HTML: ")))
    #URL = '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    #URL = '<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>'
    #URL = ""
    #print(parse(URL))

def parse(s):
    ID = re.search(r'<iframe(?: width="560" height="315")? src="https?://(?:www\.)?youtube\.com/embed/([A-Z0-9]{11})', s, re.IGNORECASE)

    if ID:
        return(f"https://youtu.be/{ID.group(1)}")
    else:
        return(None)


if __name__ == "__main__":
    main()