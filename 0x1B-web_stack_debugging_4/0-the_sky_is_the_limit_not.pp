# Here is a file to fix the webstack
exec { 'fixing the file lol':
  command => "sed -i 's/15/4096/' /etc/default/nginx",
  path    => ['/usr/local/bin', '/bin'],
}

exec { 'Dont forget to restart the web server':
    command => 'sudo service nginx restart',
    path    => ['/usr/local/bin', '/bin'],
}
