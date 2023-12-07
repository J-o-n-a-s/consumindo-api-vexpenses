from os import name, system
from time import time

from file_header import END_POINTS, LINE_SIZE
from requests import get, models


def check_inclusion_of_inactive() -> bool:
    include_inactive = ' '

    while include_inactive not in 'SN':
        division(number=1)

        include_inactive = (
            input(f'| Deseja incluir os inativos? [S/N] ').strip().upper()[0]
        )

    return True if include_inactive == 'S' else False


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

        if 'error' in locals():
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

        if 'error' in locals():
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

        if 'start_time' in locals():
            del start_time

        if 'final_time' in locals():
            del final_time

        if 'execution_time' in locals():
            del execution_time

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

    if 'copy_options' in locals():
        del copy_options

    if 'data' in locals():
        del data

    if 'number' in locals():
        del number

    if 'option' in locals():
        del option

    if 'row' in locals():
        del row

    return table


def data_ordering(datas: list, sort_by_key: str) -> list:
    copy_datas = sorted(datas, key=lambda dicionario: dicionario[sort_by_key])
    return copy_datas[:]


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

    if 'final_chars' in locals():
        del final_chars

    if 'initial_chars' in locals():
        del initial_chars


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

    if 'number' in locals():
        del number

    if 'text' in locals():
        del text

    if 'texts' in locals():
        del texts

    if option:
        division(number=1)


def list_fields(datas: list) -> list:
    information = []
    select_fields = ' '

    while select_fields not in 'SN':
        division(number=1)

        select_fields = (
            input(f'| Selecionar os campos que serão visualizados? [S/N] ').strip().upper()[0]
        )

    keys = list(datas[0].keys())
    keys.sort()

    for number, key in enumerate(keys):
        response = ' '

        if key != 'name':
            if select_fields == 'S':
                while response not in 'SN':
                    response = (
                        input(f'| Deseja visualizar "{key}"? [S/N] ').strip().upper()[0]
                    )

            else:
                response = 'S'

            if response == 'S':
                information.append(key)

    del key, keys, number, response, select_fields

    return sorted(information)


def list_users(datas: list, filters: tuple, include_inactive: bool = None) -> list:
    users = []

    for data in datas:
        if filters[1] or include_inactive:
            if include_inactive:
                text = '(ativo)' if data[filters[1]] else '(inativo)'
                user = f'{data[filters[0]]} {text}'
            else:
                user = data[filters[0]]

            users.append(user)

    if 'data' in locals():
        del data

    if 'text' in locals():
        del text

    if 'user' in locals():
        del user

    return users[:]


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

    if 'item' in locals():
        del item

    if 'menu_text' in locals():
        del menu_text

    if 'option' in locals():
        del option

    if 'spacing' in locals():
        del spacing

    if 'spacing_option' in locals():
        del spacing_option

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

            if 'error' in locals():
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

    if 'selection_ok' in locals():
        del selection_ok

    return END_POINTS[selection - 1]['url'] if selection > 0 else ''


def option_selection(options: list) -> int:
    division(number=1)
    spacing = '0' * (len(str(len(options[2]))) - 1)

    format_print(
        fill_char=' ',
        line_size=LINE_SIZE,
        text='Selecione o número da opção que deseja consultar as informações:'
    )

    for number, option in enumerate(options[2]):
        number += 1
        format_print(
            fill_char=' ',
            line_size=LINE_SIZE,
            text=f' -> {spacing + str(number) if number <= 9 else number} - {option}'
        )

    if 'number' in locals():
        del number

    if 'option' in locals():
        del option

    format_print(
        fill_char=' ',
        line_size=LINE_SIZE,
        text=f' -> {spacing}0 - Todas as opções'
    )

    if 'spacing' in locals():
        del spacing

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

            if 'error' in locals():
                del error
        else:
            if 0 <= selection <= len(options[2]):
                selection_ok = True
            else:
                format_print(
                    fill_char=' ',
                    line_size=LINE_SIZE,
                    text='Por gentileza, selecione uma opção válida.'
                )

    if 'selection_ok' in locals():
        del selection_ok

    return selection - 1


def read_datas(response: models.Response) -> list:
    datas = response.json()['data']
    return datas


def sanitize_data(datas: list, filters: tuple, include_inactive: bool) -> list:
    sanitized_data = []

    for data in datas:
        try:
            copy_filter = datas[filters[1]]
        except TypeError:
            sanitized_data.append(data)
        else:
            if data[copy_filter] or include_inactive:
                sanitized_data.append(data)

    if 'copy_filter' in locals():
        del copy_filter

    if 'data' in locals():
        del data

    return data_ordering(datas=sanitized_data, sort_by_key=filters[0])


def select_view() -> str:
    selection = ' '

    while selection not in 'GV':
        division(number=1)

        selection = (
            input('| Deseja gravar [G] em arquivo, ou visualizar [V]? [G/V] ')
            .strip()
            .upper()
            [0]
        )

    return selection


def show_options(datas: list, fields: list, selected: int, options: list) -> None:
    if selected == -1:
        for number, data in enumerate(datas):
            division(number=1)

            for field in fields:
                format_print(
                    fill_char=' ',
                    line_size=LINE_SIZE,
                    text=f'Para {options[0]} "{options[2][number]}" e chave "{field}" o valor é "{data[field]}".'
                )

        if 'number' in locals():
            del number

    else:
        division(number=1)
        data = datas[selected]

        for field in fields:
            format_print(
                fill_char=' ',
                line_size=LINE_SIZE,
                text=f'Para {options[0]} "{options[2][selected]}" e chave "{field}" o valor é "{data[field]}".'
            )

    if 'data' in locals():
        del data

    if 'field' in locals():
        del field
