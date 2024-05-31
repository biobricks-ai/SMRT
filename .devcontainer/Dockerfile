FROM mcr.microsoft.com/devcontainers/python:3.9

# Install necessary packages
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    xvfb \
    libxi6 \
    libgconf-2-4 \
    libnss3-dev \
    libxss1 \
    libappindicator1 \
    fonts-liberation \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libgbm1 \
    libasound2 \
    libdpkg-perl \
    libatomic1 \
    ca-certificates \
    curl \
    gnupg \
    python3-venv

# Install pipx and biobricks
RUN python3 -m pip install --user pipx \
    && python3 -m pipx ensurepath

# Create /mnt/biobricks directory
RUN mkdir -p /mnt/biobricks

# Install Python dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# Set up the workspace
WORKDIR /workspace

# Add the following lines to the shell profile to include pipx binaries for all users
RUN echo 'export PATH="$PATH:$HOME/.local/bin"' >> /etc/bash.bashrc \
    && echo 'export PATH="$PATH:$HOME/.local/bin"' >> /home/vscode/.bashrc

# Accept build argument for BIOBRICKS_TOKEN
ARG BIOBRICKS_TOKEN
ENV BIOBRICKS_TOKEN=${BIOBRICKS_TOKEN}

# Install biobricks
RUN /bin/bash -c 'source /etc/bash.bashrc && pipx install biobricks'

# Verify biobricks installation
RUN /bin/bash -c 'source /etc/bash.bashrc && biobricks version'

# Configure biobricks using the build argument
RUN /bin/bash -c 'source /etc/bash.bashrc && biobricks configure --bblib /mnt/biobricks --token ${BIOBRICKS_TOKEN} --interactive=False'
