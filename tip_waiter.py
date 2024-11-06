bill=float(input("Please enter the bill: "))
tip=int(input("Please enter how much tip you want to give: "))
def total_calc():
    total=bill+bill*tip/100
    total=round(total)
    return(total)
print("Please pay",total_calc())