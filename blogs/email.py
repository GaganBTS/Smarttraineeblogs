import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
def addsubscriber(name,email):
 try:
  client = MailchimpMarketing.Client()
  client.set_config({
    "api_key": "74176a99950479f3bfa6b22fd51c2cb7-us8",
    "server": "us8"
  })

  response = client.lists.add_list_member("ee9e4aaad9", {"email_address": email, "status": "subscribed","email_type":"text","merge_fields":{"FNAME":name}})
  
 except ApiClientError as error:
  pass