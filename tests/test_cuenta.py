import pytest

class Cuenta:
    def __init__(self) -> None:
        self.nombre = ""
        self.saldo = 0

    def depositar(self,agregarsaldo):
        self.saldo = self.saldo + agregarsaldo


    def restartsaldo(self,restarsaldo):
        if  (self.saldo - restarsaldo < 0):
            raise ValueError
        else:
            self.saldo = self.saldo - restarsaldo
            
        
def test_cuenta_saldo_cero():
    cuenta = Cuenta()
    assert cuenta.saldo == 0

def test_cuenta_agregar_saldo():
    cuenta = Cuenta()
    cuenta.depositar(10)
    assert cuenta.saldo == 10
    
def test_cuenta_retirar_saldo():
    cuenta = Cuenta()
    cuenta.depositar(15)
    cuenta.restartsaldo(10)
    assert cuenta.saldo == 5

def test_cuenta_retirar_error_retiro_mayor_a_saldo():
    cuenta = Cuenta()
    cuenta.depositar(15)
    with pytest.raises(ValueError):
        cuenta.restartsaldo(50)
    