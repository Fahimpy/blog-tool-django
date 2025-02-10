from django.shortcuts import render, get_object_or_404
from .models import Tools

# Create your views here.
def Keyboard_tester(request):
    return render(request, 'tools/keyboard_tester.html')

def Tools_list(request):
    tools = Tools.objects.all()
    return render(request, 'tools/tools_list.html', {'tools': tools})


def Single_tool(request, slug):
    tool = get_object_or_404(Tools, slug=slug, status="published")
    related_tools = Tools.objects.filter(status="published").exclude(slug=slug)
    return render(request, 'tools/single_tool.html', {'tool': tool, 'related_tools': related_tools})