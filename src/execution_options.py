from file_header import LINE_SIZE
from functions import data_ordering, division, format_print, list_users


def advances(datas: list) -> list:
    return ['', '', '']


def approval_flows(datas: list) -> list:
    return ['', '', '']


def costs_centers(datas: list) -> list:
    active_cost_centers = []
    copy_datas = []
    filters = ['name', 'on']
    include_inactive = ' '
    option = 'centro de custo'
    text = ''

    while include_inactive not in 'SN':
        division(number=1)

        include_inactive = (
            input(f'| Deseja incluir os inativos? [S/N] ').strip().upper()[0]
        )

    copy_datas.append(
        data_ordering(datas=datas, sort_by_key=filters[0])
    )

    copy_datas.append([])
    for data in copy_datas[0]:
        if data[filters[1]] or include_inactive == 'S':
            copy_datas[1].append(data)

    copy_datas.pop(0)
    copy_datas = copy_datas[0]

    for data in copy_datas:
        if data[filters[1]] or include_inactive == 'S':
            if include_inactive == 'S':
                if data[filters[1]]:
                    text = '(ativo)'
                else:
                    text = '(inativo)'
            active_cost_centers.append(
                data[filters[0]]
                if include_inactive != 'S'
                else f'{data[filters[0]]} {text}'
            )

    if 'data' in locals():
        del data

    if 'include_inactive' in locals():
        del include_inactive

    if 'text' in locals():
        del text

    # active_cost_centers.sort()

    return [option, filters, active_cost_centers, copy_datas]


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
    copy_datas = []
    filters = ['name', 'active']
    include_inactive = ' '
    len_datas = len(datas)
    number_of_users = '0' + str(len_datas) if len_datas <= 9 else len_datas
    option = 'usuário'
    text = f'Ao total existe(m) {number_of_users} usuário(s) cadastrado(s).'
    division(number=1)

    format_print(
        fill_char=' ',
        line_size=LINE_SIZE,
        text=text,
    )

    # INCLUIR VERIFICAÇÃO DE MEMBROS INATIVOS

    copy_datas = data_ordering(datas=datas, sort_by_key=filters[0])

    if 'include_inactive' in locals():
        del include_inactive

    if 'len_datas' in locals():
        del len_datas

    if 'number_of_users' in locals():
        del number_of_users

    if 'text' in locals():
        del text

    return [option, filters, list_users(datas=datas), copy_datas]
