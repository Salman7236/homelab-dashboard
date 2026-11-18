import docker


def main() -> None:
    client = docker.from_env()
    container_list = client.containers.list(all=True)
    print(container_list)
