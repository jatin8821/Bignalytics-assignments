from ast import Str


class Start:
    def __init__(self):
        print('-'*106)
        print("                             THANKS FOR DOWNLOADING RAPIDO")
        print('-'*106)

        print("              Please select your city from below:")


        print('''                     Enter 1 for BHOPAL
                     Enter 2 for INDORE
                     Enter 3 for JABALPUR
                     Enter 4 for ASHTA
                     Enter 5 for SEHORE    ''')

        u = int(input('                     Enter here: '))

        if u == 1:
          print("You have selected BHOPAL")
        elif u== 2:
          print("You have selected INDORE") 
        elif u== 3:
          print("You have selected JABALPUR")
        elif u == 4:
          print("You have selected ASHTA")
        elif u == 5:
          print("You have selected SEHORE")
        else:
          print("please choose a valid city")               



class Info(Start):
    def customer_details(self):
        self.name =input("Enter your name: ")
        if type(self.name)!= str:
          print("Please enter a correct name")
      
        self.phoneno = str(input("Enter your phone number: "))
        #if str(self.phoneno) !=len(10):
          #print("Please enter a correct phone number")

        self.otp = input("Enter otp: ")
        self.password = input("Enter your password: ")


class Welcome(Info):
    def wel_come(self):
         print("Welcome to RAPIDO", self.name.upper())
         print("Congratulations you got Rs.50 in your rapido wallet!")


class Service(Welcome):
    def main(self):
        print("Enter your pickup location: ")
        p = input()
        print("Enter your destination location: ")
        d = input()
        print("Enter the distance(in K.M): ")
        dis = float(input())
        if(dis >=1.0 and dis<=12.0):
          print("Your ride has been accepted!")
          print("Please wait for a while.....")
        else:
          print("Sorry your ride cannot be accepted.")  
        amt = dis * 6
        print("Your ride amount is RS.",amt)



x = Service()
x.__str__() 
x.customer_details()
x.wel_come()
x.main()    



        