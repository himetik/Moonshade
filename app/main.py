import click
from text_processor import process_text


@click.command()
@click.argument('text', required=False)
@click.option('--file', type=click.File('r'), help="Text file")
def main(text, file):
    if file:
        text = file.read()

    attempts = 3
    while attempts > 0:
        if text is None:
            text = input("Input: ")

        try:
            process_text(text)
            break

        except ValueError as e:
            print(f"Error: {e}")
            text = None
            attempts -= 1

        if attempts == 0:
            print("The number of attempts has been exceeded.")
            break


if __name__ == "__main__":
    main()
