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

Run your project

```
docker-compose up
```

Run tests

```
docker-compose run --rm app sh -c "python manage.py test && flake8"
```

Create a superuser

```
docker-compose run --rm app sh -c "python manage.py createsuperuser"
```

The app runs in port 8000

Open [http://localhost:8000/api](http://localhost:8000/api) to view swagger documentation on the browser.

## Using the DRF API Browser

Install [`ModHeader`](https://chrome.google.com/webstore/detail/modheader/idgpnmonknjnojddfkpgkljpfnnfcklj) Extension for Chrome

To login with the user created previously;

Head to the login endpoint for an AuthToken [http://localhost:8000/api/auth/login](http://localhost:8000/api/auth/login) 

Sample Token 

```
{
    "key": "af66cdf8d4853d53f9ec760170b661130bf114ea"
}
```

Then set the authorization token as shown


![Authorization Token](../images/Screenshot.png?raw=true "TokenAuth")

## License

[MIT](https://choosealicense.com/licenses/mit/)
