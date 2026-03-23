import unittest
from app.app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        # Configura o cliente de teste do Flask
        self.app = app.test_client()
        self.app.testing = True

    def test_health_check(self):
        # Teste inicial que já vem no projeto (Health Check)
        response = self.app.get('/health-check')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello, I'm Alive!", response.data)

    # --- AÇÃO 2: Caso de Sucesso (Eleva para 91%) ---
    def test_print_hello_success(self):
        # Simula a rota /hello passando o parâmetro 'name'
        response = self.app.get('/hello?name=DevOps')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello, DevOps!", response.data)

    # --- AÇÃO 3: Caso de Erro (Eleva para 100%) ---
    def test_print_hello_error(self):
        # Simula a rota /hello SEM passar o parâmetro 'name'
        response = self.app.get('/hello')
        self.assertEqual(response.status_code, 400)
        # Nota: O texto deve ser idêntico ao que está no app.py (atenção aos acentos)
        self.assertIn("Nome não informado".encode('utf-8'), response.data)

if __name__ == '__main__':
    unittest.main()