class DataExtractor:
    def __init__(self,dataStation):
        self.dataStattion = dataStation
    def getData(self):
        return [('d1','v1'),('d2','v2')]

class OutputFormat:
    def __init__(self,logInformation):
        self.logInformation = logInformation
    def getInJson(self,data):
        return {data[0][0]:data[0][1]}
    def getHtmlData(self):
        return 'converted data'

d = DataExtractor('bombay')
o = OutputFormat('log_all')
output = o.getInJson(d.getData())
print(output)
        