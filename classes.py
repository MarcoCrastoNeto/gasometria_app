import functions

class gasometry_values():
    def __init__(self, fio2, ph, pco2, po2, lac, hco3):
        self.fio2 = fio2
        self.ph = ph
        self.pco2 = pco2
        self.po2 = po2
        self.lac = lac
        self.hco3 = hco3
    def ph_meaning(self):
        ph_meaning = functions.find_ph_meaning(self.ph)
        pco2_meaning = functions.find_pco2_meaning(self.pco2)
        hco3_meaning = functions.find_hco3_meaning(self.hco3)
        if ph_meaning == 'PH Alcalótico':
            ph_result = functions.find_alcalosis_meaning(pco2_meaning, hco3_meaning, self.pco2, self.hco3)
        elif ph_meaning == 'PH Acidótico':
            ph_result = functions.find_acidosis_meaning(pco2_meaning, hco3_meaning, self.pco2, self.hco3)
        elif ph_meaning == 'PH Normal':
            ph_result = functions.find_normal_meaning(pco2_meaning, hco3_meaning, self.pco2, self.hco3)
        return ph_result
    def po2_meaning(self):
        po2_meaning = functions.find_po2_meaning(self.po2)
        return po2_meaning
    def lac_meaning(self):
        lac_meaning = functions.find_lac_meaning(self.lac)
        return lac_meaning
    def io_meaning(self):
        io_meaning = functions.find_io_meaning(self.po2, self.fio2)
        return io_meaning