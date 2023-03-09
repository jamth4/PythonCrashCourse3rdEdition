def send_messages(text, sent):
    while text:
        text_message = text.pop()
        print(f"sending text message: {text_message}")
        sent.append(text_message)
    
messages = ['sos', 'lmfao', 'rtfm']
sent_messages = []

send_messages(messages, sent_messages)

print(messages)
print(sent_messages)