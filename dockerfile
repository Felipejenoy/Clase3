# Usar una imagen base adecuada
FROM python:3.11

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requisitos y la aplicación
COPY requirements.txt .
COPY app.py .

# Instalar las dependencias necesarias
RUN apt-get update && \
    apt-get install -y unixodbc-dev && \
    pip install --no-cache-dir -r requirements.txt

# Exponer el puerto que usará la aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000"]
