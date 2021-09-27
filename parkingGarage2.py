class ParkingGarage():
    ticket = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    unavailable_ticket = []
    parkingspace = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    unavailable_parking = []
    currentTicket = {}

#Extra - sorry we're full 
    # def __init__(self):
    #   self.ticket = ticket
    #   self.parkingspace = parkingspace
       
    def taketicket():
      ParkingGarage.unavailable_ticket = ParkingGarage.ticket.pop()
      ParkingGarage.unavailable_parking = ParkingGarage.parkingspace.pop()
      ParkingGarage.currentTicket["Ticket"] = "True"
      print("Here is your ticket.")
      run()
    def payforParking():
      while ParkingGarage.currentTicket == {}: 
          print('You have not parked yet, please input "Park"')
          run()
      if ParkingGarage.currentTicket["Ticket"] == "True":
        variable = float(input ("Please pay your parking fee. Minimum is 1.00/hr: "))
        if variable >= 1:
            ParkingGarage.currentTicket["Ticket"] = "False"
        if variable < 1 :
            variable2 = float(input ("PLEASE enter a real number to pay for parking fee. PLEASE "))
            if variable2 == 0:
              print("Security is on it's way")
      run()

    def LeaveGarage():
      if ParkingGarage.currentTicket == {}:
        print("Sorry to see you go")
      elif ParkingGarage.currentTicket["Ticket"] == "False":
        print("Thank you, have a nice day!")
        ParkingGarage.ticket.append(ParkingGarage.unavailable_ticket)
        ParkingGarage.parkingspace.append(ParkingGarage.unavailable_ticket)
      else:
        ParkingGarage.payforParking()

#Suzette    
 
#Suzette
def run():
  while True:
    response = input("What would you like to do?: Park/Pay/Leave/Spots? ").lower()
    if response == 'park':
      ParkingGarage.taketicket()
    if response == 'pay':
      ParkingGarage.payforParking()
    if response == 'leave':
      ParkingGarage.LeaveGarage()
    if response == 'spots':
      print(f'(There is {len(ParkingGarage.ticket)} tickets and {len(ParkingGarage.parkingspace)} spots left)')
      if ParkingGarage.ticket and ParkingGarage.parkingspace == []:
          print("sorry we're full. Have a nice day!")

run() 

#if ParkingGarage.ticket and ParkingGarage.parkingspace == 1:
  #print("Sorry we're full. Have a nice day!")

#currentTicket -dictionary key == True when 


