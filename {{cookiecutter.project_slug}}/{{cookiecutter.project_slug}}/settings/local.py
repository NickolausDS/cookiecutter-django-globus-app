SECRET_KEY = "django-insecure-47f(ub2qs-n!b@&&)tis&l$&qf1%^@&jy-95jx!bahqrm^19m2"
SOCIAL_AUTH_GLOBUS_KEY = "{{ cookiecutter.globus_client_id }}"
SOCIAL_AUTH_GLOBUS_SECRET = "{{ cookiecutter.globus_secret_key }}"

COLLECTIONS = [
    {
        "id": "{{ cookiecutter.globus_portal_endpoint_id }}",
        "name": "",
        "description": "",
    },
]
