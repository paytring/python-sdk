import os
os.environ['key'] = "prod_key"
os.environ['secret'] = "prod_secret"
from paytring.client import Subscription
subscription = Subscription()

receipt_id = "sub123456789"
plan_id = "PLAN123456789"
callback_url = "https://httpbin.org/post"
customer_info = {
    "cname" : "Ramsharan",
    "email" : "ramsharan@paytring.com",
    "phone" : "7737291210",
}

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
billing_info = {
    "firstname" : "John",
    "lastname" : "Doe",
    "phone" : "09999999999",
    "line1" : "Address Line 1",
    "line2" : "Address Line 2",
    "city" : "Gurugram",
    "state" : "Haryana",
    "country" : "India",
    "zipcode" : "122001"
}
shipping_info = {
    "firstname" : "John",
    "lastname" : "Doe",
    "phone" : "09999999999",
    "line1" : "Address Line 1",
    "line2" : "Address Line 2",
    "city" : "Gurugram",
    "state" : "Haryana",
    "country" : "India",
    "zipcode" : "122001"
}
notes = {
    "udf1" : "udf1",
    "udf2" : "udf2",
    "udf3" : "udf3",
}

response  = subscription.create_plan(
    plan_id,
    payment_info,
    plan_info,
    notes
)

# response  = subscription.fetch_plan(
#     "552410243112370870"
# )

# response  = subscription.fetch_plan_by_receipt_id(
#     "PLAN123456789"
# )

# response  = subscription.create_subscription(
#     receipt_id,
#     "552410243112370870",
#     callback_url,
#     customer_info,
#     billing_info,
#     shipping_info,
#     notes,
# )

# response  = subscription.fetch_subscription(
#     "552423987880135115",
# )

# response  = subscription.fetch_subscription_by_receipt_id(
#     "sub123456789",
# )

print(response)