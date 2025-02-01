import os
# Mevcut çalışma dizinini alır
current_directory = os.getcwd()
# from ..AppSettings import LOGGING_CONFIG
Configfile = os.path.join(current_directory, 'SimulationSettings/Config.py').replace("/", "\\")
if not os.path.exists(Configfile):
    print("Dosya bulunamadı")
else:
    print(f"Dosya yolu: {Configfile}")

class ConfigUpdater:
    def __init__(self):
        self.config_file = Configfile
        self.content = self.read_file()

    def read_file(self):
        """Dosyayı okur ve içeriği döndürür."""
        try:
            with open(self.config_file, 'r') as file:
                content = file.readlines()
            return content
        except FileNotFoundError:
            print(f"Hata: Dosya {self.config_file} bulunamadı.")
            return []

    def write_file(self):
        """Güncellenmiş içeriği dosyaya yazar."""
        try:
            with open(self.config_file, 'w') as file:
                file.writelines(self.content)
            print(f"{self.config_file} dosyasına başarıyla yazıldı.")
        except IOError as e:
            print(f"Dosya yazma hatası: {e}")

    def update_key_value(self, key, new_value):
        """Belirli bir anahtarın (key) değerini (value) günceller."""
        for i, line in enumerate(self.content):
            # Satırda key bulunursa, değeri değiştirmek için işleme alır
            if key in line:
                # Key: Value formatında olduğu varsayılır
                parts = line.split(":")
                if len(parts) == 2:
                    # Yeni değeri eski değerin yerine koyar
                    self.content[i] = f"    '{key}': {new_value},\n"
                    print(f"{key} değeri '{new_value}' olarak güncellendi.")
                    break

    def update_config_file(self, new_host=None, new_port=None, new_database=None):
        """Tüm güncellemeleri yapar ve dosyayı kaydeder."""
        # Güncelleme işlemleri
        self.update_key_value('host', f"'{new_host}'")  # Host değerini değiştir
        self.update_key_value('port', new_port)  # Port değerini değiştir
        self.update_key_value('database_name', f"'{new_database}'")  # Veritabanı adını değiştir
        
        # Dosyayı güncellenmiş içerikle kaydet
        self.write_file()  # Dosyayı yazdır
        print(f"{self.config_file} dosyası başarıyla güncellendi.")


# Kullanım örneği
config_updater = ConfigUpdater()
config_updater.update_config_file('127.0.0.1', 3307, 'new_database')

### bu fonksiyonu init metodu ekleyerek düzenledikten sonra yapacağım 
# from SimulationSettings import Config  # config.py dosyasını içe aktarıyoruz

# class ConfigUpdater:
#     def __init__(self):
#         self.config = Config.DATABASE_CONFIG  # DATABASE_CONFIG sözlüğünü alıyoruz

#     def update_key_value(self, key, new_value):
#         """Belirli bir anahtarın (key) değerini (value) günceller."""
#         if key in self.config:
#             self.config[key] = new_value
#             print(f"{key} değeri '{new_value}' olarak güncellendi.")
#         else:
#             print(f"{key} anahtarı bulunamadı.")

#     def save_config(self):
#         """Güncellenmiş sözlüğü config.py dosyasına kaydeder."""
#         with open('config.py', 'w') as file:
#             file.write(f"DATABASE_CONFIG = {self.config}\n")
#         print("config.py dosyasına başarıyla yazıldı.")

#     def update_config_file(self, new_host, new_port, new_name):
#         """Tüm güncellemeleri yapar ve dosyayı kaydeder."""
#         self.update_key_value('host', new_host)  # Host değerini değiştir
#         self.update_key_value('port', new_port)  # Port değerini değiştir
#         self.update_key_value('database_name', new_name)  # Veritabanı adını değiştir
#         self.save_config()  # Güncellenmiş veriyi kaydet
#         print("config.py dosyası başarıyla güncellendi.")


# # Kullanım örneği
# config_updater = ConfigUpdater()
# config_updater.update_config_file('127.0.0.2', 3308, 'updated_database')
