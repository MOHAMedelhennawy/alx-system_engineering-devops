$packages = ['vim', 'git', 'curl']

package { $packages:
    ensure => 'isntalled'
}
