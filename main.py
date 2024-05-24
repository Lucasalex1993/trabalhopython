from flask import Flask
from modules import app, db

def create_app():
    """Função para criar e configurar a aplicação Flask."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgre:1234@localhost/meubanco'
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()  # Cria as tabelas do banco de dados
    
    return app

if __name__ == '__main__':
    flask_app = create_app()
    flask_app.run(debug=True)
