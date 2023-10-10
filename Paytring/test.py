import os
os.environ['key'] = "test_key"
os.environ['secret'] = "test_secret"
from paytring.client import Subscription
subscription = Subscription()

receipt_id = "PLAN123456789"
payment_info = {
    "amount" : "100",
    "currency" : "INR",
}
plan_info = {
    "title": "Daily 1 rupee plan",
    "description": "test plan",
    "frequency": "1",
    "cycle": "12",
}
notes = {
    "udf1" : "udf1",
    "udf2" : "udf2",
    "udf3" : "udf3",
}

response  = subscription.create_plan(
    receipt_id,
    payment_info,
    plan_info,
    notes
)

print(response)