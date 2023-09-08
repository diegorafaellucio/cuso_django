from rest_framework import serializers
from apps.escola.models import Aluno, Curso, Matricula


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ('__all__')


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []
        fields = ('__all__')


class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ('curso', 'periodo')
    def get_periodo(self, obj):
        return obj.get_periodo_display()

class ListaAlunosMatriculadosCursoSerializer(serializers.ModelSerializer):
    nome = serializers.ReadOnlyField(source='aluno.nome')
    # periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ('nome', )
    # def get_periodo(self, obj):
    #     return obj.get_periodo_display()
