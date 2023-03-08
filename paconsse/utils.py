from rich import print

def pprint(string, name="undefined", category="INFO"):
    """
    Use this function anywhere to pretty print anything to the console.
    The first argument is the string to be printed, the second is the name of the function or script that is printing it, typically __name__.
    An optional third argument is the category of the print, which is "INFO" by default. It can be "WARNING", "ERROR", or "SUCCESS".
    The color of the tag is determined by the name of the category. The text always appears in white.
    """

    color = {
        "INFO": "blue",
        "WARNING": "yellow",
        "ERROR": "red",
        "SUCCESS": "green",
    }.get(category, "blue")

    print(
        f"[bold {color}][{category}][/bold {color}][bold red]\[{name}][/bold red] {string}"
    )
