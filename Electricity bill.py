x=float(input("ENTER UNITS:"))
if  x>=0 and x<=100 :
    print("NO ELECTRICITY BILL")

elif x>=101 and x<=10000:
    c=x*6
    print("ELECTRICITY BILL (₹):", c)

else :
    print("INVALID INPUT")
    