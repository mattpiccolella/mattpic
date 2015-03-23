#/bin/bash

echo "Updating system"
apt-get -qq update

echo "Installing Git"
apt-get install -y  git-core
apt-get install -y  git

echo "Installing Pip"
apt-get install -y  python
apt-get install -y  python-dev
apt-get install -y  python-pip

echo "Installing Vim"
apt-get install -y  vim

echo "Installing SASS"
gem install sass

echo "Installing requirements.txt"
pip install -r /vagrant/config/requirements.txt
