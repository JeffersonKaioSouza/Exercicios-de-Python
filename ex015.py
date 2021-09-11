dias = int(input('Digite a quantidade de dias: '))
km = float(input('Digite a quantida de km rodados: '))
cdias = dias * 60
ckm = km * 0.15

print('O valor a ser pago pelo aluguel é de R$:{:.2f}'.format(cdias + ckm))