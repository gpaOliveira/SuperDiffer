# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  config.vm.box = "ubuntu/trusty32"

  # Disable automatic box update checking. 
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine.
  config.vm.network "forwarded_port", guest: 8080, host: 8080

  config.vm.provision :shell, :path => "bootstrap.sh"
  
  # Share an additional folder to the guest VM.
  config.vm.synced_folder ".", "/home/vagrant/"
  
  # Use it for debugging the VM in a visual mode, if needed
  #config.vm.provider :virtualbox do |vb|
  # vb.gui = true;
  #end
end
