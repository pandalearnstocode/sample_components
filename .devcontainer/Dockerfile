ARG PYTHON_VERSION
FROM mcr.microsoft.com/vscode/devcontainers/python:${PYTHON_VERSION}

ARG REMOTE_USER
ENV HOME="/home/${REMOTE_USER}" \
    JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64" \
    PYSPARK_PYTHON="/usr/local/bin/python" \
    PYSPARK_DRIVER_PYTHON="/usr/local/bin/python"

RUN apt-get update && \
    apt-get -y install --no-install-recommends software-properties-common && \
    apt-add-repository 'deb http://security.debian.org/debian-security stretch/updates main' && \
    apt-get update && \
    apt-get -y install --no-install-recommends \
      openjdk-8-jre \
      cmake

ARG POETRY_VERSION="none"
RUN if [ "${POETRY_VERSION}" != "none" ]; then su vscode -c "umask 0002 && pip3 install poetry==${POETRY_VERSION}"; fi

# Switch to non-root user
USER ${REMOTE_USER}
WORKDIR ${HOME}
