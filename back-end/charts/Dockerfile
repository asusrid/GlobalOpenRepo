FROM continuumio/miniconda3

RUN conda create -n env python=3.7
RUN echo "source activate env" > ~/.bashrc
ENV PATH /opt/conda/envs/env/bin:$PATH

ENV PYTHONDONTWRITEBYTECODE 1
ENV FLASK_APP "app/app.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True

RUN mkdir /app
WORKDIR /app

COPY Pip* /app/

RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --dev --system --deploy --ignore-pipfile

RUN conda install ffmpeg

ADD . /app

EXPOSE 5000

CMD flask run --host=0.0.0.0