from datetime import date, datetime
import sys
import inflect


class date_caclulations:
    def __init__(self, birth_date, date_format) -> None:
        self.birth_date = birth_date
        self.date_format = date_format
        self.minute_delta = 0

    def check(self):
        try:
            datetime.strptime(self.birth_date, self.date_format)
            return True
        except:
            return False

    def __str__(self):
        date_now = date.today()
        split_year, split_month, split_day = str(self.birth_date).split("-")

        date_birth = date(int(split_year), int(split_month), int(split_day))

        date_delta = date_now-date_birth
        date_delta = int(date_delta.days)*24*60

        inf = inflect.engine()
        return  f"{inf.number_to_words(date_delta, andword="").capitalize()} minutes"


def main():

    my_season = date_caclulations(input("Date of birth: "), "%Y-%m-%d")

    if my_season.check():
        print(my_season)
    else:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()
