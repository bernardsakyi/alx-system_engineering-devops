# automating nginx to return an HTTP Response HEADER X-Served-By
exec { 'update_apt_cache':
  command => '/usr/bin/apt-get update',
  path    => '/usr/bin:/usr/sbin:/bin',
}

package { 'nginx':
  ensure => installed,
}

$hostname = $facts['hostname']

$file_content = "add_header X-Served-By ${hostname};\n"

file_line { 'add_x_server_by_header':
  path => '/etc/nginx/sites-available/default',
  line => $file_content,
  match => '^\s*server_name\s',
}

service { 'nginx':
  ensure => running,
  enable => true,
  subscribe => File_line['add_x_server_by_header'],
}

