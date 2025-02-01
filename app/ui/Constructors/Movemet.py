from PyQt5.QtGui import QVector3D

class MovementControl:
    def __init__(self, initial_speed: QVector3D, max_speed: float, acceleration: float):
        # Sabit parametreler
        self._max_speed = max_speed  # Sabit: Maksimum hız değişmeyecek

        # Değişebilir parametreler
        self._movement_speed = initial_speed  # Hareket hızı
        self._acceleration = acceleration    # Hızlanma değeri

    # Getter metodları
    def getMovementSpeed(self) -> QVector3D:
        return self._movement_speed

    def getMaxSpeed(self) -> float:
        return self._max_speed

    def getAcceleration(self) -> float:
        return self._acceleration

    # Setter metodları (Değiştirilebilen parametreler)
    def setMovementSpeed(self, new_speed: QVector3D):
        # Burada hız sınırını kontrol edebilirsiniz
        if new_speed.length() <= self._max_speed:
            self._movement_speed = new_speed
        else:
            # Eğer yeni hız max_speed'yi aşıyorsa, max_speed'e ayarlayabilirsiniz.
            # Eğer daha ileri seviyede hız denetimi yapmak isterseniz, burada bir şeyler ekleyebilirsiniz.
            self._movement_speed = self._movement_speed.normalized() * self._max_speed

    def setAcceleration(self, new_acceleration: float):
        # İstediğiniz gibi hızlanma değeri değiştirilebilir.
        self._acceleration = new_acceleration
