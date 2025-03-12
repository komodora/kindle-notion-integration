import requests
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    NOTION_API_KEY: str


settings = Settings()  # type: ignore


class NotionClient:
    NOTION_VERSION = "2022-06-28"

    def __init__(self) -> None:
        self.api_key = settings.NOTION_API_KEY

    def append_block_children(self, page_id: str, blocks: list):
        url = f"https://api.notion.com/v1/blocks/{page_id}/children"
        headers = {
            "Notion-Version": self.NOTION_VERSION,
            "Authorization": f"Bearer {self.api_key}",
        }
        payload = {"children": blocks}
        return requests.patch(url, headers=headers, json=payload)

    def retrieve_block_children(self, page_id: str):
        url = f"https://api.notion.com/v1/blocks/{page_id}/children"
        headers = {
            "Notion-Version": self.NOTION_VERSION,
            "Authorization": f"Bearer {self.api_key}",
        }
        return requests.get(url, headers=headers)


def define_bulleted_list_item(text: str):
    bulleted_list_item = {
        "object": "block",
        "type": "bulleted_list_item",
        "bulleted_list_item": {
            "rich_text": [{"type": "text", "text": {"content": text}}]
        },
    }
    return bulleted_list_item


def define_paragraph(text: str):
    paragraph = {
        "object": "block",
        "type": "paragraph",
        "paragraph": {"rich_text": [{"type": "text", "text": {"content": text}}]},
    }
    return paragraph
