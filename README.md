# Installation

Install this new credrntials plugin

```
awx-python -m pip install git+https://github.com/riadhhamdi/AWX_SAAM_Plugin.git
```

Add the new created credentials to the list of credentials

```
awx-manage setup_managed_credential_types
```

Restart AWX/Ansible Tower by restarting the service / Container 
```
ansible-tower-service restart 
```


Check the full Installation Process here  [Show as video](https://youtu.be/2iGpTgmuYbse "Installing new credentials plugin")



