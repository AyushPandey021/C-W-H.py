# Can you change the self-perameter inside a class to someting else (say"ayush").try Changeing self to "sif" or "Harry" and see the effect.

# write a class train which has mathod to book a ticket get status (no of seats) and get fare infomation of train which runing under indian railways

from random import randint


class Train:
    def __init__(slf,trainNo):
        slf.trainNo = trainNo
       
   
    def book(ayush, fro ,to):
        print(f"Train no: {ayush.trainNo} is runing on time {fro} to {to}")
    def getStatus(slf):
        print(f"Traini no: {slf.trainNo} is runing on time" )
    def getFare(slf, fro, to):
        print(
            f"Ticket is fare in Train on: {slf.trainNo} from {fro} to {to} is {randint(222,5555)}"
        )

TrainChali = Train(12132)
TrainChali.book("Rampur", "Delhi")
TrainChali.getFare("Rampur", "Delhi")