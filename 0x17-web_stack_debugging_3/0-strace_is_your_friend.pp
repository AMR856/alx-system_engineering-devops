# A file that fixes that stack that has a typo error
exec { 'Hi I'm fixing something':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path => '/usr/local/bin/:/bin/'
}
