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

exec { 'redirecting':
    command => 'sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:www.facebook.com permanent;/" /etc/nginx/sites-available/default',
    provider => shell
}

exec { 'finishing':
    command => 'sudo service nginx restart',
    provider => shell
}