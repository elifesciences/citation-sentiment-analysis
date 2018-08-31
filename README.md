# Citation Sentiment Analysis

## Notebooks

The [notebooks](./notebooks) can be run via [Jupyter](https://jupyter.org/).

### Using Docker to run Jupyter

Pre-requisites:

- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/)

```bash
docker-compose up --build sciencebeam-judge-jupyter
```

Open [http://localhost:8891/](http://localhost:8891/).

(The port can be configured using the _CITATION_SENTIMENT_JUPYTER_PORT_ environment variable)

### Using Local Jupyter installation

Pre-requisites:

- [Jupyter](https://jupyter.org/)

Install the additional dependencies:

```bash
pip install -r requirements.txt
```
