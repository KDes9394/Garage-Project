class ParkingGarage():
    ticket = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    parkingspace = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    currentTicket = {}

#Extra - sorry we're full 
    # def __init__(self):
    #   self.ticket = ticket
    #   self.parkingspace = parkingspace
       
    def taketicket():
      ParkingGarage.ticket.pop()
      ParkingGarage.parkingspace.pop()
      ParkingGarage.currentTicket["Ticket"] = "True"
      print("thank you")
      run()
    def payforParking():
      if ParkingGarage.currentTicket['Ticket'] == "True":
        print("please pay")
        continue
    def LeaveGarage():
      if ParkingGarage.currentTicket[Ticket] == "True":
        print("Thank you, have a nice day!")
      else:
        ParkingGarage.payforParking()

#Suzette    
 
#Suzette
def run():
  new_occupant = ParkingGarage()
  while True:
    response = input("What would you like to do?: Park/Leave/Spots? ").lower()
    if response == 'park':
      ParkingGarage.taketicket()
    if response == 'leave':
      ParkingGarage.LeaveGarage()
    if response == 'spots':
      print(f'(There is {len(ParkingGarage.ticket)} tickets and {len(ParkingGarage.parkingspace)} spots left'))
  

run() 

#if ParkingGarage.ticket and ParkingGarage.parkingspace == 1:
  #print("Sorry we're full. Have a nice day!")

#currentTicket -dictionary key == True when 



