# docker-weasyprint

[Weasyprint](http://weasyprint.org/) as a microservice in a docker image.

# Usage

Run the docker image, exposing port 5001

```
docker run -p 5001:5001 aquavitae/weasyprint
```

A `POST` to port 5001 with an html body with give a response containing a PDF.
