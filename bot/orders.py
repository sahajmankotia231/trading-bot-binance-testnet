import logging

from bot.client import get_client

def place_order(
    symbol,
    side,
    order_type,
    quantity,
    price=None
):

    client = get_client()

    try:

        logging.info(
            f"REQUEST: "
            f"{symbol} "
            f"{side} "
            f"{order_type}"
        )

        if order_type == "MARKET":

            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        else:

            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logging.info(
            f"RESPONSE: {response}"
        )

        return response

    except Exception as error:

        logging.error(
            f"ERROR: {error}"
        )

        raise