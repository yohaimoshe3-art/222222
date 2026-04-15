
def snake_to_camel(text: str) -> str:
    if '_' in text:
        parts_split = text.split('_')
        return parts_split[0] + "".join(word.capitalize() for word in parts_split[1:])
    else:
        return text


user_input = str(input("enter a sentence with '_': "))

result = snake_to_camel(user_input)

print(result)














