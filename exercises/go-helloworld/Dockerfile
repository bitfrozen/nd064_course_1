# Get full go image for building
FROM golang:alpine3.12 AS build
# Get source
WORKDIR /go/src/app
COPY . .
# Build binary
RUN go build -o helloworld

# Get empty image for runtime
FROM golang:alpine3.12 AS runtime
WORKDIR /go/bin
LABEL maintainer="Antanas Domarkas"
COPY --from=build /go/src/app/helloworld /go/bin/helloworld

EXPOSE 6111
CMD [ "./helloworld" ]
