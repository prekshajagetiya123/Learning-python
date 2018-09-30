names = ["Preksha", "Shikhar", "Shipra", "Aditya" ]
amount = ["34.65","211", "322", "433"]

msg = """HI {name}!

Thank you for joining us for the event on {date}!
we had a lovely conversation with you and it was great listening to your experiences and work.

Your incredible down to earth behaviour amazed everyone.

Thank you for being there. we'll catch you at the fest again!

Team EDC!
"""

def make_msg(make_name, make_amount):
    messages = []
    if len(names)== len(amount):
        i = 0;
        for name in names:
            new_msg = msg.format(
                name = name,
                date = '29 aug, 2018')

            print(new_msg)

make_msg(names, amount)