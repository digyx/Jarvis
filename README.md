# Jarvis

Written in Python.  The engine will create a new Docker container when a change in the Git repo is detected, and then run the job in said container.

## Config Reference
```
{
    'jobs': [
        {
            'name': 'Job Name,
            'url': 'https://github.com/username/repo-name' 
        },
        {
            'name': 'Jarvis',
            'url': 'https://github.com/digyx/Jarvis'
        },
    ],
} 
```

## Yaml Reference
``` yaml
language: python
dependencies: requirements.txt

env_vars:
  - SECRETKEY: 'hello world'
  - PUBLICKEY: 'hello, world'

commands:
  - "python -m unittest -v tests/*.py"
  - "python build.py"
```
