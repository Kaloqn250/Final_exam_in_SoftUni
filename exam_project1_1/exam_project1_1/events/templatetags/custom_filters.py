from django import template

register = template.Library()


@register.filter
def stars_range_filter(value):
    return range(value)


@register.filter
def empty_stars_filter(value, value1):
    return range(value - value1)


def star_rating(value, max_stars=5):
    """
    Converts a numeric rating into stars.
    :param value: The rating (e.g., 3)
    :param max_stars: The maximum number of stars (default: 5)
    :return: A string of filled and empty stars
    """
    try:
        value = int(value)
        max_stars = int(max_stars)
        filled_stars = '★' * value
        empty_stars = '☆' * (max_stars - value)
        return filled_stars + empty_stars
    except (ValueError, TypeError):
        return '☆' * max_stars



