##I just want to finish this task
exec { 'nginx':
    command  => 'sudo apt-get -y install nginx',
    provider => shell,
    before   => Exec['file']
}

exec { 'installing':
    command  => 'sudo apt-get -y update; sudo apt-get -y install nginx',
    provider => shell,
    before   => Exec['nginx']
}

exec { 'file':
    command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
    provider => shell,
    before   => Exec['theCommand']
}

exec { 'theCommand':

    command     => 'sudo sed -i "s#listen 80 default_server;#listen 80 default_server;\n\\tadd_header X-Served-By $HOSTNAME;#" /etc/nginx/sites-enabled/default'
    provider    => shell,
    environment => ["HOSTNAME=${hostname}"],
    before      => Exec['finishing']
}

exec { 'finishing':
    command  => 'sudo service nginx restart',
    provider => shell
}