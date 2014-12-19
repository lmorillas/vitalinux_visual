# coding: utf-8

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'migasfree.settings'

from migasfree.server.models import Property


def ordenadores_centro():
    ETIQUETAS =  ["PRIMARIA", "CENTRO"]


    props = Property.objects.filter(name__in=ETIQUETAS)

    datos = {}
    for p in props:
        print p.name
        for at in p.attribute_set.all():
            datos[at.value] = at.computer_set.all()
            print at.value, len(datos.get(at.value))
    return datos

datos = ordenadores_centro()
