from django.http import JsonResponse

def estudantes(request):
    if request.method == 'GET':
        estudante = {
            'id': 1,
            'nome': 'João',
        }
        return JsonResponse(estudante)
    

def cursos(request):
    if request.method == 'GET':
        curso = {
            'codigo': 'PYT01',
            'descricao': 'Python Fundamentos',
            'nivel': 'B'
        }
        return JsonResponse(curso)