FROM jupyter/minimal-notebook

ENV PROJECT_HOME=/home/jovyan/citation-sentiment-analysis

WORKDIR ${PROJECT_HOME}

COPY requirements.txt ${PROJECT_HOME}/
RUN pip install --upgrade pip && \
  pip install -r requirements.txt

COPY download-nltk-data.sh ${PROJECT_HOME}/
RUN bash ./download-nltk-data.sh

COPY docker/docker-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]

WORKDIR ${PROJECT_HOME}/notebooks

USER root
