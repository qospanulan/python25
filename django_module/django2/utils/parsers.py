

def parse_list_from_str(l: str) -> list:
    """
    :param l: Example: '[2, 3]', '["banana", "apple"]'
    :return: [2, 3]
    """

    values = [elem.strip(' ') for elem in l[1:-1].split(",")]

    return values

