initStreams = int(input())
streams = []
for _ in range(initStreams):
    streams.append(int(input()))

operations = []

instruction = 0
while instruction != 77:
    instruction = int(input())
    if instruction == 99:
        numSplit = int(input())-1
        percentSplit = float(input())
        splitStream1 = streams[numSplit] * (percentSplit/100)
        splitStream2 = streams[numSplit] * (1-(percentSplit/100))
        streams[numSplit] = splitStream1
        streams.insert(numSplit+1, splitStream2)
    elif instruction == 88:
        numJoin = int(input())-1
        joinStream1 = streams[numJoin]
        joinStream2 = streams[numJoin+1]
        streams[numJoin] = joinStream1 + joinStream2
        streams.pop(numJoin+1)

strStream = ''

for i in streams:
    strStream += str(int(i))
    strStream += ' '

print(strStream)