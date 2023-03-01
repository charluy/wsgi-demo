'''
    Instrucciones:
        - Ejecutar: docker volume rm control-center_db_control_center_data
        - Ejecutar: docker exec -it control-center_control_center_1 bash
        - Ejecutar: python manange.py shell
        - Copiar y pegar el contenido de este archivo (Demora un poco en
          terminar).
        - Ahora se puede entrar en el admin con el usuario "admin" y
          contraseña "qazwsx".
'''

from django.contrib.auth.models import User


# Superuser creation:
user = User.objects.create_user('admin', password='qazwsx')
user.is_superuser = True
user.is_staff = True
user.save()
