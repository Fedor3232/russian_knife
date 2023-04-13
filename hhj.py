import ny as n

def seev(name, x, y):
    conektor = n.Connector(bind = n.database)
    if name_control(name) == False:
        senchi = n.Senchiies(name = name, x = x, y = y)
        conektor.add(senchi)
    else:
        objects = conektor.query(n.Senchiies).filter(n.Senchiies.name == name)
        Individuell = objects.first()
        Individuell.x = x
        Individuell.y = y
        print(Individuell.name)
    conektor.commit()
    conektor.close()

def name_control(name):
    conektor = n.Connector(bind = n.database)
    objects = conektor.query(n.Senchiies)
    for dd in objects:
        if dd.name == name:
            return True
    return False

def spavner(name):
    if name_control(name) == True:
        kon = n.Connector(bind = n.database)
        retorn = kon.query(n.Senchiies).filter(n.Senchiies.name == name)
        chel = retorn.first()
        return (chel.x, chel.y)
    else:
        return (7345, 6700)
