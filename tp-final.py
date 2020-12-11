import random
import threading
import time
import pylint
import array


cantidadAbonados = 10
saldoInicial = 3
saldoRecarga = 3
costoLlamada = 2
costoSMS = 1
listaDeAbonados = []

#tiempo de espera
def tiempoEspera(maximo):
    time.sleep(random.randrange(1,maximo))

#base de datos
class baseOCS():
    bbdd = []

    def leerBase(self,index):
        return self.bbdd[index]
    
    def escribirBase(self, index, saldo):
        self.bbdd[index] = saldo
    
    def asignarSaldoInicial(self,cantidadAbonados,saldoInicial):
        for i in range(0,cantidadAbonados):
            self.bbdd.insert(i,saldoInicial)


class Abonado(threading.Thread):
    def __init__(self,id,name):
        super().__init__()
        self.id = id
        self.name = name
        self.semaforoLlamada = threading.Semaphore(1) #Monitor de llamada, si esta en una llamada no se puede cargar saldo.
        self.monitorSaldoCero = threading.Condition() #Monitor de saldo, espera a tener saldo para llamar.

    def consumirSaldo(self,saldoConsumido):
        saldoActual = baseOCS().leerBase(self.id)
        baseOCS().escribirBase(self.id,(saldoActual - saldoConsumido))
    
    def consultarSaldo(self):
        return baseOCS().leerBase(self.id)
    
    def cargarSaldo(self,recarga):
        with self.semaforoLlamada:
            saldoActual = baseOCS().leerBase(self.id)
            baseOCS().escribirBase(self.id,(saldoActual + recarga))

    def hacerLlamada(self):
        self.esperarRecargaDeSaldo(costoLlamada)
        with self.semaforoLlamada:
            print("Abonado",self.id, "- Iniciando llamada - Mi saldo actual es de $: " ,self.consultarSaldo())
            tiempoEspera(60)
            self.consumirSaldo(costoLlamada)
            print("Abonado",self.id, "- Finalizando llamada - Costo $:",costoLlamada,"- Mi saldo actual es de $: " ,self.consultarSaldo())

    def enviarSMS(self):
        self.esperarRecargaDeSaldo(costoSMS)
        with self.semaforoLlamada:
            self.consumirSaldo(costoSMS)
            print("Abonado",self.id, "- Envio SMS - Costo $:",costoSMS,"- Mi saldo actual es de $: " ,self.consultarSaldo())
            tiempoEspera(2)

    def esperarRecargaDeSaldo(self,aConsumir):
        if self.consultarSaldo() < aConsumir:
            with self.monitorSaldoCero:
                print("Abonado",self.id, "- Esperando recarga diaria - Mi saldo actual es de $: " ,self.consultarSaldo())
                self.monitorSaldoCero.wait()

            
    def operacionRandom(self):
        operacion = random.randint(0,1)        
        if operacion == 0:
            self.hacerLlamada()
        else:
            self.enviarSMS()

    def run(self):
        while True:
            self.operacionRandom()
            tiempoEspera(30)



class Operador(threading.Thread):
    def __init__(self,id):
        super().__init__()
        self.id = id

    def recargaDiariaDeSaldo(self):
        for id in range(0,cantidadAbonados):
            abonado = listaDeAbonados[id]
            abonado.cargarSaldo(saldoRecarga)
            print("Operador", self.id, "- Le di una recarga de $",saldoRecarga,"al abonado", abonado.name )
            with abonado.monitorSaldoCero:
                abonado.monitorSaldoCero.notify()
                time.sleep(1)
        
    def run(self):
        while True:
            time.sleep(60)
            self.recargaDiariaDeSaldo()

            
    

#RUN
baseOCS().asignarSaldoInicial(cantidadAbonados,saldoInicial)

for i in range(0,cantidadAbonados):
    nombre = 'Abonado' + str(i)
    listaDeAbonados.append(Abonado(i,name=nombre))

for i in range(0,cantidadAbonados):
    abonado = listaDeAbonados[i]
    abonado.start()

Operador(0).start()