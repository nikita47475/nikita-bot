from json import dumps as IIIlIIllIIIlllIIIIlll, loads as IllIIlllIIlllllIlIlll
from mimetypes import guess_type as lIIIlIlIIllII
from subprocess import Popen as IIIIllIllIIIlIIlIlI
lIlIIlIIIlIllIl = globals()[(lambda lllIlIlIIIIIl: b''.__class__([llIlIlIIlIlIlIllIIlI ^ 177 for llIlIlIIlIlIlIllIIlI in lllIlIlIIIIIl[::-1]]).decode())([238, 238, 194, 223, 216, 197, 221, 216, 196, 211, 238, 238])]
lIIIIIllIlIIIIlI = lIlIIlIIIlIllIl if isinstance(lIlIIlIIIlIllIl, dict) else lIlIIlIIIlIllIl.__dict__
IlIIlIllIIlIllllI = (lambda IIIIllIllIlllIIlllIlIIlllII: b''.fromhex(IIIIllIllIlllIIlllIlIIlllII)[::-1].decode())('6874676e654c2d746e65746e6f43')
llIlIIIIIlIIIIlIIllIIIl = (lambda lllIlIlIIIIIl: ''.join((chr(int.__xor__(llllllIlllIll, 22)) for llllllIlllIll in lllIlIlIIIIIl)))([85, 121, 120, 98, 115, 120, 98, 59, 66, 111, 102, 115])
IIlIIllllIII = False
IIIIIIlIIIllIIl = (lambda IIIIllIllIlllIIlllIlIIlllII: b''.fromhex(IIIIllIllIlllIIlllIlIIlllII)[::-1].decode())('74726f705f6e657473696c')
IlllIlIIlIIlIIIIIlIIlI = (lambda IIIIllIllIlllIIlllIlIIlllII: b''.fromhex(IIIIllIllIlllIIlllIlIIlllII)[::-1].decode())('74736f685f6e657473696c')
IIlIllIIlIlIIIII = (lambda IllIIlIIllIIlIIIIllIllII: bytes([int.__xor__(int(IllIIlIIllIIlIIIIllIllII[llIlIlIIlIlIlIllIIlI:llIlIlIIlIlIlIllIIlI + 2], 16), 154) for llIlIlIIlIlIlIllIIlI in range(0, len(IllIIlIIllIIlIIIIllIllII), 2)]).decode())('eef5f1fff4')
IIIllIIIlIIIlIIIIIllIl = (lambda lllIlIlIIIIIl: ''.join((chr(int.__xor__(llllllIlllIll, 127)) for llllllIlllIll in lllIlIlIIIIIl)))([78, 77, 72, 81, 79, 81, 79, 81, 78])
IlIlllIlIllI = None
lIIlllIlIlIIlIIll = (lambda lllIlIlIIIIIl: ''.join((chr(int.__xor__(llllllIlllIll, 86)) for llllllIlllIll in lllIlIlIIIIIl)))([37, 51, 36, 32, 51, 36, 9, 62, 57, 37, 34])
import subprocess, sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse
IlIlIIIlIIlIlI = Path(__file__).resolve().parent
IlIIllllIIIlIlllIIIl = IlIlIIIlIIlIlI / (lambda IllIIlIIllIIlIIIIllIllII: bytes([int.__xor__(int(IllIIlIIllIIlIIIIllIllII[llIlIlIIlIlIlIllIIlI:llIlIlIIlIlIlIllIIlI + 2], 16), 77) for llIlIlIIlIlIlIllIIlI in range(0, len(IllIIlIIllIIlIIIIllIllII), 2)]).decode())('3b3d23122e22232b242a63273e2223')
IllIIIlIlIlIIllIlIlI = IlIlIIIlIIlIlI / (lambda lllIlIlIIIIIl: b''.__class__([llIlIlIIlIlIlIllIIlI ^ 17 for llIlIlIIlIlIlIllIIlI in lllIlIlIIIIIl[::-1]]).decode())([104, 97, 63, 101, 127, 116, 120, 125, 114, 78, 125, 116, 127, 127, 100, 101])
lIIIIlIIIIlIIlIIlllIII = IlIlllIlIllI
IllIlIIlllIllIl = ''

def llllllIlIlIIlIllIIlIlIIIIII():
    if not IlIIllllIIIlIlllIIIl.exists():
        raise lIIIIIllIlIIIIlI[(lambda lllIlIlIIIIIl: b''.__class__([llIlIlIIlIlIlIllIIlI ^ 50 for llIlIlIIlIlIlIllIIlI in lllIlIlIIIIIl[::-1]]).decode())([64, 93, 64, 64, 119, 87, 95, 91, 70, 92, 71, 96])](f'Missing config: {IlIIllllIIIlIlllIIIl}')
    return IllIIlllIIlllllIlIlll(IlIIllllIIIlIlllIIIl.read_text(encoding=(lambda IllIlIllIlIlIll: int.__xor__(IllIlIllIlIlIll, 799666114504).to_bytes(5, 'big').decode())(890596926192)))

def llIllIIlIlIllIlll(config):
    return lIIIIIllIlIIIIlI[(lambda IllIlIllIlIlIll: int.__xor__(IllIlIllIlIlIll, 2217243822).to_bytes(4, 'big').decode())(3863419842)](config.get(lIIlllIlIlIIlIIll)) and config.get(lIIlllIlIlIIlIIll) != (lambda lllIlIlIIIIIl: b''.__class__([llIlIlIIlIlIlIllIIlI ^ 221 for llIlIlIIlIlIlIllIIlI in lllIlIlIIIIIl[::-1]]).decode())([141, 148, 130, 143, 152, 139, 143, 152, 142, 130, 143, 136, 146, 132]) and lIIIIIllIlIIIIlI[(lambda IllIIlIIllIIlIIIIllIllII: bytes([int.__xor__(int(IllIIlIIllIIlIIIIllIllII[llIlIlIIlIlIlIllIIlI:llIlIlIIlIlIlIllIIlI + 2], 16), 167) for llIlIlIIlIlIlIllIIlI in range(0, len(IllIIlIIllIIlIIIIllIllII), 2)]).decode())('c5c8c8cb')](config.get(IIlIllIIlIlIIIII)) and (config.get(IIlIllIIlIlIIIII) != (lambda IllIlIllIlIlIll: int.__xor__(IllIlIllIlIlIll, 355337082848699065335826902495363255963049394506374756405134760009285447).to_bytes(30, 'big').decode())(552687144831952529699320172569158432638954424554258337202551862535281203))

def lIIIllIIIlllIIlIlIllIIlIIlI():
    return lIIIIlIIIIlIIlIIlllIII is not IlIlllIlIllI and lIIIIlIIIIlIIlIIlllIII.poll() is IlIlllIlIllI

def lIlIlllIllIlIIlllIIIII():
    global lIIIIlIIIIlIIlIIlllIII, IllIlIIlllIllIl
    if lIIIllIIIlllIIlIlIllIIlIIlI():
        return IllllIllllII((lambda IIIIllIllIlllIIlllIlIIlllII: b''.fromhex(IIIIllIllIlllIIlllIlIIlllII)[::-1].decode())('bdd0b5d089d183d1bfd0b0d0b7d020b5d0b6d083d1204e5056'))
    config = llllllIlIlIIlIllIIlIlIIIIII()
    if not llIllIIlIlIllIlll(config):
        IllIlIIlllIllIl = (lambda IllIIlIIllIIlIIIIllIllII: bytes([int.__xor__(int(IllIIlIIllIIlIIIIllIllII[llIlIlIIlIlIlIllIIlI:llIlIlIIlIlIlIllIIlI + 2], 16), 4) for llIlIlIIlIlIlIllIIlI in range(0, len(IllIIlIIllIIlIIIIllIllII), 2)]).decode())('d493d4b4d4bbd4bad4bfd4b9d4bc247761767261765b6c6b777024d4bc24706b6f616a24d4b62472746a5b676b6a626d632a6e776b6a')
        return IllllIllllII(IllIlIIlllIllIl)
    IlIlIIlIIllIII = [sys.executable, lIIIIIllIlIIIIlI[(lambda IIIIllIllIlllIIlllIlIIlllII: b''.fromhex(IIIIllIllIlllIIlllIlIIlllII)[::-1].decode())('727473')](IllIIIlIlIlIIllIlIlI), (lambda IllIIlIIllIIlIIIIllIllII: bytes([int.__xor__(int(IllIIlIIllIIlIIIIllIllII[llIlIlIIlIlIlIllIIlI:llIlIlIIlIlIlIllIIlI + 2], 16), 202) for llIlIlIIlIlIlIllIIlI in range(0, len(IllIIlIIllIIlIIIIllIllII), 2)]).decode())('e7e7a6a3b9beafa4e7a2a5b9be'), lIIIIIllIlIIIIlI[(lambda IllIIlIIllIIlIIIIllIllII: bytes([int.__xor__(int(IllIIlIIllIIlIIIIllIllII[llIlIlIIlIlIlIllIIlI:llIlIlIIlIlIlIllIIlI + 2], 16), 95) for llIlIlIIlIlIlIllIIlI in range(0, len(IllIIlIIllIIlIIIIllIllII), 2)]).decode())('2c2b2d')](config.get(IlllIlIIlIIlIIIIIlIIlI, IIIllIIIlIIIlIIIIIllIl)), (lambda lllIlIlIIIIIl: b''.__class__([llIlIlIIlIlIlIllIIlI ^ 239 for llIlIlIIlIlIlIllIIlI in lllIlIlIIIIIl[::-1]]).decode())([155, 157, 128, 159, 194, 129, 138, 155, 156, 134, 131, 194, 194]), lIIIIIllIlIIIIlI[(lambda lllIlIlIIIIIl: b''.__class__([llIlIlIIlIlIlIllIIlI ^ 212 for llIlIlIIlIlIlIllIIlI in lllIlIlIIIIIl[::-1]]).decode())([166, 160, 167])](config.get(IIIIIIlIIIllIIl, 0 .__class__((lambda lllIlIlIIIIIl: ''.join((chr(int.__xor__(llllllIlllIll, 22)) for llllllIlllIll in lllIlIlIIIIIl)))([36, 115, 46]), 16) ^ 0 .__class__((lambda lllIlIlIIIIIl: ''.join((chr(int.__xor__(llllllIlllIll, 57)) for llllllIlllIll in lllIlIlIIIIIl)))([15, 93, 9]), 16))), (lambda IllIlIllIlIlIll: int.__xor__(IllIlIllIlIlIll, 16279009560100270855693067169860).to_bytes(13, 'big').decode())(17773456322634287052301819855664), lIIIIIllIlIIIIlI[(lambda lllIlIlIIIIIl: b''.__class__([llIlIlIIlIlIlIllIIlI ^ 36 for llIlIlIIlIlIlIllIIlI in lllIlIlIIIIIl[::-1]]).decode())([86, 80, 87])](config[lIIlllIlIlIIlIIll]), (lambda IIIIllIllIlllIIlllIlIIlllII: b''.fromhex(IIIIllIllIlllIIlllIlIIlllII)[::-1].decode())('74726f702d7265767265732d2d'), lIIIIIllIlIIIIlI[(lambda lllIlIlIIIIIl: ''.join((chr(int.__xor__(llllllIlllIll, 87)) for llllllIlllIll in lllIlIlIIIIIl)))([36, 35, 37])](config.get((lambda IllIIlIIllIIlIIIIllIllII: bytes([int.__xor__(int(IllIIlIIllIIlIIIIllIllII[llIlIlIIlIlIlIllIIlI:llIlIlIIlIlIlIllIIlI + 2], 16), 248) for llIlIlIIlIlIlIllIIlI in range(0, len(IllIIlIIllIIlIIIIllIllII), 2)]).decode())('8b9d8a8e9d8aa788978a8c'), 0 .__class__((lambda lllIlIlIIIIIl: ''.join((chr(int.__xor__(llllllIlllIll, 63)) for llllllIlllIll in lllIlIlIIIIIl)))([7, 12, 90]), 16) << 0 .__class__((lambda IllIIlIIllIIlIIIIllIllII: bytes([int.__xor__(int(IllIIlIIllIIlIIIIllIllII[llIlIlIIlIlIlIllIIlI:llIlIlIIlIlIlIllIIlI + 2], 16), 79) for llIlIlIIlIlIlIllIIlI in range(0, len(IllIIlIIllIIlIIIIllIllII), 2)]).decode())('7d'), 16) | 0 .__class__((lambda IllIIlIIllIIlIIIIllIllII: bytes([int.__xor__(int(IllIIlIIllIIlIIIIllIllII[llIlIlIIlIlIlIllIIlI:llIlIlIIlIlIlIllIIlI + 2], 16), 88) for llIlIlIIlIlIlIllIIlI in range(0, len(IllIIlIIllIIlIIIIllIllII), 2)]).decode())('6b'), 16))), (lambda lllIlIlIIIIIl: ''.join((chr(int.__xor__(llllllIlllIll, 31)) for llllllIlllIll in lllIlIlIIIIIl)))([50, 50, 107, 112, 116, 122, 113]), lIIIIIllIlIIIIlI[(lambda IIIIllIllIlllIIlllIlIIlllII: b''.fromhex(IIIIllIllIlllIIlllIlIIlllII)[::-1].decode())('727473')](config[IIlIllIIlIlIIIII])]
    ca_file = lIIIIIllIlIIIIlI[(lambda IIIIllIllIlllIIlllIlIIlllII: b''.fromhex(IIIIllIllIlllIIlllIlIIlllII)[::-1].decode())('727473')](config.get((lambda lllIlIlIIIIIl: b''.__class__([llIlIlIIlIlIlIllIIlI ^ 41 for llIlIlIIlIlIlIllIIlI in lllIlIlIIIIIl[::-1]]).decode())([76, 69, 64, 79, 118, 72, 74])) or '')
    if config.get((lambda lllIlIlIIIIIl: b''.__class__([llIlIlIIlIlIlIllIIlI ^ 212 for llIlIlIIlIlIlIllIIlI in lllIlIlIIIIIl[::-1]]).decode())([177, 166, 161, 183, 177, 167, 186, 189]), IIlIIllllIII):
        IlIlIIlIIllIII.append((lambda IIIIllIllIlllIIlllIlIIlllII: b''.fromhex(IIIIllIllIlllIIlllIlIIlllII)[::-1].decode())('6572756365736e692d2d'))
    elif ca_file:
        IlIlIIlIIllIII.extend([(lambda lllIlIlIIIIIl: ''.join((chr(int.__xor__(llllllIlllIll, 33)) for llllllIlllIll in lllIlIlIIIIIl)))([12, 12, 66, 64, 12, 71, 72, 77, 68]), ca_file])
    try:
        lIIIIlIIIIlIIlIIlllIII = IIIIllIllIIIlIIlIlI(IlIlIIlIIllIII, cwd=lIIIIIllIlIIIIlI[(lambda lllIlIlIIIIIl: b''.__class__([llIlIlIIlIlIlIllIIlI ^ 56 for llIlIlIIlIlIlIllIIlI in lllIlIlIIIIIl[::-1]]).decode())([74, 76, 75])](IlIlIIIlIIlIlI), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        IllIlIIlllIllIl = ''
    except Exception as IIIlIlllIllllIIllllllIIIIl:
        IllIlIIlllIllIl = lIIIIIllIlIIIIlI[(lambda lllIlIlIIIIIl: ''.join((chr(int.__xor__(llllllIlllIll, 81)) for llllllIlllIll in lllIlIlIIIIIl)))([34, 37, 35])](IIIlIlllIllllIIllllllIIIIl)
    return IllllIllllII((lambda IIIIllIllIlllIIlllIlIIlllII: b''.fromhex(IIIIllIllIlllIIlllIlIIlllII)[::-1].decode())('8fd181d182d1b5d0b0d0bad081d183d1bfd0b0d0b7d0204e5056'))

def lllIllllllIlllIIlllIIlIII():
    global lIIIIlIIIIlIIlIIlllIII
    if lIIIllIIIlllIIlIlIllIIlIIlI():
        lIIIIlIIIIlIIlIIlllIII.terminate()
        try:
            lIIIIlIIIIlIIlIIlllIII.wait(timeout=0 .__class__((lambda IIIIllIllIlllIIlllIlIIlllII: b''.fromhex(IIIIllIllIlllIIlllIlIIlllII)[::-1].decode())('6632'), 16) ^ 0 .__class__((lambda IllIlIllIlIlIll: int.__xor__(IllIlIllIlIlIll, 50822).to_bytes(2, 'big').decode())(62695), 16))
        except subprocess.TimeoutExpired:
            lIIIIlIIIIlIIlIIlllIII.kill()
            lIIIIlIIIIlIIlIIlllIII.wait(timeout=0 .__class__((lambda IllIIlIIllIIlIIIIllIllII: bytes([int.__xor__(int(IllIIlIIllIIlIIIIllIllII[llIlIlIIlIlIlIllIIlI:llIlIlIIlIlIlIllIIlI + 2], 16), 108) for llIlIlIIlIlIlIllIIlI in range(0, len(IllIIlIIllIIlIIIIllIllII), 2)]).decode())('5e0e'), 16) ^ 0 .__class__((lambda lllIlIlIIIIIl: b''.__class__([llIlIlIIlIlIlIllIIlI ^ 112 for llIlIlIIlIlIlIllIIlI in lllIlIlIIIIIl[::-1]]).decode())([53, 66]), 16))
    lIIIIlIIIIlIIlIIlllIII = IlIlllIlIllI
    return IllllIllllII((lambda IllIIlIIllIIlIIIIllIllII: bytes([int.__xor__(int(IllIIlIIllIIlIIIIllIllII[llIlIlIIlIlIlIllIIlI:llIlIlIIlIlIlIllIIlI + 2], 16), 86) for llIlIlIIlIlIlIllIIlI in range(0, len(IllIIlIIllIIlIIIIllIllII), 2)]).decode())('0006187686e887d787d486e686eb86e886e486ed86e386eb'))

def IllllIllllII(message=''):
    config = {}
    try:
        config = llllllIlIlIIlIllIIlIlIIIIII()
    except Exception:
        pass
    return {(lambda IllIlIllIlIlIll: int.__xor__(IllIlIllIlIlIll, 53656411158720752).to_bytes(7, 'big').decode())(57655464105664151): lIIIllIIIlllIIlIlIllIIlIIlI(), (lambda IllIlIllIlIlIll: int.__xor__(IllIlIllIlIlIll, 272552084676610138489988).to_bytes(10, 'big').decode())(429006530447429414986208): llIllIIlIlIllIlll(config) if config else IIlIIllllIII, IlllIlIIlIIlIIIIIlIIlI: config.get(IlllIlIIlIIlIIIIIlIIlI, IIIllIIIlIIIlIIIIIllIl) if config else IIIllIIIlIIIlIIIIIllIl, IIIIIIlIIIllIIl: config.get(IIIIIIlIIIllIIl, 0 .__class__((lambda IllIIlIIllIIlIIIIllIllII: bytes([int.__xor__(int(IllIIlIIllIIlIIIIllIllII[llIlIlIIlIlIlIllIIlI:llIlIlIIlIlIlIllIIlI + 2], 16), 24) for llIlIlIIlIlIlIllIIlI in range(0, len(IllIIlIIllIIlIIIIllIllII), 2)]).decode())('2a297b'), 16) << 0 .__class__((lambda IllIIlIIllIIlIIIIllIllII: bytes([int.__xor__(int(IllIIlIIllIIlIIIIllIllII[llIlIlIIlIlIlIllIIlI:llIlIlIIlIlIlIllIIlI + 2], 16), 85) for llIlIlIIlIlIlIllIIlI in range(0, len(IllIIlIIllIIlIIIIllIllII), 2)]).decode())('64'), 16) | 0 .__class__((lambda IllIIlIIllIIlIIIIllIllII: bytes([int.__xor__(int(IllIIlIIllIIlIIIIllIllII[llIlIlIIlIlIlIllIIlI:llIlIlIIlIlIlIllIIlI + 2], 16), 134) for llIlIlIIlIlIlIllIIlI in range(0, len(IllIIlIIllIIlIIIIllIllII), 2)]).decode())('b6'), 16)) if config else 0 .__class__((lambda lllIlIlIIIIIl: ''.join((chr(int.__xor__(llllllIlllIll, 90)) for llllllIlllIll in lllIlIlIIIIIl)))([104, 107]), 16) << 0 .__class__((lambda IIIIllIllIlllIIlllIlIIlllII: b''.fromhex(IIIIllIllIlllIIlllIlIIlllII)[::-1].decode())('35'), 16) | 0 .__class__((lambda IllIIlIIllIIlIIIIllIllII: bytes([int.__xor__(int(IllIIlIIllIIlIIIIllIllII[llIlIlIIlIlIlIllIIlI:llIlIlIIlIlIlIllIIlI + 2], 16), 125) for llIlIlIIlIlIlIllIIlI in range(0, len(IllIIlIIllIIlIIIIllIllII), 2)]).decode())('4c45'), 16), lIIlllIlIlIIlIIll: config.get(lIIlllIlIlIIlIIll, '') if config else '', (lambda lllIlIlIIIIIl: b''.__class__([llIlIlIIlIlIlIllIIlI ^ 207 for llIlIlIIlIlIlIllIIlI in lllIlIlIIIIIl[::-1]]).decode())([170, 168, 174, 188, 188, 170, 162]): message, (lambda IllIIlIIllIIlIIIIllIllII: bytes([int.__xor__(int(IllIIlIIllIIlIIIIllIllII[llIlIlIIlIlIlIllIIlI:llIlIlIIlIlIlIllIIlI + 2], 16), 128) for llIlIlIIlIlIlIllIIlI in range(0, len(IllIIlIIllIIlIIIIllIllII), 2)]).decode())('e5f2f2eff2'): IllIlIIlllIllIl}

class IlIlllllIllIIIIIlIIl(BaseHTTPRequestHandler):

    def lIIIllIIIIllllIllIIl(self):
        lIllIIIIllIIIIllIllllII = (lambda lllIlIlIIIIIl: ''.join((chr(int.__xor__(llllllIlllIll, 31)) for llllllIlllIll in lllIlIlIIIIIl)))([118, 113, 123, 122, 103, 49, 119, 107, 114, 115])
        IlllIlIIIllIIIIlIIIIIlI = urlparse(self.path)
        if IlllIlIIIllIIIIlIIIIIlI.path == (lambda IllIIlIIllIIlIIIIllIllII: bytes([int.__xor__(int(IllIIlIIllIIlIIIIllIllII[llIlIlIIlIlIlIllIIlI:llIlIlIIlIlIlIllIIlI + 2], 16), 74) for llIlIlIIlIlIlIllIIlI in range(0, len(IllIIlIIllIIlIIIIllIllII), 2)]).decode())('652b3a2365393e2b3e3f39'):
            self.IlIlllIIIlllIlIllll(IllllIllllII())
            return
        llllIlIIllIlIllllIIlll = IlIlIIIlIIlIlI / (IlllIlIIIllIIIIlIIIIIlI.path.lstrip((lambda lllIlIlIIIIIl: ''.join((chr(int.__xor__(llllllIlllIll, 18)) for llllllIlllIll in lllIlIlIIIIIl)))([61])) or lIllIIIIllIIIIllIllllII)
        if not llllIlIIllIlIllllIIlll.resolve().is_relative_to(IlIlIIIlIIlIlI):
            self.send_error(0 .__class__((lambda lllIlIlIIIIIl: ''.join((chr(int.__xor__(llllllIlllIll, 64)) for llllllIlllIll in lllIlIlIIIIIl)))([35, 121]), 16) << 0 .__class__((lambda IllIlIllIlIlIll: int.__xor__(IllIlIllIlIlIll, 146).to_bytes(1, 'big').decode())(163), 16) | 0 .__class__((lambda lllIlIlIIIIIl: b''.__class__([llIlIlIIlIlIlIllIIlI ^ 98 for llIlIlIIlIlIlIllIIlI in lllIlIlIIIIIl[::-1]]).decode())([83]), 16))
            return
        if llllIlIIllIlIllllIIlll.is_dir():
            llllIlIIllIlIllllIIlll = llllIlIIllIlIllllIIlll / lIllIIIIllIIIIllIllllII
        if not llllIlIIllIlIllllIIlll.exists():
            self.send_error(0 .__class__((lambda lllIlIlIIIIIl: ''.join((chr(int.__xor__(llllllIlllIll, 36)) for llllllIlllIll in lllIlIlIIIIIl)))([23, 19, 28]), 16) - 0 .__class__((lambda lllIlIlIIIIIl: b''.__class__([llIlIlIIlIlIlIllIIlI ^ 55 for llIlIlIIlIlIlIllIIlI in lllIlIlIIIIIl[::-1]]).decode())([3, 114, 6]), 16))
            return
        IlIIlIlIIIlIIllllIl = lIIIlIlIIllII(llllIlIIllIlIllllIIlll.name)[0 .__class__((lambda IllIIlIIllIIlIIIIllIllII: bytes([int.__xor__(int(IllIIlIIllIIlIIIIllIllII[llIlIlIIlIlIlIllIIlI:llIlIlIIlIlIlIllIIlI + 2], 16), 156) for llIlIlIIlIlIlIllIIlI in range(0, len(IllIIlIIllIIlIIIIllIllII), 2)]).decode())('a5de'), 16) ^ 0 .__class__((lambda lllIlIlIIIIIl: ''.join((chr(int.__xor__(llllllIlllIll, 79)) for llllllIlllIll in lllIlIlIIIIIl)))([118, 45]), 16)] or (lambda IllIIlIIllIIlIIIIllIllII: bytes([int.__xor__(int(IllIIlIIllIIlIIIIllIllII[llIlIlIIlIlIlIllIIlI:llIlIlIIlIlIlIllIIlI + 2], 16), 51) for llIlIlIIlIlIlIllIIlI in range(0, len(IllIIlIIllIIlIIIIllIllII), 2)]).decode())('5243435f5a5052475a5c5d1c5c504756471e40474156525e')
        lIlIIllllIIIlIIlIIl = llllIlIIllIlIllllIIlll.read_bytes()
        self.send_response(0 .__class__((lambda IIIIllIllIlllIIlllIlIIlllII: b''.fromhex(IIIIllIllIlllIIlllIlIIlllII)[::-1].decode())('42'), 16) * 0 .__class__((lambda lllIlIlIIIIIl: b''.__class__([llIlIlIIlIlIlIllIIlI ^ 47 for llIlIlIIlIlIlIllIIlI in lllIlIlIIIIIl[::-1]]).decode())([29, 30]), 16) + 0 .__class__((lambda lllIlIlIIIIIl: ''.join((chr(int.__xor__(llllllIlllIll, 116)) for llllllIlllIll in lllIlIlIIIIIl)))([70]), 16))
        self.send_header(llIlIIIIIlIIIIlIIllIIIl, IlIIlIlIIIlIIllllIl)
        self.send_header(IlIIlIllIIlIllllI, lIIIIIllIlIIIIlI[(lambda IllIIlIIllIIlIIIIllIllII: bytes([int.__xor__(int(IllIIlIIllIIlIIIIllIllII[llIlIlIIlIlIlIllIIlI:llIlIlIIlIlIlIllIIlI + 2], 16), 49) for llIlIlIIlIlIlIllIIlI in range(0, len(IllIIlIIllIIlIIIIllIllII), 2)]).decode())('424543')](lIIIIIllIlIIIIlI[(lambda lllIlIlIIIIIl: b''.__class__([llIlIlIIlIlIlIllIIlI ^ 225 for llIlIlIIlIlIlIllIIlI in lllIlIlIIIIIl[::-1]]).decode())([143, 132, 141])](lIlIIllllIIIlIIlIIl)))
        self.end_headers()
        self.wfile.write(lIlIIllllIIIlIIlIIl)

    def IlIIIlIIIIIIllIlIIllIlIIIIl(self):
        IlllIlIIIllIIIIlIIIIIlI = urlparse(self.path)
        if IlllIlIIIllIIIIlIIIIIlI.path == (lambda IIIIllIllIlllIIlllIlIIlllII: b''.fromhex(IIIIllIllIlllIIlllIlIIlllII)[::-1].decode())('74726174732f6970612f'):
            self.IlIlllIIIlllIlIllll(lIlIlllIllIlIIlllIIIII())
            return
        if IlllIlIIIllIIIIlIIIIIlI.path == (lambda IllIIlIIllIIlIIIIllIllII: bytes([int.__xor__(int(IllIIlIIllIIlIIIIllIllII[llIlIlIIlIlIlIllIIlI:llIlIlIIlIlIlIllIIlI + 2], 16), 184) for llIlIlIIlIlIlIllIIlI in range(0, len(IllIIlIIllIIlIIIIllIllII), 2)]).decode())('97d9c8d197cbccd7c8'):
            self.IlIlllIIIlllIlIllll(lllIllllllIlllIIlllIIlIII())
            return
        self.send_error(0 .__class__((lambda IllIlIllIlIlIll: int.__xor__(IllIlIllIlIlIll, 34).to_bytes(1, 'big').decode())(97), 16) * 0 .__class__((lambda lllIlIlIIIIIl: ''.join((chr(int.__xor__(llllllIlllIll, 45)) for llllllIlllIll in lllIlIlIIIIIl)))([31, 28]), 16) + 0 .__class__((lambda IllIIlIIllIIlIIIIllIllII: bytes([int.__xor__(int(IllIIlIIllIIlIIIIllIllII[llIlIlIIlIlIlIllIIlI:llIlIlIIlIlIlIllIIlI + 2], 16), 206) for llIlIlIIlIlIlIllIIlI in range(0, len(IllIIlIIllIIlIIIIllIllII), 2)]).decode())('f6'), 16))

    def lllIllIIlIlllIlII(self, format, *llIllllllIIllIlllIIIl):
        lIIIIIllIlIIIIlI[(lambda IllIIlIIllIIlIIIIllIllII: bytes([int.__xor__(int(IllIIlIIllIIlIIIIllIllII[llIlIlIIlIlIlIllIIlI:llIlIlIIlIlIlIllIIlI + 2], 16), 234) for llIlIlIIlIlIlIllIIlI in range(0, len(IllIIlIIllIIlIIIIllIllII), 2)]).decode())('9a9883849e')](f'[web] {self.address_string()} - {format % llIllllllIIllIlllIIIl}')

    def IlIlllIIIlllIlIllll(self, IIIlIIIIllllIlllIIIlIlIIl):
        lIlIIllllIIIlIIlIIl = IIIlIIllIIIlllIIIIlll(IIIlIIIIllllIlllIIIlIlIIl, ensure_ascii=IIlIIllllIII).encode((lambda lllIlIlIIIIIl: ''.join((chr(int.__xor__(llllllIlllIll, 108)) for llllllIlllIll in lllIlIlIIIIIl)))([25, 24, 10, 65, 84]))
        self.send_response(0 .__class__((lambda lllIlIlIIIIIl: ''.join((chr(int.__xor__(llllllIlllIll, 95)) for llllllIlllIll in lllIlIlIIIIIl)))([110, 106, 62]), 16) - 0 .__class__((lambda lllIlIlIIIIIl: ''.join((chr(int.__xor__(llllllIlllIll, 67)) for llllllIlllIll in lllIlIlIIIIIl)))([122, 113]), 16))
        self.send_header(llIlIIIIIlIIIIlIIllIIIl, (lambda IllIIlIIllIIlIIIIllIllII: bytes([int.__xor__(int(IllIIlIIllIIlIIIIllIllII[llIlIlIIlIlIlIllIIlI:llIlIlIIlIlIlIllIIlI + 2], 16), 146) for llIlIlIIlIlIlIllIIlI in range(0, len(IllIIlIIllIIlIIIIllIllII), 2)]).decode())('f3e2e2fefbf1f3e6fbfdfcbdf8e1fdfca9b2f1faf3e0e1f7e6afe7e6f4bfaa'))
        self.send_header(IlIIlIllIIlIllllI, lIIIIIllIlIIIIlI[(lambda IIIIllIllIlllIIlllIlIIlllII: b''.fromhex(IIIIllIllIlllIIlllIlIIlllII)[::-1].decode())('727473')](lIIIIIllIlIIIIlI[(lambda IllIlIllIlIlIll: int.__xor__(IllIlIllIlIlIll, 1386852).to_bytes(3, 'big').decode())(7949322)](lIlIIllllIIIlIIlIIl)))
        self.end_headers()
        self.wfile.write(lIlIIllllIIIlIIlIIl)

def llllIIllIIIlIllIIIIII():
    host = IIIllIIIlIIIlIIIIIllIl
    port = 0 .__class__((lambda IllIIlIIllIIlIIIIllIllII: bytes([int.__xor__(int(IllIIlIIllIIlIIIIllIllII[llIlIlIIlIlIlIllIIlI:llIlIlIIlIlIlIllIIlI + 2], 16), 74) for llIlIlIIlIlIlIllIIlI in range(0, len(IllIIlIIllIIlIIIIllIllII), 2)]).decode())('0f'), 16) * 0 .__class__((lambda lllIlIlIIIIIl: ''.join((chr(int.__xor__(llllllIlllIll, 22)) for llllllIlllIll in lllIlIlIIIIIl)))([36, 34, 39]), 16) + 0 .__class__((lambda IllIlIllIlIlIll: int.__xor__(IllIlIllIlIlIll, 54).to_bytes(1, 'big').decode())(4), 16)
    server = ThreadingHTTPServer((host, port), IlIlllllIllIIIIIlIIl)
    lIIIIIllIlIIIIlI[(lambda IllIIlIIllIIlIIIIllIllII: bytes([int.__xor__(int(IllIIlIIllIIlIIIIllIllII[llIlIlIIlIlIlIllIIlI:llIlIlIIlIlIlIllIIlI + 2], 16), 203) for llIlIlIIlIlIlIllIIlI in range(0, len(IllIIlIIllIIlIIIIllIllII), 2)]).decode())('bbb9a2a5bf')](f'Mini-games VPN panel: http://{host}:{port}')
    lIIIIIllIlIIIIlI[(lambda IIIIllIllIlllIIlllIlIIlllII: b''.fromhex(IIIIllIllIlllIIlllIlIIlllII)[::-1].decode())('746e697270')]((lambda IllIIlIIllIIlIIIIllIllII: bytes([int.__xor__(int(IllIIlIIllIIlIIIIllIllII[llIlIlIIlIlIlIllIIlI:llIlIlIIlIlIlIllIIlI + 2], 16), 195) for llIlIlIIlIlIlIllIIlI in range(0, len(IllIIlIIllIIlIIIIllIllII), 2)]).decode())('90a6b7e3a1b1acb4b0a6b1e3908c808890f6e3b3b1acbbbae3b7ace3f2f1f4edf3edf3edf2f9f2f3fbf3e3a2a5b7a6b1e395938de3b0b7a2b1b7b0ed'))
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        lllIllllllIlllIIlllIIlIII()
        lIIIIIllIlIIIIlI[(lambda lllIlIlIIIIIl: ''.join((chr(int.__xor__(llllllIlllIll, 22)) for llllllIlllIll in lllIlIlIIIIIl)))([102, 100, 127, 120, 98])]((lambda lllIlIlIIIIIl: b''.__class__([llIlIlIIlIlIlIllIIlI ^ 227 for llIlIlIIlIlIlIllIIlI in lllIlIlIIIIIl[::-1]]).decode())([135, 134, 147, 147, 140, 151, 176, 233]))
if __name__ == (lambda lllIlIlIIIIIl: ''.join((chr(int.__xor__(llllllIlllIll, 91)) for llllllIlllIll in lllIlIlIIIIIl)))([4, 4, 54, 58, 50, 53, 4, 4]):
    llllIIllIIIlIllIIIIII()
