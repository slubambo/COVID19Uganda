from District import District
from CovidData import CovidData

class COVID19Uganda:

    districts = []

    def addDistrict(self, name, confirmedCases, hospitalizations, deaths):
        return District(name, confirmedCases, hospitalizations, deaths)

    def getCovidDistrictData(self,name):
        return next((d for d in self.districts if d.name == name), None)


    def getCovidSummedInformation(self):
        totalConfirmedCases = sum(d.confirmedCases for d in self.districts if d.confirmedCases != None)
        totalHospitalization = sum(d.hospitalizations for d in self.districts if d.hospitalizations != None)
        totalDeaths = sum(d.deaths for d in self.districts if d.deaths != None)

        return CovidData(totalConfirmedCases, totalHospitalization, totalDeaths)

    def getCovidAverageInformation(self):
        covidCases = self.getCovidSummedInformation();
        count = len(self.districts)

        return CovidData(covidCases.confirmedCases//count, covidCases.hospitalizations//count,
                         covidCases.deaths//count)