from models import Doctor
from models import User


class Prescriptions:

    def __init__(self, userType, rx, dosageMg, date, rxType, pharmLoc):

        # check if doctor
        def checkUser():
            if userType.is_authenticated:
                self.userType = userType
                self.rx = rx
                self.dosageMg = dosageMg
                self.date = date
                self.rxType = rxType
                self.pharmLoc = pharmLoc

    # xanax dosage min:0.25mg max:0.5mg
    # create dosage min and max table

    def dosageCheck(self):
        dosageMin = 0.25
        dosageMax = 0.5
        if self.dosageMg < dosageMin or self.dosageMg > dosageMax:
            print("\nError: invalid dosage...please check dosage and reenter")

    def printScript(self):
        dosageMin = 0.25  # fetch from table
        dosageMax = 0.5  # fetch from table

        if self.dosageMg >= dosageMin and self.dosageMg <= dosageMax:
            print("Patient Prescription: \n")
            print("Rx: \t\t", self.rx)
            print("dosageMg: \t", self.dosageMg, "mg")
            print("date: \t\t", self.date)
            print("rxType: \t", self.rxType)
            print("pharmLoc: \t", self.pharmLoc)

        else:
            self.dosageCheck()



