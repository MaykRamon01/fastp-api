from fastapi.testclient import TestClient
from app import app # Importa o seu objeto 'app' do app.py

client = TestClient(app)

def test_read_main():
    # Simula um acesso à rota raiz
    response = client.get("/")

    # Verifica se o status é 200 (Sucesso)
    assert response.status_code == 200

    # Verifica se a mensagem está correta
    assert response.json() == {"Hello": "World"}
