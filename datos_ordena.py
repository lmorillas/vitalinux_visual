#  coding:  utf-8


from migasfree.server.models import Computer
from django.db.models import Max

BUSCADOS = 'memory processor disk'.split()


def busca_datos(co):
    datos = {'id': co.id}
    datos['memoria'] = co.hwnode_set.filter(classname='memory').aggregate(Max('size')).get('size__max')
    datos['procesador'] =  [p.product for p in co.hwnode_set.filter(classname='processor') if p.product is not None]
    datos['disco'] = [x.size for x in  co.hwnode_set.filter(classname='disk') if x.size ]
    return datos


if __name__ ==  '__main__':
    c = Computer.objects.get(pk=68)
    print list(busca_datos(c))
