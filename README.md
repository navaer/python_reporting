# 📊 GoContact Report Downloader

Aplicación en **Python** para conectarse a la API de **GoContact** y descargar reportes en formato CSV de forma automática.  

El script se encarga de:
- 🔐 Autenticarse con credenciales seguras (hash SHA512 de la contraseña).
- 📅 Generar un reporte del rango de fechas actual (desde el inicio del mes hasta hoy).
- 💾 Descargar y guardar el reporte como `report.csv`.

---

## ⚙️ Requisitos

- Python **3.8+**  
- Librerías Python:
  - `python-dotenv`

---

## 📥 Instalación

1. **Clonar el repositorio o copiar los archivos** en tu máquina local:

   ```bash
   git clone https://github.com/tu-usuario/gocontact-downloader.git
   cd gocontact-downloader
