import imapclient
import pprint



imapobj=imapclient.IMAPClient('imap.gmail.com',ssl=True)



rec_email=input('enter your email')
password=(input('enter your password'))
imapobj.login(rec_email,password)

# print all folders
pprint.pprint(imapobj.list_folders())

# selector_folders
imapobj.select_folder('INBOX',readonly=True)

# search in folders


UIDs = imapobj.search(['ALL'])

print(UIDs)

rawMessages = imapobj.fetch(UIDs, ['BODY[]'])
pprint.pprint(rawMessages)

import pyzmail

message=pyzmail.PyzMessage.factory(rawMessages[126][b'body[]'])

print(message.get_subject())
print(message.get_addresses('from'))
print(message.get_addresses('to'))

print(message.text_part.get_payload().decode(message.text_part.charset))
print(message.html_part.get_payload().decode(message.text_part.charset))

imapobj.logout()