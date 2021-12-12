import pytesseract
import PIL.Image
import re
import datefinder

if __name__ == '__main__':

    text = pytesseract.image_to_string(PIL.Image.open("OCRChallenge.png"))
print('DATES: ')
dates = datefinder.find_dates(text)
for match in dates:
    print(match)

print('_____________________')

print('ROOM NAMES: ')
room_name = re.findall(r'R[a-z]+:\s[a-zA-Z]+', text)
for rooms in room_name:
    print(rooms)
print('_____________________')

print('RATES: ')
rates = re.findall(r'\$\d+', text)
for rate in rates:
    print(rate)
print('_____________________')

print('NAMES: ')
last_first = re.findall(r'Al\s[a-zA-Z]+.\s[a-zA-Z]+', text)
for names in last_first:
    print(names)
print('_____________________')

print('EMAILS: ')
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
for email in emails:
    print(email)

