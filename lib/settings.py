from enum import Enum
from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


DOTENV = Path.joinpath(Path(__file__).parent.parent.resolve(), ".env")


class Settings(BaseSettings):
    data_path: str = Field("/data", env="DATA_PATH")
    grb_license_file: str = Field("", env="GRB_LICENSE_FILE")
    log_level: str = Field("INFO", env="LOG_LEVEL")

    model_config = SettingsConfigDict(env_file=DOTENV)


settings = Settings()
