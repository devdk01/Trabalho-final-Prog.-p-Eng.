# 🕐 Sistema de Ponto em Python

> Sistema de controle de ponto desenvolvido em Python — registra entrada e saída de funcionários via terminal.

---

## 📋 Sumário

- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Como Executar](#-como-executar)
- [Menu Principal](#-menu-principal)
- [Estrutura do Código](#-estrutura-do-código)
  - [Cadastrar Funcionário](#cadastrar-funcionário)
  - [Registrar Entrada](#registrar-entrada)
  - [Registrar Saída](#registrar-saída)
  - [Histórico de Ponto](#histórico-de-ponto)
- [Melhorias Futuras](#-melhorias-futuras)
- [Tecnologias](#-tecnologias)

---

## 📌 Sobre o Projeto

Sistema de terminal desenvolvido em Python para controle de ponto de funcionários. Utiliza uma lista global `funcionarios` para armazenar os dados em memória e o módulo `datetime` para capturar automaticamente os horários de entrada e saída.

**Estrutura de dados principal:**

```python
funcionario = {
    "id": id_func,
    "nome": nome,
    "pontos": []
}
```

---

## ✅ Funcionalidades

- [x] Cadastrar funcionários com ID automático
- [x] Registrar horário de entrada
- [x] Registrar horário de saída com validações
- [x] Consultar histórico de ponto por funcionário
- [x] Tratamento de erros com `try/except`

---

## ▶️ Como Executar

**Pré-requisito:** Python 3.x instalado

```bash
# Clone o repositório
git clone https://github.com/devdk01/sistema-de-ponto

# Entre na pasta
cd sistema-de-ponto

# Execute o programa
python ponto_atualizado.py
```

---

## 🖥️ Menu Principal

O sistema roda em loop com `while opcao != 5`, exibindo o menu a cada iteração com tratamento de erro para entradas inválidas.

```
=================================
       SISTEMA DE PONTO
=================================
1 - Cadastrar Funcionário
2 - Registrar Entrada
3 - Registrar Saída
4 - Ver Histórico
5 - Sair
=================================
```

```python
try:
    opcao = int(input("Escolha uma opção: "))
except:
    print("Digite apenas números!")
    continue
```

---

## 🗂️ Estrutura do Código

### Cadastrar Funcionário

Função `cadastrar()` — solicita o nome, valida se não está vazio, gera ID automático e adiciona o funcionário à lista global.

```python
id_func = len(funcionarios) + 1

funcionario = {
    "id": id_func,
    "nome": nome,
    "pontos": []
}

funcionarios.append(funcionario)
```

---

### Registrar Entrada

Função `entrada()` — busca o funcionário pelo ID e registra o horário atual com `datetime.now()`, criando um registro com saída vazia.

```python
hora = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")

registro = {
    "entrada": hora,
    "saida": ""
}

f["pontos"].append(registro)
```

---

### Registrar Saída

Função `saida()` — realiza 3 validações antes de registrar a saída:

| # | Validação |
|---|-----------|
| 1 | Funcionário não encontrado |
| 2 | Nenhuma entrada registrada (lista de pontos vazia) |
| 3 | Última entrada já possui saída registrada |

```python
if f["pontos"][-1]["saida"] != "":
    print("Erro: A última entrada já possui saída registrada!")
    return

f["pontos"][-1]["saida"] = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
```

---

### Histórico de Ponto

Função `historico()` — busca o funcionário pelo ID e exibe todos os registros numerados com `enumerate()`. Informa caso não haja nenhum registro.

```python
for i, p in enumerate(f["pontos"], start=1):
    print(f"Registro {i}")
    print(f"Entrada: {p['entrada']}")
    print(f"Saída  : {p['saida']}")
```

---

## 🚀 Melhorias Futuras

- [ ] **Persistência de dados** — salvar com arquivo JSON ou banco SQLite
- [ ] **Cálculo de horas trabalhadas** — diferença automática entre entrada e saída
- [ ] **Interface gráfica** — UI com Tkinter para melhor experiência
- [ ] **Exportação PDF** — geração de relatório de ponto em PDF

---

## 🛠️ Tecnologias

- **Python 3.x**
- **Módulo `datetime`** — captura automática de data e hora

---

> Sistema funcional e extensível — uma base sólida para evoluir com boas práticas Python! 🐍
