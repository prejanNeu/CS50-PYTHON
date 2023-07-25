def date_check(date):
    if date[:2].isdigit()and date[2]=='/' and (date[3] and date[4]).isdigit() and date[5]=='/'and  date[-4:].isdigit():
        return True
    elif date[0].isdigit()and date[1]=='/' and (date[2] and date[3]).isdigit() and date[5]=='/'and  date[-4:].isdigit():
        return True
    elif date[0].isdigit()and date[1]=='/' and date[2].isdigit() and date[3]=='/'and  date[-4:].isdigit():
        return True
    elif date[:2].isdigit()and date[2]=='/' and date[3].isdigit() and date[4]=='/'and  date[-4:].isdigit():
        return True
    else:
        return False


month_list = [
    "January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"
]
while True:
    try:
        date = input("Date: ").strip()

        for char in date:
            if char.isalpha():
                month_day, year = date.split(",")
                month, day = month_day.split(" ")
                break
        else:
            if (date_check(date)):
                month, day, year = date.split("/")
            else:
                pass


        if month.strip() in month_list:
            index = month_list.index(month.strip())
            day = int(day)  # Convert day to an integer
            year = int(year)
            if day<=32:
                print(f"{year:04d}-{index+1:02d}-{day:02d} ")
                break
            else :
                pass
        else:
            day = int(day)  # Convert day to an integer
            year = int(year)
            month= int (month)# Convert year to an integer
            if month<=12 and day<=32:
                print(f"{year:04d}-{month:02d}-{day:02d} ")
                break
            else:
                pass


    except EOFError:
        pass
    except KeyError:
        pass
    except NameError:
        pass
    except ValueError:
        pass
