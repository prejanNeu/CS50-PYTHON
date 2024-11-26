from datetime import date,datetime
import inflect
import sys



def returnIntoMinute(birth_date):
    try:
        current=date.today()
        birth_str=birth_date.split("-")
        birth=date(int(birth_str[0]),int(birth_str[1]),int(birth_str[2]))
        days=current-birth
        day=days.days
        minute=day*24*60
        p = inflect.engine()
        temp=p.number_to_words(minute).capitalize()
        temp=temp.replace(" and","")
        return temp+" minutes"

    except ValueError:
        sys.exit("Invalid date")


def main():
    birth_date=input("Date of Birth: ")
    print(returnIntoMinute(birth_date))


if __name__ == "__main__":
    main()
