Prototype of build pipe for Python projects consisting of multiple packages and Docker images.
   
#### Configure:
1. Install automake, Python >= 3 and Docker. They should be accessible from PATH, without sudo.
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
make
```
