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
      print("Here is your ticket.")
      run()
    def payforParking():
      if ParkingGarage.currentTicket["Ticket"] == "True":
        variable = int(input ("Please pay your parking fee. "))
        if variable >= 1:
          ParkingGarage.currentTicket["Ticket"] = "False"
        if variable < 1 :
          variable2 = int(input ("PLEASE enter a real number to pay for parking fee. PLEASE "))
          if variable2 == 0:
            print("Security is on it's way")
        run()
      else: 
        print('You have not parked yet, please input "Park"')
        run()
        
    def LeaveGarage():
      if ParkingGarage.currentTicket == {}:
        print("Sorry to see you go")
      elif ParkingGarage.currentTicket["Ticket"] == "False":
        print("Thank you, have a nice day!")
         #ParkingGarage.ticket.append(max(ParkingGarage.ticket, + 1))
         #ParkingGarage.parkingspace.append(max(ParkingGarage.parkingspace, +1))
      else:
        ParkingGarage.payforParking()

#Suzette    
 
#Suzette
def run():
  new_occupant = ParkingGarage()
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
  

run() 

#if ParkingGarage.ticket and ParkingGarage.parkingspace == 1:
  #print("Sorry we're full. Have a nice day!")

#currentTicket -dictionary key == True when 


