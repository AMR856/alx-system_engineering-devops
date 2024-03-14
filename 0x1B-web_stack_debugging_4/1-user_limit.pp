# Here is a file to fix the user problems
exec { 'fixing the hard files':
  command => "sed -i '/holberton hard/s/5/50000/' /etc/security/limits.conf",
  path    => ['/usr/local/bin', '/bin'],
}

exec { 'fixing the soft files':
    command => "sed -i '/holberton soft/s/4/50000/' /etc/security/limits.conf",
    path    => ['/usr/local/bin', '/bin'],
}
