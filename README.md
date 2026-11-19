# Gestão Financeira

Sistema desktop de gestão financeira desenvolvido em Python, com interface
em Tkinter e banco de dados SQLite.

## Sobre o projeto

Projeto solo, criado para praticar Python, SQL e desenvolvimento de
interfaces desktop. O sistema permite controlar clientes, cobranças,
pagamentos e despesas, e saber rapidamente quem está com débito em aberto.

## Funcionalidades

**(versão 1)**
- [ ] Cadastro de clientes
- [ ] Registro de cobranças (valor e data de vencimento)
- [ ] Registro de pagamentos (inclusive parciais)
- [ ] Registro de despesas
- [ ] Relatório de débitos em aberto
- [ ] Resumo mensal de entradas e saídas

**Planejado**
- [ ] Categorias de despesa e filtros por período
- [ ] Exportação para CSV/Excel
- [ ] Alertas de cobranças vencidas
- [ ] Tela de login

## Tecnologias

- [Python](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html) (interface gráfica)
- [SQLite](https://www.sqlite.org/) (banco de dados)
- [pytest](https://pytest.org/) (testes)

## Como rodar

**Pré-requisitos:** Python 3.10 ou superior.
No Linux, o Tkinter pode precisar ser instalado à parte: `sudo apt install python3-tk`.

```bash
# 1. Clonar o repositório
git clone https://github.com/[SEU-USUARIO]/gestao-financeira.git
cd gestao-financeira

# 2. Criar e ativar o ambiente virtual
python -m venv .venv

# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

# 3. Instalar as dependências
pip install -r requirements.txt

# 4. Criar o banco de dados
python src/database.py

# 5. Executar o sistema
python src/main.py
```

O banco (`financeiro.db`) é criado localmente e **não** é versionado.

## Estrutura do projeto

```
gestao-financeira/
├── src/
│   ├── database.py    # conexão e consultas ao banco
│   ├── services.py    # regras de negócio (cálculo de dívidas etc.)
│   ├── main.py        # ponto de entrada
│   └── ui/            # telas em Tkinter
├── tests/             # testes automatizados
├── LICENSE
├── README.md
└── requirements.txt
```

## Decisões de projeto

- **Valores monetários em centavos (inteiro):** evita erros de arredondamento do `float`.
- **Débito em aberto é calculado, não armazenado:** o estado vem de
  `total cobrado - total pago`, evitando dados dessincronizados.
- **Regras de negócio separadas da interface:** `services.py` não depende do Tkinter, o que permite testá-lo isoladamente.

## Testes

```bash
pytest
```

## Licença

Distribuído sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Autor

[SEU NOME] - [link do seu GitHub ou LinkedIn]