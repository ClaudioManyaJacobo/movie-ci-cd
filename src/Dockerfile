# src/Dockerfile

# Usa imagen base de Python
FROM python:3.13-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el contenido del proyecto al contenedor
COPY src/ /app

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto
EXPOSE 5000

# Comando para correr la app Flask
CMD ["flask", "run", "--host=0.0.0.0"]
