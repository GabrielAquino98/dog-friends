from rest_framework import serializers
from .models import TbProprietario, TbEndereco, TbEnderecoProp

class ProprietarioSerializer(serializers.ModelSerializer):

    class Meta:

        model = TbProprietario
        fields = '__all__'

class EnderecoSerializer(serializers.ModelSerializer):

    class Meta:

        model = TbEndereco
        fields = '__all__'

class EnderecoPropSerializer(serializers.ModelSerializer):

    class Meta:

        model = TbEnderecoProp
        fields = '__all__'