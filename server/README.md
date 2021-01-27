# Students REST API Setup

## Installation & Usage

First clone repo from Gitbub and switch to `server` directory

```bash
git clone git@github.com:benedictkioko/react-typescript-startups.git

cd server
```

Make sure that docker is running

```
open -a Docker
```

Build your images

```
docker-compose build
```

Run tests

```
docker-compose run --rm app sh -c "python manage.py test && flake8"
```

Now, run your project

```
docker-compose up
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
