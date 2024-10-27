# Usa una imagen base de Python
FROM python:3.10

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requisitos y luego instala las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos de la aplicación
COPY . .

# Expone el puerto en el que corre tu aplicación (Heroku espera que uses el puerto 5000)
EXPOSE 5000

# Comando para iniciar la aplicación
CMD ["python", "app.py"]
