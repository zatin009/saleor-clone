from django.utils.translation import pgettext_lazy


class ShippingMethodType:
    PRICE_BASED = "price"
    WEIGHT_BASED = "weight"
    PERCENTAGE_BASED = "percentage"

    CHOICES = [
        (PRICE_BASED, pgettext_lazy("Type of shipping", "Price Based Shipping")),
        (WEIGHT_BASED, pgettext_lazy("Type of shipping", "Weight Based Shipping")),
        (PERCENTAGE_BASED,pgettext_lazy("Type of shipping", "Percentage Based Shipping"))
    ]
