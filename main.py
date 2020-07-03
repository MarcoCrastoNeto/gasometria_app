import functions
from classes import gasometria_valor

print('Coloque os valores correspondentes da Gasometria abaixo: \n(Obs: Colocar somente números nos valores, e usar pontos para decimais)')

#* Loop serve para prevenir o erro 'ValueError' na entrada dos valores da gasometria.

while True:
    try:
        fio2_valor = float(input('Entre com o valor da FiO2 aqui (em porcentagem): '))
        ph_valor = float(input('Entre com o valor do pH aqui: '))
        pco2_valor = float(input('Entre com o valor do PCO2 aqui: '))
        po2_valor = float(input('Entre com o valor do PO2 aqui: '))
        lac_valor = float(input('Entre com o valor do Lactato aqui: '))
        hco3_valor = float(input('Entre com o valor do HCO3 aqui: '))
        break
    except ValueError:
        print('Dado colocado não válido!')

gasometria_atual = gasometria_valor(fio2_valor, ph_valor, pco2_valor, po2_valor, lac_valor, hco3_valor)

#* Código abaixo copia os valores inseridos e os valores retornados e os salva em um arquivo.txt, além de imprimi-los no terminal!

gasometria_file = open('gasometria.txt', 'w')

gasometria_file.write('Valores Inseridos:\n'
                    'FiO2: {fio2}\n'
                    'pH: {ph}\n'
                    'PCO2: {pco2}\n'
                    'PO2: {po2}\n'
                    'Lactato: {lac}\n'
                    'Bicarbonato: {hco3}'
                    '\n\nResultado:'
                    '\nContexto de pH: {ph_m}' \
                    '\nNível de oxigênio: {po2_m}' \
                    '\nNível de Lactato: {lac_m}' \
                    '\nÍndice de Oxigenação: {io_m}'.format(fio2 = fio2_valor,
                                                            ph = ph_valor,
                                                            pco2 = pco2_valor,
                                                            po2 = po2_valor,
                                                            lac = lac_valor,
                                                            hco3 = hco3_valor,
                                                            ph_m = gasometria_atual.ph_significado(),
                                                            po2_m = gasometria_atual.po2_significado(),
                                                            lac_m = gasometria_atual.lac_significado(),
                                                            io_m = gasometria_atual.io_significado()))

gasometria_file.close()

gasometria_file = open('gasometria.txt', 'r')

print(gasometria_file.read())

gasometria_file.close()