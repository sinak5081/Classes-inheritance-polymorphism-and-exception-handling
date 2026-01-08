class student:
    def __init__(self,stName,stEmail,stAve):
        self.name = stName
        self.email = stEmail
        self.ave = stAve
    def displaye(self):
        print(self.name,self.email,self.ave)
    def sendemail(self):
        print("We are going send email:")
    def verify(self):
        print("We are going to verify the mail")
