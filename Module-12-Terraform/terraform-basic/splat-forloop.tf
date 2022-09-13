terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "2.21.0"
    }
  }
}

provider "docker" {}

resource "random_string" "random" {
  count   = 2
  length  = 4
  special = false
}


resource "docker_image" "nodered_image" {
  name = "nodered/node-red:latest"
}

resource "docker_container" "nodered_contianer" {
  count = 2
  name  = join("-", ["nodered", random_string.random[count.index].result])
  image = docker_image.nodered_image.name
  ports {
    internal = 1880
    #external = 1880
  }
}


output "Container-name" {
  value       = docker_container.nodered_contianer[*].name
  description = "The name of the container"
}

output "IP-addrees-Port" {
  value       = [for i in docker_container.nodered_contianer[*] : join(":", [i.ip_address], i.ports[*]["external"])]
  description = "The IP addres of container and port of container"
}
