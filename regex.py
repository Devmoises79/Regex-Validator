import re
import csv
from datetime import datetime

def validar_nome(nome):
    if not re.match(r"^[A-Za-zÀ-ÿ\s]+$", nome):
        return False
    # Verifica se tem pelo menos duas palavras
    return len(nome.strip().split()) >= 2

def validar_email(email):
    return re.match(r'^[a-zA-Z\.]+[0-9]+@gmail\.com$', email)

def validar_telefone(telefone):
    telefone_limpo = re.sub(r"\D", "", telefone)
    return len(telefone_limpo) in [10, 11]

def validar_cpf(cpf):
    cpf = re.sub(r"\D", "", cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    def calc_digito(digs):
        soma = sum(int(d)*w for d, w in zip(digs, range(len(digs)+1, 1, -1)))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)

    dig1 = calc_digito(cpf[:9])
    dig2 = calc_digito(cpf[:9] + dig1)
    return cpf[-2:] == dig1 + dig2

def validar_data(data):
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def calcular_idade(data_nasc):
    nasc = datetime.strptime(data_nasc, "%d/%m/%Y")
    hoje = datetime.today()
    idade = hoje.year - nasc.year - ((hoje.month, hoje.day) < (nasc.month, nasc.day))
    return idade

def obter_dado(campo, funcao_validacao, mensagem_erro, formato_exemplo=""):
    while True:
        valor = input(f"Digite seu {campo}{formato_exemplo}: ").strip()
        if funcao_validacao(valor):
            return valor
        print(mensagem_erro)

def main():
    print("\n--- Validador de Formulário ---\n")

    nome = obter_dado(
        "nome completo", 
        validar_nome, 
        "Nome inválido. Use apenas letras e espaços e ao menos um sobrenome (ex: João Silva)."
    )
    email = obter_dado(
        "email", 
        validar_email, 
        "Email inválido. Use o formato: seunome123@gmail.com", 
        " (formato: seunome123@gmail.com)"
    )
    telefone = obter_dado(
        "telefone", 
        validar_telefone, 
        "Telefone inválido. Use 10 ou 11 dígitos (ex: 99999-0000).", 
        " (com ou sem hífen)"
    )
    cpf = obter_dado(
        "CPF", 
        validar_cpf, 
        "CPF inválido.", 
        " (somente números ou com pontuação)"
    )
    data_nasc = obter_dado(
        "data de nascimento", 
        validar_data, 
        "Data inválida. Use o formato DD/MM/AAAA.", 
        " (formato: DD/MM/AAAA)"
    )
    idade = calcular_idade(data_nasc)

    print("\n✅ Dados validados com sucesso!")
    print(f"📌 Nome: {nome}")
    print(f"📌 Email: {email}")
    print(f"📌 Telefone: {telefone}")
    print(f"📌 CPF: {cpf}")
    print(f"📌 Data de Nascimento: {data_nasc}")
    print(f"📌 Idade: {idade} anos")

    with open("dados_validos.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo, delimiter=';')
        escritor.writerow(["Nome", "Email", "Telefone", "CPF", "Data de Nascimento", "Idade"])
        escritor.writerow([nome, email, telefone, cpf, data_nasc, idade])

    print("\n📁 Dados salvos em: dados_validos.csv\n")

if __name__ == "__main__":
    main()
