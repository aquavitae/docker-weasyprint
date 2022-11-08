# docker-weasyprint

[![Build Status](https://travis-ci.org/aquavitae/docker-weasyprint.svg?branch=master)](https://travis-ci.org/aquavitae/docker-weasyprint)

[Weasyprint](http://weasyprint.org/) as a microservice in a Docker image.

# Usage

Run the Docker image, exposing port 5001

```bash
docker run -p 5001:5001 aquavitae/weasyprint
```

A `POST` to port `/pdf` on port 5001 with an HTML body with give a response containing a PDF. The filename may be set using a query parameter, e.g.:

```bash
curl -X POST -d @source.html http://127.0.0.1:5001/pdf?filename=result.pdf
```

This will use the file `source.html` and return a response with `Content-Type: application/pdf` and `Content-Disposition: inline; filename=result.pdf` headers. The body of the response will be the PDF.

In addition `/health` is a health check endpoint and a `GET` returns 'ok'.

# Security

To restrict access to only trusted clients, set the environment variable `X_API_KEY` with a client secret when running the image:

```bash
docker run -e X_API_KEY=somethingMOREsecure -p 5001:5001 aquavitae/weasyprint
```

PDF requests will now only be accepted if they provide the matching header:

```bash
curl -X POST -H "X_API_KEY: somethingMOREsecure" -d @source.html http://127.0.0.1:5001/pdf?filename=result.pdf
```
