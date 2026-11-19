import sqlite3
import tkinter as tk
from tkinter import messagebox

# - - modelo de criação de botões para menus - -

#     for opcao in opcoes:
#        tk.Button(
#            menu_contas,
#            text=opcao,
#            font=("Arial", 14),
#            bg=COR_BOTAO,
#            fg=COR_TEXTO,
#            width=28,
#        ).pack(pady=7)


CAMINHO_BANCO = "banco.db"
COR_FUNDO = "#2B2B2B"
COR_BOTAO = "#3A3A3A"
COR_TEXTO = "#FFFFFF"


def inicializar_banco():
    conexao = sqlite3.connect(CAMINHO_BANCO)
    try:
        with conexao:
            conexao.execute("""CREATE TABLE IF NOT EXISTS receitas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                valor REAL NOT NULL,
                data DATE NOT NULL
            )""")
            conexao.execute("""CREATE TABLE IF NOT EXISTS despesas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                valor REAL NOT NULL,
                data DATE NOT NULL
            )""")
            conexao.execute("""CREATE TABLE IF NOT EXISTS contas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                tipo TEXT NOT NULL,
                saldo REAL NOT NULL DEFAULT 0
            )""")
            conexao.execute("""CREATE TABLE IF NOT EXISTS relatorios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                tipo TEXT NOT NULL,
                criado_em TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )""")
    finally:
        conexao.close()


def centralizar_janela(janela, largura, altura):
    x = (janela.winfo_screenwidth() - largura) // 2
    y = (janela.winfo_screenheight() - altura) // 2
    janela.geometry(f"{largura}x{altura}+{x}+{y}")


def abrir_menu_contas(janela_admin):
    menu_contas = tk.Toplevel(janela_admin)
    menu_contas.title("Contas - Clientes")
    centralizar_janela(menu_contas, 500, 480)
    menu_contas.configure(bg=COR_FUNDO)
    menu_contas.transient(janela_admin)

    titulo = tk.Label(
        menu_contas,
        text="Gerenciar clientes",
        font=("Arial", 22),
        bg=COR_FUNDO,
        fg=COR_TEXTO,
    )
    titulo.pack(pady=20)

    opcoes = (
        "Adicionar cliente",
        "Remover cliente",
        "Editar cliente",
        "Ver todos os clientes",
        "Pesquisar clientes",
    )
    for opcao in opcoes:
        tk.Button(
            menu_contas,
            text=opcao,
            font=("Arial", 14),
            bg=COR_BOTAO,
            fg=COR_TEXTO,
            width=28,
        ).pack(pady=7)


def abrir_janela_admin(janela_login):
    janela_admin = tk.Toplevel(janela_login)
    janela_admin.title("Sistema Financeiro - Admin")
    janela_admin.state("zoomed")
    janela_admin.configure(bg=COR_FUNDO)
    janela_admin.iconbitmap("icon.ico")

    cabecalho = tk.Frame(janela_admin, bg=COR_FUNDO)
    cabecalho.pack(fill="x", padx=30, pady=20)

    titulo = tk.Label(
        cabecalho,
        text="Sistema Financeiro",
        font=("Arial", 24),
        bg=COR_FUNDO,
        fg=COR_TEXTO,
    )
    titulo.pack(side="left")

    perfil = tk.Label(
        cabecalho,
        text="Perfil: admin",
        font=("Arial", 14),
        bg=COR_FUNDO,
        fg=COR_TEXTO,
    )
    perfil.pack(side="right", padx=15)

    def sair():
        janela_admin.destroy()
        janela_login.deiconify()

    botao_logout = tk.Button(
        cabecalho,
        text="Logout",
        font=("Arial", 12),
        bg="#F44336",
        fg=COR_TEXTO,
        command=sair,
    )
    botao_logout.pack(side="right")
    janela_admin.protocol("WM_DELETE_WINDOW", sair)

    opcoes_frame = tk.Frame(janela_admin, bg=COR_FUNDO)
    opcoes_frame.pack(fill="both", expand=True, padx=80, pady=40)

    for indice in range(2):
        opcoes_frame.grid_rowconfigure(indice, weight=1)
        opcoes_frame.grid_columnconfigure(indice, weight=1)

    opcoes = (
        ("Receitas", None),
        ("Despesas", None),
        ("Contas", lambda: abrir_menu_contas(janela_admin)),
        ("Relatórios", None),
    )
    for indice, (nome, comando) in enumerate(opcoes):
        botao = tk.Button(
            opcoes_frame,
            text=nome,
            font=("Arial", 20),
            bg=COR_BOTAO,
            fg=COR_TEXTO,
            command=comando,
        )
        botao.grid(
            row=indice // 2,
            column=indice % 2,
            sticky="nsew",
            padx=20,
            pady=20,
        )


def validar_login(entrada_usuario, entrada_senha, janela_login):
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    if not usuario or not senha:
        messagebox.showerror(
            "Erro",
            "Por favor, preencha todos os campos.",
            parent=janela_login,
        )
        return

    if usuario != "admin" or senha != "admin":
        messagebox.showerror(
            "Erro",
            "Usuário ou senha incorretos.",
            parent=janela_login,
        )
        return

    abrir_janela_admin(janela_login)
    janela_login.withdraw()


def criar_janela_login():
    janela = tk.Tk()
    janela.title("Sistema Financeiro")
    centralizar_janela(janela, 900, 600)
    janela.configure(bg=COR_FUNDO)
    janela.iconbitmap("icon.ico")

    titulo = tk.Label(
        janela,
        text="Sistema Financeiro",
        font=("Arial", 24),
        bg=COR_FUNDO,
        fg=COR_TEXTO,
    )
    titulo.pack(pady=20)

    rotulo_usuario = tk.Label(
        janela,
        text="Usuário",
        font=("Arial", 18),
        bg=COR_FUNDO,
        fg=COR_TEXTO,
    )
    rotulo_usuario.pack(pady=10)

    entrada_usuario = tk.Entry(janela, font=("Arial", 14), width=30)
    entrada_usuario.pack(pady=5)

    rotulo_senha = tk.Label(
        janela,
        text="Senha",
        font=("Arial", 18),
        bg=COR_FUNDO,
        fg=COR_TEXTO,
    )
    rotulo_senha.pack(pady=10)

    entrada_senha = tk.Entry(janela, font=("Arial", 14), width=30, show="*")
    entrada_senha.pack(pady=5)

    botao_confirmar = tk.Button(
        janela,
        text="Confirmar",
        font=("Arial", 14),
        bg="#4CAF50",
        fg=COR_TEXTO,
        command=lambda: validar_login(entrada_usuario, entrada_senha, janela),
    )
    botao_confirmar.pack(pady=20)

    return janela


def main():
    inicializar_banco()
    janela = criar_janela_login()
    janela.mainloop()


if __name__ == "__main__":
    main()
