import click
from text_processor import process_text


@click.command()
@click.argument('text', required=False)
def main(text):
    while True:
        if text is None:
            text = input("Введите текст: ")

        try:
            process_text(text)
            break

        except ValueError:
            text = None


if __name__ == "__main__":
    main()
