from apscheduler.schedulers.blocking import BlockingScheduler
import stripe

def get_all_users():
    # fetch all users from the db
    return users

def create_transfer(user_id, amount):
    user = get_user_from_database(users_id)
    stripe.Transfer.create(
        amount= int(amount * 100),
        currency= "usd",
        destination= user.stripe_account_id
    )

def payout_job():
    users = get_all_users()
    for user in users:
        if user.earnings > 0:
            create_transfer(user.user_id, user.earnings)
            #  Reset earnings after payout
            user.earnings = 0
            save_user_to_database(user)
scheduler = BlockingScheduler()
scheduler.add_job(payout_job, 'interval', weeks=1)
scheduler.start() 