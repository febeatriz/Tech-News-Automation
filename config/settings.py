import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')

class Settings:
    # Webhook
    MAKE_WEBHOOK_URL: str = os.getenv('MAKE_WEBHOOK_URL', '')

    # Scraper
    USER_AGENT: str = os.getenv("USER_AGENT", "tech-news-bot/1.0")
    REQUEST_TIMEOUT: int = int(os.getenv("REQUEST_TIMEOUT", "10"))

    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_DIR: Path = BASE_DIR / "logs"

    # Banco de dados
    DB_PATH: Path = BASE_DIR / "data" / "history.db"

    @classmethod
    def validate(cls):
        """Falha rápido se alguma variável obrigatória estiver faltando."""
        missing = []
        if not cls.MAKE_WEBHOOK_URL:
            missing.append("MAKE_WEBHOOK_URL")
        if missing:
            raise EnvironmentError(
                f"Variáveis obrigatórias ausentes no .env: {', '.join(missing)}"
            )
        

settings = Settings()