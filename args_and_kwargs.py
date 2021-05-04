
def funargs(normal,*args,**kwargs):
    print("\n")
    print(normal)
    print("\n")
    for item in args:
        print(item)
    print("\n\n")
    for key,value in kwargs.items():
        print(f"{key} is a {value}")


normal="The legendary peoples are : "
har=["Jaahanava Joshi", "Sachin Tendulkar", "Virat Kohli"]
kw={"Jaahanava Joshi":"Programmer", "Manthan":"Cook", "Raina":"Cricketer"}

funargs(normal,*har,**kw)