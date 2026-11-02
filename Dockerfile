FROM python:3.12-slim
WORKDIR /app
COPY feature_cart.py .
CMD ["python", "feature_cart.py"]
