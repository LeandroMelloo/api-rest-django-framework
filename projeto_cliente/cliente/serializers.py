from cliente.validators import *
from rest_framework import serializers
from cliente.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    """Exibindo todos os clientes"""
    class Meta:
        model = Cliente
        fields = '__all__' # disponibilazando todos os dados do Banco de Dados para visualização
    
    def validate(self, data):
        if not cpf_valido(data['cpf']):
           raise serializers.ValidationError({'cpf':'Número de CPF inválido'})

        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':'O formato NOME está incorreto, inclua apenas letras'})
        
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':'O formato RG está incorreto, deve conter 9 dígitos'})
        
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':'O formato CELULAR está incorreto, deve seguir este modelo: 11 91234-1234'})
        
        return data