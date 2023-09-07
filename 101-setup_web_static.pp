#Script to seup web servers for the deployeent of web_static

exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install Nginx'],
}

exec {'install Nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['start Nginx'],
}

exec {'start Nginx':
  provider => shell,
  command  => 'sudo service nginx start',
  before   => Exec['create test dir'],
}

exec {'create test dir':
  provider => shell,
  command  => 'sudo mkdir -p /data/web_static/releases/test/',
  before   => Exec['create shared dir'],
}

exec {'create shared dir':
  provider => shell,
  command  => 'sudo mkdir -p /data/web_static/shared/',
  before   => Exec['create index.html'],
}

exec {'create index.html':
  provider => shell,
  command  => 'echo "Just for test" | sudo tee /data/web_static/releases/test/index.html',
  before   => Exec['create sym link'],
}

exec {'create sym link':
  provider => shell,
  command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
  before   => Exec['add location'],
}

exec {'add location':
  provider => shell,
  command  => 'sudo sed -i \'38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n\' /etc/nginx/sites-enabled/default',
  before   => Exec['restart Nginx'],
}

exec {'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
  before   => File['/data/'],
}

file {'/data/':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}
