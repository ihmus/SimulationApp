import os,sys
import pymunk
from PyQt5.QtCore import QTimer, QUrl, Qt
from PyQt5.QtGui import QColor, QVector3D, QQuaternion, QMouseEvent
from PyQt5.Qt3DCore import QEntity, QTransform
from PyQt5.Qt3DExtras import (Qt3DWindow, QPhongMaterial, QCuboidMesh, 
                             QTextureMaterial, QOrbitCameraController,QFirstPersonCameraController)
from PyQt5.Qt3DRender import QTextureLoader,QMesh
from PyQt5.QtWidgets import QApplication
from math import sin,cos
from  .objects import Drone
class Simulation(Qt3DWindow):
    def __init__(self):
        super().__init__()
        self.rootEntity = QEntity()
        self.setRootEntity(self.rootEntity)
        self.create_ground()

        # Kamera oluşturulur ve ayarlanır
        self.camera = self.camera()
        self.camera.lens().setPerspectiveProjection(45.0, 16/9, 0.1, 1000.0)
        self.camera.setPosition(QVector3D(0, 20, 10))
        self.camera.setViewCenter(QVector3D(0, 0, 0))
        
        # # Kamera kontrolü için timer
        # self.camera_timer = QTimer()
        # self.camera_timer.timeout.connect(self.update_camera)
        # self.camera_timer.start(16)

        self.camera_timer = QTimer()
        self.camera_timer.timeout.connect(self.update_movement)
        self.camera_timer.start(16)  # approximately 60 FPS
        self.movement_speed = QVector3D(0, 0, 0)
        self.acceleration = 0.01
        self.max_speed = 1

        self.panda = Drone(self.rootEntity)
        
        self.panda.entity.setParent(self.rootEntity)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_W:
            self.movement_speed.setZ(min(self.movement_speed.z() + self.acceleration, self.max_speed))
        elif event.key() == Qt.Key_S:
            self.movement_speed.setZ(max(self.movement_speed.z() - self.acceleration, -self.max_speed))
        elif event.key() == Qt.Key_A:
            self.movement_speed.setX(min(self.movement_speed.x() - self.acceleration, self.max_speed))
        elif event.key() == Qt.Key_D:
            self.movement_speed.setX(max(self.movement_speed.x() + self.acceleration, -self.max_speed))

    def keyReleaseEvent(self, event):
        if event.key() in (Qt.Key_W, Qt.Key_S):
            self.movement_speed.setZ(0)
        elif event.key() in (Qt.Key_A, Qt.Key_D):
            self.movement_speed.setX(0)

    def update_movement(self):
        if not self.movement_speed.isNull():
            self.camera.translate(self.movement_speed)

    def mouseMoveEvent(self, event: QMouseEvent):
        if event.buttons() == Qt.LeftButton:
            delta = event.localPos() - self.last_mouse_position
            rotation_axis_x = QVector3D(1, 0, 0)  # x-axis
            rotation_axis_y = QVector3D(0, 1, 0)  # y-axis
            rotation_quaternion_x = QQuaternion.fromAxisAndAngle(rotation_axis_x, delta.y() * 0.1)
            rotation_quaternion_y = QQuaternion.fromAxisAndAngle(rotation_axis_y, delta.x() * 0.1)
            self.camera.rotate(rotation_quaternion_x)
            self.camera.rotate(rotation_quaternion_y)
        self.last_mouse_position = event.localPos()


    def create_ground(self):
        # Zemin oluşturma işlemleri
        groundEntity = QEntity(self.rootEntity)
        
        groundMesh = QCuboidMesh()
        groundEntity.addComponent(groundMesh)
        
        groundMaterial = QPhongMaterial()
        groundMaterial.setDiffuse(QColor(0, 255, 0))
        groundEntity.addComponent(groundMaterial)
        
        groundTransform = QTransform()
        groundTransform.setScale(10.0)
        groundTransform.setTranslation(QVector3D(0, -10, 0))
        groundEntity.addComponent(groundTransform)
        
    def update_camera(self):
        # Kamera güncellenir. Örneğin, kameranın konumu veya bakış açısı değiştirilebilir.
        # Bu örnek, kamerayı belirli bir yörüngede döndürür.
        angle = 0.01  # Döndürme açısı
        camera_position = self.camera.position()
        self.camera.setPosition(QVector3D(camera_position.x() * cos(angle) - camera_position.z() * sin(angle),
                                          camera_position.y(),
                                          camera_position.x() * sin(angle) + camera_position.z() * cos(angle)))

# # Qt uygulamasını başlatma kodu
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     simulation = Simulation()
#     simulation.show()
#     sys.exit(app.exec_())