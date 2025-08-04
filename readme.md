# 🧾 Validador de Formulários com Regex - Python

Este projeto é um sistema de validação de dados de formulários utilizando expressões regulares (Regex) em Python. Ele solicita as seguintes informações do usuário:

- Nome completo
- E-mail
- Telefone
- CPF
- Data de nascimento

Cada entrada é validada com regras específicas para garantir a integridade dos dados. Caso algum campo esteja incorreto, o sistema informa o erro e solicita uma nova entrada, garantindo um fluxo interativo e amigável.

---

## 🚀 Funcionalidades

✔️ Validação de nome completo (apenas letras e espaços, mínimo dois nomes)  
✔️ E-mail com formato obrigatório `seunome123@gmail.com`  
✔️ Telefone com 10 ou 11 dígitos (DDD + número), com ou sem hífen  
✔️ CPF válido no formato `XXX.XXX.XXX-XX` ou apenas números  
✔️ Data de nascimento no formato `DD/MM/AAAA`  
✔️ Cálculo automático da idade a partir da data de nascimento

---

## 🧠 Tecnologias Utilizadas

- Python 3
- Módulos nativos: `re` (Regex), `datetime`, `json` (para exportar os dados validados)

---

## 💻 Como Executar

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/validador-formulario-python.git
```

* Navegue até o diretório do projeto:

```bash
cd validador-formulario-python
```

- Execute o arquivo principal:

```bash

python validador.py
```


📦 Estrutura

```bash

validador-formulario-python/
│
├── validador.py       # Script principal com todas as lógicas de validação
├── dados_validados.json  # Arquivo gerado com os dados salvos (após execução)
└── README.md          # Este arquivo
```

# ✍️ Exemplo de Uso

```bash

Digite seu nome completo: Joao
Nome inválido. Use apenas letras e espaços (ex: João Silva).
Digite seu nome completo: Joao Silva
Digite seu email: joao.silva@gmail.com
Email inválido. Use o formato nome+numero@gmail.com (ex: joaosilva123@gmail.com)
Digite seu email: joaosilva123@gmail.com
```


# 📈 Resultado Final
* Os dados validados são salvos automaticamente em um arquivo dados_validados.json para posterior uso ou integração com outras aplicações.



# 👨‍💻 Autor
* Moisés Aniceto. 
* Desenvolvedor iniciante com foco em projetos práticos, lógicos e educativos, voltados para o cotidiano da área.

# 📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.