import customtkinter as ctk

# Define o tema (pode trocar para "Dark" ou "Light")
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

# Cria a janela principal
app = ctk.CTk()
app.title("Sistema de Ordem de Serviço")
app.geometry("1200x650")  # Largura x Altura

# Mantém a janela aberta
app.mainloop()
