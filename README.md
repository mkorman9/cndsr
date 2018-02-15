## cndsr (condenser)
cndsr is a simple URL shortening software. It's free, open source and ready to deploy basically anywhere.

[TODO: add screenshot here :>]

### Why?
Project is maintained for educational purposes.

### How to build?

##### Configure (do only once):
1. Install Python >= 3, Docker and docker-compose. They should be accessible from PATH, without sudo.
2. Clone project
```bash
git clone https://github.com/mkorman9/cndsr.git
cd cndsr
```
3. Setup local virtualenv
```bash
make config
```

##### Build and run feature tests locally:
```bash
make all  # or simply "make"
make validate
```

#### Technologies used
- Python 3
- Django
- behave
- uWSGI
- Docker, docker-compose
- Kubernetes
- redis
- React

Technical details are described [in separated document](https://github.com/mkorman9/cndsr/blob/master/TECHNICAL_DETAILS.md).
