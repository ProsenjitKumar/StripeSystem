from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):  # new
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


def charge(request): # new
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        return render(request, 'charge.html')



