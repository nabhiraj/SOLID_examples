from abc import ABC,abstractmethod
class DataExtractor:
    def __init__(self,dataStation):
        self.dataStattion = dataStation
    def getData(self):
        return [('d1','v1'),('d2','v2')]

class OutputFormat(ABC):
    @abstractmethod
    def getInFormat(self):
        pass

class OutputJsonFormat(OutputFormat):
    def __init__(self,logInformation):
        self.logInformation = logInformation
    def getInFormat(self,data):
        return {data[0][0]:data[0][1]}

class OutputHTMLFOrmat(OutputFormat):
    def __init__(self,logInformation):
        self.logInformation = logInformation
    def getInFormat(self,data):
        return {data[0][0]:data[0][1]}

d = DataExtractor('bombay')
o = OutputJsonFormat('log_all')
output = o.getInFormat(d.getData())
print(output)