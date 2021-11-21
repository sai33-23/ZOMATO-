def Hotel_names(a):
    print("OUR RESTURANTS")
    print(a)
    user=input("select own choice resturant")
    i=0
    while i<len(a):
        if user in a:
            print("Available....")
            break
            
        else:
            print("OOPS!it's not available")
            break
        i+=1
Hotel_names(["Green chilli","Biriyani House","Jail Cafe","Chulha chauki ka Dhaba","Illusion Cafe","Swasti Plaza","The Marriot","Paradise","Chill out","Taj"])
def items(m):
    print("-:MENUS:-")
    for i in m:
        print(i,"-",m[i])
    user_1=input("select food from the above menu")
    quantity=int(input("Your quantiy Add to cart"))
    for i in m.keys():
        if user_1==i:
            price=quantity*m[i]
            print("Pay Rs.",price)
    
m={"Egg roll":90,"Biriyani":120,"Kabab":60,"kollhapuri vegetable":80,"Panner makkhani":140,"Mutton korma":250,"Alfahm chicken":170,"Chilli manchurian":130,"Black peeper mushroom":175,"chicken/paneer pizza":110,"Mutton kimma":220,"Hydrabadi dum biriyani":130}
items(m)
def Amount(payment):
    print(payment)
    p=input("enter the payment method")
    for i in payment:
        if i==p:
            print("go ahead with",p)
Amount(["phonepe","googlepe","credit card","cash on delivery"])
def time(a):
    user=input("again enter same hotel name for knowing time")
    for i in a:
        if user==i:
            print("It will reach soon between",a[i],"minutes")
            break
h={"Green chilli":35,"Biriyani House":48,"Jail Cafe":10,"Chulha chauki ka Dhaba":15,"Illusion Cafe":45,"Swasti Plaza":32,"The Marriot":50,"Paradise":48,"Chill out":56,"Taj":51}
time(h)
def review(l):
    a=int(input("RATINGS"))
    for i in dict:
        if i==a:
            print("customer's ratings:")
            print(dict[i])
dict={1:"*",2:"**",3:"***",4:"****",5:"*****"}
review(  dict )
print("THANKS FOR ORDERING,,FROM SANAYA RICH TABLE")
print("SEARCH IT AGAIN")