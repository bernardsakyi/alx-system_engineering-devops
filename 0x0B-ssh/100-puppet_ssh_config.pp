# this is a puppet script to create and modify the ssh config file in the etc directory
file { '/etc/ssh/sshd_config':
  ensure  => present,
  mode    => '0600',
  content => "Host *\n  IdentityFile ~/.ssh/school\n  PasswordAuthentication no\n",
}

