import time, threading, smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from read_config import read_config
from SQLConnect import SQLConn

SQL_SELECT = "SELECT sb_id, last_battery_change FROM `spin_bikes`;"
SQL_SELECT_BM = "SELECT schedule.bm_id, spin_bikes.sb_id FROM `schedule` join `location` on schedule.l_id=location.l_id join `spin_bikes` on spin_bikes.l_id=location.l_id;"
SQL_SELECT_BM_EMAIL = "SELECT bm_id, email FROM `bike_manager`;"

class autoEmail():

    def __init__(self):
        read_config()
        self.sql = SQLConn()

        self.previous = self.sql.select_query(SQL_SELECT)
        self.current = self.sql.select_query(SQL_SELECT)
        self.previous = self.refactorDateDict(self.previous)
        self.current = self.refactorDateDict(self.current)

        self.spinBikeManagers = {}
        self.getSpinBikeManagers()

        self.bikeManagerEmails = {}
        self.getBikeManagerEmails()

    def getBikeManagerEmails(self):
        emailDict = {}
        result = self.sql.select_query(SQL_SELECT_BM_EMAIL)
        for item in result:
            item_key = item['bm_id']
            item_value = item['email']
            emailDict[item_key] = item_value

        self.bikeManagerEmails = emailDict.copy()

    def refactorDateDict(self, unfactoredDict):
        newDict = {}
        for item in unfactoredDict:
            key = item["sb_id"]
            value = item["last_battery_change"]
            newDict[key] = value

        return newDict

    def refactorBikeManagerDict(self, unfactoredDict):
        newDict = {}
        for item in unfactoredDict:
            key = item["sb_id"]
            value = item["bm_id"]
            
            if key in newDict:
                newDict[key] = newDict[key] + [value]
            else:
                newDict[key] = [value]

        return newDict

    def getSpinBikeManagers(self):
        result = self.sql.select_query(SQL_SELECT_BM)
        self.spinBikeManagers = self.refactorBikeManagerDict(result).copy()

    def compareDateValues(self):
        different = {}
        for key, value in self.previous.items():
            if key in self.current:
                if self.previous[key] != self.current[key]:
                    # sql query to get bike managers and bikes
                    # bike_managers = self.sql.select_query(SQL_SELECT_BM)
                    different[key] = {"old": value, "new": self.current[key]}
        
        return different

    def updateCurrentDates(self):
        self.previous = self.current.copy()
        self.current = self.sql.select_query(SQL_SELECT)
        self.current = self.refactorDateDict(self.current)
    
    def sendEmail(self):
        batteryChangeDict = self.compareDateValues()
        needsChange = bool(batteryChangeDict)

        if needsChange:
            #At least one battery needs to be changed
            self.getSpinBikeManagers()
            
            receivers = []
            for key, value in batteryChangeDict.items():
                for receiver in self.spinBikeManagers[key]:
                    receiverDict = {}
                    receiverDict['bm_id'] = receiver
                    receiverDict['sb_id'] = key
                    receivers.append(receiverDict)

            #Send email
            sender = os.environ["EUSER"]
            sender_pwd = os.environ["EPWD"]
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender, sender_pwd)

            for receiver in receivers:
                receiver_email = self.bikeManagerEmails[receiver["bm_id"]]
                try:
                    print("Sending to bm: {bm_id}".format(bm_id=receiver["bm_id"]))
                    msg = MIMEMultipart()
                    msg['From'] = sender
                    msg['To'] = receiver_email
                    print("TO: {to}".format(to=msg['To']))
                    msg['Subject'] = "SpinBike Battery replacement notice"
                    body = "SpinBike id: {sb_id} needs a battery change".format(sb_id=receiver["sb_id"])
                    msg.attach(MIMEText(body, 'plain'))
                    text = msg.as_string()
                    server.sendmail(sender, receiver_email, text)
                except smtplib.SMTPRecipientsRefused as e:
                    print("Invalid email send attempt")
                    print(e)
            server.quit()
         
    def emailCheck(self):
        print(time.ctime())
        self.updateCurrentDates()
        self.sendEmail()

        #Debugging Value
        threading.Timer(10, self.emailCheck).start()

        #Real Value
        # threading.Timer(900, emailCheck).start()

auto = autoEmail()
auto.emailCheck()
# auto.getBikeManagerEmails()