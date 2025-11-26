import json
def ler():
    try:
        with open("tarefa.json","r") as f:
            return json.load(f)
    except (FileNotFoundError,json.decoder.JSONDecodeError):
        return []
    
def Criar(a):
    copia=a
    id = len(copia)+1
    nome = input("Digite um nome para a tarefa:")
    descricao = input("Digite uma descricao: ")
    copia.append({
            "id":id,
            "nome":nome,
            "descricao":descricao,
            "situacao":"pendente"})
    with open("tarefa.json","w") as f:
        json.dump(copia,f,indent=4)

        
opcao=0
print("Digite uma opção")
print("1 - criar tarefa\n"+
        "2 - atualizar tarefa\n"+
        "3 - deletar tarefa\n"
        "4 - sair do programa\n")
while opcao!=4:
    opcao = input("Digite uma opção:")
    match opcao:
        case "1":
            Criar(ler())
        #case "2":
        
        #case "3":
        case _:
            print("Opção invalida")
print("programa encerrado")
