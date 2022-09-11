terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "2.21.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "nodered_image" {
  name = "nodered/node-red:latest"
}

resource "docker_container" "nodered_contianer" {
  name  = "nodered"
  image = docker_image.nodered_image.name
  ports {
    internal = 1880
    external = 1880
  }
}

output "IP-Address" {
  value       = docker_container.nodered_contianer.ip_address
  description = "The IP address of the container"
}

output "Container-name" {
  value       = docker_container.nodered_contianer.name
  description = "The name of the container"
}

output "IP-addrees-Port" {
  value       = join(":", [docker_container.nodered_contianer.ip_address, docker_container.nodered_contianer.ports[0].external])
  description = "The IP addres of container and port of container"
}
