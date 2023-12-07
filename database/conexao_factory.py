import psycopg2


class ConexaoFactory:

    def get_conexao(self):
        return psycopg2.connect(
            host='berry.db.elephantsql.com',
            database='kzoyxhin',
            user='kzoyxhin',
            password='J1LOCafRQt4ZhwD2ojHqKtqwHeVFMw3S'
        )
