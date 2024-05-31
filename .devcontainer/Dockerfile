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
    libindicator7 \
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

# Install Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' \
    && apt-get update \
    && apt-get install -y google-chrome-stable

# Install ChromeDriver
RUN CHROME_VERSION=$(google-chrome --version | grep -oP '\d+\.\d+\.\d+') \
    && CHROMEDRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION) \
    && wget -N https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip -d /usr/local/bin/ \
    && rm chromedriver_linux64.zip

# Install pipx and biobricks
RUN python3 -m pip install --user pipx \
    && python3 -m pipx ensurepath \
    && ~/.local/bin/pipx install biobricks

# Create /mnt/biobricks directory
RUN mkdir -p /mnt/biobricks

# Install Python dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# Set up the workspace
WORKDIR /workspace

# Add the following lines to the shell profile to include pipx binaries
RUN echo 'export PATH="$PATH:$HOME/.local/bin"' >> /home/vscode/.bashrc

# Configure biobricks with a GitHub secret token
RUN echo 'biobricks configure --bblib /mnt/biobricks --token $GITHUB_TOKEN' >> /home/vscode/.bashrc
