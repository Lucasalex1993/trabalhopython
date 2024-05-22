from .models import Usuario

def criar_usuario(nome=nome, email=email, senha=senha, telefone=telefone,
                           data_nascimento=data_nascimento, genero=genero,
                           endereco_rua=endereco_rua, endereco_rua2=endereco_rua2,
                           pais=pais, cidade=cidade, regiao=regiao, cep=cep):

    novo_usuario = Usuario(nome=nome, email=email, senha=senha, telefone=telefone,
                           data_nascimento=data_nascimento, genero=genero,
                           endereco_rua=endereco_rua, endereco_rua2=endereco_rua2,
                           pais=pais, cidade=cidade, regiao=regiao, cep=cep)
    db.session.add(novo_usuario)
    db.session.commit()

    return 'Usuário cadastrado com sucesso!'
    