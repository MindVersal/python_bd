import python_qt_bd_model


def select_from_db(family='', name='', farther='',
                   birthday_year='', birthday_month='', birthday_day='',
                   ksiva='', city='', selsovet='',
                   street='', house='', flat='',
                   zodiak='', interactive=True):
    sql_request_start = """
                          SELECT * 
                            FROM db2005 
                        """
    sql_request_where = """ WHERE """
    # sql_request_where = """
    #                     WHERE NAME LIKE 'АБУ%'
    #                   """
    no_first_where_in_sql = False
    #
    # Знак Зодиака 	Дата рождения
    #
    # Овен 	        21.03 - 20.04
    # Телец 	    21.04 - 21.05
    # Близнецы 	    22.05 - 21.06
    # Рак 	        22.06 - 22.07
    # Лев 	        23.07 - 21.08
    # Дева 	        22.08 - 23.09
    # Весы 	        24.09 - 23.10
    # Скорпион 	    24.10 - 22.11
    # Стрелец 	    23.11 - 22.12
    # Козерог 	    23.12 - 20.01
    # Водолей 	    21.01 - 19.02
    # Рыбы 	        20.02 - 20.03
    #
    zodiak_dates_months = {'': '',
                           'ОВЕН': '03-04',
                           'ТЕЛЕЦ': '04-05',
                           'БЛИЗНЕЦЫ': '05-06',
                           'РАК': '06-07',
                           'ЛЕВ': '07-08',
                           'ДЕВА': '08-09',
                           'ВЕСЫ': '09-10',
                           'СКОРПИОН': '10-11',
                           'СТРЕЛЕЦ': '11-12',
                           'КОЗЕРОГ': '12-01',
                           'ВОДОЛЕЙ': '01-02',
                           'РЫБЫ': '02-03'}
    zodiak_dates_days = {'': '',
                         'ОВЕН': '21-20',
                         'ТЕЛЕЦ': '21-21',
                         'БЛИЗНЕЦЫ': '22-21',
                         'РАК': '22-22',
                         'ЛЕВ': '23-21',
                         'ДЕВА': '22-23',
                         'ВЕСЫ': '24-23',
                         'СКОРПИОН': '24-22',
                         'СТРЕЛЕЦ': '23-22',
                         'КОЗЕРОГ': '23-20',
                         'ВОДОЛЕЙ': '21-19',
                         'РЫБЫ': '20-20'}
    if zodiak != '' and zodiak != ' ':
        temp_birthday_month = zodiak_dates_months[zodiak].upper().split(sep='-')
        temp_birthday_day = zodiak_dates_days[zodiak].upper().split(sep='-')
        if no_first_where_in_sql:
            sql_request_where += """ AND """
        else:
            no_first_where_in_sql = True
        sql_request_where += """ (
                                    (BIRTHDAY_MONTH=\'{0}\' AND
                                        (BIRTHDAY_DAY BETWEEN \'{1}\' AND \'{2}\')
                                    )
                                    OR
                                    (BIRTHDAY_MONTH=\'{3}\' AND
                                        (BIRTHDAY_DAY BETWEEN \'{4}\' AND \'{5}\')
                                    )
                                )
                             """. \
            format(temp_birthday_month[0],  # 0
                   temp_birthday_day[0],    # 1
                   '31',                    # 2
                   temp_birthday_month[1],  # 3
                   '01',                    # 4
                   temp_birthday_day[1])    # 5

        birthday_month = ''
        birthday_day = ''
    if family != '':
        if no_first_where_in_sql:
            sql_request_where += """ AND """
        else:
            no_first_where_in_sql = True
        if interactive:
            sql_request_where += """ (FAMILY LIKE \'{0}%\') """.format(family.upper())
        else:
            sql_request_where += """ (FAMILY=\'{0}\') """.format(family.upper())
    if name != '':
        if no_first_where_in_sql:
            sql_request_where += """ AND """
        else:
            no_first_where_in_sql = True
        if interactive:
            sql_request_where += """ (NAME LIKE \'{0}%\')""".format(name.upper())
        else:
            sql_request_where += """ (NAME=\'{0}\')""".format(name.upper())
    if farther != '':
        if no_first_where_in_sql:
            sql_request_where += """ AND """
        else:
            no_first_where_in_sql = True
        if interactive:
            sql_request_where += """ (FARTHER LIKE \'{0}%\')""".format(farther.upper())
        else:
            sql_request_where += """ (FARTHER=\'{0}\')""".format(farther.upper())
    if birthday_year != '':
        if no_first_where_in_sql:
            sql_request_where += """ AND """
        else:
            no_first_where_in_sql = True
        if len(birthday_year) == 2:
            birthday_year = '19' + birthday_year
        sql_request_where += """ (BIRTHDAY_YEAR=\'{0}\')""".format(birthday_year.upper())
    if birthday_month != '':
        if no_first_where_in_sql:
            sql_request_where += """ AND """
        else:
            no_first_where_in_sql = True
        birthday_month_list = birthday_month.replace(' ', '').split(sep='-')
        if len(birthday_month_list) == 1:
            sql_request_where += """ (BIRTHDAY_MONTH=\'{0}\')""".format(birthday_month.upper())
        elif len(birthday_month_list) == 2:
            sql_request_where += """ (BIRTHDAY_MONTH BETWEEN \'{0}\' AND \'{1}\')""".\
                format(birthday_month_list[0].upper(), birthday_month_list[1].upper())
    if birthday_day != '':
        if no_first_where_in_sql:
            sql_request_where += """ AND """
        else:
            no_first_where_in_sql = True
        birthday_day_list = birthday_day.replace(' ', '').split(sep='-')
        if len(birthday_day_list) == 1:
            sql_request_where += " (BIRTHDAY_DAY=\'{0}\')".format(birthday_day_list[0].upper())
        elif len(birthday_day_list) == 2:
            sql_request_where += """ (BIRTHDAY_DAY BETWEEN \'{0}\' AND \'{1}\')""".\
                format(birthday_day_list[0].upper(), birthday_day_list[1].upper())
    if ksiva != '':
        if no_first_where_in_sql:
            sql_request_where += """ AND """
        else:
            no_first_where_in_sql = True
        if interactive:
            sql_request_where += """ (KSIVA LIKE \'%{0}%\')""".format(ksiva.upper())
        else:
            sql_request_where += """ (KSIVA=\'{0}\')""".format(ksiva.upper())
    if city != '':
        if no_first_where_in_sql:
            sql_request_where += """ AND """
        else:
            no_first_where_in_sql = True
        if interactive:
            sql_request_where += """ (CITY LIKE \'{0}%\')""".format(city.upper())
        else:
            sql_request_where += """ (CITY=\'{0}\')""".format(city.upper())
    if selsovet != '':
        if no_first_where_in_sql:
            sql_request_where += """ AND """
        else:
            no_first_where_in_sql = True
        if interactive:
            sql_request_where += """ (SELSOVET LIKE \'%{0}%\')""".format(selsovet.upper())
        else:
            sql_request_where += """ (SELSOVET=\'{0}\')""".format(selsovet.upper())
    if street != '':
        if no_first_where_in_sql:
            sql_request_where += """ AND """
        else:
            no_first_where_in_sql = True
        if interactive:
            sql_request_where += """ (STREET LIKE \'%{0}%\')""".format(street.upper())
        else:
            sql_request_where += """ (STREET=\'{0}\')""".format(street.upper())
    if house != '':
        if no_first_where_in_sql:
            sql_request_where += """ AND """
        else:
            no_first_where_in_sql = True
        sql_request_where += """ (STREET=\'{0}\')""".format(house.upper())
    if flat != '':
        if no_first_where_in_sql:
            sql_request_where += """ AND """
        else:
            no_first_where_in_sql = True
        sql_request_where += """ (STREET=\'{0}\')""".format(flat.upper())
    if no_first_where_in_sql:
        sql_request = sql_request_start + sql_request_where
    else:
        # sql_request = sql_request_start
        sql_request = ''
    return python_qt_bd_model.select_from_db(sql_request=sql_request)


def main():
    print('Test controller')
    for row in python_qt_bd_model.select_from_db():
        print(row)


if __name__ == '__main__':
    main()
