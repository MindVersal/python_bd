import sqlalchemy


def select_all_from_bd():
    return select_from_db("""SELECT * FROM db2005 """)


def select_from_db(sql_request=''):
    connector = (
        r'2005.db'
    )
    engine = sqlalchemy.create_engine(r'sqlite:///{}'.format(connector))
    if sql_request == '':
        sql_request = """SELECT * FROM db2005 WHERE NAME='АБУ'"""
    rows = engine.execute(sql_request)
    for row in rows:
        yield row


def main():
    print('I am finding all records in db...')
    print('I am find:')
    select_all_range = select_all_from_bd()
    for row in select_all_range:
        print(row)

if __name__ == '__main__':
    main()
