usuario = 'everton';
senha = 12345



input_usuario = input("Usuario:")
input_senha = int(input('Senha:'))

if senha == input_senha  and usuario == input_usuario:    
    print('Login realizado')
elif senha != input_senha and usuario == input_usuario:
    print('Senha errada, tente novamente');

else:
    print('Usuário errado tente novamente ')