from collections import defaultdict

def split(num):
    num = str(num) 
    mid = len(num)//2 
    return [ int(num[:mid]), int(num[mid:])  ]

dp = defaultdict(int)

stones = [0, 7, 198844, 5687836, 58, 2478, 25475, 894] 
for stone in stones: # this could be table dp
    dp[(stone, 0)] += 1 # inital

blinks = 75

# stone, step, cnt
# 
# check the previous record = step - 1
# current key number += prev(step-1) 


for blink in range(1, blinks+1):
    nxt_dp = defaultdict(int)
    for (stone, step), count in dp.items():
        if blink == step+1:
            if stone == 0:
                nxt_dp[(1, blink)] += count  # this is to update the previous records, form a new string
            elif len(str(stone)) % 2 == 0: 
                a, b = split(stone)
                nxt_dp[(a, blink)] += count
                nxt_dp[(b, blink)] += count
            else:
                nxt_dp[(stone*2024, blink)] += count
    dp = nxt_dp

print(len(dp))
print(sum( count for (a, b), count in dp.items() if b == blinks))
                





# def simulate_stones_dp(initial_stones, blinks):
#     """
#     Simulate the evolution of stones based on the rules using dynamic programming.

#     Parameters:
#         initial_stones (list of int): The initial stones.
#         blinks (int): The number of blinks to simulate.

#     Returns:
#         int: Total number of stones after the specified number of blinks.
#     """
#     from collections import defaultdict

#     def split_number(num):
#         """Split a number with an even number of digits."""
#         num_str = str(num)
#         mid = len(num_str) // 2
#         left = int(num_str[:mid])
#         right = int(num_str[mid:])
#         return left, right

#     # Dynamic programming table to track stone counts by value and blink step
#     dp = defaultdict(int)

#     # Initialize DP with the count of the initial stones
#     for stone in initial_stones:
#         dp[(stone, 0)] += 1 #stone number and current step , current count at step 0 is 1

#     # Track counts for each blink
#     for blink in range(1, blinks + 1): #total range of blinks
#         next_dp = defaultdict(int) # current iteration 
#         for (stone, step), count in dp.items():  # existing dp   
#             if step == blink - 1:  # Process stones from the previous blink
#                 if stone == 0:
#                     next_dp[(1, blink)] += count  # Rule 1, for stone 
#                 elif len(str(stone)) % 2 == 0:  # Rule 2
#                     left, right = split_number(stone)
#                     next_dp[(left, blink)] += count
#                     next_dp[(right, blink)] += count
#                 else:
#                     next_dp[(stone * 2024, blink)] += count  # Rule 3
#         dp = next_dp
#     # Total stones after the final blink
#     return sum(count for (stone, step), count in dp.items() if step == blinks)

# # Example usage
# if __name__ == "__main__":
#     # Initial stones from the problem
#     initial_stones = [0, 7, 198844, 5687836, 58, 2478, 25475, 894]

#     # Number of blinks for part 2
#     blinks = 75

#     # Calculate the total number of stones after the specified blinks using DP
#     total_stones = simulate_stones_dp(initial_stones, blinks)
#     print(f"Total number of stones after {blinks} blinks: {total_stones}")



# # input = "2333133121414131402"
# input = "4799935813741734388396718272884368753489109116876896165195936891424450717191685132736126746750181960476552308839526828877147316844591649931720174496953068926139549112138231984842811415641461958532623088186536549482634914941471443590487076967598272945344710168085756021694840122715643211898823847295639938588023236490875264961515963010539974484426312296399661724683521454379827969494425769938668791924282023247854667627548935142166144772223966647568715449558137691234646538573120213038196423161366271449969776278896883569239834325385665157232296614384158525144322477962869187698847752462518152262316586615815478732633402362553083693387972449919194417286355138552962432873193276699449912097249914217288968952645832261629109382209693222072413851528963602229572164949186213210205740221712796369198977681779985082549419578351125392875062539438541868944256199850785265318171623040646929578531593761738073908280888896342178797851883757316042962284599223411425502255336286174646145916845582666468187398557628805256419947877630292028185137857129884348837461621681284691504413213298702085294733285669808526445510351560224737195595134563194248837262463727345690969650879585528814493888354317686519581318878272505321585269628156997849639475496672844686933689916127981661853547945766347792445174104923661743871039847358256367521969133151786597123654283649199559742217827833197133518667494452146453117127847944431473361893637971849848195216562924324372472767947155237194657379826159306258794528612652442353196417139473787217492654785186293044388973942352693268336786728935237378176659281676537960725271198858373264235189319522882679679411998149172060146175416031697130148061579273218944882550842222548292125556802458298531727348151257747598557063898515493488164091804884365875945073704020762154627085746211714789577098473273698831415452596819641233513889416062829749592756242097516136196193637827617054278441475665932673783668741793853785107953653225588915259056673096475529127092952425838325478767102644393496767190487183707537549373833466332969258470907386606836313691356140855891595943905454588210342199409641774094549877501564119779386989908134911398335219348971529198394844698281543556309797286639979654807336624255487948803170299247535657587661102931374682457661597510628255891849325147377974625367311492953952843256913320544691932385152737342060817957773319284720839447814597555736227185314055819063968242567219803945428614178924984078318970376688871178158891387599951514395931602854931566834198334145843019291764674986331868555559112297667281814486162034252796743848644928524918159241185115967673826449573153674043206355352141355931748018688095714493675046412671543763217429175174545456885032626782561361722129469637514257893337744241947972632331806853798050626662883317501659922222998753135188833438604895993929158184865242932259827639721648137061316696489527272468814333788687685143978776193889717564585662876312882295672586614373282860293276763752971210254019416146944019629414359250429654158463261931917643918755387045266170854630438369538661861345637283471881731539467255496726484816916097882872747086482990662431397431655674638029584771194351657252721828362561959487671863783522829548574637387358999257668481429675825222831357316610258592864060915595811161375041147456353053108955915239966278477738623899773297164810341385496523768226438018649370617314779868152093634167847586259785414411387075304281932944855980942589693471283334872059539998626681496286504995386791205330492032641028789544189290112926404379671842858458418454246368387033811810603095315099802156257929921059719830871237901761678324832016374653233317439627906093259970525870205442832173721839304183746233173255651411828947411238371248986663207463563024938677949948285230624379247832422526252255809137738021675663999946168426855986838776775725767396314159974948157771399882927385504287516057782836439691269488315033239261406790769961405637775431657140507391942382702223497584402488106342516476352840426486732169555519926248879861902422846031862756387789144945553611638144705727373232715737945116906993969829973382983524981087456185881731278490665160677738404320568292653782216119352943455097722841251956246518528530533728464128817277149641979112702923251417812055264049434159325411926957171722473128888944117111415112206175744171251213204431298452978250963686576995531720948175673847985084949629715786228443336717607047995944545817201861577391588784446374177896131883486815268196718692928218481571286345153645809030433885315752843717902682707277505770979257771310192681698938427537877479454839844280314153313348578578628878826148258193645825816075492264916660136759608446943387985139719090851517622023218927159990844950355147591157627464344324291490798890573030631170593452173499536061996670538788986166687981781292493775839944295347686991365848746165496434902135346757783673798353651568956080907633335942645083515524501447256719231093188056752230632923128437175477247059195051281689984474686260603075941251478585441670468425633834336298107068266223453065642148631974952180222083235125468684268899471315914078561430371976378236327651347099437969501850167271387724449291424877321454787790745526584936946528542618545242456343418545335870279680362078453472631646717720714656841073738831747417332973575223221639756874568765818618782785295693428667588760228256903068208635422072629591959314261467773233929589561289462780526297804458298151457718704962293797494150398486222746292196459750274024757817555747702041857051763528268948784633822698213369526224777462185451197173204032268153819177826222367970918030168723193936189577141489917967937227987789623783635074808256709294248076818759428936797432591734678891833426489432455071971220945647551355818840976970465546233255477625211832832774234080594265257313394163345598914891493670461764445519385660317588903515528841816342539985809311313963193333756614652165511570418824573791395824964357663325288157154442658455574285317540258855152633599583576345966497254298332251151729845377251099824455984686408888149586104222393142853429441832583453576365715393415986182118686324947321366633557882404097697614299675563847609751417686933851332030707663809595551877203555484485282820589442702021641841589284514668114279218259475615145116524667312818789075641616154674323748817637887930523077236873268473139936485291826746208066864348953521383112151417705628736525702262643768735173684347916782581523129046271329859640538214597960314018719284691331129753715380777322408945493051831779305975644259644699387157829850757228212246126551453585228154361490413650756056594692374853281194854256463024549733128127606953706085849747847947958385608990108250191270814184188014507268954588494783434973882535625192851787961995151344176239967338602261885276633493228629106239237018358626741929532329781639884324407957904767503427765975276914428221558721892779122615613760172794417757853315543646969686753376385475919539977749775213125117891535852890561621189073739374887171426228802877529118396839321820148175595323888770299933785499613537872834728132374559149173191377373392261581618623529587691746536970162882176350873159733758746164524134949328799947409687126940118345639983807698538510406197927418939595134971774688281818487070315289927798923475769392186226103631253154734726671214984435683916544217457224882370488051613254813851421573581394459158331818321193116486511660849458519595231634418877796346166768226032334583449918403567358552335662156535487330597826574685865710566520195928916966218763624215742242294851719831762414674911206967941168507943541231862234909298837033122253557995801254707978727512418728959059795815732072985435601371155082975373637866278991395622652083813989987633444878421796476227184230965250136394419196568743486859724231904746875916237595252833785491847918553153903133894874163871138632471257448259451780577765499068877490391292134353709199716352276724624163165041757876122040334426952280898080212692838187738417207868184233711987357865599513656633278491236036272862116767595963582929671524588599318910255035456797421258623562428224399963706862116339996935454694783842512738364990548021505532648575993661701929158534407616947424968891609070519615774349637972786869167822606318661530537726649375771546779338995024669720449246414318617964712899418831761331196995193815233743943113215566161239432452182690476035867452775317485341303346189677141146161016558297175279477286527175792621323644906176535295754599763747999888678848454139646714867983796846652488856061613687134444998214883748281093658751708159781292666558412352817670985717692835354268653712836964626898717316201618501857353331803528594218624765862485852749112665192449179415809761283115498988244786149754246158914955517793572688636855802980596794937498411965677448464137924398888915678713858542905897672432132139323114876931314691164780797973855138912894957528118178304976345190682375952125647624523161122169779784668278951892383272922275211253705857195636593086235972643799521642366084122353489057501217149485744911903455265367126316765058156287883315317010499948408699511258256796301915298471909965929327279813406494836890984123864556826433618897588589937671833175165753733254405596233825333659301155867155524874621219701051245685916353495872335761826231157617956097102054126036771462884046547762945863878224615387295678634777123878451671337810283983228712981499289189792619755312883959551754822555179444146188379142833631223223967564833343949682534457451079792139421267168416459199576030494270956199795573771598886730342993372985126825908998221441931569157998972126371838787130133767741384218785573959577855933515514625912566358012831128108153175812137039798919805622993277158841579498782834173978805599509285908421519211336834574426925366233071512482364785847585812735486867688256787676292952938424236771854029251470355288944919929740791078812314195658673527688775608957401616663566191456447723608834424789676639998972429566671873327874801860573335527696371433547639212062953919554967333414405186836468467044648914901356783777666036775767542975991615959214339923751728178477656489772643807345929796595145398979263740294372168951529775226232756158192837181376397165403545683256872617348349314982132984571867415120901429404761681371889936289961781532973936441438885171335166799011609372533646743165227252388026536473923641673129258936292492409247541424585119432344592475487889686597861745794167622910701651735726606249344034642977718371559916836559978978673171936069307752888655185515818189466481949717443374276143105845754826541373832326894063505730995267245272881197396521888684384853318155858956393181213552691855706720882659919813347435939933373881547610674940721518931742852232296728414490388692858514613366971755426519185723724877274554759351227343827978839270357258276295671737677767659288455159502670253046775681604611802961177369825144524317874218483368211862422664608677161530731814736621578472975273786018841957343932837796638141796685145385593737333815221671687015682482495044789794688643599648535296852467696649291233484913957183968667645789942110774460111386531222336213271532557144545518912630123699968410809625399077525774155374249450851496571053526645541393442047768453763322798894296386369984625620952750125968757674496742972925104197355539756715867042297518596030287945684122822595115032843688884255866291797129711125287250576986511731333015203550153632937511323131244026514174332844509951289356101798653378635815571017356775959123747012595455566292692673842711247680957447495531544056484573176020225654789081824274105822958220109442252230775469354396653157598417841848516965383812373434699434523117852528904656415825833290375893219537547824896252162627917258717365608057514353792013392417393350494718149933922819951439437193357492703766165565834595315493203521273569331056667215916888629754489770224619758391818460798911746980673798586045415220185586804588323389685170965652877560206749946777376450857845248049727598612573518180825586102299531637927072121626133483796548815579304682707142122199331344933770929682955421572097183873985832828716929924807416417338644458331976991720315819437949932364244351702634858465608122716236424056996686159344311753421758709365953264978219337995715220426276761585762520654182462665104514641591506255837240682066259490761180368548943417101133352811233710606896689493304328648350189926895274679868735145781141658855698249336566163159208644212958785694288028195188935310271850942858605732169061642928162768592574807382833472981168828464459148386217261950119045139542977424886628455735204579594915455750739663715092702136141520736846336489556296592591629856794693997741657234499439241491488736775257845785714865481378739951865137426393544971362782695873732627767761308473362917409318686640519925284574118386981171136674163476943370302779254864517819307510753541327411211980811689587631131595255386675712595886193268725122957668741814516156188870442747655154135041165029379643364252958988928292297180895885993219503289439460648387479071119899401796421322992591919129368071956344313948196091897743368018365664261471251950972599735940972325899514705527433191974237467353607092124073946642324745549299532042829737961524398574528850326359429640714556693131588826571260511869883882244798303458883921272226366847857588308058312345328431234990159345395236903149738584794155858890874547642962116327589860992348727854329871659568887041979176271060376095142394759164892795606713762767668327554463968959218637975847474617477899789212231975295272432425856765379049483654742793508836305059744772991973525522379812625762365829963269518081519596737782587958364774632026843014558630363924881649482712953868528613145275765023903016252495842479149645313322878749424653893254496997458048736717579943442236235639265614382130715369248077623917703589821118414359666860119875511121364648291999868489292812705775228675707243693882662252451470941128745024356739837516846942836084901248851528801761825353961443689929259641502136758571807754758923161021923271734824848954835473311389142513308862199939888489211988268632382261798480964370448477749142273028841943857541145254668081182247989135832324435755778910608242141975997733504031414075726432669283397526114328734194324369172344107912568855994551214619538938423410433670923787464518323926134899325356892250911680603015498389225714713290114946398660837375181945104138512799501763252098817727534110244954825047315436718639888964859573143872678656367961238164242846849695599254479991724490462338892060818469455997311952472395364747952794217259485821604198893162325452685023495323866660411419182126124898908857674559157740132353657846735452719516977957597554639222552447771054365063785218465040298648789874481013164389845380466225207336689634833522403372209245755932137443195477664713676121722382598760565515139492479218835295932937385681219091492575992552685949696179683271227432686283269118166585253685952790909199148980702769286466506331626229889061914631984599461169868984755021818334328310655847811423368534172745901526453813266236737760655158689292103712877535343340295513753492319121885662253923454013901458298299546123263830547970703821979149799750415275512471568235847783327835663983228396721435158648982117366045712461167345458456156072665544497066541738456875833298399633441743764921231950627674653698974647126399654982453281968421614532277793516756883018805142635073384239838348181448494071191912493540604646903671372613362439692157521970362278309954391740292161296679251212717399577267825836462524393186488651727987128939213815477825709362966981878364838746848912471466473639303229953042472638857514688243932794226484356830232252976211473652924953614176354314753185943819948215935963224344996032605291147177907691908257503686333212596119529411459014636637593336138969709448914671763821996627549488229788186734648538984471756019243351459347524027861332812198792878324026882249717794531814713486148716659794655195735895126586621823529147563324248225796430813272614326865039973834972456288452212263969931525755127453561038285829913250409758882551533893744837114238719931539781102592557596916069371420707747716415441692832439388136933522607444596095215613398590733196514970719111146626199214238551659652314672689184315292814748218427784551854058705774319518562439141543541138845364333876711388945023798611611117843495921585294975368783827513553084558821612666738942663943566380547063142615984236991532437147336079693164978638841690926695593622762293184475179843615342117336809470529917679528959125435557706833665610176385208696817882103521383724164582754890327963954282637087176712952437888350256118698997985476952893642192791730379594196756409940595487271067954183968181589369178354658779992832112770124968456650163463172359954167326325807613476929365330696825362555966939929699608534979374265521751296142988525925995673255356126231399625779864986235318867841890184030787067858576195265163225808814868792197480946228573130369792733944173521736829924467243023217532291692923758952238907740852594103263567486678676483581393937572689437999111293457697427938994876614599857628385892154415412483376362856433451381108399854751246747378436599956957248339086139760515617858931801116235820808855103591739683361927779514523695577310536215529828796311224656864678171486128838938788593210975931311234771391291690828123723283113026212010946230554232534726318342689818208332655068134565876576893172582534315949977532701686907418722384233527994415701216812447155016174297781884841166933825551895244640817917873122818877947434879156217589409359303836724223535247367694735327277764165269822383108513761414246253953367625639476544995791868183774950709351801640427191581622816995823180277133708737786677818172895363599074235819783253698926168161235912545339278468913349642319684399556318641430296318649241941680246832123493623492904790128446308896142859529773694792437158484427638243101450231130388431817277342929126734513651473987154884263764565571775259413558963279392457721197474858653245415334483787947291656763917387748853596476928217202230364352522143967217202586595079104941215898687786756560663468238312411349127874628634152485211944859465987677741635696633796437165862854659865278672370964625327766942432526565161923311686592361901462435677507020808060866596525193157286622480167590802963396786433818826045452539668784575320196027183929232728817278679395324243189656329684529072217627538547469277147230503094298465471960461347543353557732508243657569774764531433348362896551528050571564174117437950695074165560744737619126525678272444224679662459981075898487685525853785277066286233131786641646222559633042384384624492644468917349842498256814966030993551883510676136366673921121123281473193863996833972292653332969551156453445871454469823794641795264709119323274938241861962132767492672472228465118485997576130512854766191836510675435286867288750795880671919189534869990311585129979982931295475111078889695794416516619406028469371391394619545666289452176899113393233211728954584682629726645889619566289796774985673622533675887945766988572433269754729766046977031955687321053355971723476868487635719955316393416182347186542139860794550369826502027121439553665748310291666894250814264485490304517267827167944348651295035927997806932745679282713791467526333672387973980796031463173925261519268726076252172465261731134977927838765235210726020207150456781505273224041249417262463636229156227683184508197535393203431357910233084365674636031149546131888203939508129255177487883473999615291417767449361433357128457114774125147636657238337707053897150365698779516486346445164419480886987463633652740147944255067647242193370491243731645749054659525876090429782802834437361854474365936422393943693768360292681177314557075268178576879652197875837913679817952343163358980487759596414407138177039503276366043752226911259851884439272486328848591905577627655179599659494951826184325866847645953895834359333911778576664967968642862952578419980448942349179144694689092345777653995712867443344563741754691249771618213173476986451596349321859593798686623108328283680107617788"

# total = [int(num) for num in input]
# grid = []
# dot_cnt = 0

# for i, num in enumerate(total):
#     if i % 2 == 0:
#         grid += [i//2] * num
#     else:
#         grid += [-1] * num
#         dot_cnt += num

# num_loc = [] #this to hold all the number locations

# for i, g in enumerate(grid):
#     if g != -1:
#         num_loc.append(i)

# number_dot = grid.count(-1) # total dots

# total_number_to_switch = grid[:len(grid) - number_dot].count(-1) #count the first half of the grid, how many -1 are in there, they are to be swaped



# cnt = 0
# for i in range(len(grid)):
#     if grid[i] == -1:
#         # print(grid[num_loc.pop()])
#         grid[i] = grid[num_loc.pop()] # put the number to current location
#         cnt += 1 
#     if cnt == total_number_to_switch:
#         break 

# # print(grid)

# answer = sum(i*num for i,num in enumerate(grid[:len(grid) - number_dot]))
# print(answer)


