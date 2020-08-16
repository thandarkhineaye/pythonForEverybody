text = "X-DSPAM-Confidence:    0.8475"
strnum = text.find('0')

print(float(text[strnum:]))