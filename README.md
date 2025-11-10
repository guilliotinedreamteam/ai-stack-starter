# AI Stack Starter  
This repository contains a minimal docker‑compose setup that wires together a Stable Diffusion web UI, a simple helper API service, and an nginx reverse proxy. The goal is to provide a quick way to spin up a local AI stack for experimentation.  

## Services  
- **Stable Diffusion web UI (sd-webui)** – built from the `universonic/stable-diffusion-webui:minimal` image. It serves a web interface on port 8080 and uses volumes so you can persist models, outputs and extensions.  
- **Helper** – a small FastAPI service defined in `helper/app.py`. It exposes a root endpoint (`/`) with a welcome message and a `/health` endpoint for health checks. This service runs on port 5000 and can be extended to add additional functionality.  
- **nginx** – a lightweight reverse proxy. nginx listens on port 80 and routes `/` to the Stable Diffusion UI and `/helper/` to the helper API.  

## Prerequisites  
You need Docker and Docker Compose installed. Ensure you have a Stable Diffusion model file (e.g. `.ckpt` or `.safetensors`) placed in a local directory that will be mounted into the `models` volume. According to the official image documentation, the container will not start unless a model file exists in the mounted models directory ([hub.docker.com](https://hub.docker.com/r/universonic/stable-diffusion-webui)).  

## Running  
1. Clone this repository:  
   ```  
   git clone https://github.com/guilliotinedreamteam/ai-stack-starter.git  
   cd ai-stack-starter  
   ```  
2. Create a directory on your host (e.g. `./data/models`) and put at least one Stable Diffusion model file in it.  
3. Edit `docker-compose.yml` if you wish to change ports or volume paths. By default the compose file mounts:  
   - `./data/extensions`, `./data/models`, `./data/outputs` and `./data/localizations` into the web UI container to persist your custom extensions, models, generated images and localisation files ([hub.docker.com](https://hub.docker.com/r/universonic/stable-diffusion-webui)).  
4. Start the stack in detached mode:  
   ```  
   docker compose up -d  
   ```  
5. Open your browser to http://localhost. The Stable Diffusion UI will be available at `/` and the helper service at `/helper/`.  

To stop the stack, run:  
```  
docker compose down  
```  

## Extending the helper service  
The helper API is defined in `helper/app.py`. You can add new endpoints using FastAPI to handle tasks such as image post‑processing or integration with other services. If you modify the helper service, rebuild the container by running `docker compose up --build`.  

## Notes  
- If you want to expose the services on different ports, modify the `ports` section in `docker-compose.yml`.  
- The nginx configuration is located in `nginx/nginx.conf`. It defines upstreams for both services and routes paths accordingly. 
