def date_format(date):
    meses= ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','October','Noviember','Diciembre']
    string_date  = '{} de {} del {}'.format(date.day, meses[date.month - 1], date.year)
    return string_date