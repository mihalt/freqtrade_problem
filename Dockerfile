FROM ghcr.io/freqtrade/freqtrade-devcontainer:latest
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN pip install --user -e .