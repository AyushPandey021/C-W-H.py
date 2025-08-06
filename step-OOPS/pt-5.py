# write a class train which has mathod to book a ticket get status (no of seats) and get fare infomation of train which runing under indian railways

from random import randint


class Train:
    def __init__(self,trainNo):
        self.trainNo = trainNo
       
   
    def book(self , fro,to):
        print(f"Train no: {self.trainNo} is runing on time {fro} to {to}")
    def getStatus(self):
        print(f"Traini no: {self.trainNo} is runing on time" )
    def getFare(self, fro, to):
        print(
            f"Ticket is fare in Train on: {self.trainNo} from {fro} to {to} is {randint(222,5555)}"
        )

TrainChali = Train(12132)
TrainChali.book("Rampur", "Delhi")
TrainChali.getFare("Rampur", "Delhi")