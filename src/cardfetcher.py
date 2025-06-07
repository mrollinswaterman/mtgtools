import json
import time

import requests


def fetch(input: list[str], mode):
    from cardparser import Card, create_df_card

    fetched_cards = []

    for name in input:
        search_query = name
        response = requests.get(
            f"https://api.scryfall.com/cards/named?exact={search_query}"
        )
        response = response.content.decode("utf8")
        data = json.loads(response)
        if "card_faces" in data:
            fetched_cards.extend(create_df_card(data, mode))
        else:
            fetched_cards.append(Card(data, mode))

        # delay to not surpass scryfall's rate limits
        time.sleep(0.100)

    return fetched_cards
