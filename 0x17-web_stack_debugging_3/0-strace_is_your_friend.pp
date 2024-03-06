# A Puppet manifest to fix a typo error in a file
exec { 'Fixing something':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ['/usr/local/bin', '/bin'],
}