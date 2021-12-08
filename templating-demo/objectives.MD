# Ansible: Template Module
## Chris Hammer, Senior Consultant | <img src="redhat-logo.png" style="width:100px;"/>
---


## Objectives:
##    1: ansible-doc template
    - supported options
    - jinja2 syntax
        
## Directory Structure (preference)
        testfordemo/
        ├── handlers
        │   └── main.yml (If services need restarted)
        ├── tasks
        │   └── main.yml (tasks file to run)
        ├── templates
        │   └── test_template.j2 (templates called in task file)
        └── vars (any variables used that need to be declared.)
        │   └── vars_file.yml


## 2: Benefits of Templating
        - Replace lineinfile playbooks
        - idempotency, jobs (Ansible Tower),  

## 3: /etc/hosts Template
        - demo

## 4: /etc/resolv.conf Template
        - demo
