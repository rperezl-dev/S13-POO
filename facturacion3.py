
from datetime import date,datetime
#Clase es un modelo con atributos y metodos.
class Empresa:
    def __init__(self,nom='El mas barato',ruc='0999999999',tel='042971234',dir='Juan Montalvo y Pedro Carbo'): #con atributos; son variables locales
         self.nombre=nom#que atributos requiere
         self.ruc=ruc
         self.telefono=tel
         self.direccion=dir
    def mostrarEmpresa(self):
        print('Empresa: {:20} RuC:{}'.format(self.nombre,self.ruc))
class Cliente:
    def __init__(self,nom,ced,tel):
        self.nombre=nom
        self.cedula=ced
        self.telefono=tel

    def mostrarCliente(self):
        print(self.nombre,self.cedula,self.telefono)

class ClienteCorporativo(Cliente): #Aplicando herencia
    def __init__(self,nomb,cedu,tele,contrato):
        super().__init__(nomb,cedu,tele)
        self.__contrato = contrato  # atributo privado representado con __
    @property
    def contrato(self):#getter: obetener el valor del aributo privado
        return self.__contrato
    @contrato.setter
    def contrato(self,value): #setter: cambiar el valor del atributo privado
        if value:
            self.__contrato=value
        else:
            self.__contrato = 'Sin contrato'

    def mostrarCliente(self):
        print(self.nombre,self.__contrato) #Poliformismo: llamar al mismo metodo pero cambiar su comportamiento, prevalece la clase que se llama.

class ClientePersonal(Cliente): #Aplicando herencia
    def __init__(self,nom,ced,tel,promocion=True):
        super().__init__(nom,ced,tel)
        self.__promocion = promocion
    @property
    def promocion(self):
        if self.__promocion==True:
            return '10% de Descuento'
        else:
            return 'No hay Promocion'

    def mostrarCliente(self):
        print(self.nombre,self.promocion)



class Articulo:
    secuencia=0
    iva=0.12
    def __init__(self,des,pre,sto):
        Articulo.secuencia+=1
        self.codigo=Articulo.secuencia
        self.descripcion=des
        self.precio=pre
        self.stock=sto
    def mostrarArticulo(self):
        print(self.codigo,self.descripcion)

class DetVenta:
    linea=0
    def __init__(self,articulo,cantidad):
        DetVenta.linea+=1
        self.lineaDetalle=DetVenta.linea
        self.articulo=articulo
        self.precio=articulo.precio
        self.cantidad=cantidad

class CabVenta:
    def __init__(self, fac,fec,cliente,tot=0):
        self.factura=fac
        self.fecha=fec
        self.cliente=cliente
        self.total=tot
        self.detalleVen=[]

    def agregarDetalle(self,articulo,cantidad):
        detalle=DetVenta(articulo,cantidad)
        self.total += detalle.precio*detalle.cantidad
        self.detalleVen.append(detalle)

    def mostrarVenta(self, empNombre,empRuc):
        print('Empresa: {:17} Ruc: {:17}'.format(empNombre,empRuc))
        print('Factura#: {:13} Fecha: {}'.format(self.factura,self.fecha))
        self.cliente.mostrarCliente()
        print('Linea articulo     Precio  Cantidad  Subtotal')
        for det in self.detalleVen:
            print('{:5} {:15} {} {:6} {:7}'.format(det.linea,det.articulo.descripcion,det.precio,det.cantidad,det.precio*det.cantidad))
        print('Total Venta: {:26}'.format(self.total))

empresa=Empresa()
cli1=ClientePersonal('Daniel','0992214888','09921241',False)
art1=Articulo('Aceite',3,100)
art2=Articulo('Coca Cola',1,100)
today=date.today()
fecha=date(2021,8,15)
venta=CabVenta('F0001',date.today(),cli1)
venta.agregarDetalle(art1,3)
venta.agregarDetalle(art2,2)
venta.mostrarVenta(empresa.nombre,empresa.ruc)
