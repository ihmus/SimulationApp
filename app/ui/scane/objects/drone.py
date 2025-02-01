import os
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QColor
from PyQt5.Qt3DCore import QEntity, QTransform
from PyQt5.Qt3DExtras import (QPhongMaterial,QTextureMaterial)
from PyQt5.Qt3DRender import QTextureLoader,QMesh
modelspath= os.path.join(os.getcwd(),'app\\ui\\scane\\models')

print(modelspath)
print(os.getcwd())
class Drone:
    def __init__(self, parent: QEntity):
        self.entity = QEntity(parent)
        # Malzeme bileşeni oluşturulur ve doku eklenir
        self.material = QPhongMaterial()
        self.material.setDiffuse(QColor(0, 255, 255))  # Bir renk belirt

        # Mesh bileşeni oluşturulur ve model dosyası yüklenir
        mesh = QMesh()
        if os.path.exists(os.path.join(modelspath, "modelfiles", "drone.obj")):
            mesh.setSource(QUrl.fromLocalFile(os.path.join(modelspath, "modelfiles", "drone.obj")))
        else:
            print(f"Dosya bulunamadı {modelspath}")
        
        # Doku yükleyici oluşturulur ve doku dosyası yüklenir
        self.textureLoader = QTextureLoader()
        self.textureLoader.setSource(QUrl.fromLocalFile(os.path.join(modelspath, "texturefiles", "metalicdrone.jpg")))

        # Doku malzemesi oluşturulur ve doku yükleyici eklenir
        self.textureMaterial = QTextureMaterial()
        self.textureMaterial.setTexture(self.textureLoader) 
        
        # Bileşenler varlığa eklenir
        self.entity.addComponent(mesh)
        self.entity.addComponent(self.textureMaterial)
        
        self.transform = QTransform()
        self.entity.addComponent(self.transform)