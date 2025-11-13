import json
class Task:
    def __init__(self,id,nome,descricao):
        self.id=id
        self.nome=nome
        self.descricao=descricao

def Ler():
    try:
        with open("tarefa.json","r") as lista:
            return json.load(lista)
    except (json.JSONDecodeError):
        return []
    
def Escrever(todas):
    with open("tarefa.json","w") as i:
        json.dump(todas.sort(), i, indent=4, ensure_ascii=False)

todas = Ler()

def Criar():
    nome = input("Digite um nome:")
    descricao = input("Digite uma descrição:")
    
    id = len(todas)+1
    nova = Task(id,nome,descricao) 
    todas.append({
        "Id" : nova.id,
        "Nome" : nova.nome,
        "Descricao" : nova.descricao
    })
    Escrever(todas)


def Atualizar():
    print(todas)
    opcao = input("Digite o id da tarefa que voce quer atualizar:")
    nova = Task(opcao) 
    
    

while True:
    opcao = int(input("Digite uma opção:"))
    match opcao:
        case 1:
            Criar()
        case 2:
            Atualizar()
        case 3:
            Remover()
        case 4:
            break
        case _:
            print("Opção invalida")