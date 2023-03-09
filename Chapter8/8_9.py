def show_messages(messages):
    """Prints messages from list"""
    for message in messages:
        print(message)

messages = ['sos', 'lmfao', 'rtfm']

list_message = show_messages(messages)
print(list_message)
