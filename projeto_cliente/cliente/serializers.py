from rest_framework import serializers
from cliente.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    """Exibindo todos os clientes"""
    class Meta:
        model = Cliente
        fields = '__all__' # disponibilazando todos os dados do Banco de Dados para visualização