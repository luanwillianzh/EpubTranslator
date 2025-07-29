import os
import shutil
import tempfile
import zipfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from g4f.client import Client

client = Client()

class EpubTranslator:
    def __init__(self):
        pass

    def _translate_html_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        try:
            # Adicionando um prompt mais claro para a tradução
            prompt = f"Traduza o seguinte texto do inglês para o português, mantendo a formatação e o tom originais: '{content}'"
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                web_search=False
            ).choices[0].message.content.split("```xml\n")[1].split("\n```")[0]
        except Exception as e:
            print(f"Aviso: Não foi possível traduzir o conteúdo: {content[:50]}... Erro: {e}")
            response = content
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(response)

    def translate_epub(self, input_path, output_path, progress_callback=None):
        temp_dir = tempfile.mkdtemp()
        
        try:
            # 1. Descompactar o EPUB
            with zipfile.ZipFile(input_path, 'r') as zip_ref:
                zip_ref.extractall(temp_dir)

            # 2. Listar arquivos .html e .xhtml
            files_to_translate = []
            for root, _, files in os.walk(temp_dir):
                for file in files:
                    if file.endswith(('.html', '.xhtml')):
                        if file not in ['nav.html', 'nav.xhtml', 'toc.html', 'toc.xhtml']:
                            files_to_translate.append(os.path.join(root, file))
            
            total_files = len(files_to_translate)
            
            # 3. Traduzir os arquivos listados em paralelo
            with ThreadPoolExecutor(max_workers=4) as executor:
                futures = [executor.submit(self._translate_html_file, file_path) for file_path in files_to_translate]
                
                for i, future in enumerate(as_completed(futures)):
                    future.result()  # Aguarda a conclusão e lida com exceções
                    if progress_callback:
                        progress_callback(i + 1, total_files)

            # 4. Compactar novamente em um novo arquivo EPUB
            with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, _, files in os.walk(temp_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, temp_dir)
                        zipf.write(file_path, arcname)

        finally:
            # Limpar o diretório temporário
            shutil.rmtree(temp_dir)
