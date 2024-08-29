from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email', 'class': 'form-control'
    }), label='Email')
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Senha', 'class': 'form-control'
    }), label='Senha')

class RegisterForm(forms.Form):
    fullname = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'Nome completo'}),
        label='Nome completo'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'email'}),
        label='Email'
    )
    telefone = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'numeroTelefone'}),
        label='Telefone'
    )
    endereco = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'adress'}),
        label='Endereço'
    )
    cep = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'CEP'}),
        label='CEP'
    )
    times = forms.ChoiceField(
        choices=[
            ('Nenhum', 'Nenhum'),
            ('Sport', 'SPORT CLUB DO RECIFE'),
            ('Santa', 'Santa cruz'),
            ('Nautico', 'Náutico'),
            ('Fortaleza', 'Fortaleza'),
            ('Ceará', 'Ceará'),
            ('Remo', 'Remo'),
            ('paysandu', 'Paysandu'),
            ('vitoria', 'Vitória'),
        ],
        required=False,
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'time'}),
        label='Time que torce (Opcional)'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'senha'}),
        label='Senha'
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'confirmarSenha'}),
        label='Confirme sua senha'
    )