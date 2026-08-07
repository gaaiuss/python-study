"""Exercício com Abstração, Herança, Encapsulamento e Polimorfismo

Criar um sistema de biblioteca onde usuários podem emprestar e devolver
livros. Alguns usuários possuem benefícios especiais e alguns livros possuem
regras diferentes de empréstimo.

Material (ABC)
    Livro
    Revista

Pessoa (ABC)
    Usuario
        Usuario -> Material (empréstimos)

Biblioteca
    Biblioteca -> Usuario
    Biblioteca -> Material

Dicas:

Criar classe Pessoa que possui nome e idade (atributos privados com getters).

Criar classe Usuario que herda de Pessoa.
    Usuario deve possuir uma lista de materiais emprestados.

Criar classe Material (classe abstrata).
    Todo material possui:
        - título
        - código
        - disponível (True/False)

    Deve possuir:
        - emprestar()
        - devolver()

    O método emprestar() deve ser abstrato.

Criar subclasses:

Livro
    - Pode ser emprestado por até 14 dias.
    - Não pode ser emprestado se já estiver indisponível.

Revista
    - Pode ser emprestada por apenas 7 dias.
    - Caso seja uma edição especial, não pode ser emprestada.

Biblioteca

A biblioteca agrega usuários e materiais.

Ela deve possuir métodos para:

    - cadastrar_usuario()
    - cadastrar_material()
    - autenticar_usuario()
    - autenticar_material()

Criar um método realizar_emprestimo(usuario, material).

O empréstimo só poderá acontecer se:

    * O usuário estiver cadastrado.
    * O material estiver cadastrado.
    * O material estiver disponível.
    * O método emprestar() da subclasse retornar sucesso.

Criar um método devolver_material() que devolve o material e atualiza a lista
de empréstimos do usuário.

Desafio Extra (para ir além)

Depois de terminar o exercício básico, implemente também:

⭐ Classe UsuarioPremium, que pode pegar até 10 livros.
⭐ Classe UsuarioComum, que pode pegar apenas 3 livros.
⭐ Método renovar_emprestimo().
⭐ Histórico de empréstimos.
⭐ Multa caso o material seja devolvido após o prazo.
⭐ Pesquisar livros por título.
⭐ Listar apenas materiais disponíveis.
⭐ Sobrescrever __str__ em todas as classes para facilitar a impressão dos
objetos.
⭐ Utilizar @property e @setter quando fizer sentido.
"""
