import emails

# Prepare the email
message = emails.html(
    html="<h1>Hello World. </h1><strong>Messages here.</strong>",
    subject="Subject here.",
    mail_from="hello@source.mail",
)

# Send the email
r = message.send(
    to="someone@dest.mail", 
    smtp={
        "host": "email-smtp.us-west-2.amazonaws.com", 
        "port": 587, 
        "timeout": 5,
        "user": "SMTP-Account",
        "password": "SMTP-Password",
        "tls": True,
    },
)

# Check if the email was properly sent
assert r.status_code == 250
