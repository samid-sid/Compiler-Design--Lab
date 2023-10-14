import re


def printing(key, value):
    print(f"{key} ({len(value)}) : ", end="")
    print(*value, sep=' ')


def analyzer(text):
    punctuation_pattern = r'[.,;:!?]'
    constant_pattern = r'\b\d+\b'
    parenthesis_pattern = r'[(){}\[\]]'
    arithmetic_pattern = r'[+*/%-]'
    keyword_pattern = r'\b(auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while)\b'
    exclude = "auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while"
    identifier_pattern = r"\b(?!" + exclude + r")[a-zA-Z_]\w*\b"

    try:
        temp = re.findall(punctuation_pattern, text)
        if len(temp) >= 1:
            printing("Punctuation", temp)

        temp = re.findall(constant_pattern, text)
        if len(temp) >= 1:
            printing("Constant", temp)

        temp = re.findall(parenthesis_pattern, text)
        if len(temp) >= 1:
            printing("Parenthesis", temp)

        temp = re.findall(arithmetic_pattern, text)
        if len(temp) >= 1:
            printing("Arithmatic Operator", temp)

        temp = re.findall(identifier_pattern, text)
        if len(temp) >= 1:
            printing("Identifier", temp)

        temp = re.findall(keyword_pattern, text)
        if len(temp) >= 1:
            printing("Keyword", temp)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    text = """
            int a = b+c * 10;
    
            """
    # text  = input("Write Your Text : ")
    analyzer(text)


    # print(text)
