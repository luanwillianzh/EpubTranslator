import argparse
from epub_translator.translator import EpubTranslator
from rich.progress import Progress

def main():
    parser = argparse.ArgumentParser(description='Traduz um arquivo EPUB usando g4f.')
    parser.add_argument('input_file', help='O arquivo EPUB de entrada.')
    parser.add_argument('output_file', help='O arquivo EPUB de saída.')

    args = parser.parse_args()

    translator = EpubTranslator()

    with Progress() as progress:
        task = progress.add_task("[cyan]Traduzindo...", total=100)

        def update_progress(current, total):
            progress.update(task, completed=(current / total) * 100)

        translator.translate_epub(args.input_file, args.output_file, update_progress)
    
    print(f'Epub traduzido e salvo em: {args.output_file}')

if __name__ == '__main__':
    main()