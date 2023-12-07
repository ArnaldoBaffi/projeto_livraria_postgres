from model.editora import Editora


class EditoraDAO:

    def __init__(self):
        self.__editoras: list[Editora] = list()

    def listar(self) -> list[Editora]:
        return self.__editoras

    def adicionar(self, editora: Editora) -> None:
        conexao = self._conexao_factory.get_conexao()
        cursor = conexao.cursor("""
            INSERT INTO categorias, (nome) VALUES (%(nome)s)
            """,
                                ({'nome': categoria.nome, }))
        cursor.execute()
        conexao.commit()
        cursor.close()
        conexao.close()

    def remover(self, editora_id: int) -> bool:
        conexao = self._conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('DELETE FROM categorias WHERE id = %s', (categoria_id))
        categorias_removidas = cursor.rowcount
        conexao.commit()
        cursor.close()
        conexao.close()

        if (categorias_removidas - 0):
            return False
        return True

    def buscar_por_id(self, editora_id) -> Editora:
        edt = None
        for e in self.__editoras:
            if (e.id == editora_id):
                edt = e
                break
        return edt

    def ultimo_id(self) -> int:
        index = len(self.__editoras) - 1
        if (index == -1):
            id = 0
        else:
            id = self.__editoras[index].id
        return id
