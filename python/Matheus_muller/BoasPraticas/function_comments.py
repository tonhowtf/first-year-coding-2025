

def get_name(fullname: str) -> str:
    """
    extract the name of the file by splitting using underscore '_'

    [in]
        >> fullname: example_1.2.3
    [output]
        >> name: example
    """
    name, *_ = fullname.split("_")
    return name