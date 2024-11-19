from __future__ import annotations

class TV:
    _numTV = 0
    def __init__(self, marca: Marca, estado: bool):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        self._control = None
        TV._numTV += 1  
    def getNumTV(cls):
        return cls._numTV 
    def setNumTV(cls, numTV: int):
        cls._numTV = numTV
    def setMarca(self, marca: Marca):
        self._marca = marca
    def setCanal(self, canal: int):
        if self._estado and 1 <= canal <= 120:
            self._canal = canal
    def setPrecio(self, precio: int):
        self._precio = precio
    def setVolumen(self, volumen: int):
        if self._estado and 0 <= volumen <= 7:    
            self._volumen = volumen
    def setControl(self, control: Control):
        self._control = control
    def getMarca(self) -> Marca:
        return self._marca
    def getCanal(self) -> int:
        return self._canal
    def getPrecio(self) -> int:
        return self._precio
    def getVolumen(self) -> int:
        return self._volumen
    def getControl(self) -> Control:
        return self._control
    def getEstado(self) -> bool:
        return self._estado
    def turnOn(self) -> None:
        self._estado = True
    def turnOff(self) -> None:
        self._estado = False
    def canalUp(self) -> None:
        self.setCanal(self._canal + 1)
    def canalDown(self) -> None:
        self.setCanal(self._canal - 1)
    def volumenUp(self) -> None:
        self.setVolumen(self._volumen + 1)
    def volumenDown(self) -> None:
        self.setVolumen(self._volumen - 1)
TV.setNumTV = classmethod(TV.setNumTV)
TV.getNumTV = classmethod(TV.getNumTV)