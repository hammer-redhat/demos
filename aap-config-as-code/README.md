# Ansible Automation Platform: Configuration as Code
## Chris Hammer, Senior Architect, Financial Services - Launch Team | <img src="redhat-logo.png" style="width:100px;"/>
---
## Objectives:
- Review prerequisites for Infrastructure and Configuration as Code deployment.
    - Collections: infra.aap_utilities & ansible.controller.
    - Hosts: Provisioned and running (Bastion, Controller, Automation Hub and Database).
    - Network: Firewall rules and traffic allowed for cluster.
- Demonstrate the following Using Config As Code: 
    - Uploading the manifest/license file.
    - Create credentials to sync a project from Github and connect to hosts. 
    - Create a project and sync from Github.
    - Create an inventory to run our playbooks against.
    - Populate hosts in the newly created inventory.
    - Build a job template to run our playbook from the Github project created and synced earlier. 
---
- Lab Environment:  

| Function    | Hostname |
| :--------: | :-------: |
| Bastion:   |  bastion.lan  |
| Automation Controller:  | aap.lan  |
| Automation Hub: | pah.lan  |
| Database:  |  db.lan  |

---
```
[chrhamme@bastion aap_cac]$ tree
.
├── aap_deploy.yml
├── ansible.cfg
├── configure_aap.yml
├── files
│   ├── controller_auth
│   ├── id_rsa
│   └── manifest_automation-controller_20240218T001941Z.zip
├── inventory_vars
│   └── variables.yml
└── reset_aap_ui.yml

2 directories, 8 files
```