$file_path = '/tmp/school'

file { $file_path:
    mode => '0744',
    owner => 'www-data',
    group => 'www-data',
    content => 'I love Puppet'
}
