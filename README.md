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


# Creating Lookup Secret 

The lookup secret will be the link between the third-party tool providing the secret and the credentials that will be used to connect to the server. 
For example, if you need to authenticate to the external tool you may provide a token of a username/password to get access to the secrets. 


# Creating the server Credentials based on the lookup Secret 
In this part we are going to create a new machine credentials based on the lookup plugin, So the username and the password are not static values stored in the credentials, but they will be looked up by our credentials plugin. 

**Note**: We are using a very simple plugin returning static values (username=riadh and password=redhat) check the code below. In real production environment the lookup is done based on other crtiterias.


          ```
          if token != 'VALID':
            raise ValueError('Invalid token!')

          value = {
            'username': 'riadh',
            'email': 'rhamdi@redhat.com',
            'password': 'redhat'
          }

          ```
