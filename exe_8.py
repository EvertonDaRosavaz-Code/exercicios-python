tarefas = [];

control = True;

while control:
    tarefa = input('Tarefa:')
    tarefas.append(tarefa)

    interrouper = input('Adicionar mais uma tarefa ? (s/n)');
    if interrouper == 'n':
        control = False


len = len(tarefas);
for i in range(len):
    print(f'{i+1} - {tarefas[i]} ')