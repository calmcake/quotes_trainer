import json
from random import choice
from colorama import Fore, init

def create_dict():
    with open("qwe.json", "r", encoding='utf-8') as file_data:
        parsed_data = json.load(file_data)

    return parsed_data

def get_quotes_quantity(in_dict):
    count = 0

    for key in in_dict:
        value = in_dict[key]

        if isinstance(value, list):
            count += len(value)

        else:
            count += 1

    return count


def print_result(is_right):
    if is_right:
        print(Fore.GREEN + "Правильный ответ")

    else:
        print(Fore.RED + "Неверный ответ")


def get_quote(quotes_dict):
    while True:
        composition_name = choice(list(quotes_dict.keys()))
        quote = choice(quotes_dict[composition_name])

        if quote not in checked_quote:
            checked_quote.append(quote)
            return quote


def get_user_answer():
    return input("Из какого произведения цитата выше? \n").strip()


def check_answer(answer, quote, quotes_dict):
    answer_is = False

    if answer in quotes_dict:
        if quote in quotes_dict[answer]:
            answer_is = True

    return answer_is


def ask_quotes(quotes_dict):
    for _ in range(get_quotes_quantity(quotes_dict)):
        quote = get_quote(quotes_dict)
        print("\n"+quote+"\n")
        print_result(check_answer(get_user_answer(), quote, quotes_dict))


init(autoreset=True)

checked_quote = []

ask_quotes(create_dict())
