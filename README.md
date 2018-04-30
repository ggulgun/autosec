# Autosec
Autosec is autonomous application security engine based on owasp/glue

## Getting Started

Autosec is an application that runs with the functionality of the rest API which can integrate with jenkins and travis.

### Prerequisites

What things you need to install the software and how to install them

```
python
docker
pip install -r requirements.txt
```

### Installing


```
yum -y install docker-io
yum -y install docker
```
### Before run
Enter docker image directory
```
docker build -t autosec .
```

### Sample run

In project directory

```
flask run
```

### Sample initial task

```
curl -X POST http://127.0.0.1:5000/scan --form "repository=aHR0cHM6Ly9naXRodWIuY29tL0plbXVyYWkvdHJpYWdlLmdpdA=="

curl -X POST http://127.0.0.1:5000/logs --form "name=trial"
```
