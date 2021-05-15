from emergency import create_app
from dotenv import load_dotenv

load_dotenv('.env')
app = create_app()
if __name__ == '__main__':
    print(app.config.get('API'))
    app.run(debug=True)
