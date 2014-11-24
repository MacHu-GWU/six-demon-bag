import StringIO

s = StringIO.StringIO()
s.write('abc\ndef\nhij')

# for line in s:
#     print line
s.seek(0)
