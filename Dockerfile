FROM ubuntu:22.04

# Install necessary packages
RUN apt-get update && apt-get install -y python3.11 python3.11-venv python3-pip curl 
#RUN apt-get install libmysqlclient-dev
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11
RUN apt-get install -y net-tools sudo vim curl
# Set working directory
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Setup 
#RUN pip install -y toml
#RUN ./update_toml_py.py
RUN chmod 777 init_setup.sh
RUN ./init_setup.sh
#RUN python3.11 -m venv venv
#RUN /bin/bash -c "source ./venv/bin/activate"
#RUN /bin/bash -c "python3.11 -m pip install -e ."
EXPOSE 8002
#EXPOSE 8501
# Run CMD
CMD ["uvicorn", "src.snakesay.INGEST:app", "--reload", "--port", "8002", "--host", "0.0.0.0"]