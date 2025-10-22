# Usa una imagen oficial de Python
FROM python:3.12-slim

# Evita que Python escriba archivos .pyc y que guarde el output en buffer
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instala dependencias del sistema operativo necesarias para compilar mysqlclient
RUN apt-get update && apt-get install -y pkg-config default-libmysqlclient-dev build-essential

# Crea y establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requerimientos e instala las dependencias
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia el resto del código de la aplicación al directorio de trabajo
COPY . .

# Expone el puerto en el que correrá la aplicación
EXPOSE 8000

# Comando para iniciar la aplicación
# Asegúrate de que manage.py esté en la raíz del proyecto
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
