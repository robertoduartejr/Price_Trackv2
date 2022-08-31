from django.core.mail import send_mail
import smtplib


def send_email_confirmation(form):
    # form.instance.user = self.request.user
    # if form.instance.user:
    send_mail('Bem-vindo ao Track Price', f'Querido(a), {form.cleaned_data["username"]}.\n\n Seja muito bem-vindo ao Track Price. \n\nEsperamos que possa tirar proveito da ferramenta.\n\nAtt, equipe.', 'trackpricedjango@gmail.com', [form.cleaned_data['email']],fail_silently=False)
