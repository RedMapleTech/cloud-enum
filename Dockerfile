# Dockerfile for building to single executable file with pyinstaller
FROM python:alpine
ARG TARGETARCH
ENV TARGETARCH=$TARGETARCH

RUN apk add binutils

WORKDIR /usr/src/cloud-enum

COPY . .

RUN pip3 install -r ./requirements.txt

CMD ["sh", "-c", "pyinstaller --onefile --add-data=enum_tools/fuzz.txt:enum_tools --add-data=enum_tools/ns.txt:enum_tools -n cloud-enum-${TARGETARCH} cloud_enum.py"]