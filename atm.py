class Atm(object):
    def __init__(self,cardnumber,pinnumber):
        self.cardnumber=cardnumber
        self.pinnumber=pinnumber

    def cashWithdrawl(self):
        print("cashWithdrawed=$150")

    def bankEnquiry(self):
        print("$500")

card = Atm("4264 3542 9871","3587")
print(card.cardnumber)
print(card.pinnumber)
card.cashWithdrawl()
card.bankEnquiry()      