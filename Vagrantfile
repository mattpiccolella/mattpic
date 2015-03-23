# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # Use an Ubuntu 12.04 64-bit VirtualBox image
  config.vm.box = "precise64"
  config.vm.box_url = "http://cloud-images.ubuntu.com/vagrant/precise/current/precise-server-cloudimg-amd64-vagrant-disk1.box"

  config.vm.network "private_network", type: "dhcp"
  # Access port 8000 via localhost:8000
  config.vm.network :forwarded_port, guest: 8005, host: 8005

  # SSH Key Forwarding
  config.ssh.forward_agent = true

  config.vm.provision "shell", path: "config/provision.sh"
end