codes = {'A' : 'z', 'a' : 'Z', 'B' : 'y', 'b' : 'Y', 'C' : 'x', 'c' : 'X', 'D' : 'w', 'd' : 'W', 'E' : 'v', 'e' : 'V', 'F' : 'u', 'f' : 'U',
'G' : 't', 'g' : 'T', 'H' : 's', 'h':'S', 'I':'r','i': 'R', 'J' : 'q', 'j' : 'Q', 'K' : 'p', 'k' : 'P', 'L' : 'o', 'l' : 'O', 'M' : 'n', 'm' : 'N'
, 'N' : 'a', 'n' : 'A', 'O' : 'b', 'o' : 'B', 'P' : 'c', 'p' : 'C', 'Q' : 'd', 'q' : 'D', 'R' : 'e', 'r' : 'E', 'S' : 'f', 's' : 'F',
'T' : 'm', 't' : 'M', 'U' : 'l', 'u' : 'L', 'V' : 'k', 'v' : 'K', 'W' : 'j', 'w' : 'J', 'X' : 'i', 'x' : 'I', 'Y' : 'h', 'y' : 'H',
'Z' : 'g', 'z' : 'G'}

infile = open('info_security.txt','r')
outfile = open('encrypted.txt', 'w')


data=infile.read()

for key,value in codes.items():
    search= key
    replace = value

    data = data.replace(search,replace)

outfile.write(data)