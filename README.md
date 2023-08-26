# Ansible Playbook for Deploying Django

This playbook is designed to deploy a Django application using Ansible. It sets up a Postgres database, Nginx, and Gunicorn on a Linux server.

## Setup

Edit your variables in `/deploy.yml`:

```yaml
become_user: john_doe
port: 8000
port_devel: 8001
secret_key: "my-django-secret-key"  # Replace with a secure key
db_user: "john_doe"
db_name: "testsite"
db_name_devel: "testsite-db"
db_pass: "q#JX6zy#AxbhEid$"  # Replace with a secure password
app_name: "testsite"
app_name_devel: "testsite_devel"
proj_name: "{{ app_name }}"
app_user: "john_doe"
server_name: "testsite.com"
server_name_www: "www.testsite.com"
server_name_devel: "devel.testsite.com"
domain: testsite.com
domain_devel: devel.testsite.com
git_link: https://github.com/john_doe/project.git  # Replace with your repository link
```

Let Ansible do the work
====

For getting good results I prefer doing each tag in following order:

Install Postgres
====

````
ansible-playbook deploy.yml --tags postgres
`````

Install App
====

````
ansible-playbook deploy.yml --tags app
`````

Install Gunicorn
====

````
ansible-playbook deploy.yml --tags gunicorn
`````

Install Nginx
====

````
ansible-playbook deploy.yml --tags nginx
`````

Git Pull
====

For Pulling changes on github:

````
ansible-playbook deploy.yml --tags git_pull
`````
