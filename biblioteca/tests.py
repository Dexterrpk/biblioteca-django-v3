from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Colecao

class ColecaoTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_create_colecao(self):
        data = {'nome': 'Minha Coleção', 'descricao': 'Descrição da coleção'}
        response = self.client.post('/api/colecoes/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Colecao.objects.count(), 1)
        self.assertEqual(Colecao.objects.first().colecionador, self.user)

    def test_permission_denied(self):
        other_user = User.objects.create_user(username='otheruser', password='otherpass')
        colecao = Colecao.objects.create(nome='Coleção alheia', colecionador=other_user)
        response = self.client.delete(f'/api/colecoes/{colecao.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
