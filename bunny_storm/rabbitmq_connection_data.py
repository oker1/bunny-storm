from dataclasses import dataclass


@dataclass
class RabbitMQConnectionData:
    """
    Dataclass responsible for organizing RabbitMQ connection credentials and parameters.
    Allows to name connections using connection_name.
    Use uri() to get the connection URI which corresponds to the credentials and parameters given.
    """
    username: str = "guest"
    password: str = "guest"
    host: str = "localhost"
    port: int = 5672
    virtual_host: str = "/"
    connection_name: str = ""
    scheme: str = "amqp"
    ssl_options: dict = None

    def uri(self) -> str:
        """
        Creates connection URI for a RabbitMQ server with the given connection credentials.
        :return: Connection URI
        """
        vhost = "" if self.virtual_host == "/" else self.virtual_host

        query = ""
        query_list = []
        if self.connection_name:
            query_list.append(f"name={self.connection_name}")
        if self.ssl_options:
            for option, value in self.ssl_options.items():
                query_list.append(f"{option}={value}")
        if query_list:
            query = "?" + "&".join(query_list)

        return f"{self.scheme}://{self.username}:{self.password}@{self.host}:{self.port}/{vhost}{query}"
