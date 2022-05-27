# hello-github-actions
Playground for experiments with GitHub actions

It's a simple web server.

# Installation
```bash
pipenv sync
pipenv shell
```

# Run server
```bash
python server.py   # run server on http://localhost:8080
curl http://localhost:8080/hello    # > Hello, world!
```

# Run tests

```bash
pytest tests
```