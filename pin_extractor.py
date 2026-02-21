from typing import List


def pin_extractor(poems: List[str]) -> List[str]:

    if not isinstance(poems, list):
        raise TypeError("Input 'poems' must be a list of strings.")

    secret_codes: List[str] = []
    for poem in poems:
        if not isinstance(poem, str):
            raise TypeError("Each poem must be a string.")

        code_chars: List[str] = []
        lines = poem.split("\n")
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                code_chars.append(str(len(words[line_index])))
            else:
                code_chars.append("0")

        secret_codes.append("".join(code_chars))

    return secret_codes


if __name__ == "__main__":
    test_poems = [
        "Stars and the moon\nshine in the sky\nwhite and bright\nuntil the end of the night",
        "The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow",
        "There\nonce\nwas\na\ndragon",
    ]

    try:
        pins = pin_extractor(test_poems)
        print(f"Extracted PINs: {pins}")
    except TypeError as e:
        print(f"Error: {e}")
