import functions

class gasometria_valor():
    def __init__(self, fio2, ph, pco2, po2, lac, hco3):
        self.fio2 = fio2
        self.ph = ph
        self.pco2 = pco2
        self.po2 = po2
        self.lac = lac
        self.hco3 = hco3
    def ph_significado(self):
        ph_significado = functions.achar_ph_significado(self.ph)
        pco2_significado = functions.achar_pco2_significado(self.pco2)
        hco3_significado = functions.achar_hco3_significado(self.hco3)
        if ph_significado == 'PH Alcalótico':
            ph_resultado = functions.achar_alcalose_significado(pco2_significado, hco3_significado, self.pco2, self.hco3)
        elif ph_significado == 'PH Acidótico':
            ph_resultado = functions.achar_acidose_significado(pco2_significado, hco3_significado, self.pco2, self.hco3)
        elif ph_significado == 'PH Normal':
            ph_resultado = functions.achar_normal_significado(pco2_significado, hco3_significado, self.pco2, self.hco3)
        return ph_resultado
    def po2_significado(self):
        po2_significado = functions.achar_po2_significado(self.po2)
        return po2_significado
    def lac_significado(self):
        lac_significado = functions.achar_lac_significado(self.lac)
        return lac_significado
    def io_significado(self):
        io_significado = functions.achar_io_significado(self.po2, self.fio2)
        return io_significado