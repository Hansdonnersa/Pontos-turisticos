from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
# IsAuthenticatedOrReadOnly, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = (TokenAuthentication, )
    filter_backends = [SearchFilter]
    search_fields = ['nome', 'descricao']
    lookup_field = 'id'

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(id=id)

        if nome:
            queryset = queryset.filter(pk=nome)

        if descricao:
            queryset = queryset.filter(pk=descricao)

        return queryset


    @action(methods=['POST'], detail=True)
    def associa_atracaoes(self, request, pk):
        atracoes = request.data['ids']

        ponto = PontoTuristico.objects.get(id=pk)

        ponto.atracoes.set(atracoes)

        ponto.save()
        return HttpResponse('OK')

       # def list(self, request, *args, **kwargs):
       #     return Response({'teste' : 123})
       #  def create(self, request, *args, **kwargs):
       #      return Response({'Hello': request.data['nome']})
       #  def delete(self, request, *args, **kwargs):
       #      pass
       #  def retrieve(self, request, *args, **kwargs):
       #     pass
       #  def update(self, request, *args, **kwargs):
       #      pass
       #  def partial_update(self, request, *args, **kwargs):
       #      pass
       #
       #  @action(method=['get'], detail=True)
       #  def denunciar(self, request, pk=None):
       #      pass
       #
       #  @action(method=['get'], detail=False)
       #  def teste(self, request, pk=None):
       #      pass

 
