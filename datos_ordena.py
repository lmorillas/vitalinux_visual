#  coding:  utf-8


from migasfree.server.models import Computer

BUSCADOS = 'memory processor disk'.split()


def busca_datos(co):
    datos = {'id': co.id}
    datos{'memoria':  c.hwnode_set.filter(classname='memory').aggregate(Max('size')).get('size__max')}
    datos{'procesador'}:  c.hwnode_set.filter(classname='processor')
    datos{'disco'}:  [x.size for x in  c.hwnode_set.filter(classname='disk') if x.size ]
    return datos


if __name__ ==  '__main__':
    c = Computer.objects.get(pk=68)
    print list(busca_datos(c))
