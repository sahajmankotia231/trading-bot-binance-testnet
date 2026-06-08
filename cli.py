import argparse

from bot.orders import place_order

from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity
)

from bot.logging_config import (
    setup_logger
)

setup_logger()

parser = argparse.ArgumentParser(
    description="Trading Bot"
)

parser.add_argument(
    "--symbol",
    required=True
)

parser.add_argument(
    "--side",
    required=True
)

parser.add_argument(
    "--type",
    required=True
)

parser.add_argument(
    "--quantity",
    required=True
)

parser.add_argument(
    "--price"
)

args = parser.parse_args()

try:

    validate_side(
        args.side.upper()
    )

    validate_order_type(
        args.type.upper()
    )

    validate_quantity(
        args.quantity
    )

    if (
        args.type.upper() == "LIMIT"
        and not args.price
    ):

        raise ValueError(
            "Price required for LIMIT order"
        )

    response = place_order(
        symbol=args.symbol.upper(),
        side=args.side.upper(),
        order_type=args.type.upper(),
        quantity=args.quantity,
        price=args.price
    )

    print("\nORDER REQUEST")
    print("----------------")

    print(
        f"Symbol: {args.symbol}"
    )

    print(
        f"Side: {args.side}"
    )

    print(
        f"Type: {args.type}"
    )

    print(
        f"Quantity: {args.quantity}"
    )

    print("\nORDER RESPONSE")
    print("----------------")

    print(
        f"Order ID: "
        f"{response.get('orderId')}"
    )

    print(
        f"Status: "
        f"{response.get('status')}"
    )

    print(
        f"Executed Qty: "
        f"{response.get('executedQty')}"
    )

    print(
        f"Avg Price: "
        f"{response.get('avgPrice','N/A')}"
    )

    print(
        "\nSUCCESS: Order placed"
    )

except Exception as error:

    print(
        f"\nFAILED: {error}"
    )