#Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and 
# get fare information of train running under Indian Railways.
import random

class Train:
    def __init__(self, TrainNo):
        self.TrainNo = TrainNo
    def book(self, _From, _To):
        print (f"Ticket from {_From} to {_To} is Booked in Train No : {self.TrainNo}")
    def GetStatus(self):
        print(f"Train is No {self.TrainNo} is Running")
    def GetFare(self, _From, _To):
        print(f"Fare from {_From} to {_To} is : {random.randint(500,5000)}")
    def GetName(self,name):
        print(f"Name : {self.name} is booked in Train no: {self.TrainNo}")

t = Train(12543)
t.book("BBSR","KDJR")
t.GetStatus()
t.GetFare("CTC","Puri")
t.GetName("Ashutosh")