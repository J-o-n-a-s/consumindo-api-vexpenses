from excel_files import save_file, select_path
from execution_options import (advances, approval_flows, costs_centers,
                               currencies, expenses, expenses_type, projects,
                               reports, team_members)
from file_header import HEADERS, URL
from functions import (clear_screen, connection, create_table, data_ordering,
                       header_and_footer, list_fields, option_selection,
                       options_menu, read_datas, select_view, show_options)

if __name__ == '__main__':
    # Cabeçalho
    header_and_footer(option=False)

    # Seleção de opção
    selected_url = options_menu()

    connected = False
    response = None

    if selected_url != '':
        # Tentativa de conexão
        results_list = connection(headers=HEADERS, url=URL + selected_url)

        # Retorno da tentativa de conexão
        connected = results_list[0]
        response = results_list[1]

        if 'results_list' in locals():
            del results_list

    # Conectado
    if connected:
        del connected
        datas = read_datas(response=response)
        del response
        fields = list_fields(datas=datas)
        result_of_options = []
        exec(
            'result_of_options = '
            + selected_url.replace('-', '_')
            + '(datas=datas)'
        )

        datas = data_ordering(datas=datas, sort_by_key=result_of_options[1])
        selected_option = option_selection(options=result_of_options)

        if select_view() == 'G':
            save_file(
                path=select_path(),
                rows=create_table(
                    datas=datas, options=fields, user=selected_option
                ),
            )
        else:
            show_options(
                datas=datas,
                fields=fields,
                selected=selected_option,
                options=result_of_options,
            )

        if 'datas' in locals():
            del datas

        if 'options' in locals():
            del fields

        if 'selected_option' in locals():
            del selected_option

        if 'result_of_options' in locals():
            del result_of_options

    # Rodapé
    header_and_footer(option=True)
