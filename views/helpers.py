from rich.console import Console
from rich.table import Table


def title_1(message):
    space = 20
    print(
        "\n\n"
        f"{' '*space}"
        "********************************** \n"
        f"{' '*space}"
        f"***          {message}         *** \n"
        f"{' '*space}"
        "********************************** \n"
        "\n\n"
    )


def title_2(message):
    space = 10
    print(
        "\n\n"
        f"{' '*space}"
        "---------------------------------- \n"
        f"{' '*space}"
        f"            {message}             \n"
        f"{' '*space}"
        "---------------------------------- \n"
        "\n\n"
    )


def title_3(message):
    space = 5
    print(
        "\n\n"
        f"{' '*space}"
        "°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°° \n"
        f"{' '*space}"
        f"            {message}             \n"
        f"{' '*space}"
        "°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°° \n"
        "\n\n"
    )


def title_4(message):
    space = 5
    print(
        "\n\n"
        f"{' '*space}"
        ":::::::::::::::::::::::::::::::::: \n"
        f"{' '*space}"
        f"            {message}             \n"
        f"{' '*space}"
        ":::::::::::::::::::::::::::::::::: \n"
        "\n\n"
    )


def print_table(title: str, columns: list, rows: list[list]):
    table = Table(title=title)
    for column in columns:
        table.add_column(column)

    for row in rows:
        table.add_row(*row, style="bright_green")

    console = Console()
    print("\n")
    console.print(table)
    print("\n")
