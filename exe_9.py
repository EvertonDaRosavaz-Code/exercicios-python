#----------------------------
#Controle Financeiro pessoal
#----------------------------

import time
from datetime import datetime

#==========VARIÁVEIS GLOBAIS==============#
lista                 = {};
reserva_emergencia    = 0;
investimento_nacional  = 0;
valor_paraUso    = 0;
meses_ingles_para_portugues = {
    "January"  : "Janeiro",
    "February" : "Fevereiro",
    "March"    : "Março",
    "April"    : "Abril",
    "May"      : "Maio",
    "June"     : "Junho",
    "July"     : "Julho",
    "August"   : "Agosto",
    "September": "Setembro",
    "October"  : "Outubro",
    "November" : "Novembro",
    "December" : "Dezembro"
}

#=========================================


salario = float(input('Salário mensal: '));
print('Logo abaixo adicione o nome e valor do seu gasto')

controle = True;
soma = 0
while controle:
    primeiro_gasto = input('Nome do gasto :')
    try:
        valor_do_gasto = float(input('Valor do gasto:'))
    except ValueError:
           print('Digite um número valido')


    lista[primeiro_gasto] = valor_do_gasto;

    finalizar = input('Deseja finalizar a adição de contas (S/N)?')
    if finalizar == "S":
        controle = False
     

for i in lista.items():
        soma+=i[1]
                                 
sobra  = salario-soma                
print('----'*20)
print(f'Salário de R${salario:.2f} - R${soma:.2f} = R${sobra:.2f}  reais após pagar suas contas')
print('----'*20)
time.sleep(3)
print("⏳ Processando...")
time.sleep(0.9)

print("\n" + "=" * 50)
print("📊 SUGESTÃO DE DISTRIBUIÇÃO DO VALOR")
print("=" * 50)

print("💰 50% → Reserva de emergência")
print("📈 20% → Investimentos nacionais")
print("🛒 30% → Uso do mês")

print("=" * 50)
print('\n')

nome_do_mes = datetime.now().strftime('%B')


mes = meses_ingles_para_portugues.get(nome_do_mes, nome_do_mes)
distribuicao = input(f'Deseja fazer essa distribuição para o mês atual de {mes} (S/N)?');
if distribuicao == 'S':
                reserva_emergencia      += (sobra*50)/100
                investimento_nacional    += (sobra*20)/100
                valor_paraUso           += (sobra*30)/100
                print("\n" + "=" * 50)
                print(  
                        f'Valor  atual da sua reserva de emergência: R${reserva_emergencia:.2f}\n'
                        f'Valor para seu investimento nacional R${investimento_nacional:.2f}\n'
                        f'Valor para o uso do mês R${valor_paraUso:.2f}'   
                        )
                print("=" * 50)






