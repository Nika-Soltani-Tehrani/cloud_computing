import requests


def send_email(email, post_id, status):
    if status:
        text = f"Your ad with id {post_id} has been accepted!"
    else:
        text = f"Your ad with id {post_id} has been rejected!"
    return requests.post(
        f"https://api.mailgun.net/v3/sandboxc305dae9f952473683fd46513fd5a5f3.mailgun.org/messages",
        auth=("api", "028fd61580bd19c163c47f2a4a3df341-48c092ba-e87ad38c"),
        data={"from": "<mailgun@sandboxc305dae9f952473683fd46513fd5a5f3.mailgun.org>",
              "to": [email],
              "subject": "Post Submission Status",
              "text": text},
        verify=False
    )


status = True
post_id = 123
email_address = "nsoltanitehrani@gmail.com"
response = send_email(email_address, post_id, status)
print(response.json()['id'])
