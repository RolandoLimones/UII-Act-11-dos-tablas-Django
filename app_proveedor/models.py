from django.db import models

class Proveedor(models.Model):
    nombre_proveedor = models.CharField(max_length=50, help_text="Nombre del proveedor")
    telefono = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    direccion = models.CharField(max_length=150)
    dias_entrega = models.CharField(max_length=100)
    foto = models.FileField(upload_to='img_proveedores/', blank=True, null=True) 

    def __str__(self):
        return self.nombre_proveedor

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='productos')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    almacen_id = models.IntegerField()
    foto = models.FileField(upload_to='img_productos/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_producto} - {self.proveedor.nombre_proveedor}"

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"