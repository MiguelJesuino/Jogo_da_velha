import customtkinter as ctk
from tkinter import messagebox

# definindo tema
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


# Criação da classe principal do aplicativo, herdando de CTk (CustomTkinter)
class JogoDaVelhaApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Jogo da Velha")
        self.geometry("300x400")
        self.resizable(False, False)

        self.jogador_atual = "X"

        self.botoes = [[None for _ in range(3)] for _ in range(3)]

        self.label_turno = ctk.CTkLabel(self, text=f"Turno: {self.jogador_atual}", font=("Arial", 16))
        self.label_turno.pack(pady=10)

        self.frame = ctk.CTkFrame(self)
        self.frame.pack()

        # Cria os botões do tabuleiro (3x3) e adiciona ao frame
        for i in range(3):
            for j in range(3):
                botao = ctk.CTkButton(self.frame, text="", width=80, height=80,
                                      command=lambda i=i, j=j: self.clique(i, j),
                                      font=("Arial", 24))
                botao.grid(row=i, column=j, padx=5, pady=5)
                self.botoes[i][j] = botao

        self.botao_resetar = ctk.CTkButton(self, text="Resetar", command=self.resetar)
        self.botao_resetar.pack(pady=10)

    #  Método chamado quando um botão do tabuloeiro é clicado
    def clique(self, i, j):
        botao = self.botoes[i][j]
        if botao.cget("text") == "":
            botao.configure(text=self.jogador_atual)
            if self.verificar_vitoria():
                messagebox.showinfo("Fim de Jogo", f"Jogador {self.jogador_atual} venceu!")
                self.desabilitar_botoes()
            elif self.verificar_empate():
                messagebox.showinfo("Empate", "O jogo empatou!")
                self.desabilitar_botoes()
            else:
                self.jogador_atual = "O" if self.jogador_atual == "X" else "X"
                self.label_turno.configure(text=f"Turno: {self.jogador_atual}")

    # Verifica se há uma linha, coluna ou diagonal com três símbolos iguais
    def verificar_vitoria(self):
        for i in range(3):
            # Verifica linhas
            if self.botoes[i][0].cget("text") == self.botoes[i][1].cget("text") == self.botoes[i][2].cget("text") != "":
                return True
            # Verifica colunas
            if self.botoes[0][i].cget("text") == self.botoes[1][i].cget("text") == self.botoes[2][i].cget("text") != "":
                return True

        # Verifica diagonais
        if self.botoes[0][0].cget("text") == self.botoes[1][1].cget("text") == self.botoes[2][2].cget("text") != "":
            return True
        if self.botoes[0][2].cget("text") == self.botoes[1][1].cget("text") == self.botoes[2][0].cget("text") != "":
            return True
        return False

    # Verifica se todos os botões foram clicados sem vencedor
    def verificar_empate(self):
        for linha in self.botoes:
            for botao in linha:
                if botao.cget("text") == "":
                    return False
        return True

    # Desabilita todos os botões do tabuleiro
    def desabilitar_botoes(self):
        for linha in self.botoes:
            for botao in linha:
                botao.configure(state="disabled")

    # Reinicia o jogo: limpa os botões e reinicia o turno
    def resetar(self):
        for linha in self.botoes:
            for botao in linha:
                botao.configure(text="", state="normal")
        self.jogador_atual = "X"
        self.label_turno.configure(text=f"Turno: {self.jogador_atual}")

# Executar o aplicativo
if __name__ == "__main__":
    app = JogoDaVelhaApp()
    app.mainloop()

