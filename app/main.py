import click
from text_processor import process_text


@click.command()
@click.argument('text')
def main(text):
    process_text(text)


if __name__ == "__main__":
    main()
