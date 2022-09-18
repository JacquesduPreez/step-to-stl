# STEP to STL converter

A simple python script using [Freecad](https://www.freecadweb.org/) to batch convert Step files into the STL format.

## Running Locally

```bash
git clone JacquesduPreez/step-to-stl.git
cd step-to-stl
```

With `docker`
```bash
docker run -v $PWD/convert:/app/convert -v $PWD/step_to_stl.py:/app/step_to_stl.py -w /app amrit3701/freecad-cli:latest python3 step_to_stl.py
```

With `docker-compose`

```bash
docker-compose up
```

