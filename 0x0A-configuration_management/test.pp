$package = "neovim"
exec { 'update':
    command => '/usr/bin/apt-get update',
}

package { $package:
    ensure  => 'installed',
    require => Exec['update'],
}
