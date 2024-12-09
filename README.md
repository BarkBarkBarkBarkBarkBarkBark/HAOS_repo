# Install Home Assistant
follow directions : https://aeotec.freshdesk.com/support/solutions/articles/6000267254-setup-home-assistant-with-windows-and-virtualbox
Use Bridged Adaptor en0, and recieve a local ip address

Dashboard at http://homeassistant.(local):8123/hacs/dashboard

Sign Into Home Assistant Cloud
Install "Add-on" File Editor
Install "Integration" OpenAI Conversation

# HAOS_repo

HAOS_VM_repo is a clone of a python_scripts repo inside the home assistant directory, which is hosted on a virtual machine

Launch HomeAssistantVM from VirtualBox

Directory is exposed by samba with smb://192.168.1.156

When accessing from local host, the repo is found at /Volumes/config/python_scripts/HAOS_repo

## Managing the Repo

### IDE (PyCharm)

#### Git Clone
Open HAOS_VM_repo at /Users/marco/PycharmProjects/HAOS_VM_repo

git clone https://github.com/BarkBarkBarkBarkBarkBarkBark/HAOS_repo.git

username :Bark...Bark
password : GitHub PAT

#### Make Changes in PyCharm
Make changes, push, and commit

Github desktop, fetch origin, pull origin

### GitHUb Desktop 

Expose directory using Samba, instructions above

Open HAOS_Repo

Edit in dashboard : http://homeassistant.local:8123/hassio/ingress/core_configurator

