FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Copiar el código de la aplicación a la imagen
COPY . /app

# Exponer el puerto 8001
EXPOSE 8002

# Comando para iniciar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]
