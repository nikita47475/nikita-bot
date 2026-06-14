from argparse import ArgumentParser as lIlIIlIlIllllllIIIIllI
from asyncio import gather as IIlIllllllIlllIIlIlIlIlIlI, open_connection as IIlIIlllIIIIlIIIIIIl, run as IlIlIIllIIlllIIIlIlIIIIlI, start_server as IIIlIlIIIlIl
from json import dumps as IlllIIlIlIllIIIlIlIlll, loads as lllIlIllllllllIllI
from socket import inet_ntoa as lIIllIIllllllIlIIIllllIl, inet_ntop as IllIlIIIlIlIIlIIlIIIII
from ssl import create_default_context as llIllIIIlIlllIIlllII
from struct import pack as IIIIlllllllllllIlIIllI, unpack as IIllIIIIIIllIIIIlIIIl
IlllllIllllIlIIlll = globals()[(lambda llIllIlIIlIIlIlIl: b''.fromhex(llIllIlIIlIIlIlIl)[::-1].decode())('5f5f736e69746c6975625f5f')]
llIIllIIIlllI = IlllllIllllIlIIlll if isinstance(IlllllIllllIlIIlll, dict) else IlllllIllllIlIIlll.__dict__
llllIlllIIIIlIIIIIIlllI = (lambda IllllIlIlllllll: b''.__class__([IlIlllllllllll ^ 154 for IlIlllllllllll in IllllIlIlllllll[::-1]]).decode())([244, 245, 243, 233, 232, 255, 236, 186, 201, 209, 217, 213, 201, 186, 254, 255, 238, 232, 245, 234, 234, 239, 233, 244, 239])
IIIllIlIIllIllllIllllIIlll = True
import asyncio, socket, ssl
from typing import Optional, Tuple
IIlIlIIIIIIlIlIllllIIIIIl = 0 .__class__((lambda llIllIlIIlIIlIlIl: b''.fromhex(llIllIlIIlIIlIlIl)[::-1].decode())('37'), 16) * 0 .__class__((lambda IllllIlIlllllll: b''.__class__([IlIlllllllllll ^ 200 for IlIlllllllllll in IllllIlIlllllll[::-1]]).decode())([250, 241, 252, 250]), 16) + 0 .__class__((lambda llIllIlIIlIIlIlIl: b''.fromhex(llIllIlIIlIIlIlIl)[::-1].decode())('32'), 16)
IlllIIlllllll = 0 .__class__((lambda llIllIllIIlIllIIl: int.__xor__(llIllIllIIlIllIIl, 7651093).to_bytes(3, 'big').decode())(4556835), 16) - 0 .__class__((lambda llIllIllIIlIllIIl: int.__xor__(llIllIllIIlIllIIl, 10950739).to_bytes(3, 'big').decode())(9842530), 16)

class IlIIIlIIllIIlIlIIIlIIll(Exception):
    0 .__class__((lambda IllllIlIlllllll: ''.join((chr(int.__xor__(llIlllllllllll, 49)) for llIlllllllllll in IllllIlIlllllll)))([117, 115]), 16) ^ 0 .__class__((lambda llIllIlIIlIIlIlIl: b''.fromhex(llIllIlIIlIIlIlIl)[::-1].decode())('6264'), 16)

async def lIIIlIllIIlIlIlIIIlII(lIIIlIIIlllIIIl, llIllIllIIlIllIIl):
    return await lIIIlIIIlllIIIl.readexactly(llIllIllIIlIllIIl)

async def llIllIllIllII(lIIIlIIIlllIIIl):
    version, lIIIllllIllIlIIllIIlllIllI, IIIIIlIlllIIIIIIlIIIlllll, lIllIlllIlllIIIl = await lIIIlIllIIlIlIlIIIlII(lIIIlIIIlllIIIl, 0 .__class__((lambda llIllIlIIlIIlIlIl: b''.fromhex(llIllIlIIlIIlIlIl)[::-1].decode())('61'), 16) * 0 .__class__((lambda IllllIlIlllllll: ''.join((chr(int.__xor__(llIlllllllllll, 121)) for llIlllllllllll in IllllIlIlllllll)))([73]), 16) + 0 .__class__((lambda IllllIlIlllllll: b''.__class__([IlIlllllllllll ^ 32 for IlIlllllllllll in IllllIlIlllllll[::-1]]).decode())([20]), 16))
    if version != IlllIIlllllll:
        raise IlIIIlIIllIIlIlIIIlIIll(llllIlllIIIIlIIIIIIlllI)
    if lIIIllllIllIlIIllIIlllIllI != 0 .__class__((lambda llIllIllIIlIllIIl: int.__xor__(llIllIllIIlIllIIl, 13302025).to_bytes(3, 'big').decode())(16489790), 16) - 0 .__class__((lambda llIllIllIIlIllIIl: int.__xor__(llIllIllIIlIllIIl, 4664862).to_bytes(3, 'big').decode())(7752232), 16):
        raise IlIIIlIIllIIlIlIIIlIIll((lambda llIllIlIIlIIlIlIl: b''.fromhex(llIllIlIIlIIlIlIl)[::-1].decode())('646574726f70707573207369205443454e4e4f4320796c6e6f'))
    if lIllIlllIlllIIIl == 0 .__class__((lambda IlllllIIlllIlIllIlIllI: bytes([int.__xor__(int(IlllllIIlllIlIllIlIllI[IlIlllllllllll:IlIlllllllllll + 2], 16), 199) for IlIlllllllllll in range(0, len(IlllllIIlllIlIllIlIllI), 2)]).decode())('f6f2f0'), 16) - 0 .__class__((lambda IllllIlIlllllll: ''.join((chr(int.__xor__(llIlllllllllll, 61)) for llIlllllllllll in IllllIlIlllllll)))([12, 8, 11]), 16):
        host = lIIllIIllllllIlIIIllllIl(await lIIIlIllIIlIlIlIIIlII(lIIIlIIIlllIIIl, 0 .__class__((lambda IllllIlIlllllll: b''.__class__([IlIlllllllllll ^ 149 for IlIlllllllllll in IllllIlIlllllll[::-1]]).decode())([209]), 16) ^ 0 .__class__((lambda IllllIlIlllllll: b''.__class__([IlIlllllllllll ^ 71 for IlIlllllllllll in IllllIlIlllllll[::-1]]).decode())([126]), 16)))
    elif lIllIlllIlllIIIl == 0 .__class__((lambda IlllllIIlllIlIllIlIllI: bytes([int.__xor__(int(IlllllIIlllIlIllIlIllI[IlIlllllllllll:IlIlllllllllll + 2], 16), 140) for IlIlllllllllll in range(0, len(IlllllIIlllIlIllIlIllI), 2)]).decode())('bc'), 16) << 0 .__class__((lambda IlllllIIlllIlIllIlIllI: bytes([int.__xor__(int(IlllllIIlllIlIllIlIllI[IlIlllllllllll:IlIlllllllllll + 2], 16), 76) for IlIlllllllllll in range(0, len(IlllllIIlllIlIllIlIllI), 2)]).decode())('7e'), 16) | 0 .__class__((lambda llIllIllIIlIllIIl: int.__xor__(llIllIllIIlIllIIl, 24).to_bytes(1, 'big').decode())(43), 16):
        lIlIIlIllIlIlIIllIIlIIIIllI = (await lIIIlIllIIlIlIlIIIlII(lIIIlIIIlllIIIl, 0 .__class__((lambda llIllIlIIlIIlIlIl: b''.fromhex(llIllIlIIlIIlIlIl)[::-1].decode())('4332'), 16) ^ 0 .__class__((lambda IllllIlIlllllll: b''.__class__([IlIlllllllllll ^ 171 for IlIlllllllllll in IllllIlIlllllll[::-1]]).decode())([207, 153]), 16)))[0 .__class__((lambda IllllIlIlllllll: ''.join((chr(int.__xor__(llIlllllllllll, 13)) for llIlllllllllll in IllllIlIlllllll)))([58, 63]), 16) ^ 0 .__class__((lambda IlllllIIlllIlIllIlIllI: bytes([int.__xor__(int(IlllllIIlllIlIllIlIllI[IlIlllllllllll:IlIlllllllllll + 2], 16), 164) for IlIlllllllllll in range(0, len(IlllllIIlllIlIllIlIllI), 2)]).decode())('9396'), 16)]
        host = (await lIIIlIllIIlIlIlIIIlII(lIIIlIIIlllIIIl, lIlIIlIllIlIlIIllIIlIIIIllI)).decode((lambda IllllIlIlllllll: ''.join((chr(int.__xor__(llIlllllllllll, 76)) for llIlllllllllll in IllllIlIlllllll)))([37, 40, 34, 45]))
    elif lIllIlllIlllIIIl == 0 .__class__((lambda IllllIlIlllllll: b''.__class__([IlIlllllllllll ^ 22 for IlIlllllllllll in IllllIlIlllllll[::-1]]).decode())([38, 37]), 16) ^ 0 .__class__((lambda IllllIlIlllllll: b''.__class__([IlIlllllllllll ^ 156 for IlIlllllllllll in IllllIlIlllllll[::-1]]).decode())([168, 175]), 16):
        host = IllIlIIIlIlIIlIIlIIIII(socket.AF_INET6, await lIIIlIllIIlIlIlIIIlII(lIIIlIIIlllIIIl, 0 .__class__((lambda llIllIllIIlIllIIl: int.__xor__(llIllIllIIlIllIIl, 9127).to_bytes(2, 'big').decode())(4752), 16) ^ 0 .__class__((lambda llIllIlIIlIIlIlIl: b''.fromhex(llIllIlIIlIIlIlIl)[::-1].decode())('37'), 16)))
    else:
        raise IlIIIlIIllIIlIlIIIlIIll((lambda llIllIlIIlIIlIlIl: b''.fromhex(llIllIlIIlIIlIlIl)[::-1].decode())('65707974207373657264646120646574726f707075736e75'))
    port = IIllIIIIIIllIIIIlIIIl((lambda llIllIlIIlIIlIlIl: b''.fromhex(llIllIlIIlIIlIlIl)[::-1].decode())('4821'), await lIIIlIllIIlIlIlIIIlII(lIIIlIIIlllIIIl, 0 .__class__((lambda IllllIlIlllllll: b''.__class__([IlIlllllllllll ^ 164 for IlIlllllllllll in IllllIlIlllllll[::-1]]).decode())([224, 150]), 16) ^ 0 .__class__((lambda IlllllIIlllIlIllIlIllI: bytes([int.__xor__(int(IlllllIIlllIlIllIlIllI[IlIlllllllllll:IlIlllllllllll + 2], 16), 69) for IlIlllllllllll in range(0, len(IlllllIIlllIlIllIlIllI), 2)]).decode())('7723'), 16)))[0 .__class__((lambda IlllllIIlllIlIllIlIllI: bytes([int.__xor__(int(IlllllIIlllIlIllIlIllI[IlIlllllllllll:IlIlllllllllll + 2], 16), 130) for IlIlllllllllll in range(0, len(IlllllIIlllIlIllIlIllI), 2)]).decode())('b7b3'), 16) ^ 0 .__class__((lambda llIllIlIIlIIlIlIl: b''.fromhex(llIllIlIIlIIlIlIl)[::-1].decode())('3135'), 16)]
    return (host, port)

async def IIlIIlIllIlIlllIIIIlIIII(lIIIlIIIlllIIIl, IlIIllIIlIlIllllIllIIlI):
    version, IIIIlIIIlIllIIlllI = await lIIIlIllIIlIlIlIIIlII(lIIIlIIIlllIIIl, 0 .__class__((lambda IllllIlIlllllll: b''.__class__([IlIlllllllllll ^ 231 for IlIlllllllllll in IllllIlIlllllll[::-1]]).decode())([130, 214]), 16) - 0 .__class__((lambda IllllIlIlllllll: b''.__class__([IlIlllllllllll ^ 241 for IlIlllllllllll in IllllIlIlllllll[::-1]]).decode())([146, 192]), 16))
    if version != IlllIIlllllll:
        raise IlIIIlIIllIIlIlIIIlIIll(llllIlllIIIIlIIIIIIlllI)
    IIlllIIlIIIllIIlIIllI = await lIIIlIllIIlIlIlIIIlII(lIIIlIIIlllIIIl, IIIIlIIIlIllIIlllI)
    if 0 .__class__((lambda IlllllIIlllIlIllIlIllI: bytes([int.__xor__(int(IlllllIIlllIlIllIlIllI[IlIlllllllllll:IlIlllllllllll + 2], 16), 113) for IlIlllllllllll in range(0, len(IlllllIIlllIlIllIlIllI), 2)]).decode())('1240'), 16) ^ 0 .__class__((lambda llIllIllIIlIllIIl: int.__xor__(llIllIllIIlIllIIl, 6184).to_bytes(2, 'big').decode())(23321), 16) not in IIlllIIlIIIllIIlIIllI:
        IlIIllIIlIlIllllIllIIlI.write(llIIllIIIlllI[(lambda IllllIlIlllllll: ''.join((chr(int.__xor__(llIlllllllllll, 97)) for llIlllllllllll in IllllIlIlllllll)))([3, 24, 21, 4, 18])]([IlllIIlllllll, 0 .__class__((lambda IllllIlIlllllll: b''.__class__([IlIlllllllllll ^ 141 for IlIlllllllllll in IllllIlIlllllll[::-1]]).decode())([236]), 16) * 0 .__class__((lambda llIllIlIIlIIlIlIl: b''.fromhex(llIllIlIIlIIlIlIl)[::-1].decode())('3931'), 16) + 0 .__class__((lambda IllllIlIlllllll: ''.join((chr(int.__xor__(llIlllllllllll, 22)) for llIlllllllllll in IllllIlIlllllll)))([35]), 16)]))
        await IlIIllIIlIlIllllIllIIlI.drain()
        raise IlIIIlIIllIIlIlIIIlIIll((lambda llIllIllIIlIllIIl: int.__xor__(llIllIllIIlIllIIl, 27925085345996990925371927719990457469633478869878332255192876251565509383134447320036007).to_bytes(37, 'big').decode())(45401995700257875913201519523150881610847537823467270730664281954332273615823366150601204))
    IlIIllIIlIlIllllIllIIlI.write(llIIllIIIlllI[(lambda IllllIlIlllllll: b''.__class__([IlIlllllllllll ^ 20 for IlIlllllllllll in IllllIlIlllllll[::-1]]).decode())([103, 113, 96, 109, 118])]([IlllIIlllllll, 0 .__class__((lambda IllllIlIlllllll: ''.join((chr(int.__xor__(llIlllllllllll, 45)) for llIlllllllllll in IllllIlIlllllll)))([20, 108]), 16) ^ 0 .__class__((lambda llIllIllIIlIllIIl: int.__xor__(llIllIllIIlIllIIl, 27077).to_bytes(2, 'big').decode())(20644), 16)]))
    await IlIIllIIlIlIllllIllIIlI.drain()
    return await llIllIllIllII(lIIIlIIIlllIIIl)

def lIIllIIIIIllllIIllII(IlIlIIlIllIllllIIIIIlI):
    return llIIllIIIlllI[(lambda IllllIlIlllllll: ''.join((chr(int.__xor__(llIlllllllllll, 85)) for llIlllllllllll in IllllIlIlllllll)))([55, 44, 33, 48, 38])]([IlllIIlllllll, IlIlIIlIllIllllIIIIIlI, 0 .__class__((lambda llIllIllIIlIllIIl: int.__xor__(llIllIllIIlIllIIl, 15239).to_bytes(2, 'big').decode())(31412), 16) ^ 0 .__class__((lambda IllllIlIlllllll: ''.join((chr(int.__xor__(llIlllllllllll, 67)) for llIlllllllllll in IllllIlIlllllll)))([2, 112]), 16), 0 .__class__((lambda IlllllIIlllIlIllIlIllI: bytes([int.__xor__(int(IlllllIIlllIlIllIlIllI[IlIlllllllllll:IlIlllllllllll + 2], 16), 137) for IlIlllllllllll in range(0, len(IlllllIIlllIlIllIlIllI), 2)]).decode())('bbeb'), 16) ^ 0 .__class__((lambda IllllIlIlllllll: ''.join((chr(int.__xor__(llIlllllllllll, 19)) for llIlllllllllll in IllllIlIlllllll)))([33, 82]), 16), 0 .__class__((lambda llIllIllIIlIllIIl: int.__xor__(llIllIllIIlIllIIl, 16328).to_bytes(2, 'big').decode())(3067), 16) ^ 0 .__class__((lambda IllllIlIlllllll: b''.__class__([IlIlllllllllll ^ 43 for IlIlllllllllll in IllllIlIlllllll[::-1]]).decode())([24, 31]), 16), 0 .__class__((lambda llIllIllIIlIllIIl: int.__xor__(llIllIllIIlIllIIl, 59843).to_bytes(2, 'big').decode())(43138), 16) ^ 0 .__class__((lambda llIllIlIIlIIlIlIl: b''.fromhex(llIllIlIIlIIlIlIl)[::-1].decode())('6161'), 16), 0 .__class__((lambda IllllIlIlllllll: ''.join((chr(int.__xor__(llIlllllllllll, 123)) for llIlllllllllll in IllllIlIlllllll)))([67, 57]), 16) ^ 0 .__class__((lambda IlllllIIlllIlIllIlIllI: bytes([int.__xor__(int(IlllllIIlllIlIllIlIllI[IlIlllllllllll:IlIlllllllllll + 2], 16), 198) for IlIlllllllllll in range(0, len(IlllllIIlllIlIllIlIllI), 2)]).decode())('fe84'), 16), 0 .__class__((lambda IllllIlIlllllll: ''.join((chr(int.__xor__(llIlllllllllll, 9)) for llIlllllllllll in IllllIlIlllllll)))([58, 60]), 16) ^ 0 .__class__((lambda llIllIlIIlIIlIlIl: b''.fromhex(llIllIlIIlIIlIlIl)[::-1].decode())('3533'), 16), 0 .__class__((lambda IlllllIIlllIlIllIlIllI: bytes([int.__xor__(int(IlllllIIlllIlIllIlIllI[IlIlllllllllll:IlIlllllllllll + 2], 16), 214) for IlIlllllllllll in range(0, len(IlllllIIlllIlIllIlIllI), 2)]).decode())('e2e2'), 16) ^ 0 .__class__((lambda llIllIlIIlIIlIlIl: b''.fromhex(llIllIlIIlIIlIlIl)[::-1].decode())('3434'), 16), 0 .__class__((lambda IllllIlIlllllll: ''.join((chr(int.__xor__(llIlllllllllll, 28)) for llIlllllllllll in IllllIlIlllllll)))([41, 40]), 16) ^ 0 .__class__((lambda llIllIlIIlIIlIlIl: b''.fromhex(llIllIlIIlIIlIlIl)[::-1].decode())('3435'), 16)])

async def llIIIIIIllIIllIlIllIIIIIl(IlIIllIIlIlIllllIllIIlI, host, port, token):
    IlIIllIIlIIlllIlIlllIlIIIIl = IlllIIlIlIllIIIlIlIlll({(lambda llIllIllIIlIllIIl: int.__xor__(llIllIllIIlIllIIl, 3550582023).to_bytes(4, 'big').decode())(3150898803): host, (lambda IllllIlIlllllll: ''.join((chr(int.__xor__(llIlllllllllll, 32)) for llIlllllllllll in IllllIlIlllllll)))([80, 79, 82, 84]): port, (lambda IllllIlIlllllll: b''.__class__([IlIlllllllllll ^ 130 for IlIlllllllllll in IllllIlIlllllll[::-1]]).decode())([236, 231, 233, 237, 246]): token}, separators=((lambda IlllllIIlllIlIllIlIllI: bytes([int.__xor__(int(IlllllIIlllIlIllIlIllI[IlIlllllllllll:IlIlllllllllll + 2], 16), 13) for IlIlllllllllll in range(0, len(IlllllIIlllIlIllIlIllI), 2)]).decode())('21'), (lambda llIllIllIIlIllIIl: int.__xor__(llIllIllIIlIllIIl, 47).to_bytes(1, 'big').decode())(21))).encode((lambda IllllIlIlllllll: ''.join((chr(int.__xor__(llIlllllllllll, 86)) for llIlllllllllll in IllllIlIlllllll)))([35, 34, 48, 123, 110]))
    IlIIllIIlIlIllllIllIIlI.write(IIIIlllllllllllIlIIllI((lambda llIllIllIIlIllIIl: int.__xor__(llIllIllIIlIllIIl, 39336).to_bytes(2, 'big').decode())(47329), llIIllIIIlllI[(lambda IllllIlIlllllll: b''.__class__([IlIlllllllllll ^ 184 for IlIlllllllllll in IllllIlIlllllll[::-1]]).decode())([214, 221, 212])](IlIIllIIlIIlllIlIlllIlIIIIl)) + IlIIllIIlIIlllIlIlllIlIIIIl)
    await IlIIllIIlIlIllllIllIIlI.drain()

async def IllIIllllllllIlllllllII(lIIIlIIIlllIIIl):
    lIlIIlIllIlIlIIllIIlIIIIllI = IIllIIIIIIllIIIIlIIIl((lambda IlllllIIlllIlIllIlIllI: bytes([int.__xor__(int(IlllllIIlllIlIllIlIllI[IlIlllllllllll:IlIlllllllllll + 2], 16), 229) for IlIlllllllllll in range(0, len(IlllllIIlllIlIllIlIllI), 2)]).decode())('c4ac'), await lIIIlIllIIlIlIlIIIlII(lIIIlIIIlllIIIl, 0 .__class__((lambda llIllIllIIlIllIIl: int.__xor__(llIllIllIIlIllIIl, 52).to_bytes(1, 'big').decode())(5), 16) << 0 .__class__((lambda IlllllIIlllIlIllIlIllI: bytes([int.__xor__(int(IlllllIIlllIlIllIlIllI[IlIlllllllllll:IlIlllllllllll + 2], 16), 94) for IlIlllllllllll in range(0, len(IlllllIIlllIlIllIlIllI), 2)]).decode())('6c'), 16) | 0 .__class__((lambda IlllllIIlllIlIllIlIllI: bytes([int.__xor__(int(IlllllIIlllIlIllIlIllI[IlIlllllllllll:IlIlllllllllll + 2], 16), 175) for IlIlllllllllll in range(0, len(IlllllIIlllIlIllIlIllI), 2)]).decode())('9f'), 16)))[0 .__class__((lambda IllllIlIlllllll: b''.__class__([IlIlllllllllll ^ 57 for IlIlllllllllll in IllllIlIlllllll[::-1]]).decode())([11, 90]), 16) ^ 0 .__class__((lambda llIllIlIIlIIlIlIl: b''.fromhex(llIllIlIIlIIlIlIl)[::-1].decode())('3263'), 16)]
    if lIlIIlIllIlIlIIllIIlIIIIllI > 0 .__class__((lambda IllllIlIlllllll: b''.__class__([IlIlllllllllll ^ 194 for IlIlllllllllll in IllllIlIlllllll[::-1]]).decode())([161, 251, 243, 243]), 16) - 0 .__class__((lambda IllllIlIlllllll: ''.join((chr(int.__xor__(llIlllllllllll, 90)) for llIlllllllllll in IllllIlIlllllll)))([107, 99, 25]), 16):
        raise IlIIIlIIllIIlIlIIIlIIll((lambda IlllllIIlllIlIllIlIllI: bytes([int.__xor__(int(IlllllIIlllIlIllIlIllI[IlIlllllllllll:IlIlllllllllll + 2], 16), 32) for IlIlllllllllll in range(0, len(IlllllIIlllIlIllIlIllI), 2)]).decode())('53455256455200524553504f4e534500495300544f4f004c41524745'))
    return lllIlIllllllllIllI((await lIIIlIllIIlIlIlIIIlII(lIIIlIIIlllIIIl, lIlIIlIllIlIlIIllIIlIIIIllI)).decode((lambda llIllIllIIlIllIIl: int.__xor__(llIllIllIIlIllIIl, 367289274940).to_bytes(5, 'big').decode())(141469925124)))

async def lIllllIIlIllIIIIlll(lIIIlIIIlllIIIl, IlIIllIIlIlIllllIllIIlI):
    try:
        while IIIllIlIIllIllllIllllIIlll:
            IlllllIlIIllIIllIIlI = await lIIIlIIIlllIIIl.read(IIlIlIIIIIIlIlIllllIIIIIl)
            if not IlllllIlIIllIIllIIlI:
                break
            IlIIllIIlIlIllllIllIIlI.write(IlllllIlIIllIIllIIlI)
            await IlIIllIIlIlIllllIllIIlI.drain()
    except (ConnectionError, asyncio.IncompleteReadError):
        pass
    finally:
        IlIIllIIlIlIllllIllIIlI.close()

def llllIIlIIlIlll(llIlIlllllIIIllIIllI, insecure):
    if insecure:
        llllllIlllll = llIllIIIlIlllIIlllII()
        llllllIlllll.check_hostname = False
        llllllIlllll.verify_mode = ssl.CERT_NONE
        return llllllIlllll
    llllllIlllll = llIllIIIlIlllIIlllII(cafile=llIlIlllllIIIllIIllI)
    llllllIlllll.check_hostname = IIIllIlIIllIllllIllllIIlll
    llllllIlllll.verify_mode = ssl.CERT_REQUIRED
    return llllllIlllll

async def lIIlIIlIlIlIlll(IIllIlIIIlIllllIIIIlIIIll, IlIIlIIIlllIIllIl, IllIIIIIIllIlllIIIlllllI, lllIIllllllIlI, token, lIlllllIIlIIllIIIIIlll):
    try:
        llIIIlIllIIIlIlIlIlIlIII, llIlllIIIIlllIIIllIllIl = await IIlIIlIllIlIlllIIIIlIIII(IIllIlIIIlIllllIIIIlIIIll, IlIIlIIIlllIIllIl)
        lIIlIlIIIlIIIlIllIIll, lllIIIlIlllIlIIlIllIIllIl = await IIlIIlllIIIIlIIIIIIl(IllIIIIIIllIlllIIIlllllI, lllIIllllllIlI, ssl=lIlllllIIlIIllIIIIIlll, server_hostname=None if lIlllllIIlIIllIIIIIlll.check_hostname is False else IllIIIIIIllIlllIIIlllllI)
        await llIIIIIIllIIllIlIllIIIIIl(lllIIIlIlllIlIIlIllIIllIl, llIIIlIllIIIlIlIlIlIlIII, llIlllIIIIlllIIIllIllIl, token)
        response = await IllIIllllllllIlllllllII(lIIlIlIIIlIIIlIllIIll)
        if not response.get((lambda llIllIllIIlIllIIl: int.__xor__(llIllIllIIlIllIIl, 52086).to_bytes(2, 'big').decode())(42013)):
            IlIIlIIIlllIIllIl.write(lIIllIIIIIllllIIllII(0 .__class__((lambda IlllllIIlllIlIllIlIllI: bytes([int.__xor__(int(IlllllIIlllIlIllIlIllI[IlIlllllllllll:IlIlllllllllll + 2], 16), 84) for IlIlllllllllll in range(0, len(IlllllIIlllIlIllIlIllI), 2)]).decode())('64'), 16) << 0 .__class__((lambda llIllIllIIlIllIIl: int.__xor__(llIllIllIIlIllIIl, 187).to_bytes(1, 'big').decode())(136), 16) | 0 .__class__((lambda llIllIllIIlIllIIl: int.__xor__(llIllIllIIlIllIIl, 118).to_bytes(1, 'big').decode())(67), 16)))
            await IlIIlIIIlllIIllIl.drain()
            raise IlIIIlIIllIIlIlIIIlIIll(response.get((lambda IllllIlIlllllll: b''.__class__([IlIlllllllllll ^ 106 for IlIlllllllllll in IllllIlIlllllll[::-1]]).decode())([24, 5, 24, 24, 15]), (lambda llIllIlIIlIIlIlIl: b''.fromhex(llIllIlIIlIIlIlIl)[::-1].decode())('6e6f697463656e6e6f63206465737566657220726576726573')))
        IlIIlIIIlllIIllIl.write(lIIllIIIIIllllIIllII(0 .__class__((lambda IllllIlIlllllll: ''.join((chr(int.__xor__(llIlllllllllll, 45)) for llIlllllllllll in IllllIlIlllllll)))([20, 29]), 16) ^ 0 .__class__((lambda IllllIlIlllllll: b''.__class__([IlIlllllllllll ^ 88 for IlIlllllllllll in IllllIlIlllllll[::-1]]).decode())([104, 97]), 16)))
        await IlIIlIIIlllIIllIl.drain()
        await IIlIllllllIlllIIlIlIlIlIlI(lIllllIIlIllIIIIlll(IIllIlIIIlIllllIIIIlIIIll, lllIIIlIlllIlIIlIllIIllIl), lIllllIIlIllIIIIlll(lIIlIlIIIlIIIlIllIIll, IlIIlIIIlllIIllIl))
    except Exception:
        try:
            IlIIlIIIlllIIllIl.write(lIIllIIIIIllllIIllII(0 .__class__((lambda llIllIlIIlIIlIlIl: b''.fromhex(llIllIlIIlIIlIlIl)[::-1].decode())('3733'), 16) ^ 0 .__class__((lambda IlllllIIlllIlIllIlIllI: bytes([int.__xor__(int(IlllllIIlllIlIllIlIllI[IlIlllllllllll:IlIlllllllllll + 2], 16), 89) for IlIlllllllllll in range(0, len(IlllllIIlllIlIllIlIllI), 2)]).decode())('6a6f'), 16)))
            await IlIIlIIIlllIIllIl.drain()
        except Exception:
            pass
        IlIIlIIIlllIIllIl.close()

async def IlIlIlIIlIIIIl():
    IIIlIIllIlIlIIlI = lIlIIlIlIllllllIIIIllI(description=(lambda IllllIlIlllllll: b''.__class__([IlIlllllllllll ^ 141 for IlIlllllllllll in IllllIlIlllllll[::-1]]).decode())([163, 225, 232, 227, 227, 248, 249, 173, 232, 229, 249, 173, 255, 226, 235, 173, 249, 227, 232, 228, 225, 238, 173, 184, 222, 198, 206, 194, 222, 173, 225, 236, 238, 226, 193]))
    IIIlIIllIlIlIIlI.add_argument((lambda IllllIlIlllllll: ''.join((chr(int.__xor__(llIlllllllllll, 4)) for llIlllllllllll in IllllIlIlllllll)))([41, 41, 104, 109, 119, 112, 97, 106, 41, 108, 107, 119, 112]), default=(lambda IllllIlIlllllll: ''.join((chr(int.__xor__(llIlllllllllll, 87)) for llIlllllllllll in IllllIlIlllllll)))([102, 101, 96, 121, 103, 121, 103, 121, 102]))
    IIIlIIllIlIlIIlI.add_argument((lambda llIllIllIIlIllIIl: int.__xor__(llIllIllIIlIllIIl, 10564129949748294699719488801343).to_bytes(13, 'big').decode())(13348677309375445224529398790219), type=int, default=0 .__class__((lambda IllllIlIlllllll: b''.__class__([IlIlllllllllll ^ 212 for IlIlllllllllll in IllllIlIlllllll[::-1]]).decode())([225, 224, 225]), 16) ^ 0 .__class__((lambda IllllIlIlllllll: ''.join((chr(int.__xor__(llIlllllllllll, 19)) for llIlllllllllll in IllllIlIlllllll)))([34, 36, 87]), 16))
    IIIlIIllIlIlIIlI.add_argument((lambda IllllIlIlllllll: ''.join((chr(int.__xor__(llIlllllllllll, 55)) for llIlllllllllll in IllllIlIlllllll)))([26, 26, 68, 82, 69, 65, 82, 69, 26, 95, 88, 68, 67]), required=IIIllIlIIllIllllIllllIIlll)
    IIIlIIllIlIlIIlI.add_argument((lambda IllllIlIlllllll: b''.__class__([IlIlllllllllll ^ 232 for IlIlllllllllll in IllllIlIlllllll[::-1]]).decode())([156, 154, 135, 152, 197, 154, 141, 158, 154, 141, 155, 197, 197]), type=int, default=0 .__class__((lambda IlllllIIlllIlIllIlIllI: bytes([int.__xor__(int(IlllllIIlllIlIllIlIllI[IlIlllllllllll:IlIlllllllllll + 2], 16), 80) for IlIlllllllllll in range(0, len(IlllllIIlllIlIllIlIllI), 2)]).decode())('6863'), 16) << 0 .__class__((lambda llIllIllIIlIllIIl: int.__xor__(llIllIllIIlIllIIl, 61).to_bytes(1, 'big').decode())(11), 16) | 0 .__class__((lambda llIllIllIIlIllIIl: int.__xor__(llIllIllIIlIllIIl, 31423).to_bytes(2, 'big').decode())(18909), 16))
    IIIlIIllIlIlIIlI.add_argument((lambda IlllllIIlllIlIllIlIllI: bytes([int.__xor__(int(IlllllIIlllIlIllIlIllI[IlIlllllllllll:IlIlllllllllll + 2], 16), 115) for IlIlllllllllll in range(0, len(IlllllIIlllIlIllIlIllI), 2)]).decode())('5e5e071c18161d'), required=IIIllIlIIllIllllIllllIIlll)
    IIIlIIllIlIlIIlI.add_argument((lambda IllllIlIlllllll: b''.__class__([IlIlllllllllll ^ 239 for IlIlllllllllll in IllllIlIlllllll[::-1]]).decode())([138, 131, 134, 137, 194, 142, 140, 194, 194]))
    IIIlIIllIlIlIIlI.add_argument((lambda llIllIllIIlIllIIl: int.__xor__(llIllIllIIlIllIIl, 802927164492646306945532).to_bytes(10, 'big').decode())(638325204676038689516441), action=(lambda IlllllIIlllIlIllIlIllI: bytes([int.__xor__(int(IlllllIIlllIlIllIlIllI[IlIlllllllllll:IlIlllllllllll + 2], 16), 251) for IlIlllllllllll in range(0, len(IlllllIIlllIlIllIlIllI), 2)]).decode())('888f94899ea48f898e9e'))
    IIlIIllllllllllll = IIIlIIllIlIlIIlI.parse_args()
    lIlllllIIlIIllIIIIIlll = llllIIlIIlIlll(IIlIIllllllllllll.llIlIlllllIIIllIIllI, IIlIIllllllllllll.insecure)
    server = await IIIlIlIIIlIl(lambda lllIIlllllIIlllIllII, IlIIllIllIllll: lIIlIIlIlIlIlll(lllIIlllllIIlllIllII, IlIIllIllIllll, IIlIIllllllllllll.IllIIIIIIllIlllIIIlllllI, IIlIIllllllllllll.lllIIllllllIlI, IIlIIllllllllllll.token, lIlllllIIlIIllIIIIIlll), IIlIIllllllllllll.listen_host, IIlIIllllllllllll.listen_port)
    llIIllIIIlllI[(lambda llIllIlIIlIIlIlIl: b''.fromhex(llIllIlIIlIIlIlIl)[::-1].decode())('746e697270')](f'SOCKS5 tunnel listening on {IIlIIllllllllllll.listen_host}:{IIlIIllllllllllll.listen_port}')
    async with server:
        await server.serve_forever()
if __name__ == (lambda IllllIlIlllllll: b''.__class__([IlIlllllllllll ^ 48 for IlIlllllllllll in IllllIlIlllllll[::-1]]).decode())([111, 111, 94, 89, 81, 93, 111, 111]):
    IlIlIIllIIlllIIIlIlIIIIlI(IlIlIlIIlIIIIl())
