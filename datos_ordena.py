#  coding:  utf-8


from migasfree.server.models import Computer

BUSCADOS = 'memory processor disk'.split()


def busca_datos(co):
    datos = [{'id': co.id}]
    for hw in co.hwnode_set.all():
        if hw.classname in BUSCADOS:
            _tmp =  muestra(hw)
            if _tmp and None not in _tmp.values(): datos.append(_tmp)
    return datos

def muestra(hw):
    if hw.classname=='memory':
        if "Placa" in hw.parent.description:
            return  {'memoria': hw.size}
    if hw.classname=='processor':
        return  {'procesador': hw.product}
    if hw.classname=='disk':
        return  {'disco': hw.size}


if __name__ ==  '__main__':
    c = Computer.objects.get(pk=68)
    print list(busca_datos(c))
