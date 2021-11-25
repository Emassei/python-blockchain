#to run locally from docker, build the image:
```
docker build -t python-blockchain .
```
#Run the container in interactive mode with bash
```
docker run -it python-blockchain bash
```

#If you wanna go the venv route

```
#create venv
python -m venv blockchain-env
source blockchain-env/bin/activate
pip install -r requirments.txt
```

#Tests
```
source blockchain-env/bin/activate
python -m pytest backend/tests
```
