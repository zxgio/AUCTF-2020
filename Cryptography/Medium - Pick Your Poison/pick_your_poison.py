#references:
# https://crypto.stackexchange.com/questions/18631/chosen-plaintext-attack-on-textbook-rsa-decryption
# applied cryptography, Schneier

import sys

n = 10221357148514336684111571397474179139093198252188953889343506516423709613718895061478720691981867849170787294195745723433520727656626277340717251893118927
e = 65537
d = 7904836439191611463715319357150636975842648583455833177098223664165575135933232094087493738937385495472344976450600376134806845564323099973819842116336705
flag = 'auctf{D0nT_5igN_r4nd0m_Cr4P_w1tH_y0uR_pr1vAT3_k3y_d00d}'
pub = (n,e)
priv = (n,d)

enc = [8978389248978338034309953768380336384357866486977211921110763631015762911953285026606846346990877597310734105139662779843431848891846422126202795577821536, 2448211090977504314591281359347662288532053371504697017669328198650362138468795424653794231870404998654050969071089638492547899406576880451735032665053415, 5073868553642007541037382560266122348116066932939519429466409436521020082796309108136148876922563304842137108184071351490764646620586256568322131086730471, 1684005565938636347148651183499352991968259344473546208552703035081802195353025784333914992504943690420410774660082414458844955313305386683009869967486601, 9688056522476045734880233753061752908386549597508196003184047035939370924476476516136840749335828486617027498640359137909620415259940325638500074995757481, 4918987431298937066704112000215903078103748640095041023549040696896815095947072020028293483151784998677212418289906638213160264741104646453384074063521792, 8593777289443568375823034466520277641424749851512233551628579437816165423157292246008761312262610891122718159724804135859723321115578130467596229705428843, 8484666758211615026797998942402424346301966799583675181538298484204880370290033018724243648059678151446054251579700329595981607949497499335435499752484005, 308394980388651850045113217576537313482545112249694258661743866313455096362758075227867869714781094418335514368399281611453415772649409354839236417463034, 7222561693035183317939799370452547261489852774503733521495532016312174265825247590460570991538147486504899944049357485797281273740558123366840011333855861, 8764211673077276911580049002194203275110775854026649658891117745329313494122187728508791353400340684438271855390345226496201817120306064057097120594244449, 1525706348605296719795367548319235591425685977296587923981931346280437224966840784381546611884291756431319382322085757444318162241739389789300558663127971, 9042476810664190988979962995658660625221988719661614429315294422664984939900872337615754049522514891060506613557194150664969331992683598571210341612667081, 5573610559829704254254970052048798111899653692559529597079581870880152965063438906641115166650757927060289266359201478309460055279596866206180134177194052, 5997032928834757975345830513279787029141906960493878610251437820689760009956181524409535055917506125192739484936615881055153790127175763005626940179934481, 8764211673077276911580049002194203275110775854026649658891117745329313494122187728508791353400340684438271855390345226496201817120306064057097120594244449, 3072093814632334677016885991224059539791286231968695860693599418318777454342743444981847451981735377416191582023877333001187098655891884494761145027811099, 4409363874096421231130160580892683023085889519975285004079551934717184316599673212332129926417842319107222100249528345572378878233344713135736163695123553, 308394980388651850045113217576537313482545112249694258661743866313455096362758075227867869714781094418335514368399281611453415772649409354839236417463034, 8471051308249972738685410995699762364601031636092478757220464501716470617436401595397130332730301404350693145842639921823041717805482218454235349240079369, 8484666758211615026797998942402424346301966799583675181538298484204880370290033018724243648059678151446054251579700329595981607949497499335435499752484005, 1892729392836146512546104825955987261308911568877315805980584997481031457988019103205983228488881541767074294908633617939913201375646443515814805712092276, 8764211673077276911580049002194203275110775854026649658891117745329313494122187728508791353400340684438271855390345226496201817120306064057097120594244449, 8924728162299432989991037199542376340467732311323845888628737296234400945283222133297106115637705263582854244187362503246189856041798348761851631784694335, 3072093814632334677016885991224059539791286231968695860693599418318777454342743444981847451981735377416191582023877333001187098655891884494761145027811099, 4409363874096421231130160580892683023085889519975285004079551934717184316599673212332129926417842319107222100249528345572378878233344713135736163695123553, 9297943974098673590307080997773019882537588307205294802229376188123292091353775908887174636541706910611124696665467141425564562425938468850553771227013866, 8764211673077276911580049002194203275110775854026649658891117745329313494122187728508791353400340684438271855390345226496201817120306064057097120594244449, 5293786978507820383162334283403054776584415228619270805370919518885915179529902031810412433124286953640570794900656676025713249074097705987383995921354939, 8067250983643235828836760732787757580544623783606045241457137079778274386864121700142772654604006958040270077684100437351360806915101461266277344720047604, 1684005565938636347148651183499352991968259344473546208552703035081802195353025784333914992504943690420410774660082414458844955313305386683009869967486601, 5389714014543748153818548674237484309951728219587249809796190773201064158961318669719961027413461891793500029215880423642438867145923122922274998344308985, 8764211673077276911580049002194203275110775854026649658891117745329313494122187728508791353400340684438271855390345226496201817120306064057097120594244449, 5867324943689989748224346315874714431061534794156720378227907668168298633030217916431751674791892946854045771148350932300336003862671514196590545640396104, 8484666758211615026797998942402424346301966799583675181538298484204880370290033018724243648059678151446054251579700329595981607949497499335435499752484005, 2448211090977504314591281359347662288532053371504697017669328198650362138468795424653794231870404998654050969071089638492547899406576880451735032665053415, 3159497745702164627257356413032926095273215453723128751822502842103132100048547046507797829727039508789484826536974050396170606111178867433209452595762071, 8764211673077276911580049002194203275110775854026649658891117745329313494122187728508791353400340684438271855390345226496201817120306064057097120594244449, 8446312898272377013144682233006266143075154732870696052606975729890311415806374255462557568344302449494686591780755644452586883419701389851445816803457753, 3072093814632334677016885991224059539791286231968695860693599418318777454342743444981847451981735377416191582023877333001187098655891884494761145027811099, 8067250983643235828836760732787757580544623783606045241457137079778274386864121700142772654604006958040270077684100437351360806915101461266277344720047604, 1014599519833738717545873593360162890157893035197783380110724692525047008109852068814021506323779464277323143935111618947314696159728907150302569375379234, 368602340785698643006246242781528989713269926996861558041237835015174312853226660780824616503539083415377971242383717302696264171494417150892900578556123, 7222561693035183317939799370452547261489852774503733521495532016312174265825247590460570991538147486504899944049357485797281273740558123366840011333855861, 5293653939308704136313578556004514924199912544822219413428198541005999557176948606212500561518409652659531226935786970834627918809291941837645336019697631, 8764211673077276911580049002194203275110775854026649658891117745329313494122187728508791353400340684438271855390345226496201817120306064057097120594244449, 6538310645414424249873196014956652324979245657339756776291194602473587141026424963680552278355926179330067858372483892298424394447485720977355788078531056, 5293653939308704136313578556004514924199912544822219413428198541005999557176948606212500561518409652659531226935786970834627918809291941837645336019697631, 5867324943689989748224346315874714431061534794156720378227907668168298633030217916431751674791892946854045771148350932300336003862671514196590545640396104, 8764211673077276911580049002194203275110775854026649658891117745329313494122187728508791353400340684438271855390345226496201817120306064057097120594244449, 8471051308249972738685410995699762364601031636092478757220464501716470617436401595397130332730301404350693145842639921823041717805482218454235349240079369, 8484666758211615026797998942402424346301966799583675181538298484204880370290033018724243648059678151446054251579700329595981607949497499335435499752484005, 8484666758211615026797998942402424346301966799583675181538298484204880370290033018724243648059678151446054251579700329595981607949497499335435499752484005, 8471051308249972738685410995699762364601031636092478757220464501716470617436401595397130332730301404350693145842639921823041717805482218454235349240079369, 5251475613897619674914684730897474760039912098976341266767762217309825485363167860697615792935766568539006941927656577582201123235103683963530531839639593]


def main():
    r = input("Please give me something to sign: ")
    if r in enc:
        print("nope")
    else:
        print(encrypt(r, priv))

def encrypt(msg, key):
    n = key[0]
    e = key[1]
    ciphertext = []
    format = type(msg)
    if format == int:
        ciphertext.append(_encrypt_letter(msg, n, e))
    if format == str:
        for letter in msg:
            ciphertext.append(_encrypt_letter(letter, n, e))
    return ciphertext

def _encrypt_letter(letter, n, e):
    if type(letter) == int:
        return pow(letter, e, n)
    else:
        return pow(ord(letter), e, n)

def decrypt(ciphertext, priv_key):
    n=priv_key[0]
    d = priv_key[1]
    plaintext = []
    for letter in ciphertext:
        plaintext.append(_decrypt_letter(letter, n, d))
    return ''.join(plaintext)

def _decrypt_letter(letter, n, d):
    if type(letter) == int:
        return chr(pow(letter, d, n))
    else:
        return chr(pow(int(letter), d, n))

if __name__ == '__main__':
    main()