
import math
#p=31093551302922880999883020803665536616272147022877428745314830867519351013248914244880101094365815998050115415308439610066700139164376274980650005150267949853671653233491784289493988946869396093730966325659249796545878080119206283512342980854475734097108975670778836003822789405498941374798016753689377992355122774401780930185598458240894362246194248623911382284169677595864501475308194644140602272961699230282993020507668939980205079239221924230430230318076991507619960330144745307022538024878444458717587446601559546292026245318907293584609320115374632235270795633933755350928537598242214216674496409625928797450473
#q=31093551302922880999883020803665536616272147022877428745314830867519351013248914244880101094365815998050115415308439610066700139164376274980650005150267949853671653233491784289493988946869396093730966325659249796545878080119206283512342980854475734097108975670778836003822789405498941374798016753689377992355122774401780930185598458240894362246194248623911382284169677595864501475308194644140602272961699230282993020507668939980205079239221924230430230318076991507619960330144745307022538024878444458717587446601559546292026245318907293584609320115374632235270795633933755350928537598242214216674496409625928997877221
#q=8683574289808398551680690596312519188712344019929990563696863014403818356652403139359303583094623893591695801854572600022831462919735839793929311522108161
#p=8683574289808398551680690596312519188712344019929990563696863014403818356652403139359303583094623893591695801854572600022831462919735839793929311522108161
q=5
p=7


#e=65537
e=5
#c=168502910088858295634315070244377409556567637139736308082186369003227771936407321783557795624279162162305200436446903976385948677897665466290852769877562167487142385308027341639816401055081820497002018908896202860342391029082581621987305533097386652183849657065952062433988387640990383623264405525144003500286531262674315900537001845043225363148359766771033899680111076181672797077410584747509581932045540801777738548872747597899965366950827505529432483779821158152928899947837196391555666165486441878183288008753561108995715961920472927844877569855940505148843530998878113722830427807926679324241141182238903567682042410145345551889442158895157875798990903715105782682083886461661307063583447696168828687126956147955886493383805513557604179029050981678755054945607866353195793654108403939242723861651919152369923904002966873994811826391080318146260416978499377182540684409790357257490816203138499369634490897553227763563553981246891677613446390134477832143175248992161641698011195968792105201847976082322786623390242470226740685822218140263182024226228692159380557661591633072091945077334191987860262448385123599459647228562137369178069072804498049463136233856337817385977990145571042231795332995523988174895432819872832170029690848
#c=9560634911497745583378708911423730041871108408354273851105442823652482446584728244370275783778971812977745029111313416532500401836444585708475658254699672285618254670808419777671613020408027434193662041848593393740726639973784613890042844233861571190841541366812077582649290826487514627722655599040743377675
c=10
n=p*q
fn=long((p-1)*(q-1))

i = 1
while(True):
    x=(i*fn)+1
    if(x%e==0):
        d=x/e
        break
    i=i+1
print(pow(c,d,n))

    
