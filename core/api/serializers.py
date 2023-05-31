from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from enderecos.models import Endereco
from core.models import DocIdentificacao



class DocIdentificacaoSerializer(ModelSerializer):
      class Meta:
            model = DocIdentificacao
            fields ='__all__'

class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    enderecos = EnderecoSerializer(read_only=True)
    comentarios = ComentarioSerializer(many=True, read_only=True)
    avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    doc_identificacao = DocIdentificacaoSerializer()
    # descricao_completa = SerializerMethodField()
    class Meta:
            model = PontoTuristico
            fields = ('id', 'nome', 'descricao', 'aprovado', 'foto',
                      'atracoes', 'comentarios', 'avaliacoes', 'enderecos',
                      'doc_identificacao'
                      # 'descricao_completa'
            )
            read_only_fields = ('comentarios',)

    # def get_descricao_completa(self, obj):
    #     return 'ds5 - ds5' % (obj.nome, obj.descricao)

    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
              at = Atracao.objects.create(**atracao)
              ponto.atracoes.add(at)

    def create(self, validated_data):
          atracoes = validated_data['atracoes']
          del validate_data['atracoes']

          endereco = validated_data['endereco']
          del validate_data['enderecos']

          doc = validated_data['doc_identificacao']
          del validate_data['doc_identificacao']
          doci = DocIdentificacao.objects.create(**doc)

          ponto = PontoTustistico.objects.create(**validated_data)
          self.cria_atracoes(atracoes, ponto)

          end = Endereco.objects.create(**endereco)
          ponto.endereco =end
          ponto.dos_identificacao = doci

          ponto.save()

          return ponto

