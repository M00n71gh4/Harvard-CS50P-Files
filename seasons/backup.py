from datetime import datetime, timedelta
import inflect # Flertalls ord
import sys



def main():

    birth_date = input("Date of Birth: ")
    #birth_date = "1978-09-22"

    b_day = birth_date_calculation()
    b_day.set_birth_date = birth_date
    print(b_day.calculate())


class birth_date_calculation():
    def __init__(self) -> None:
        self._b_date = None
        self._format = "%Y-%m-%d"

    @property
    def get_minutes(self):
        print("getter method called")
        return self._a

    @get_minutes.setter
    def set_birth_date(self, b_day):
        try:
            datetime.strptime(b_day, self._format)
            self._a = b_day
        except ValueError:
            sys.exit("Invalid date")

    def calculate(self):
        b_date = f"{self._a} 00:00:00"
        b_date = datetime.strptime(b_date, "%Y-%m-%d %H:%M:%S")

        str_date_now = datetime.now()
        str_date_now = str_date_now.replace(hour=0, minute=0, second=0, microsecond=0)

        time_delta = str_date_now - b_date
        #time_delta = int(time_delta)
        #total_minutes = timedelta.total_seconds /60
        print(time_delta)
        inf = inflect.engine()
        wordly = inf.number_to_words(time_delta, andword = "").capitalize()
        return  f"{wordly} minutes"

if __name__ == "__main__":
    main()
