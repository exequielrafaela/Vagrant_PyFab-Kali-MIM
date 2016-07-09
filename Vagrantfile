# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.define "kali", primary: true do |kali|
    kali.vm.box = "hashicorp/precise64"
    kali.vm.hostname = "kali2"
    kali.vm.network "public_network", bridge: "wlan0"
    kali.vm.provider :virtualbox do |vb|
      vb.memory = 512
      vb.cpus = 1
    end
    kali.vm.provision :fabric do |fabric|
      fabric.fabfile_path = "./fabfile.py"
      fabric.tasks = ["kali", ]
    end
    #kali.ssh.username = 'root'
    #kali.ssh.password = 'vagrant'
    #kali.ssh.insert_key = 'true'
  end
end

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network :private_network, ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network :public_network

  # If true, then any SSH connections made will enable agent forwarding.
  # Default value: false
  # config.ssh.forward_agent = true

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

   # The url from where the 'config.vm.box' box will be fetched if it
   # doesn't already exist on the user's system.
   # config.vm.box_url = "http://domain.com/path/to/above.box"