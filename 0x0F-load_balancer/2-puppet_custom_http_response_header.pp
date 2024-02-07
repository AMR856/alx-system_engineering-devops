i## I just want to finish this task
package { 'nginx':
    ensure => 'present'
}

exec { 'installing':
    command => 'sudo apt-get -y update; sudo apt-get -y install nginx',
    provider => shell
}

exec { 'file':
    command => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
    provider => shell
}

exec { 'theCommand':
    command => sudo sed -i "s#listen 80 default_server;#listen 80 default_server;\n\\tadd_header X-Served-By $HOSTNAME;#" /etc/nginx/sites-enabled/default
    provider => shell

}

exec { 'finishing':
    command => 'sudo service nginx restart',
    provider => shell
}