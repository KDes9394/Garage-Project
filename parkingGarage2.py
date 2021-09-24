class ParkingGarage():
    ticket = 15
    parkingspace = 15
    currentTicket = {}

#Extra - sorry we're full 
    def __init__(self, ticket, parkingspace):
      self.ticket = ticket
      self.parkingspace = parkingspace
       
    def taketicket():
      ParkingGarage.ticket -= 1
      ParkingGarage.parkingspace -= 1

    def payforParking():
     # totalticket = int(input("How many tickets would you like?"))
      print("your ticket has been paid. You have 15mins to leave")
      #currentTicket += 1

    def LeaveGarage():
      #if ticket == True:
      #Print("Thank you, have a nice day!")
      ParkingGarage.parkingspace += 1
      ParkingGarage.ticket += 1

new_occupant = ParkingGarage(1, 1)
#if ParkingGarage.ticket and ParkingGarage.parkingspace == 1:
  #print("Sorry we're full. Have a nice day!")

#currentTicket -dictionary key == True when 

#Leave Garage