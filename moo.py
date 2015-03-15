#! /usr/bin/env python

import socket
import sys
import time
import random



DIGITS = 6
PINS = 4

RAND = False

def server_listen(server_address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(server_address)
    loop = 0
    while loop != 1:
        print >>sys.stderr, '\nwaiting to receive guess...'
        client_guess, address = sock.recvfrom(4096)
        print >>sys.stderr, '\nclient guessed "%s"' % client_guess
        guesses = 0
        y = ''.join([str(i) for i in client_guess])
        z = tuple([int(i) for i in y])
        res = moo(answer, z)
        bulls = str(res[1][0])
        cows = str(res[1][1])
        print >>sys.stderr, ' The guess had %s Bulls and %s Cows, sending opponent the resutl!\n' % (
            bulls, cows)
        resp = '%s %s' % (bulls, cows)
        sent = sock.sendto(resp, address)
        loop += 1
        sock.close()
    return res


def client_guess(guess):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    my_guess_resp = None
    time.sleep(0.1)
    try:
        time.sleep(0.1)
        guess_2send = ''.join([str(i) for i in guess])
        sent = sock.sendto(guess_2send, client_address)
        print >>sys.stderr, 'waiting to receive response for my guess "%s"...' % guess_2send
        my_guess_resp, server = sock.recvfrom(4096)
        bulls = my_guess_resp[0]
        cows = my_guess_resp[2]
        print >>sys.stderr, 'my guess had %s bulls and %s cows ' % (bulls, cows)
    finally:
        time.sleep(0.1)
    sock.close()
    client_resp = guess, my_guess_resp
    bulls = int(client_resp[1][0])
    cows = int(client_resp[1][2])
    guess = tuple([int(i) for i in client_resp[0]])
    return (guess, (bulls, cows))


def moo(answer, guess):
    bulls = cows = 0
    for i in range(size):
        if guess[i] == answer[i]:
            bulls += 1
        elif guess[i] in answer:
            cows += 1
    res = (guess, (bulls, cows))
    return res
import argparse
import random
import sys


def allPatterns():
    """Generator function to yield all possible color combinations"""
    cur = [0] * PINS
    while True:
        yield tuple(cur)
        for i in range(PINS):
            cur[i] += 1
            if cur[i] < DIGITS:
                break
            cur[i] = 0
            if i == PINS - 1:
                return


def check(answer, probe):
    """Given an answer and a guess, return a score of (red, white)"""
    acolcnt = [0] * DIGITS
    pcolcnt = [0] * DIGITS

    red = 0
    for (a, p) in zip(answer, probe):
        if a == p:
            red = red + 1
        else:
            acolcnt[a] += 1
            pcolcnt[p] += 1
    white = 0
    for a, p in zip(acolcnt, pcolcnt):
        white += min(a, p)
    return (red, white)


def unique(seq, keepstr=True):
    t = type(seq)
    if t in (str, unicode):
        t = (list, ''.join)[bool(keepstr)]
    seen = []
    return t(c for c in seq if not (c in seen or seen.append(c)))


def possibleAnswers(prevRounds):
    pr = tuple(prevRounds)
    ans = (candidate for candidate in allPatterns() if all(
        (check(candidate, probe) == result for (probe, result) in pr)))
    return (candidate for candidate in ans if len(unique(candidate)) == 4)


def randomPattern():
    return tuple((random.randint(0, DIGITS - 1) for i in range(PINS)))


def chooseFirst(answers):
    guess = answers.next()
    answersCount = lambda: len(list(answers)) + 1
    return (guess, answersCount)


def chooseBest(answers):
    allAnswers = list(answers)
    bestGuess = None
    bestScore = pow(DIGITS, PINS)
    bestResults = {}
    for guess in allAnswers:
        results = {}
        for possibleAnswer in allAnswers:
            possibleResult = check(possibleAnswer, guess)
            results[possibleResult] = 1 + results.get(possibleResult, 0)
        score = max(results.values())
        if score < bestScore:
            bestGuess = guess
            bestScore = score
            bestResults = results
    return (bestGuess, lambda: len(allAnswers))


def chooseRandom(answers):
    allAnswers = list(answers)
    guess = random.choice(allAnswers)
    return (guess, lambda: len(allAnswers))


server_port = int(sys.argv[2])
client_port = int(sys.argv[3])
server_address = ('localhost', server_port)
client_address = ('localhost', client_port)
my_guess = str(0)
client_resp = None
resp = None
my_guess_resp = None
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
digits = range(10)
size = 4

res = ((0, 0, 0, 0), (0, 0))
guesses = 0

if server_port < client_port:
    if RAND == True:
        answer = random.sample(digits, size)
    else:
        ans = sys.argv[1]
        answer = [int(i) for i in ans]

    rounds = []
    while int(res[1][0]) != 4:
        res = server_listen(server_address)
        time.sleep(0.1)
        if res[1][0] == 4:
            break
        print >>sys.stderr, "computing probabilistic guess..."
        answers = possibleAnswers(rounds)
        (guess, answersCount) = chooseBest(answers)
        print >>sys.stderr, "done"
        print >>sys.stderr, 'guessing "%s"' % ''.join([str(i) for i in guess])
        guesses += 1
        client_resp = client_guess(guess)
        if client_resp[1][0] == 4:
            guess_2send = ''.join([str(i) for i in guess])
            print 'My guess "%s" was correct, I win!' % guess_2send
            break
    print >>sys.stderr, "opponent guessed corect!!"

if server_port > client_port:
    rounds = []
    if RAND == True:
        answer = random.sample(digits, size)
    else:
        ans = sys.argv[1]
        answer = [int(i) for i in ans]
    while int(res[1][0]) != 4:
        print >>sys.stderr, "computing probabilistic guess..."
        answers = possibleAnswers(rounds)
        (guess, answersCount) = chooseBest(answers)
        print >>sys.stderr, "done"
        print >>sys.stderr, 'guessing "%s"' % ''.join([str(i) for i in guess])
        guesses += 1
        client_resp = client_guess(guess)
        if client_resp[1][0] == 4:
            guess_2send = ''.join([str(i) for i in guess])
            print 'My guess "%s" was correct, I win!' % guess_2send
            break
        rounds.append(client_resp)
        res = server_listen(server_address)
        if res[1][0] == 4:
            print >>sys.stderr, "opponent guessed corect!!"
            break
