# Road To Kubernetes
Installed nginx on a remote ubuntu based server by running the commands: 
```bash
sudo apt update
sudo apt install nginx

```
Wrote a custom html template to the path /var/www/html/index.html by removing the default nginx welcome page by running:
```bash
sudo rm /var/www/html/nginx-debian.html
sudo tee > var/www/html/index.html <<EOF
<!DOCTYPE html>
<html>
    <head>
      <title>Hello world</title>
    </head>
    <body>
      <h1>Hello World!</h1>
      <p1>We're coming soon!</p1>
    </body>
</html>
EOF
```

## Bare repository 
A bare repository is repo with no actual diretory to store the code.The code is stored in a clone of the bare repo.
Initialize bare repo by running -> First create a directory 
```bash
mkdir -p /var/repos/roadtok8s/py.git
git init --bare
git symbolic-ref HEAD refs/heads/main

```











