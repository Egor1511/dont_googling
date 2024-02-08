FROM python:3.12
WORKDIR /tree_menu
COPY infra/requirements.txt .
RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt --no-cache-dir
COPY task_test .