from file_header import LINE_SIZE
from functions import (check_inclusion_of_inactive, division, format_print,
                       list_users, sanitize_data)


def advances(datas: list) -> list:
    return ['', '', '']


def approval_flows(datas: list) -> list:
    approval_flow_list = []
    copy_datas = []
    filters = ('description', '')
    title = 'fluxo de aprovação'

    copy_datas = sanitize_data(
        datas=datas, filters=filters, include_inactive=True
    )

    for data in copy_datas:
        approval_flow_list.append(data[filters[0]])

    if 'data' in locals():
        del data

    return [title, filters, approval_flow_list, copy_datas]


def costs_centers(datas: list) -> list:
    copy_datas = []
    filters = ('name', 'on')
    list_of_cost_centers = []
    text = ''
    title = 'centro de custo'

    include_inactive = check_inclusion_of_inactive()
    copy_datas = sanitize_data(
        datas=datas, filters=filters, include_inactive=include_inactive
    )

    for data in copy_datas:
        if data[filters[1]] or include_inactive:
            if include_inactive:
                if data[filters[1]]:
                    text = '(ativo)'
                else:
                    text = '(inativo)'

            list_of_cost_centers.append(
                data[filters[0]]
                if not include_inactive
                else f'{data[filters[0]]} {text}'
            )

    if 'data' in locals():
        del data

    if 'include_inactive' in locals():
        del include_inactive

    if 'text' in locals():
        del text

    return [title, filters, list_of_cost_centers, copy_datas]


def currencies(datas: list) -> list:
    copy_datas = []
    filters = ('name', '')
    list_of_currencies = []
    title = 'moeda'

    copy_datas = sanitize_data(
        datas=datas, filters=filters, include_inactive=True
    )

    for data in copy_datas:
        list_of_currencies.append(data[filters[0]])

    if 'data' in locals():
        del data

    return [title, filters, list_of_currencies, copy_datas]


def expenses(datas: list) -> list:
    return ['', '', '']


def expenses_type(datas: list) -> list:
    copy_datas = []
    filters = ('description', 'on')
    list_of_expenses_type = []
    text = ''
    title = 'tipo de despesa'

    include_inactive = check_inclusion_of_inactive()
    copy_datas = sanitize_data(
        datas=datas, filters=filters, include_inactive=include_inactive
    )

    for data in copy_datas:
        if data[filters[1]] or include_inactive:
            if include_inactive:
                if data[filters[1]]:
                    text = '(ativo)'
                else:
                    text = '(inativo)'

            list_of_expenses_type.append(
                data[filters[0]]
                if not include_inactive
                else f'{data[filters[0]]} {text}'
            )

    if 'data' in locals():
        del data

    if 'include_inactive' in locals():
        del include_inactive

    if 'text' in locals():
        del text

    return [title, filters, list_of_expenses_type, copy_datas]


def projects(datas: list) -> list:
    copy_datas = []
    filters = ('name', 'on')
    project_list = []
    text = ''
    title = 'projetos'

    include_inactive = check_inclusion_of_inactive()
    copy_datas = sanitize_data(
        datas=datas, filters=filters, include_inactive=include_inactive
    )

    for data in copy_datas:
        if data[filters[1]] or include_inactive:
            if include_inactive:
                if data[filters[1]]:
                    text = '(ativo)'
                else:
                    text = '(inativo)'

            project_list.append(
                data[filters[0]]
                if not include_inactive
                else f'{data[filters[0]]} {text}'
            )

    if 'data' in locals():
        del data

    if 'include_inactive' in locals():
        del include_inactive

    if 'text' in locals():
        del text

    return [title, filters, project_list, copy_datas]


def reports(datas: list) -> list:
    copy_datas = []
    filters = ('description', 'on')
    list_of_reports = []
    text = ''
    title = 'relatórios'

    include_inactive = check_inclusion_of_inactive()
    copy_datas = sanitize_data(
        datas=datas, filters=filters, include_inactive=include_inactive
    )

    for data in copy_datas:
        if data[filters[1]] or include_inactive:
            if include_inactive:
                if data[filters[1]]:
                    text = '(ativo)'
                else:
                    text = '(inativo)'

            list_of_reports.append(
                data[filters[0]]
                if not include_inactive
                else f'{data[filters[0]]} {text}'
            )

    if 'data' in locals():
        del data

    if 'include_inactive' in locals():
        del include_inactive

    if 'text' in locals():
        del text

    return [title, filters, list_of_reports, copy_datas]


def team_members(datas: list) -> list:
    copy_datas = []
    filters = ('name', 'active')
    len_datas = len(datas)
    number_of_users = '0' + str(len_datas) if len_datas <= 9 else len_datas
    text = f'Ao total existe(m) {number_of_users} usuário(s) cadastrado(s).'
    title = 'usuário'
    user_list = []

    division(number=1)

    format_print(
        fill_char=' ',
        line_size=LINE_SIZE,
        text=text,
    )

    include_inactive = check_inclusion_of_inactive()
    copy_datas = sanitize_data(
        datas=datas, filters=filters, include_inactive=include_inactive
    )
    user_list = list_users(
        datas=copy_datas, filters=filters, include_inactive=include_inactive
    )

    if 'include_inactive' in locals():
        del include_inactive

    if 'len_datas' in locals():
        del len_datas

    if 'number_of_users' in locals():
        del number_of_users

    if 'text' in locals():
        del text

    return [title, filters, user_list, copy_datas]
