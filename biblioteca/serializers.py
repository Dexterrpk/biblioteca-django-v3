from rest_framework import serializers
from .models import Colecao, Livro

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'

class ColecaoSerializer(serializers.ModelSerializer):
    livros = LivroSerializer(many=True, read_only=True)

    class Meta:
        model = Colecao
        fields = '__all__'
