import calendar
class CloudCost():
    valortempoexecucao = 0.0002080
    tempoexecucao = 3
    valorexecucao = 0.0000002
    valormsg = 0.00000040

    def lambda_execution(self):
        return (self.valortempoexecucao * self.tempoexecucao) + self.valorexecucao

    def app_execution(self, execution_times):
        return execution_times * (self.valormsg + 2 * (self.lambda_execution()))

    def month(self, execution_times, month_of_year):
        return self.app_execution(execution_times) * calendar.monthrange(2019, month_of_year)[1]

    def year(self, execution_times):
        result = []
        for month_of_year in range(1, 13):
            r = self.month(execution_times, month_of_year)
            result.append(r)
        return result

