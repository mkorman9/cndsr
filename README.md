Simplistic but fully scalable URL shortening service. It serves as my playground for learning Django stack.
It consists of backend REST API written in Django, automated tests in behave, 
and generic build pipeline for Python projects, able to test multiple packages and 
pack them as Docker images which are fully configurable using environment variables.
Execution environment is spawned on-demand with either docker-compose (local testing, CI) or Kubernetes (production).

[TODO: more details]

#### Configure:
1. Install Python >= 3, Docker and docker-compose. They should be accessible from PATH, without sudo.
2. Clone project
```bash
git clone https://github.com/mkorman9/python-build-system.git
cd python-build-system
```
3. Setup local virtualenv
```bash
make config
```

#### Build:
```bash
make all  # or simply "make"
```

#### Running feature tests:
```bash
make validate
```
