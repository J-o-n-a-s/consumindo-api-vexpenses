from file_header import LINE_SIZE
from functions import division, format_print, list_users


def advances(datas: list) -> list:
    ...


def approval_flows(datas: list) -> list:
    ...


def costs_centers(datas: list) -> list:
    ...


def currencies(datas: list) -> list:
    ...


def expenses(datas: list) -> list:
    ...


def expenses_type(datas: list) -> list:
    ...


def projects(datas: list) -> list:
    ...


def reports(datas: list) -> list:
    ...


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
    del len_datas, number_of_users, text

    return list_users(datas=datas)
