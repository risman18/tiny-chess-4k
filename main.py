import json,os,urllib.request as U
V=dict(zip('PNBRQK',(88,309,331,494,980,20000)))
S=(-11,-9,9,11,-10,-1,1,10);D={'N':(-21,-19,-12,-8,8,12,19,21),'B':S[:4],'R':S[4:],'Q':S,'K':S}
TS=dict(zip('PNBRQK','77777777SVMNMQKI@BBACBB=9;9:99:668678784576677:5586679;477777777|!*2/:+/"-2<:8;500;<>?C<749;?=?:747:;;;942689:87300567731*0/2320.|35.342644865:<816:;;:=;768:=<<8769:;;9876899::876787889416345433|;<<>?9;<;;>>?>:<7::;9;=8569::;6545777674255576622556675046798642|39<;@=<=35:;;?=<469=?@>>578:===;478;::;945777998145666344244512.|)674058799688:557;977<>65787788407655551456556634772467607615374'.split('|')))
SG={}
for p,t in TS.items():
 SG[p]=[0]*120;SG[p.lower()]=[0]*120
 for q in range(64):
  v=V[p]+(ord(t[q])-55)*5;SG[p][(q//8)*10+q%8+21]=v;SG[p.lower()][91-(q//8)*10+q%8]=-v
def gen(b,cs,ep):
 for i,c in enumerate(b):
  if c=='P':
   for d in(-11,-10,-9):
    j=i+d;t=b[j]
    if t=='.' if d==-10 else t in 'pnbrqk' or j==ep:
     yield i,j,'Q' if j<30 else ''
   if i>80 and b[i-10]==b[i-20]=='.':yield i,i-20,''
  elif c in 'NKBRQ':
   for d in D[c]:
    j=i+d
    while True:
     t=b[j]
     if t=='.':
      yield i,j,''
      if c in 'NK':break
      j+=d;continue
     if t in 'pnbrqk':yield i,j,''
     break
 for c2,r,t,e in((0,98,97,(96,97)),(1,91,93,(92,93,94))):
  if cs[c2] and b[95]=='K' and b[r]=='R' and all(b[x]=='.'for x in e):yield 95,t,''
def ap(b,cs,ep,m):
 i,j,pr=m;c=b[i];n=b[:i]+'.'+b[i+1:];n=n[:j]+(pr or c)+n[j+1:];ne=None
 if c=='P':
  if j==ep and b[j]=='.':n=n[:j+10]+'.'+n[j+11:]
  elif i-j==20:ne=i-10
 if c=='K' and abs(j-i)==2:
  r=(98,96)if j>i else(91,94);n=n[:r[0]]+'.'+n[r[0]+1:];n=n[:r[1]]+'R'+n[r[1]+1:]
 a,bb,o,p=cs
 if c=='K':a=bb=0
 if c=='R':a*=i!=98;bb*=i!=91
 return n,(a,bb,o*(j!=28),p*(j!=21)),ne
def fl(b,cs,ep):return ''.join(b[i:i+10] for i in range(110,-1,-10)).swapcase(),(cs[2],cs[3],cs[0],cs[1]),None if ep is None else vm(ep)
def atk(b):
 k=b.index('K')
 if 'p'in(b[k-9],b[k-11])or any(b[k+d]=='n' for d in D['N']):return 1
 for d in S:
  j=k+d
  while b[j]=='.':j+=d
  if b[k+d]=='k'or b[j] in('bq' if abs(d)in(9,11)else 'rq'):return 1
 return 0
M=10**5
nd=0;cap=120000;TT={};KL={}
def qs(b,cs,ep,a,be,q):
 global nd;nd+=1
 if nd>cap:raise IndexError
 ic=q<1 and atk(b)
 if not ic:
  s=sum(SG[c][i] for i,c in enumerate(b) if c in SG)
  if s>=be:return be
  if s>a:a=s
 ms=[m for m in gen(b,cs,ep) if m[2]or m[1]==ep or ic or(b[m[1]]in'pnbrqk'and V[b[m[1]].upper()]+250>=V[b[m[0]]])]
 for m in ms:
  if b[m[1]]=='k':return M
  s=-qs(*fl(*ap(b,cs,ep,m)),-be,-a,q+1)
  if s>=be:return be
  if s>a:a=s
 return -M if ic and not ms else a
def sr(b,cs,ep,d,a,be):
 global nd;nd+=1
 if nd>cap:raise IndexError
 if d<=0:return qs(b,cs,ep,a,be,0)
 k=(b,cs,ep);tm=TT.get(k);ms=list(gen(b,cs,ep))
 ms.sort(key=lambda m:(m!=tm,-(V[b[m[1]].upper()]if b[m[1]]in'pnbrqk'else V.get(m[2],0)),m not in KL.get(d,())));bm=None
 for m in ms:
  if b[m[1]]=='k':return M
  s=-sr(*fl(*ap(b,cs,ep,m)),d-1,-be,-a)
  if s>a:a=s;bm=m
  if a>=be:
   if b[m[1]]not in'pnbrqk':KL.setdefault(d,set()).add(m)
   break
 TT[k]=bm
 return a
def sq(s):return (10-int(s[1]))*10+ord(s[0])-96
def pf(fen):
 ps=fen.split();s=ps[0]
 for d in '12345678':s=s.replace(d,'.'*int(d))
 b=' '*21+'  '.join(s.split('/'))+' '*21
 cs=tuple(x in ps[2] for x in 'KQkq');ep=sq(ps[3]) if ps[3]!='-' else None
 if ps[1]=='b':b,cs,ep=fl(b,cs,ep)
 return b,cs,ep,ps[1]
vm=lambda i:(11-i//10)*10+i%10
def choose(fen,L):
 global nd
 b,cs,ep,tn=pf(fen)
 rt=[(u,(sq(u),sq(u[2:]),u[4:].upper()))for u in L]
 if tn=='b':rt=[(u,(vm(m[0]),vm(m[1]),m[2]))for u,m in rt]
 nd=0;bu=rt[0][0]
 for d in range(1,30):
  rt.sort(key=lambda t:t[0]!=bu)
  try:
   a=-M-1
   for u,m in rt:
    s=-sr(*fl(*ap(b,cs,ep,m)),d-1,-M-1,-a)
    if s>a:a=s;bu=u
  except IndexError:break
 return bu
EU=os.environ['MAKEFUN_ENV_URL']
def post(p,b):return json.load(U.urlopen(EU+p,json.dumps(b).encode()))
while True:
 g=post('/game',{})
 if g['status']=='done':break
 while g['status']=='your_move':
  lm=g['legal_moves']
  try:mv=choose(g['fen'],lm)
  except:mv=lm[0]
  g=post('/move',{'game':g['game'],'move':mv})