import random
import datetime
from django.core.management.base import BaseCommand
from core.models import Jornal, Categoria, Autor


categorias = [
    'Esporte',
    'Lazer',
    'Musica',
    'Codificacao',
    'Viajem'
]

autores = [
    'Adriana',
    'Lucas',
    'Milton',
    'Ricardo',
    'Bruno',
    'Eliane',
    'Suzana',
    'Pablo'
]


def genrar_autor():
    index = random.randint(0, 7)
    return autores[index]


def genrar_categorias():
    index = random.randint(0, 4)
    return categorias[index]


def genrar_visualizacao():
    return random.randint(0, 100)


def genrar_revisado():
    revisado = random.randint(0, 1)
    if revisado == 0:
        return False
    return True


def gerar_dia_mes_ano():
    # segue padrão americano
    ano = random.randint(2000, 2030)
    mes = random.randint(1, 12)
    dia = random.randint(1, 28)
    return datetime.date(ano, mes, dia)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str, help='Segue o arquivo que contem o nome dos titulos do meu jornal')

    def handle(self, *args, **kwargs):
        # pega o arquivo e salva nessa variavel
        file_name = kwargs['file_name']
        # abre o arquivo e salva em uma variavel chamada de file
        with open(f'{file_name}.txt') as file:
            # um loop normal que ira pegar cada linha do meu arquivo
            # e colocar no meu model Jornal com o campo de titulo
            # o que estiver escrito em cada linha
            for row in file:
                titulo = row
                autor_name = genrar_autor()
                categoria_name = genrar_categorias()
                data_publicada = gerar_dia_mes_ano()
                visualizacao = genrar_visualizacao()
                revisado = genrar_revisado()
                #print('titulo', 'autor', 'categorias', 'data_publicada', 'visualizacao', 'revisado')

            autor = Autor.objects.get_or_create(
                name=autor_name
            )

            jornal = Jornal(
                titulo=titulo,
                autor=Autor.objects.get(name=autor_name),
                data_publicada=data_publicada,
                visualizacao=visualizacao,
                revisado=revisado
            )

            jornal.save()

            categoria = Categoria.objects.get_or_create(name=categoria_name)

            jornal.categorias.add(
                Categoria.objects.get(name=categoria_name))

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
