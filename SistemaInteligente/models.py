from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.postgres.search import SearchVectorField
from datetime import datetime

class Administrador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=10)
    numero_telefono = models.CharField(max_length=10)


#Antiguos metodos    
class Archivo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    documento = models.FileField(upload_to='archivos/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    fecha = models.DateTimeField(auto_now_add=True)  # Cambio aquí para capturar automáticamente la fecha de creación

    # Resto de la definición...
class Caso(models.Model):
    numero_proceso = models.IntegerField(unique=True)
    nombre_procesado = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)


# Las clases heredadas de Caso
class Constitucional(Caso):
    articulo_constitucional = models.CharField(max_length=255, help_text="Artículo de la constitución que es relevante para el caso.")
    #artículo específico de la constitución que está siendo discutido o que es relevante para el caso.

class Penal(Caso):
    delito = models.CharField(max_length=255, help_text="Tipo de delito asociado con el caso penal.")
    #sería el tipo específico de delito (como robo, asalto, fraude, etc.) que se está procesando.
class Civil(Caso):
    monto_disputa = models.DecimalField(max_digits=10, decimal_places=2, help_text="Monto económico en disputa en el caso civil.")
    # cantidad de dinero u otra medida de valor que está en juego en el caso civil.
class AdministrativoLaboral(Caso):
    ley_laboral = models.CharField(max_length=255, help_text="Ley o regulación laboral que es relevante para el caso administrativo o laboral.")
    #sería la ley o normativa específica que está en juego en el caso, que podría ser una regulación gubernamental o un estatuto laboral.
class Familia(Caso):
    relacion_partes = models.CharField(max_length=255, help_text="Relación entre las partes involucradas en el caso de familia.")
    # describiría la relación entre las personas involucradas en el caso, como esposo-esposa, padre-hijo, etc.
class Sancion(models.Model):
    caso = models.ForeignKey(Caso, on_delete=models.CASCADE)
    tipo_sancion = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_imposicion = models.DateField()
    fecha_cumplimiento = models.DateField(null=True, blank=True)

   # def imponer_sancion(self):
        # Lógica para imponer una sanción
   #     pass

  #  def eliminar_sancion(self):
        # Lógica para eliminar una sanción
   #     pass