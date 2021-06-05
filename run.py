from emergency import create_app

app = create_app()

if __name__ == '__main__':
    print("API is ",app.config.get('API'))
    app.run(debug=True)
