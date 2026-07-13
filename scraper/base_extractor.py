from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Article:
    title: str
    url: str
    source: str
    published_at: datetime | None = None
    content: str | None = None   # preenchido só na etapa de extração de conteúdo
    summary: str | None = None   # preenchido na etapa de resumo


class BaseExtractor(ABC):
    """Toda fonte de notícia (RSS ou scraping) implementa esta interface."""

    source_name: str = "unknown"

    @abstractmethod
    def fetch_list(self) -> list[Article]:
        """
        Retorna a lista de artigos disponíveis na fonte,
        SEM o conteúdo completo (só title, url, published_at).
        """
        raise NotImplementedError

    @abstractmethod
    def fetch_content(self, article: Article) -> Article:
        """
        Recebe um Article já filtrado (não duplicado) e
        preenche o campo `content` com o texto completo.
        """
        raise NotImplementedError