#Implemente uma função que retorne uma lista de livros publicados em um intervalo de anos fornecido pelo usuário.

livros = [
    {"titulo": "Dom Quixote", "autor": "Miguel de Cervantes", "ano": 1605},
    {"titulo": "1984", "autor": "George Orwell", "ano": 1949},
    {"titulo": "Cem Anos de Solidão", "autor": "Gabriel García Márquez", "ano": 1967},
    {"titulo": "O Alquimista", "autor": "Paulo Coelho", "ano": 1988}
]

intervalo = (1900, 2000)

def publicação(livros, intervalo):
    primeiro_ano, ultimo_ano = intervalo
    return [livro for livro in livros if primeiro_ano <= livro["ano"] <= ultimo_ano]

print(publicação(livros, intervalo))