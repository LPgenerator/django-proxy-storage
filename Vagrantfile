# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "http://files.vagrantup.com/precise64.box"
  config.vm.provision :shell, path: "bootstrap.sh"
  config.vm.network "private_network", type: "dhcp"
  config.vm.synced_folder ".", "/vagrant", type: "nfs"
  config.vm.provider "virtualbox" do |v|
     v.customize ["modifyvm", :id, "--memory", "1536"]
  end
end
