exec { 'fixing the file lol':
  command => "sed -i 's/15/4096/' /etc/default/nginx",
  path    => ['/usr/local/bin', '/bin'],
}

exec { "Don't forget to restart the web server":
    command => 'sudo service nginx restart',
    path    => ['/usr/local/bin', '/bin'],
}
