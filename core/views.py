from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} {}</h1>'.format(nome, idade))


def soma(request, n1, n2):
    res = int(n1)+int(n2)
    #res = int(res)
    return HttpResponse('<h1>O resultado da soma é:{}</h1>'.format(res))


def subtrair(resquest, n1, n2):
    res = int(n1)-int(n2)
    return HttpResponse('<h1>O resultado da subtração é: {}</h1>'.format(res))


def dividir(resquest, n1, n2):
    res = int(n1)/int(n2)
    return HttpResponse('<h1>O resultado da divisão é: {}</h1>'.format(res))


def multiplicar(resquest, n1, n2):
    res = int(n1)*int(n2)
    return HttpResponse('<h1>O resultado da multiplicação é: {}</h1>'.format(res))