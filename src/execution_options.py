from file_header import LINE_SIZE
from functions import division, format_print, list_users


def advances(datas: list) -> list:
    return ['', '', '']


def approval_flows(datas: list) -> list:
    return ['', '', '']


def costs_centers(datas: list) -> list:
    active_cost_centers = []
    include_inactive = ' '

    while include_inactive not in 'SN':
        division(number=1)

        include_inactive = (
            input(f'| Deseja incluir os inativos? [S/N] ').strip().upper()
        )

    for data in datas:
        if data['on'] or include_inactive == 'S':
            active_cost_centers.append(data['name'])

    if 'data' in locals():
        del data

    active_cost_centers.sort()

    return ['centro de custo', 'name', active_cost_centers]


def currencies(datas: list) -> list:
    return ['', '', '']


def expenses(datas: list) -> list:
    return ['', '', '']


def expenses_type(datas: list) -> list:
    return ['', '', '']


def projects(datas: list) -> list:
    return ['', '', '']


def reports(datas: list) -> list:
    return ['', '', '']


def team_members(datas: list) -> list:
    len_datas = len(datas)
    number_of_users = '0' + str(len_datas) if len_datas <= 9 else len_datas
    text = f'Ao total existe(m) {number_of_users} usuário(s) cadastrado(s).'
    division(number=1)
    format_print(
        fill_char=' ',
        line_size=LINE_SIZE,
        text=text,
    )

    if 'len_datas' in locals():
        del len_datas

    if 'number_of_users' in locals():
        del number_of_users

    if 'text' in locals():
        del text

    return ['usuário', 'name', list_users(datas=datas)]
