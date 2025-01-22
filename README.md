# Kiratech Assignment

## Setting up

The project is managed by [uv](https://github.com/astral-sh/uv), please follow the installation instruction to set up the utility. Project is tested to run on 3.11 and above (uv should be able to set up the correct CPython environment).

Install the project with

```
uv sync # set up the virtual environment
uv pip install -e . # include the django app and project
```

Once done downloading the dependencies, you can start the project by

```
source .venv/bin/activate
./manage.py runserver 8081
```

Execute the migration

```
source .venv/bin/activate
./manage.py migrate
```

## Starting through docker

A development image is made available via github actions, it can be found at

```
podman pull ghcr.io/jeffrey04/kiratech-assignment:dev
```

And therefore can be started by docker/podman via

```
podman run -p0.0.0.0:8081:8081 ghcr.io/jeffrey04/kiratech-assignment:dev
```

Alternatively you can build the image by

```
podman build -t docker.io/jeffrey04/kiratech-assignment -f ./podman/Dockerfile .
```

## Usage

### Accessing the inventory list

The inventory web page can be access through

```
http://<HOSTNAME>:8081/inventory/
```

If there are inventories stored in the database, they would be displayed, and can be further filtered through the
search widget


### Accessing the inventory detail


The inventory detail page can be access through

```
http://<HOSTNAME>:8081/inventory/<ID>/
```

Alternatively, they can be accessed through the inventory list, by clicking on the inventory ID.


### Accessing the inventory API

The endpoint serving the list of inventory can be accessed through

```
http://<HOSTNAME>:8081/api/inventory/
```

Optionally it recognizes `name`, `description`, `note` GET parameters, to allow filtering of the result.


### Running the tests

The tests for inventory app can be done with the following command

```
source .venv/bin/activate
./manage.py test inventory
```


### Create a supervisor user

You can create a supervisor user by

```
source .venv/bin/activate
./manage.py createsuperuser --username <USERNAME>
```

Follow the prompts to complete the registration

### Access the admin panel

Visit the following URL,

```
http://<HOSTNAME>:8081/admin/
```

Login with the credentials created according to the instruction in the previous section.