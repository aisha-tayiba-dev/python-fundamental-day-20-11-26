age=int(input("enter your age:"))
if age>18:
    print("eligible to vote")
else:
    years=18-age
    print(f"not eligible to vote,wait for {years} more years!")
