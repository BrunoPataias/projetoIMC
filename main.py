# Lista para armazenar os usuários
usuarios = []


# Função para calcular o IMC
def calcular_imc(altura, peso):
    return peso / (altura ** 2)


# Registro dos usuários
for i in range(5):
    nome = input(f"Digite o nome do usuário {i + 1}: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    altura = float(input(f"Digite a altura de {nome} em metros: "))
    peso = float(input(f"Digite o peso de {nome} em kg: "))

    # Adicionando o usuário na lista
    usuarios.append({"nome": nome, "idade": idade, "altura": altura, "peso": peso})

# Consulta e cálculo do IMC para um usuário específico
nome_consulta = input("Digite o nome do usuário para calcular o IMC: ")

# Buscar o usuário na lista
for usuario in usuarios:
    if usuario["nome"].lower() == nome_consulta.lower():
        imc = calcular_imc(usuario["altura"], usuario["peso"])
        print(f"{usuario['nome']} tem IMC = {imc:.2f}")
        break
else:
    print("Usuário não encontrado.")
