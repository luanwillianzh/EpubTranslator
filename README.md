# Tradutor de EPUB com Gemini

Este projeto traduz arquivos EPUB para o português utilizando a API do Google Gemini.

## Instalação

1.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

## Uso

Este projeto oferece duas formas de uso: através de uma interface gráfica (GUI) ou pela linha de comando (CLI).

### Interface Gráfica (GUI)

Para iniciar a interface gráfica, execute o seguinte comando no diretório raiz do projeto:

```bash
python -m epub_translator.gui
```

A interface permite que você:

*   Insira sua chave da API Gemini.
*   Selecione o arquivo EPUB de entrada.
*   Defina o local e o nome do arquivo de saída.
*   Acompanhe o progresso da tradução.

### Linha de Comando (CLI)

Execute o script a partir do diretório raiz do projeto:

```bash
python -m epub_translator.main seu_livro.epub livro_traduzido.epub --api_key SUA_CHAVE_API
```

**Argumentos:**

*   `seu_livro.epub`: O caminho para o arquivo EPUB que você deseja traduzir.
*   `livro_traduzido.epub`: O nome do arquivo de saída para o EPUB traduzido.
*   `--api_key`: Sua chave de API do Google Gemini. Você pode obter uma no [Google AI Studio](https://aistudio.google.com/app/apikey).
