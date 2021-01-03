# expertonica-test

# Prerequisites
- [Docker](https://docs.docker.com/docker-for-mac/install/)  

# Local Development

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```
or while running containers
```bash
docker exec -it expertonica-test_back_1 bash
```

After docker-compose:
 1. Create superuser in shell
 2. Launch import_website_urls task from /api/v1/websites/load-websites/
    or manually from shell

# Swagger
    /api/docs/