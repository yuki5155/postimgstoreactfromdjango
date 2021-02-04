from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import TodoSerializers
from .models import TodoApp
from django.views import View
from .forms import TodoForms

#permission_classes = [IsAuthenticated]


# permission_classes = [AllowAny]

class TaskTodo(APIView):
    #authentication_classes = [JWTAuthentication, ]
    #permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    def get(self, request):
        todo = TodoApp.objects.all()
        serializer = TodoSerializers(todo, many=True,context={"request":request})
        return Response(serializer.data)
    def post(self, request):



        serializer = TodoSerializers(data=request.data)

        if serializer.is_valid():

            serializer.save()

        todo = TodoApp.objects.all()

        serializer = TodoSerializers(todo, many=True, context={"request": request})
        return Response(serializer.data)


class IndexView(View):
    def get(self, request):

        todo = TodoApp.objects.all()

        form = TodoForms


        context = {"todo":todo,
                   'form':form}

        return render(request, 'todo/index.html', context)
    def post(self, request):
        todo = TodoApp.objects.all()
        #, request.FILES
        form = TodoForms(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            context = {"todo": todo,
                       'form': form}

        return render(request, 'todo/index.html', context)