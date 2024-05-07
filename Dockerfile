FROM python:3
USER root

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y vim less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN python -m pip install jupyterlab
RUN python -m pip install requests
RUN python -m pip install beautifulsoup4
RUN python -m pip install selenium
RUN python -m pip install gspread
RUN python -m pip install oauth2client
RUN python -m pip install google-api-python-client
RUN python -m pip install google-auth-httplib2
RUN python -m pip install google-auth-oauthlib