from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from helpdesk.models import Ticket
from projects.models import Projects
from django_pandas.io import read_frame
import pandas as pd
import datetime
from api.serializers import ProjectDetailsSerializer, ProjectsSerializer

# Create your views here.


def ticket_stats_total_api(request):
    
    df = read_frame(Ticket.objects.filter(created__gte="2018-03-01"))

    # Format date field to Year-Month
    df["created"] = df["created"].dt.strftime("%Y-%m")

    # Groupby and count
    df = df.groupby(["created", "queue"])["id"].count().reset_index()

    # Tidy data
    df["date"] = df["created"] + "-01"
    df["total"] = df["id"]
    df = df[["date", "queue", "total"]]

    # Convert from long format to wide format
    df = df.pivot(columns="queue", index=df["date"])["total"].reset_index()
    df["date2"] = pd.to_datetime(df["date"])
    df["date2"] = df["date2"].dt.strftime("%b %Y")

    # Write to csv for use in graph
    # df.to_csv(r"C:\Users\smitran\Documents\GITHUB\novosite\static\data\office.csv", index = False, na_rep = "")
    
    csv = df.to_csv(index=False, na_rep="")
    response = HttpResponse(csv, content_type="text/plain")
    return response


def ticket_stats_office_api(request):

    df = read_frame(Ticket.objects.filter(queue=1, created__gte="2018-03-01"))

    # Format date field to Year-Month
    df["created"] = df["created"].dt.strftime("%Y-%m")

    # Groupby and count
    df = df.groupby(["created", "novo_office"])["id"].count().reset_index()

    # Tidy data
    df["date"] = df["created"] + "-01"
    df["total"] = df["id"]
    df = df[["date", "novo_office", "total"]]

    # Convert from long format to wide format
    df = df.pivot(columns="novo_office", index=df["date"])["total"].reset_index()
    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%b %Y")
    
    csv = df.to_csv(index=False, na_rep="")
    response = HttpResponse(csv, content_type="text/plain")
    return response


def projects_list(request):
    
    today = datetime.datetime.today() + datetime.timedelta(days=1)
    year_ago = datetime.datetime.today() - datetime.timedelta(days=365)
    projects = Projects.objects.prefetch_related("contact", "account","assigned_to").filter(start_date__range=(year_ago, today))
    serializer = ProjectsSerializer(projects, many=True)
    
    return JsonResponse(serializer.data, safe=False)


def projects_detailed_api(request, pk):
    
    opportunity_record = Projects.objects.prefetch_related("contact", "account").filter(id=pk)
    
    serializer = ProjectDetailsSerializer(opportunity_record, many=True)
    
    return JsonResponse(serializer.data, safe=False)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        