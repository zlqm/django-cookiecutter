#######################
django-cookiecutter
#######################

A cookiecutter template that helps you qucikly to generate blank django project

**********
Usuage
**********

.. code:: bash

    $: rm -rf AwesomeWebApp/
    $: cookiecutter django-cookiecutter/
    project_name [AwesomeWebApp]:
    docker_image_name [awesome-web-app]:
    secret_key [nmZU,e?)kN=N!>]m&*_+/V+Rt`ja+)%kGX``*+:p<vKD@;x"]:
    $: tree AwesomeWebApp/
    AwesomeWebApp/
    ├── compose
    │   ├── build_docker_image.sh
    │   ├── Dockerfile
    │   └── VERSION
    ├── config
    ├── docs
    ├── logs
    │   └── running.log
    ├── requirements
    │   ├── base.txt
    │   ├── local.txt
    │   └── production.txt
    └── src
        ├── apps
        │   └── __init__.py
        ├── config
        │   ├── logging.yml
        │   └── project.yaml
        ├── manage.py
        └── server
            ├── django_settings.py
            ├── extension_settings.py
            ├── __init__.py
            ├── settings.py
            ├── urls.py
            └── wsgi.py
    
    11 directories, 24 files
