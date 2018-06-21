import sys
import re
sentence = list()
sentences = list()
validsentence = True
unvalid = 0


with open(sys.argv[1],"r") as f:
    for idx, line in enumerate(f):
        if line in ('[\n'):
            pass
        else:
            if line == '{\n':
                if sentence:
                    if validsentence:
                        sentences.append(sentence)
                    validsentence = True
                sentence = [line]
            elif "tokenid" in line and validsentence:
                token_no_pat = re.search('\d+',line)
                no = token_no_pat.group()
                if int(no) > 500:
                    unvalid += 1
                    validsentence = False
                sentence.append(line)
            else:
                sentence.append(line)
        if idx % 1000000 == 1:
            print('Processed 1 000 000 lines...')

if validsentence:
    sentences.append(sentence)

print('{} too long sentences found!'.format(unvalid))

lines = ""
print('joining sentences...')
for idx, sentence in enumerate(sentences):
    lines += ''.join(sentence)
    if idx % 1000 == 1:
        print('Processed {}/{}'.format(idx, len(sentences)),end='\r')

print('writing...')
with open(sys.argv[1] + ".cleaned","w") as f:
    f.write("[\n" + lines)


