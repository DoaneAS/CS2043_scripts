import socket
import sys
import time
import random

# # Create a UDP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server_port = int(sys.argv[1])
# print server_port
# client_port = int(sys.argv[2])
# # Bind the socket to the port
# #sever address listens for guess and sends response back

# #server_address = ('localhost', 4000)
# server_address = ('localhost', server_port)
# print server_address
# client_address = ('localhost', client_port)
# #print >>sys.stderr, 'starting up on %s port %s' % server_address
# #sock.bind(server_address)

# #listen

# #client server sends guess and listens for respnse




# def eval_guess(client_guess):
#     if int(client_guess) <= 20:
#         resp = 'GUESS LOW'
#     else:
#         resp = "CORRECT"
#     return resp

def server_listen(server_address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(server_address)
    print >>sys.stderr, '\nSERVER LISTENING'
    loop = 0
    while loop != 1:
        print >>sys.stderr, '\nwaiting to receive guess'
        client_guess, address = sock.recvfrom(4096)
        print >>sys.stderr, '\nclient guessed "%s"' % client_guess
        #resp = eval_guess(client_guess)
        guesses = 0
        res = moo(client_guess, guesses)
        guesses = str(res[1])
        bulls = str(res[2])
        cows = str(res[3])
        mess = res[4]
        print >>sys.stderr, ' The guess had %s Bulls\n  %s Cows' % (bulls, cows)
        resp = ' The guess had %s Bulls\n  %s Cows %s' % (bulls, cows, mess)
        sent = sock.sendto(resp, address)
        print >>sys.stderr, '\nsent response to clients'
        #time.sleep(1)
        loop += 1
        sock.close()
    return res

def  client_guess(my_guess):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    my_guess_resp = None
    time.sleep(1)
    try:
        # Send data
        time.sleep(1)
        print >>sys.stderr, 'sending my guess "%s"' % my_guess
        sent = sock.sendto(my_guess, client_address)

        # Receive response
        print >>sys.stderr, 'waiting to receive response for my guess'
        #while my_guess_resp != "CORRECT":
        my_guess_resp, server = sock.recvfrom(4096)
        print >>sys.stderr, 'received response "%s"' % my_guess_resp
    #modify guess and close
    finally:
        #if my_guess_resp != "CORRECT":
         #   n = int(my_guess) +1
          #  my_guess = str(n)
       # print >>sys.stderr, 'new guess will be "%s" \nclosing socket' % my_guess
        time.sleep(1)
    sock.close()
    return my_guess, my_guess_resp

###moo program##
def moo(guess, guesses):
        guesses += 1
        while True:
            # get a good guess
            #guess = raw_input('\nNext guess [%i]: ' % guesses).strip()
            if len(guess) == size and \
               all(char in digits for char in guess) \
               and len(set(guess)) == size:
                break
            mess = "Problem, try again. You need to enter %i unique digits from 1 to 9" % size
            res = [0,0,0,0,mess]
            return res
        if guess == chosen:
            mess = '\n Congratulations you guessed correctly in %s attempts' % str(guesses)
        else:
            mess = "\n"
        bulls = cows = 0
        for i in range(size):
            if guess[i] == chosen[i]:
                bulls += 1
            elif guess[i] in chosen:
                cows += 1
            else:
                break
        print >>sys.stderr, '  %i Bulls\n  %i Cows' % (bulls, cows)
        res = [guess, guesses, bulls, cows, mess]
        return res

# Create a UDP socket
#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_port = int(sys.argv[1])
print server_port
client_port = int(sys.argv[2])
# Bind the socket to the port
#sever address listens for guess and sends response back

#server_address = ('localhost', 4000)
server_address = ('localhost', server_port)


client_address = ('localhost', client_port)
print >>sys.stderr, 'server is "%s"' % str(server_address)
print >>sys.stderr, 'client is "%s"' % str(client_address)

my_guess = str(0)
client_resp = None
resp = None

my_guess_resp = None
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# while resp != "CORRECT":
#     if server_port < client_port:
#         resp = server_listen(server_address)
#     client_resp = client_guess(my_guess)
#     my_guess = client_resp[0]
#     if client_resp[1] != "CORRECT":
#         resp = server_listen(server_address)
#     else:
#         resp = "CORRECT"
#         print >>sys.stderr, "corect wow"
guesses = 0
digits = '123456789'
size = 4
#chosen = ''.join(random.sample(digits,size))
chosen = "1234"
#

#my_guess = raw_input('\nNext guess [%i]: ' % guesses).strip()


# #for port 4000 4001
# if server_port < client_port:
#     while resp != "CORRECT":
#         resp = server_listen(server_address)
#         time.sleep(2)
#         client_resp = client_guess(my_guess)
#         n = int(my_guess) +1
#         my_guess = str(n)
#     resp = "CORRECT"
#     print >>sys.stderr, "corect wow"

# if server_port > client_port:
#     while resp != "CORRECT":
#         client_resp = client_guess(my_guess)
#         n = int(my_guess) +1
#         my_guess = str(n)
#         resp = server_listen(server_address)
#     resp = "CORRECT"
#     print >>sys.stderr, "corect wow"


res = [0, 0, 0, 0]
guesses = 0
#for port 4000 4001
if server_port < client_port:
    while int(res[2]) != 4:
        res = server_listen(server_address)
        time.sleep(2)
        my_guess = raw_input('\nNext guess [%i]: ' % guesses).strip()
        guesses += 1
        client_resp = client_guess(my_guess)
    resp = "CORRECT"
    print >>sys.stderr, "corect wow"

if server_port > client_port:
    while int(res[2]) != 4:
    #while res[2] != '4': #could use this instead
        my_guess = raw_input('\nNext guess [%i]: ' % guesses).strip()
        guesses += 1
        client_resp = client_guess(my_guess)
        res = server_listen(server_address)
    resp = "CORRECT"
    print >>sys.stderr, "corect wow"




