# Constantes

END_POINTS = [
    {'menu': 'Adiantamentos', 'url': 'advances'},  # Apenas post
    {'menu': 'Centros de custo', 'url': 'costs-centers'},
    {'menu': 'Despesas', 'url': 'expenses'},
    {'menu': 'Fluxo de aprovação', 'url': 'approval-flows'},
    {'menu': 'Membros da equipe', 'url': 'team-members'},
    {'menu': 'Moedas', 'url': 'currencies'},
    {'menu': 'Projetos', 'url': 'projects'},
    {
        'menu': 'Relatórios',
        'url': 'reports?include=expenses,expenses.apportionment,expenses.expense_type,expenses.gps,'
               'expenses.costs_center,user,payment_method,advance,approval,invoice,history',
    },
    {'menu': 'Tipo de despesas', 'url': 'expenses-type'},
]

HEADERS = {
    'Accept': 'application/json',
    'Authorization': 'xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy',  # Inserir o token
}

LINE_SIZE = 156

URL = 'https://api.vexpenses.com/v2/'
