
#* Função abaixo usa o input ph_value para dar o valor ph_meaning

def achar_ph_significado(ph_valor):
    if ph_valor > 7.450:
        ph_significado = 'PH Alcalótico'
    elif ph_valor < 7.350:
        ph_significado = 'PH Acidótico'
    else:
        ph_significado = 'PH Normal'
    return ph_significado

#* Função abaixo usa o input po2_value para dar o valor po2_meaning.

def achar_po2_significado(po2_valor):
    if po2_valor < 80.0:
        po2_significado = 'Hipóxia'
    elif po2_valor > 100.0:
        po2_significado = 'Hiperóxia'
    else:
        po2_significado = 'Bom nível de oxigenação'
    return po2_significado

#* Função abaixo usa os inputs po2_value e fio2_value para dar o valor io + io_meaning.

def achar_io_significado(po2_valor, fio2_valor):
    if fio2_valor > 1.0:
        fio2_valor = fio2_valor * 0.01
    io_valor = po2_valor / fio2_valor
    if io_valor < 100.0:
        io_significado = 'Indice de Oxigenação Péssimo'
    elif io_valor < 200.0:
        io_significado = 'Indice de Oxigenação Ruim'
    elif io_valor < 300.0:
        io_significado = 'Indice de Oxigenação Moderado'
    elif io_valor >  400.0:
        io_significado = 'Indice de Oxigenação Bom'
    else:
        io_significado = 'Indice de Oxigenação Mediano'
    return (str(io_valor)) + ', ' + io_significado

#* Função abaixo usa o input lac_value para dar o valor lac_meaning.

def achar_lac_significado(lac_valor):
    if lac_valor > 2.2:
        lac_significado = 'Hiperlactatemia'
    else:
        lac_significado = 'Lactato Normal'
    return lac_significado

#* Função abaixo usa o input pco2_value para dar o valor pco2_meaning.

def achar_pco2_significado(pco2_valor):
    if pco2_valor > 45.0:
        pco2_significado = 'Alteração Respiratória Acidótica'
    elif pco2_valor < 35.0:
        pco2_significado = 'Alteração Respiratória Alcalótica'
    else:
        pco2_significado = 'PCO2 Normal'
    return pco2_significado

#* Função abaixo usa o input hco3_value para dar o valor hco3_meaning.

def achar_hco3_significado(hco3_valor):
    if hco3_valor > 26.0:
        hco3_significado = 'Alteração Metabólica Alcalótica'
    elif hco3_valor < 22.0:
        hco3_significado = 'Alteração Metabólica Acidótica'
    else:
        hco3_significado = 'HCO3 Normal'
    return hco3_significado

#* Função abaixo levará os parametros resultantes das funções find_pco2_meaning e find_hco3_meaning, e deverá devolver o parametro acidosis_meaning.
#TODO Pesquisar algum jeito de identificar o fator principal de acidose e alcalose causador do distúrbio.

def achar_acidose_significado(pco2_significado, hco3_significado, pco2_valor, hco3_valor):
    if pco2_significado == 'Alteração Respiratória Acidótica' and hco3_significado == 'Alteração Metabólica Acidótica':
    #TODO Identificar fator principal
        acidose_significado = 'Acidose de Caratér Misto, Correlacionar com Clínica'
    elif pco2_significado == 'Alteração Respiratória Acidótica':
        if hco3_valor <= ((((pco2_valor - 40) / 10) + 24) + 2) and hco3_valor >= ((((pco2_valor - 40) / 10) + 24) - 2):
            acidose_significado = 'Acidose Respiratória com Compensação Metabólica'
        else:
            acidose_significado = 'Acidose Respiratória não Compensada'
    elif hco3_significado == 'Alteração Metabólica Acidótica':
        if pco2_valor <= (((1.5 * hco3_valor) + 8) + 2) and pco2_valor >= (((1.5 * hco3_valor) + 8) - 2):
            acidose_significado = 'Acidose Metabólica com Compensação Respiratória'
        else:
            acidose_significado = 'Acidose Metabólica não Compensada'
    else:
        acidose_significado = 'Acidose com Valores de PCO2 e HCO3 nos limites da normalidade'
    return acidose_significado

#* Função abaixo levará os parametros resultantes das funções find_pco2_meaning e find_hco3_meaning, e deverá devolver o parametro alcalosis_meaning.

def achar_alcalose_significado(pco2_significado, hco3_significado, pco2_valor, hco3_valor):
    if pco2_significado == 'Alteração Respiratória Alcalótica' and hco3_significado == 'Alteração Metabólica Acidótica':
    #TODO Identificar fator principal
        alcalose_significado = 'Alcalose de Caratér Misto, Correlacionar com Clínica'
    elif pco2_significado == 'Alteração Respiratória Alcalótica':
        if hco3_valor <= ((24 - ((40 - pco2_valor) / 5)) + 2) and hco3_valor >= ((24 - ((40 - pco2_valor) / 5)) - 2):
            alcalose_significado = 'Alcalose Respiratória com Compensação Metabólica'
        else:
            alcalose_significado = 'Alcalose Respiratória não Compensada'
    elif hco3_significado == 'Alteração Metabólica Alcalótica':
        if pco2_valor <= (((0.7 * hco3_valor) + 21) + 2) and pco2_valor >= (((0.7 * hco3_valor) + 21) - 2):
            alcalose_significado = 'Alcalose Metabólica com Compensação Respiratória'
        else:
            alcalose_significado = 'Alcalose Metabólica não Compensada'
    else:
        alcalose_significado = 'Alcalose com Valores de PCO2 e HCO3 nos limites da normalidade'
    return alcalose_significado

#TODO Fazer uma função avaliando as possibilidades de pH normal com alterações metabólicas ou respiratórias.

def achar_normal_significado(pco2_significado, hco3_significado, pco2_valor, hco3_valor):
    if pco2_significado == 'Alteração Respiratória Acidótica' and hco3_significado == 'Alteração Metabólica Alcalótica':
        #TODO Implementar as duas próximas funções!
        normal_significado = 'Função ainda não implementada'
    elif pco2_significado == 'Alteração Respiratória Alcalótica' and hco3_significado == 'Alteração Metabólica Acidótica':
        normal_significado = 'Função ainda não implementada'
    elif pco2_significado == 'Alteração Respiratória Acidótica':
        if hco3_valor <= ((((pco2_valor - 40) / 10) + 24) + 2) and hco3_valor >= ((((pco2_valor - 40) / 10) + 24) - 2):
            normal_significado = 'Acidose Respiratória com Compensação Metabólica sem Alteração de PH'
        else:
            normal_significado = 'Acidose Respiratória não Compensada sem Alteração de PH'
    elif pco2_significado == 'Alteração Respiratória Alcalótica':
        if hco3_valor <= ((24 - ((40 - pco2_valor) / 5)) + 2) and hco3_valor >= ((24 - ((40 - pco2_valor) / 5)) - 2):
            normal_significado = 'Alcalose Respiratória com Compensação Metabólica sem Alteração de PH'
        else:
            normal_significado = 'Alcalose Respiratória não Compensada sem Alteração de PH'
    elif hco3_significado == 'Alteração Metabólica Acidótica':
        if pco2_valor <= (((1.5 * hco3_valor) + 8) + 2) and pco2_valor >= (((1.5 * hco3_valor) + 8) - 2):
            normal_significado = 'Acidose Metabólica com Compensação Respiratória sem Alteração de PH'
        else:
            normal_significado = 'Acidose Metabólica não Compensada sem Alteração de PH'
    elif hco3_significado == 'Alteração Metabólica Alcalótica':
        if pco2_valor <= (((0.7 * hco3_valor) + 21) + 2) and pco2_valor >= (((0.7 * hco3_valor) + 21) - 2):
            normal_significado = 'Alcalose Metabólica com Compensação Respiratória sem Alteração de PH'
        else:
            normal_significado = 'Alcalose Metabólica não Compensada sem Alteração de PH'
    else:
        normal_significado = 'PH normal, com HCO3 e PCO2 dentro dos limites da normalidade'
    return normal_significado