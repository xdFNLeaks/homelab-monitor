# HomeLab Monitor

HomeLab Monitor is a simple web application built with Flask to monitor and display system statistics of your homelab device.

This is the most lightweight HomeLab Monitor.

This repository also includes a Docker setup for easy deployment.

## Features

- View CPU usage
- Monitor memory usage
- Easy-to-use/Very very simple web interface (auto refreshes every 32s)

## Getting Started

### Prerequisites

- Docker installed on your machine.

### Usage

1. Clone this repository:

    ```bash
    git clone https://github.com/xdfnleaks/homelab-monitor.git
    cd homelab-monitor
    ```

2. Build and run the Docker container:

    ```bash
    sudo docker-compose up -d
    ```

3. Access the HomeLab Monitor web interface:

    Open your web browser and navigate to [http://localhost:5000](http://localhost:5000).

And now your all set!

### Deploying with Portainer

If you prefer using Portainer to manage your Docker containers, follow these steps:

1. Make sure you have Portainer installed. If not, you can deploy it using the following Docker Compose file:

    ```yaml
    version: '3'

    services:
      portainer:
        image: portainer/portainer-ce
        restart: always
        ports:
          - "9000:9000"
        volumes:
          - /var/run/docker.sock:/var/run/docker.sock
    ```

    Run `docker-compose up -d` to start Portainer.

2. Open your web browser and navigate to [http://localhost:9000](http://localhost:9000) to set up Portainer.

3. Once Portainer is set up, create a new stack.

4. Copy the contents of the `docker-compose.yml` file displayed below

    ```yaml
    version: '3'

    services:
      homelab-monitor:
        image: ghcr.io/xdfnleaks/homelab-monitor:latest
        restart: always
        ports:
          - "5000:5000"
        container_name: homelab-monitor

    ```

5. Paste the copied content into the Portainer stack editor.

6. Deploy the stack.

7. Access the HomeLab Monitor web interface through Portainer.

# Issues

**Please report any issues you have with the bot in the Issues tab!**
