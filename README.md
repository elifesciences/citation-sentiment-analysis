# Citation Sentiment Analysis

## Notebooks using Jupyter

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

## Notebook Overview

The following notebooks are currently present:

- [athar-dataset.ipynb](notebooks/athar-dataset.ipynb): A look at the Athar dataset itself
- [athar-bag-of-words-baseline-naive-bayes.ipynb](notebooks/athar-bag-of-words-baseline-naive-bayes.ipynb): Baseline Naive Bayes model
- [athar-bag-of-words-baseline-naive-bayes-balance-and-bias.ipynb](notebooks/athar-bag-of-words-baseline-naive-bayes-balance-and-bias.ipynb): Showing different options of balancing the Athar dataset (and importance of randomising it)
- [athar-bag-of-words-model-comparison.ipynb](notebooks/athar-bag-of-words-model-comparison.ipynb): Comparison of some standard models using Bag of Words as an input (including Naive Bayes)
