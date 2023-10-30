from pydantic_settings import BaseSettings


class ServerSettings(BaseSettings):
    
    host: str
    port: int
    

    class Config:
        env_prefix = "SERVER_"
