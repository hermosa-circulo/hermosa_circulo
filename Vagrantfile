# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

    config.vm.box = "centos7"

        config.vm.network "private_network", ip: "192.168.108.108", virtualbox__intnet: "internal"
    config.vm.provider "virtualbox" do |vb|
        vb.memory = "1024"
    end
    config.vm.provision "shell", inline: <<-SHELL
        sudo localectl set-locale LANG=ja_JP.UTF-8
    SHELL
    config.vm.provision "ansible" do |ansible|
        ansible.playbook = "ansible-playbook/deploy.yml"
    end
end
