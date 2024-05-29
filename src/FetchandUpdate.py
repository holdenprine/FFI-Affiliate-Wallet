import stripe
import requests

stripe.api_key = 'api key for stripe goes here'

def track_signup_with_coupon(coupon_code):
    user_id = validate_coupon_code(coupon_code)
    if user_id:
        update_earnings(user_id, 7)
    else:
        raise ValueError("invalid coupon")

def update_earnings(user_id, amount):
    # update earnings in your database -> see how that can be done?
    user = get_user_from_database(user_id)
    user.earnings += amount
    save_user_to_database(user)

