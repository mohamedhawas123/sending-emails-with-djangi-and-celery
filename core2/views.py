from django.shortcuts import render
from django.views import generic
from core2.forms import ReviewForm
from django.views.generic.edit import FormView
from django.http import HttpResponse


class ReviewEmail(FormView):
    template_name = 'core2/form.html'
    form_class = ReviewForm


    def form_valid(self, form):
        form.send_email()
        msg = "Thanks for nothing"

        return HttpResponse(msg)


