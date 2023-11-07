from sqlalchemy import create_engine, text


class DatabaseInfo:
    def __init__(self, user, password, host, port, name):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.name = name
        self.engine = None
        self.__connection = None

    def __build_connection_string(self):
        return f"mysql+mysqlconnector://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"

    def connect(self):
        self.engine = create_engine(self.__build_connection_string())
        self.__connection = self.engine.connect()
        return self

    def disconnect(self):
        self.__connection.close()
        return self

    def execute(self, query):
        self.__connection.execute(text(query))
        return self
