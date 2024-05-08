#puppet manifest to fix apache 500 error

class apache_config {
  file { '/etc/httpd/conf/httpd.cong':
    ensure  => file,
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
    source  => 'puppet:///modules/apache_configuration/httpd.conf',
    require => Package['httpd'],
    notify  => Service['httpd'],
  }
  service { 'httpd':
    ensure  => running,
    enable  => true,
  }
}
include apache_config
