
#* Função abaixo usa o input ph_value para dar o valor ph_meaning

def find_ph_meaning(ph_value):
    if ph_value > 7.450:
        ph_meaning = 'PH Alcalótico'
    elif ph_value < 7.350:
        ph_meaning = 'PH Acidótico'
    else:
        ph_meaning = 'PH Normal'
    return ph_meaning

#* Função abaixo usa o input po2_value para dar o valor po2_meaning.

def find_po2_meaning(po2_value):
    if po2_value < 80.0:
        po2_meaning = 'Hipóxia'
    elif po2_value > 100.0:
        po2_meaning = 'Hiperóxia'
    else:
        po2_meaning = 'Bom nível de oxigenação'
    return po2_meaning

#* Função abaixo usa os inputs po2_value e fio2_value para dar o valor io + io_meaning.

def find_io_meaning(po2_value, fio2_value):
    if fio2_value > 1.0:
        fio2_value = fio2_value * 0.01
    io_value = po2_value / fio2_value
    if io_value < 100.0:
        io_meaning = 'Indice de Oxigenação Péssimo'
    elif io_value < 200.0:
        io_meaning = 'Indice de Oxigenação Ruim'
    elif io_value < 300.0:
        io_meaning = 'Indice de Oxigenação Moderado'
    elif io_value >  400.0:
        io_meaning = 'Indice de Oxigenação Bom'
    else:
        io_meaning = 'Indice de Oxigenação Mediano'
    return (str(io_value)) + ', ' + io_meaning

#* Função abaixo usa o input lac_value para dar o valor lac_meaning.

def find_lac_meaning(lac_value):
    if lac_value > 2.2:
        lac_meaning = 'Hiperlactatemia'
    else:
        lac_meaning = 'Lactato Normal'
    return lac_meaning

#* Função abaixo usa o input pco2_value para dar o valor pco2_meaning.

def find_pco2_meaning(pco2_value):
    if pco2_value > 45.0:
        pco2_meaning = 'Alteração Respiratória Acidótica'
    elif pco2_value < 35.0:
        pco2_meaning = 'Alteração Respiratória Alcalótica'
    else:
        pco2_meaning = 'PCO2 Normal'
    return pco2_meaning

#* Função abaixo usa o input hco3_value para dar o valor hco3_meaning.

def find_hco3_meaning(hco3_value):
    if hco3_value > 26.0:
        hco3_meaning = 'Alteração Metabólica Alcalótica'
    elif hco3_value < 22.0:
        hco3_meaning = 'Alteração Metabólica Acidótica'
    else:
        hco3_meaning = 'HCO3 Normal'
    return hco3_meaning

#* Função abaixo levará os parametros resultantes das funções find_pco2_meaning e find_hco3_meaning, e deverá devolver o parametro acidosis_meaning.
#TODO Pesquisar algum jeito de identificar o fator principal de acidose e alcalose causador do distúrbio.

def find_acidosis_meaning(pco2_meaning, hco3_meaning, pco2_value, hco3_value):
    if pco2_meaning == 'Alteração Respiratória Acidótica' and hco3_meaning == 'Alteração Metabólica Acidótica':
    #TODO Identificar fator principal
        acidosis_meaning = 'Acidose de Caratér Misto, Correlacionar com Clínica'
    elif pco2_meaning == 'Alteração Respiratória Acidótica':
        if hco3_value <= ((((pco2_value - 40) / 10) + 24) + 2) and hco3_value >= ((((pco2_value - 40) / 10) + 24) - 2):
            acidosis_meaning = 'Acidose Respiratória com Compensação Metabólica'
        else:
            acidosis_meaning = 'Acidose Respiratória não Compensada'
    elif hco3_meaning == 'Alteração Metabólica Acidótica':
        if pco2_value <= (((1.5 * hco3_value) + 8) + 2) and pco2_value >= (((1.5 * hco3_value) + 8) - 2):
            acidosis_meaning = 'Acidose Metabólica com Compensação Respiratória'
        else:
            acidosis_meaning = 'Acidose Metabólica não Compensada'
    else:
        acidosis_meaning = 'Acidose com Valores de PCO2 e HCO3 nos limites da normalidade'
    return acidosis_meaning

#* Função abaixo levará os parametros resultantes das funções find_pco2_meaning e find_hco3_meaning, e deverá devolver o parametro alcalosis_meaning.

def find_alcalosis_meaning(pco2_meaning, hco3_meaning, pco2_value, hco3_value):
    if pco2_meaning == 'Alteração Respiratória Alcalótica' and hco3_meaning == 'Alteração Metabólica Acidótica':
    #TODO Identificar fator principal
        alcalosis_meaning = 'Alcalose de Caratér Misto, Correlacionar com Clínica'
    elif pco2_meaning == 'Alteração Respiratória Alcalótica':
        if hco3_value <= ((24 - ((40 - pco2_value) / 5)) + 2) and hco3_value >= ((24 - ((40 - pco2_value) / 5)) - 2):
            alcalosis_meaning = 'Alcalose Respiratória com Compensação Metabólica'
        else:
            alcalosis_meaning = 'Alcalose Respiratória não Compensada'
    elif hco3_meaning == 'Alteração Metabólica Alcalótica':
        if pco2_value <= (((0.7 * hco3_value) + 21) + 2) and pco2_value >= (((0.7 * hco3_value) + 21) - 2):
            alcalosis_meaning = 'Alcalose Metabólica com Compensação Respiratória'
        else:
            alcalosis_meaning = 'Alcalose Metabólica não Compensada'
    else:
        alcalosis_meaning = 'Alcalose com Valores de PCO2 e HCO3 nos limites da normalidade'
    return alcalosis_meaning

#TODO Fazer uma função avaliando as possibilidades de pH normal com alterações metabólicas ou respiratórias.

def find_normal_meaning(pco2_meaning, hco3_meaning, pco2_value, hco3_value):
    if pco2_meaning == 'Alteração Respiratória Acidótica' and hco3_meaning == 'Alteração Metabólica Alcalótica':
        #TODO Implementar as duas próximas funções!
        normal_meaning = 'Função ainda não implementada'
    elif pco2_meaning == 'Alteração Respiratória Alcalótica' and hco3_meaning == 'Alteração Metabólica Acidótica':
        normal_meaning = 'Função ainda não implementada'
    elif pco2_meaning == 'Alteração Respiratória Acidótica':
        if hco3_value <= ((((pco2_value - 40) / 10) + 24) + 2) and hco3_value >= ((((pco2_value - 40) / 10) + 24) - 2):
            normal_meaning = 'Acidose Respiratória com Compensação Metabólica sem Alteração de PH'
        else:
            normal_meaning = 'Acidose Respiratória não Compensada sem Alteração de PH'
    elif pco2_meaning == 'Alteração Respiratória Alcalótica':
        if hco3_value <= ((24 - ((40 - pco2_value) / 5)) + 2) and hco3_value >= ((24 - ((40 - pco2_value) / 5)) - 2):
            normal_meaning = 'Alcalose Respiratória com Compensação Metabólica sem Alteração de PH'
        else:
            normal_meaning = 'Alcalose Respiratória não Compensada sem Alteração de PH'
    elif hco3_meaning == 'Alteração Metabólica Acidótica':
        if pco2_value <= (((1.5 * hco3_value) + 8) + 2) and pco2_value >= (((1.5 * hco3_value) + 8) - 2):
            normal_meaning = 'Acidose Metabólica com Compensação Respiratória sem Alteração de PH'
        else:
            normal_meaning = 'Acidose Metabólica não Compensada sem Alteração de PH'
    elif hco3_meaning == 'Alteração Metabólica Alcalótica':
        if pco2_value <= (((0.7 * hco3_value) + 21) + 2) and pco2_value >= (((0.7 * hco3_value) + 21) - 2):
            normal_meaning = 'Alcalose Metabólica com Compensação Respiratória sem Alteração de PH'
        else:
            normal_meaning = 'Alcalose Metabólica não Compensada sem Alteração de PH'
    else:
        normal_meaning = 'PH normal, com HCO3 e PCO2 dentro dos limites da normalidade'
    return normal_meaning