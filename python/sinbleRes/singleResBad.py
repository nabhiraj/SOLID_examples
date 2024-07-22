class DataExtractor:
    def __init__(self,dataStation):
        self.dataStattion = dataStation
    def getData(self):
        return [('d1','v1'),('d2','v2')]
    def getJsonData(self):
        data = self.getData()
        return {data[0][0]:data[0][1]}
    def getHtmlData(self):
        return 'converted data'

d = DataExtractor('delhi')
print(d.getJsonData())
    