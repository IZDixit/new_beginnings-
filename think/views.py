from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from .models import UserInput
from .graphs import GraphGenerator


# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"


class DashboardView(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = UserInput.objects.all()
        graph_gen = GraphGenerator(data)
        
        context['sleep_graph'] = graph_gen.sleep_analysis_graph()
        context['exercise_graph'] = graph_gen.exercise_analysis_graph()
        context['sunlight_graph'] = graph_gen.sunlight_analysis_graph()
        
        return context


class InputView(TemplateView):
    template_name = "input.html"

    def post(self, request, *args, **kwargs):
        try:
            UserInput.objects.create(
                sleep=request.POST.get('sleep'),
                wake=request.POST.get('wake'),
                exercise_start=request.POST.get('exercise_start'),
                exercise_end=request.POST.get('exercise_end'),
                exercise_type=request.POST.get('exercise_type'),
                sunlight_start=request.POST.get('sunlight_start'),
                sunlight_end=request.POST.get('sunlight_end')
            )
            messages.success(request, "Data saved successfully!")
        except Exception as e:
            messages.error(request, f"Error saving data: {str(e)}")
        
        return redirect('input')
