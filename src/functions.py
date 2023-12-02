from os import name, system
from time import time

from file_header import END_POINTS, LINE_SIZE
from requests import get, models


def clear_screen() -> None:
    try:
        if name == 'nt':
            system('cls')
        else:
            system('clear')
    except Exception as error:
        format_print(
            fill_char=' ',
            line_size=LINE_SIZE,
            text=f'Falha ao limpar a tela. Ocorreu erro na classe -> {error.__class__}'
        )
        del error


def connection(headers: dict, url: str) -> list:
    start_time = time()
    response = models.Response
    result = False
    division(number=1)

    try:
        response = get(headers=headers, url=url)
    except Exception as error:
        format_print(
            fill_char=' ',
            line_size=LINE_SIZE,
            text=f'Falha na conexão com o VExpenses. Ocorreu erro na classe -> {error.__class__}'
        )
        del error
    else:
        if response.status_code == 200:
            format_print(
                fill_char=' ',
                line_size=LINE_SIZE,
                text='Conexão com o VExpenses realizada com sucesso.'
            )
            result = True
        else:
            format_print(
                fill_char=' ',
                line_size=LINE_SIZE,
                text=f'Falha na conexão com o VExpenses. Código de falha -> {response}.'
            )
    finally:
        final_time = time()
        execution_time = str(round((final_time - start_time), 2)).replace(".", ",")
        format_print(
            fill_char=' ',
            line_size=LINE_SIZE,
            text=f'O tempo de execução foi {execution_time} s.'
        )

        del start_time, final_time, execution_time
        return [result, response]


def create_table(datas: list, options: list, user: int) -> list:
    row = list()
    table = list()
    copy_options = options[:]
    copy_options.insert(0, 'name')
    table.append(copy_options[:])

    for number, data in enumerate(datas):
        if number == user or user == -1:
            for option in copy_options:
                row.append(data[option])
            table.append(row[:])
            row.clear()

    del copy_options, data, number, option, row

    return table


def division(number: int = 1) -> None:
    for value in range(number):
        format_print(fill_char='-', line_size=LINE_SIZE, text='')


def format_print(fill_char: str = ' ', line_size: int = 116, text: str = '') -> None:
    initial_chars = '| '
    final_chars = ' |'

    if text == '':
        initial_chars = '+' + fill_char
        final_chars = fill_char + '+'

    print(initial_chars + text.ljust(line_size, fill_char) + final_chars)

    del final_chars, initial_chars


def header_and_footer(option: bool = False) -> None:
    texts = [
        '>>> PROGBIN AUTOMAÇÃO INDUSTRIAL LTDA <<<',
        'Seja bem-vindo ao software de integração com o VExpenses'
    ]

    if option:
        texts.clear()
        texts = ['Grato pela utilização. Até logo.']

    for number, text in enumerate(texts):
        division(number=1)
        text = text.center(LINE_SIZE, ' ')
        format_print(fill_char=' ', line_size=LINE_SIZE, text=text)

    del number, text, texts

    if option:
        division(number=1)


def list_options(datas: list) -> list:
    information = []
    select_fields = ' '

    while select_fields not in 'SN':
        division(number=1)

        select_fields = (
            input(f'| Selecionar os campos que serão visualizados? [S/N] ').strip().upper()
        )

    keys = list(datas[0].keys())
    keys.sort()

    for number, key in enumerate(keys):
        response = ' '

        if key != 'name':
            if select_fields == 'S':
                while response not in 'SN':
                    response = (
                        input(f'| Deseja visualizar "{key}"? [S/N] ').strip().upper()
                    )

            else:
                response = 'S'

            if response == 'S':
                information.append(key)

    del key, keys, number, response, select_fields

    return sorted(information)


def list_users(datas: list) -> list:
    users = list()
    for number in range(len(datas)):
        user = datas[number]['name']
        users.append(user)
        del user

    del number

    return users


def options_menu() -> str:
    division(number=1)
    menu_text = 'MENU DE OPÇÕES'.center(LINE_SIZE, ' ')
    format_print(fill_char=' ', line_size=LINE_SIZE, text=menu_text)
    division(number=1)
    spacing = '0' * (len(str(len(END_POINTS))) - 1)
    item = 0

    for option in END_POINTS:
        item += 1
        spacing_option = spacing[0:len(spacing) - (len(str(item)) - 1)]
        menu_text = f'-> {spacing_option + str(item)} - {option['menu']}'
        format_print(fill_char=' ', line_size=LINE_SIZE, text=menu_text)

    menu_text = f'-> {spacing}0 - Sair'
    format_print(fill_char=' ', line_size=LINE_SIZE, text=menu_text)
    del item, menu_text, option, spacing, spacing_option
    division(number=1)
    selection_ok = False
    selection = ' '

    while not selection_ok:
        try:
            selection = int(
                input(
                    '| Selecione uma das opções acima: '
                ).strip().upper()
            )
        except ValueError:
            format_print(
                fill_char=' ',
                line_size=LINE_SIZE,
                text='Por gentileza, selecione uma opção válida.'
            )
        except Exception as error:
            print(error.__class__)
            format_print(
                fill_char=' ',
                line_size=LINE_SIZE,
                text=f'Ocorreu erro {error.__class__} ao selecionar uma opção.'
            )
            del error
        else:
            if 0 <= selection <= len(END_POINTS):
                selection_ok = True
            else:
                format_print(
                    fill_char=' ',
                    line_size=LINE_SIZE,
                    text='Por gentileza, selecione uma opção válida.'
                )

    del selection_ok
    # division(number=1)

    return END_POINTS[selection - 1]['url'] if selection > 0 else ''


def read_datas(response: models.Response) -> list:
    datas = response.json()['data']
    return datas


def select_view() -> str:
    selection = ' '

    while selection not in 'GV':
        division(number=1)

        selection = (
            input('| Deseja gravar [G] em arquivo, ou visualizar [V]? [G/V] ')
            .strip()
            .upper()
        )

    return selection


def show_options(datas: list, options: list, user: int) -> None:
    for number, data in enumerate(datas):
        if number == user or user == -1:
            division(number=1)

            for option in options:
                format_print(
                    fill_char=' ',
                    line_size=LINE_SIZE,
                    text=f'Para o usuário "{data['name']}" e chave "{option}" o valor é "{data[option]}".'
                )

    del data, number, option


def option_selection(options: list) -> int:
    division(number=1)
    spacing = '0' * (len(str(len(options))) - 1)

    format_print(
        fill_char=' ',
        line_size=LINE_SIZE,
        text='Selecione o número da opção que deseja consultar as informações:'
    )

    for number, option in enumerate(options):
        number += 1
        format_print(
            fill_char=' ',
            line_size=LINE_SIZE,
            text=f' -> {spacing + str(number) if number <= 9 else number} - {option}'
        )

    del number, option
    format_print(
        fill_char=' ',
        line_size=LINE_SIZE,
        text=f' -> {spacing}0 - Todas as opções'
    )
    selection_ok = False
    selection = -1

    while not selection_ok:
        try:
            selection = int(input('| > '))
        except ValueError:
            format_print(
                fill_char=' ',
                line_size=LINE_SIZE,
                text='Por gentileza, selecione uma opção válida.'
            )
        except Exception as error:
            print(error.__class__)
            format_print(
                fill_char=' ',
                line_size=LINE_SIZE,
                text=f'Ocorreu erro {error.__class__} ao selecionar uma opção.'
            )
            del error
        else:
            if 0 <= selection <= len(options):
                selection_ok = True
            else:
                format_print(
                    fill_char=' ',
                    line_size=LINE_SIZE,
                    text='Por gentileza, selecione uma opção válida.'
                )

    del selection_ok

    return selection - 1
