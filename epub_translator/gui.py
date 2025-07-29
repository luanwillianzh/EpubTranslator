import customtkinter as ctk
from tkinter import filedialog, messagebox
from epub_translator.translator import EpubTranslator
import threading

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Tradutor de EPUB")
        self.geometry("500x350")

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        # Variáveis
        self.input_file = ctk.StringVar()
        self.output_file = ctk.StringVar()

        # Widgets
        self.create_widgets()

    def create_widgets(self):
        # Frame principal
        frame = ctk.CTkFrame(self)
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Arquivo de Entrada
        ctk.CTkLabel(frame, text="Arquivo de Entrada (EPUB):").pack(pady=5)
        self.input_entry = ctk.CTkEntry(frame, textvariable=self.input_file, width=300, state="readonly")
        self.input_entry.pack(pady=5)
        ctk.CTkButton(frame, text="Selecionar Arquivo", command=self.select_input_file).pack(pady=5)

        # Arquivo de Saída
        ctk.CTkLabel(frame, text="Arquivo de Saída (EPUB):").pack(pady=5)
        self.output_entry = ctk.CTkEntry(frame, textvariable=self.output_file, width=300, state="readonly")
        self.output_entry.pack(pady=5)
        ctk.CTkButton(frame, text="Selecionar Destino", command=self.select_output_file).pack(pady=5)

        # Botão de Tradução
        self.translate_button = ctk.CTkButton(frame, text="Traduzir", command=self.start_translation_thread)
        self.translate_button.pack(pady=20)

        # Progresso
        self.progress_bar = ctk.CTkProgressBar(frame, width=300)
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=5)

        self.status_label = ctk.CTkLabel(frame, text="")
        self.status_label.pack(pady=5)

    def select_input_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Arquivos EPUB", "*.epub")])
        if file_path:
            self.input_file.set(file_path)

    def select_output_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".epub", filetypes=[("Arquivos EPUB", "*.epub")])
        if file_path:
            self.output_file.set(file_path)

    def start_translation_thread(self):
        input_file = self.input_file.get()
        output_file = self.output_file.get()

        if not all([input_file, output_file]):
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
            return

        self.translate_button.configure(state="disabled")
        self.status_label.configure(text="Traduzindo...")
        self.progress_bar.set(0)

        thread = threading.Thread(
            target=self.run_translation,
            args=(input_file, output_file)
        )
        thread.start()

    def run_translation(self, input_file, output_file):
        try:
            translator = EpubTranslator()
            translator.translate_epub(input_file, output_file, self.update_progress)
            self.after(0, self._on_translation_success, output_file)
        except Exception as e:
            self.after(0, self._on_translation_error, e)
        finally:
            self.after(0, self._on_translation_finally)

    def _on_translation_success(self, output_file):
        self.status_label.configure(text="Tradução concluída!")
        messagebox.showinfo("Sucesso", f"Epub traduzido e salvo em: {output_file}")

    def _on_translation_error(self, error):
        self.status_label.configure(text="Erro na tradução.")
        messagebox.showerror("Erro", f"Ocorreu um erro: {error}")

    def _on_translation_finally(self):
        self.translate_button.configure(state="normal")
        self.progress_bar.set(0)
        self.status_label.configure(text="")

    def update_progress(self, current, total):
        progress_value = current / total
        self.after(0, self._update_progress_ui, progress_value, current, total)

    def _update_progress_ui(self, progress_value, current, total):
        self.progress_bar.set(progress_value)
        self.status_label.configure(text=f"Traduzindo: {current}/{total}")

if __name__ == "__main__":
    app = App()
    app.mainloop()