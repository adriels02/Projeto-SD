from django.db import models

class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    produto_id_externo = models.IntegerField()  # ID do produto no banco de dados externo
    name = models.CharField(max_length=255)  # Nome do produto
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Preço do produto
    image = models.ImageField(upload_to='compras/')  # Imagem do produto
    quantidade = models.PositiveIntegerField(default=1)  # Quantidade de produtos na compra
    data_compra = models.DateTimeField(auto_now_add=True)  # Data da compra
    email_cliente = models.EmailField()  # Email do cliente (vindo do banco de dados externo)

    def __str__(self):
        return f"Compra {self.id_compra} - Produto: {self.name}"

class DetalhesCompra(models.Model):
    compra = models.OneToOneField(Compra, on_delete=models.CASCADE)  # Relacionamento com a tabela de compras
    email_cliente = models.EmailField()  # Email do cliente
    total_compra = models.DecimalField(max_digits=10, decimal_places=2)  # Total da compra

    def __str__(self):
        return f"Detalhes da Compra {self.compra.id_compra} - Total: {self.total_compra}"
