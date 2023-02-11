from setuptools.command.develop import develop


class District:
    def __init__(self, name, confirmedCases, hospitalizations, deaths):
        self.name = name
        self.confirmedCases = confirmedCases
        self.hospitalizations = hospitalizations
        self.deaths = deaths

    def __str__(self):
        return f"District Details: Name: {self.name}, " \
               f"Confirmed Cases: {self.confirmedCases}, Hospitalizations: {self.hospitalizations}," \
               f"Death: {self.deaths}"

