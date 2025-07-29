# Tradutor de EPUB com G4F

Este projeto traduz arquivos EPUB para o português utilizando a API do G4F.

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

*   Selecione o arquivo EPUB de entrada.
*   Defina o local e o nome do arquivo de saída.
*   Acompanhe o progresso da tradução.

### Linha de Comando (CLI)

Execute o script a partir do diretório raiz do projeto:

```bash
python -m epub_translator.main seu_livro.epub livro_traduzido.epub
```

**Argumentos:**

*   `seu_livro.epub`: O caminho para o arquivo EPUB que você deseja traduzir.
*   `livro_traduzido.epub`: O nome do arquivo de saída para o EPUB traduzido.
