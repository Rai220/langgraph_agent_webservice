"""This module provides example tools for web scraping and search functionality.

It includes a basic Tavily search function (as an example)

These tools are intended as free examples to get started. For production use,
consider implementing more robust and specialized tools tailored to your needs.
"""

from typing import Any, Callable, List, Optional, cast

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import InjectedToolArg
from typing_extensions import Annotated

from react_agent.configuration import Configuration

cards = {
    "3101": {"data": "VISA, баланс 150 рублей", "block": False},
    "7452": {"data": "MasterCard, баланс 1000 рублей", "block": False},
    "2463": {"data": "VISA, баланс 100 рублей", "block": False},
}

async def get_cards(
    *, config: Annotated[RunnableConfig, InjectedToolArg]
) -> Optional[list[dict[str, Any]]]:
    """Возвращает состояние банковских карт пользователя в виде dict, где ключем является id карты
    """
    # configuration = Configuration.from_runnable_config(config)
    # wrapped = TavilySearchResults(max_results=configuration.max_search_results)
    # result = await wrapped.ainvoke({"query": query})

    return cast(dict[str, Any], cards)

async def block_card(card_id: str, 
    *, config: Annotated[RunnableConfig, InjectedToolArg]
) -> str:
    """Блокирует карту пользователя по card_id
    """
    if card_id in cards:
        cards[card_id]["block"] = True
        return f"Карта {card_id} заблокирована"
    else:
        return f"Карта с {card_id} не найдена"

TOOLS: List[Callable[..., Any]] = [get_cards, get_cards]
