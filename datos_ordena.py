#  coding:  utf-8


from migasfree.server.models import Computer

BUSCADOS = 'memory processor disk'.split()

c = Computer.objects.get(pk=68)

def busca_datos(co):
    for hw in co.hwnode_set.all():
        if hw.classname in BUSCADOS:
            yield muestra(hw)

def muestra(hw):
    if hw.classname=='memory':
        return  {'memoria': hw.size}
    if hw.classname=='processor':
        return  {'procesador': hw.product}
    if hw.classname=='disk':
        return  {'disco': hw.size}



print list(busca_datos(c))
