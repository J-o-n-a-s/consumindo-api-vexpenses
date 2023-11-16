from time import time

from requests import get, models

# Constantes
LINE_SIZE = 116


def connection(headers: dict, url: str) -> list:
    start_time = time()
    response = models.Response
    result = False
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
        format_print(fill_char='-', line_size=LINE_SIZE, text='')
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
        '>>> VETER AUTOMAÇÃO INDUSTRIAL LTDA. <<<',
        'Seja bem-vindo ao software de integração com o VExpenses'
    ]

    if option:
        texts.clear()
        texts = ['Grato pela utilização. Até logo.']

    for number, text in enumerate(texts):
        format_print(fill_char='-', line_size=LINE_SIZE, text='')
        text = text.center(LINE_SIZE, ' ')
        format_print(fill_char=' ', line_size=LINE_SIZE, text=text)

        if number == (len(texts) - 1):
            format_print(fill_char='-', line_size=LINE_SIZE, text='')

    del number, text, texts


def list_options(datas: list) -> list:
    information = []
    select_fields = ' '

    while select_fields not in 'SN':
        format_print(fill_char='-', line_size=LINE_SIZE, text='')

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


def read_datas(response: models.Response) -> list:
    datas = response.json()['data']
    len_datas = len(datas)
    format_print(
        fill_char=' ',
        line_size=LINE_SIZE,
        text=f'Ao total existem {"0" + str(len_datas) if len_datas <= 9 else len_datas} usuário(s) cadastrado(s).'
    )
    del len_datas

    return datas


def select_view() -> str:
    selection = ' '

    while selection not in 'GV':
        format_print(fill_char='-', line_size=LINE_SIZE, text='')

        selection = (
            input('| Deseja gravar [G] em arquivo, ou visualizar [V]? [G/V] ')
            .strip()
            .upper()
        )

    return selection


def show_options(datas: list, options: list, user: int) -> None:
    for number, data in enumerate(datas):
        if number == user or user == -1:
            format_print(fill_char='-', line_size=LINE_SIZE, text='')

            for option in options:
                format_print(
                    fill_char=' ',
                    line_size=LINE_SIZE,
                    text=f'Para o usuário "{data['name']}" e chave "{option}" o valor é "{data[option]}".'
                )

    del data, number, option


def user_selection(users: list) -> int:
    format_print(fill_char='-', line_size=LINE_SIZE, text='')

    format_print(
        fill_char=' ',
        line_size=LINE_SIZE,
        text='Selecione o número do usuário que deseja consultar as informações:'
    )

    for number, user in enumerate(users):
        format_print(
            fill_char=' ',
            line_size=LINE_SIZE,
            text=f'{" -> 0" + str(number + 1) if number + 1 <= 9 else number + 1} - {user}'
        )

    del number, user
    format_print(
        fill_char=' ',
        line_size=LINE_SIZE,
        text=' -> 00 - Todos os usuários'
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
            if 0 <= selection <= len(users):
                selection_ok = True
            else:
                format_print(
                    fill_char=' ',
                    line_size=LINE_SIZE,
                    text='Por gentileza, selecione uma opção válida.'
                )

    del selection_ok

    return selection - 1
