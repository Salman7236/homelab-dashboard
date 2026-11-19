import docker


def main() -> None:
    client = docker.from_env()
    container_list = client.containers.list(all=True)
    for container in container_list:
        print(container.short_id, container.name, container.status)
