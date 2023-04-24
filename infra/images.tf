resource "docker_image" "img_python" {
  name = "img_python"
  keep_locally = true
  build {
    context = "../scripts/general_scripts/zip"
    dockerfile = "Dockerfile"
  }
}

resource "docker_image" "img_python_trino" {
  name = "img_python_trino"
  keep_locally = true
  build {
    context = "../scripts/general_scripts/trino"
    dockerfile = "Dockerfile"
  }
}

resource "docker_image" "img_mysql" {
  name = "mysql:8.0-debian"
  keep_locally = true
}

resource "docker_image" "img_mongo" {
  name = "mongo:6.0.4"
  keep_locally = true
}

resource "docker_image" "img_starbust" {
  name = "starburstdata/starburst-enterprise:380-e.17"
  keep_locally = true
}