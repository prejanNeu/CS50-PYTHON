name= {}

while True:
    try:
        element=input().strip().upper()

        if element not in name :
            name[element]=1;
        else:
            name[element]=name[element]+1
    except EOFError:
        sorted_name=dict(sorted(list(name.items())))
        for item in sorted_name:
            print(sorted_name[item], itemcd , sep=" ")
        break
    except KeyError:
        pass
