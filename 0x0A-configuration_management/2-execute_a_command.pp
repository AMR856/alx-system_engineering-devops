# The last script
exec { 'KillingProcess':
    command  => 'pkill killmenow',
    provider => 'shell',
}