FROM continuumio/anaconda3:2021.04

ARG APP_PATH, CONDA_ENV
WORKDIR $APP_PATH
COPY . $APP_PATH
# RUN conda create -n $CONDA_ENV python=3.10.10 \
# 	numpy=1.23.5 flask=2.2.2 plotly=5.9.0 \
# 	seaborn=0.12.2 scikit-learn=1.2.2 scipy=1.10.1
RUN conda env create -f "./environment.yml"
WORKDIR $APP_PATH