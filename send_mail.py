import smtplib


def send_email(msg):
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as conn:
        conn.starttls()
        conn.login(user='anuj.nits2@gmail.com', password='wzgpcyhchhcdoret')
        conn.sendmail(from_addr='anuj.nits2@gmail.com', to_addrs='anuj.nits@gmail.com', msg=msg)
