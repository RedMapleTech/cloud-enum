# Dockerfile for building to single executable file with pyinstaller
FROM --platform=linux/amd64 python:alpine

RUN apk add binutils

WORKDIR /usr/src/cloud-enum

COPY . .

RUN pip3 install -r ./requirements.txt

CMD ["pyinstaller", "--onefile", "--add-data=enum_tools/fuzz.txt:enum_tools", "--add-data=enum_tools/ns.txt:enum_tools", "cloud_enum.py"]