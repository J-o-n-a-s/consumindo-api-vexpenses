from excel_files import save_file, select_path
from file_header import HEADERS, URL
from functions import (
    connection,
    create_table,
    header_and_footer,
    list_options,
    list_users,
    read_datas,
    select_view,
    show_options,
    user_selection,
)

if __name__ == '__main__':
    # Cabeçalho
    header_and_footer(option=False)

    # Tentativa de conexão
    results_list = connection(headers=HEADERS, url=URL)

    # Retorno da tentativa de conexão
    connected = results_list[0]
    response = results_list[1]
    del results_list

    # Conectado
    if connected:
        del connected
        datas = read_datas(response=response)
        del response
        options = list_options(datas=datas)
        selected_user = user_selection(users=list_users(datas=datas))

        if select_view() == 'G':
            save_file(
                path=select_path(),
                rows=create_table(
                    datas=datas, options=options, user=selected_user
                ),
            )
        else:
            show_options(datas=datas, options=options, user=selected_user)

        del datas, options, selected_user

    # Rodapé
    header_and_footer(option=True)
