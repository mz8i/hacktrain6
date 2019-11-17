import * as _ from 'lodash';

import { Station } from '../models/station';

export const stations: Station[] = [
    {
        "code": "PENZNCE",
        "name": "Penzance Rail Station",
        "lng": -5.5326,
        "lat": 50.1217
    },
    {
        "code": "STIVES",
        "name": "St Ives (Cornwall) Rail Station",
        "lng": -5.4779,
        "lat": 50.209
    },
    {
        "code": "CARBISB",
        "name": "Carbis Bay Rail Station",
        "lng": -5.4633,
        "lat": 50.197
    },
    {
        "code": "STERTH",
        "name": "St Erth Rail Station",
        "lng": -5.4443,
        "lat": 50.1705
    },
    {
        "code": "LELANTS",
        "name": "Lelant Saltings Rail Station",
        "lng": -5.4409,
        "lat": 50.1788
    },
    {
        "code": "LELANT",
        "name": "Lelant Rail Station",
        "lng": -5.4365,
        "lat": 50.1841
    },
    {
        "code": "HAYLE",
        "name": "Hayle Rail Station",
        "lng": -5.4198,
        "lat": 50.1856
    },
    {
        "code": "CBORNE",
        "name": "Camborne Rail Station",
        "lng": -5.2974,
        "lat": 50.2104
    },
    {
        "code": "ARISAIG",
        "name": "Arisaig Rail Station",
        "lng": -5.8391,
        "lat": 56.9125
    },
    {
        "code": "MLAIG",
        "name": "Mallaig Rail Station",
        "lng": -5.8296,
        "lat": 57.006
    },
    {
        "code": "MORAR",
        "name": "Morar Rail Station",
        "lng": -5.8219,
        "lat": 56.9697
    },
    {
        "code": "REDRUTH",
        "name": "Redruth Rail Station",
        "lng": -5.2259,
        "lat": 50.2333
    },
    {
        "code": "BEASDAL",
        "name": "Beasdale Rail Station",
        "lng": -5.7638,
        "lat": 56.8996
    },
    {
        "code": "KYLELSH",
        "name": "Kyle of Lochalsh Rail Station",
        "lng": -5.7138,
        "lat": 57.2798
    },
    {
        "code": "LCHALRT",
        "name": "Lochailort Rail Station",
        "lng": -5.6634,
        "lat": 56.881
    },
    {
        "code": "DUIRNSH",
        "name": "Duirinish Rail Station",
        "lng": -5.6913,
        "lat": 57.32
    },
    {
        "code": "PRYN",
        "name": "Penryn Rail Station",
        "lng": -5.1116,
        "lat": 50.1707
    },
    {
        "code": "PERANWL",
        "name": "Perranwell Rail Station",
        "lng": -5.1121,
        "lat": 50.2166
    },
    {
        "code": "PLOCKTN",
        "name": "Plockton Rail Station",
        "lng": -5.666,
        "lat": 57.3336
    },
    {
        "code": "PENMERE",
        "name": "Penmere Rail Station",
        "lng": -5.0832,
        "lat": 50.1503
    },
    {
        "code": "FALMTHT",
        "name": "Falmouth Town Rail Station",
        "lng": -5.0649,
        "lat": 50.1483
    },
    {
        "code": "DUNCRAG",
        "name": "Duncraig Rail Station",
        "lng": -5.6371,
        "lat": 57.337
    },
    {
        "code": "NEWQUAY",
        "name": "Newquay Rail Station",
        "lng": -5.0757,
        "lat": 50.4151
    },
    {
        "code": "TRURO",
        "name": "Truro Rail Station",
        "lng": -5.0648,
        "lat": 50.2638
    },
    {
        "code": "FALMTHD",
        "name": "Falmouth Docks Rail Station",
        "lng": -5.056,
        "lat": 50.1507
    },
    {
        "code": "QNTRLDW",
        "name": "Quintrell Downs Rail Station",
        "lng": -5.0285,
        "lat": 50.4041
    },
    {
        "code": "OBAN",
        "name": "Oban Rail Station",
        "lng": -5.4739,
        "lat": 56.4125
    },
    {
        "code": "STRMFRY",
        "name": "Stromeferry Rail Station",
        "lng": -5.5512,
        "lat": 57.3523
    },
    {
        "code": "GLNFNNN",
        "name": "Glenfinnan Rail Station",
        "lng": -5.4496,
        "lat": 56.8724
    },
    {
        "code": "MLFDHVN",
        "name": "Milford Haven Rail Station",
        "lng": -5.041,
        "lat": 51.715
    },
    {
        "code": "STCLMBR",
        "name": "St Columb Road Rail Station",
        "lng": -4.9408,
        "lat": 50.3987
    },
    {
        "code": "CONNELF",
        "name": "Connel Ferry Rail Station",
        "lng": -5.3854,
        "lat": 56.4524
    },
    {
        "code": "ATADALE",
        "name": "Attadale Rail Station",
        "lng": -5.4556,
        "lat": 57.395
    },
    {
        "code": "JHNSTND",
        "name": "Johnston (Pembrokeshire) Rail Station",
        "lng": -4.9963,
        "lat": 51.7567
    },
    {
        "code": "STCN",
        "name": "Strathcarron Rail Station",
        "lng": -5.4286,
        "lat": 57.4227
    },
    {
        "code": "FGDHGWK",
        "name": "Fishguard & Goodwick Rail Station",
        "lng": -4.9948,
        "lat": 52.0041
    },
    {
        "code": "FGDHBR",
        "name": "Fishguard Harbour Rail Station",
        "lng": -4.9856,
        "lat": 52.0115
    },
    {
        "code": "HAVRFDW",
        "name": "Haverfordwest Rail Station",
        "lng": -4.9602,
        "lat": 51.8026
    },
    {
        "code": "PEMBRKD",
        "name": "Pembroke Dock Rail Station",
        "lng": -4.938,
        "lat": 51.6939
    },
    {
        "code": "RCHE",
        "name": "Roche Rail Station",
        "lng": -4.8302,
        "lat": 50.4185
    },
    {
        "code": "PEMBROK",
        "name": "Pembroke Rail Station",
        "lng": -4.906,
        "lat": 51.6729
    },
    {
        "code": "LCHESDE",
        "name": "Locheilside Rail Station",
        "lng": -5.29,
        "lat": 56.8554
    },
    {
        "code": "ACHHSHL",
        "name": "Achnashellach Rail Station",
        "lng": -5.3331,
        "lat": 57.4821
    },
    {
        "code": "TAYNULT",
        "name": "Taynuilt Rail Station",
        "lng": -5.2396,
        "lat": 56.4308
    },
    {
        "code": "LAMPHEY",
        "name": "Lamphey Rail Station",
        "lng": -4.8733,
        "lat": 51.6672
    },
    {
        "code": "CLARBRD",
        "name": "Clarbeston Road Rail Station",
        "lng": -4.8835,
        "lat": 51.8517
    },
    {
        "code": "STAUSTL",
        "name": "St Austell Rail Station",
        "lng": -4.7894,
        "lat": 50.3395
    },
    {
        "code": "BUGLE",
        "name": "Bugle Rail Station",
        "lng": -4.7921,
        "lat": 50.4003
    },
    {
        "code": "LUXULYN",
        "name": "Luxulyan Rail Station",
        "lng": -4.7474,
        "lat": 50.39
    },
    {
        "code": "LCEILOB",
        "name": "Loch Eil Outward Bound Rail Station",
        "lng": -5.1916,
        "lat": 56.8553
    },
    {
        "code": "STRNRR",
        "name": "Stranraer Rail Station",
        "lng": -5.0247,
        "lat": 54.9096
    },
    {
        "code": "MNORBER",
        "name": "Manorbier Rail Station",
        "lng": -4.7918,
        "lat": 51.6602
    },
    {
        "code": "PARR",
        "name": "Par Rail Station",
        "lng": -4.7047,
        "lat": 50.3553
    },
    {
        "code": "FLSCRHN",
        "name": "Falls of Cruachan Rail Station",
        "lng": -5.1125,
        "lat": 56.3939
    },
    {
        "code": "CORPACH",
        "name": "Corpach Rail Station",
        "lng": -5.122,
        "lat": 56.8428
    },
    {
        "code": "FRTWLM",
        "name": "Fort William Rail Station",
        "lng": -5.1061,
        "lat": 56.8204
    },
    {
        "code": "LSTWTHL",
        "name": "Lostwithiel Rail Station",
        "lng": -4.666,
        "lat": 50.4072
    },
    {
        "code": "BODMNPW",
        "name": "Bodmin Parkway Rail Station",
        "lng": -4.6629,
        "lat": 50.4459
    },
    {
        "code": "BANAVIE",
        "name": "Banavie Rail Station",
        "lng": -5.0954,
        "lat": 56.8433
    },
    {
        "code": "PNALLY",
        "name": "Penally Rail Station",
        "lng": -4.7221,
        "lat": 51.6589
    },
    {
        "code": "CLYNDRW",
        "name": "Clunderwen Rail Station",
        "lng": -4.7318,
        "lat": 51.8405
    },
    {
        "code": "NRBERTH",
        "name": "Narberth Rail Station",
        "lng": -4.7272,
        "lat": 51.7994
    },
    {
        "code": "LOCHAWE",
        "name": "Loch Awe Rail Station",
        "lng": -5.042,
        "lat": 56.402
    },
    {
        "code": "SDRSFOT",
        "name": "Saundersfoot Rail Station",
        "lng": -4.7166,
        "lat": 51.7221
    },
    {
        "code": "KILGETY",
        "name": "Kilgetty Rail Station",
        "lng": -4.7152,
        "lat": 51.7321
    },
    {
        "code": "TENBY",
        "name": "Tenby Rail Station",
        "lng": -4.7067,
        "lat": 51.6729
    },
    {
        "code": "DLMALLY",
        "name": "Dalmally Rail Station",
        "lng": -4.9836,
        "lat": 56.4012
    },
    {
        "code": "ACHNSHN",
        "name": "Achnasheen Rail Station",
        "lng": -5.0723,
        "lat": 57.5793
    },
    {
        "code": "GIRVAN",
        "name": "Girvan Rail Station",
        "lng": -4.8484,
        "lat": 55.2463
    },
    {
        "code": "WEMYSSB",
        "name": "Wemyss Bay Rail Station",
        "lng": -4.8891,
        "lat": 55.8761
    },
    {
        "code": "WHLAND",
        "name": "Whitland Rail Station",
        "lng": -4.6144,
        "lat": 51.818
    },
    {
        "code": "LARGS",
        "name": "Largs Rail Station",
        "lng": -4.8672,
        "lat": 55.7927
    },
    {
        "code": "INVERKP",
        "name": "Inverkip Rail Station",
        "lng": -4.8726,
        "lat": 55.9061
    },
    {
        "code": "WKILBRD",
        "name": "West Kilbride Rail Station",
        "lng": -4.8517,
        "lat": 55.6962
    },
    {
        "code": "FAIRLIE",
        "name": "Fairlie Rail Station",
        "lng": -4.8533,
        "lat": 55.7519
    },
    {
        "code": "SPEANBD",
        "name": "Spean Bridge Rail Station",
        "lng": -4.9216,
        "lat": 56.89
    },
    {
        "code": "ARDRSHB",
        "name": "Ardrossan Harbour Rail Station",
        "lng": -4.8211,
        "lat": 55.6399
    },
    {
        "code": "BRRHL",
        "name": "Barrhill Rail Station",
        "lng": -4.7818,
        "lat": 55.097
    },
    {
        "code": "ARDRSTN",
        "name": "Ardrossan Town Rail Station",
        "lng": -4.8127,
        "lat": 55.6397
    },
    {
        "code": "IBMM",
        "name": "IBM (Greenock) Rail Station",
        "lng": -4.8272,
        "lat": 55.9294
    },
    {
        "code": "ARDRSSB",
        "name": "Ardrossan South Beach Rail Station",
        "lng": -4.8012,
        "lat": 55.6414
    },
    {
        "code": "COOMBE",
        "name": "Coombe Junction Halt (Rail Station)",
        "lng": -4.4819,
        "lat": 50.4459
    },
    {
        "code": "GRLCHHD",
        "name": "Garelochhead Rail Station",
        "lng": -4.8257,
        "lat": 56.0799
    },
    {
        "code": "GOUROCK",
        "name": "Gourock Rail Station",
        "lng": -4.8167,
        "lat": 55.9623
    },
    {
        "code": "LISKARD",
        "name": "Liskeard Rail Station",
        "lng": -4.4696,
        "lat": 50.4469
    },
    {
        "code": "HLYH",
        "name": "Holyhead Rail Station",
        "lng": -4.631,
        "lat": 53.3077
    },
    {
        "code": "CAUSLND",
        "name": "Causeland Rail Station",
        "lng": -4.4664,
        "lat": 50.4057
    },
    {
        "code": "SLCT",
        "name": "Saltcoats Rail Station",
        "lng": -4.7843,
        "lat": 55.6339
    },
    {
        "code": "SDPLACE",
        "name": "Sandplace Rail Station",
        "lng": -4.4645,
        "lat": 50.3868
    },
    {
        "code": "BRNCHTN",
        "name": "Branchton Rail Station",
        "lng": -4.8035,
        "lat": 55.9406
    },
    {
        "code": "STKEYNE",
        "name": "St Keyne Wishing Well Halt (Rail Station)",
        "lng": -4.4635,
        "lat": 50.423
    },
    {
        "code": "LOOE",
        "name": "Looe Rail Station",
        "lng": -4.4562,
        "lat": 50.3592
    },
    {
        "code": "FRTMTLD",
        "name": "Fort Matilda Rail Station",
        "lng": -4.7953,
        "lat": 55.959
    },
    {
        "code": "ACHANLT",
        "name": "Achanalt Rail Station",
        "lng": -4.9139,
        "lat": 57.6096
    },
    {
        "code": "DRMFCHR",
        "name": "Drumfrochar Rail Station",
        "lng": -4.7748,
        "lat": 55.9412
    },
    {
        "code": "STVNSTN",
        "name": "Stevenston Rail Station",
        "lng": -4.7508,
        "lat": 55.6343
    },
    {
        "code": "ROYBDGE",
        "name": "Roy Bridge Rail Station",
        "lng": -4.8372,
        "lat": 56.8884
    },
    {
        "code": "GRENCKW",
        "name": "Greenock West Rail Station",
        "lng": -4.7678,
        "lat": 55.9473
    },
    {
        "code": "GRENCKC",
        "name": "Greenock Central Rail Station",
        "lng": -4.7526,
        "lat": 55.9453
    },
    {
        "code": "WHINH",
        "name": "Whinhill Rail Station",
        "lng": -4.7467,
        "lat": 55.9384
    },
    {
        "code": "MENHENT",
        "name": "Menheniot Rail Station",
        "lng": -4.4092,
        "lat": 50.4262
    },
    {
        "code": "VALLEY",
        "name": "Valley Rail Station",
        "lng": -4.5634,
        "lat": 53.2813
    },
    {
        "code": "CRTSDYK",
        "name": "Cartsdyke Rail Station",
        "lng": -4.7316,
        "lat": 55.9422
    },
    {
        "code": "KILWNNG",
        "name": "Kilwinning Rail Station",
        "lng": -4.71,
        "lat": 55.6559
    },
    {
        "code": "HLNSBRC",
        "name": "Helensburgh Central Rail Station",
        "lng": -4.7328,
        "lat": 56.0042
    },
    {
        "code": "DALRY",
        "name": "Dalry Rail Station",
        "lng": -4.7111,
        "lat": 55.7062
    },
    {
        "code": "MAYBOLE",
        "name": "Maybole Rail Station",
        "lng": -4.6853,
        "lat": 55.3547
    },
    {
        "code": "HLNSBRU",
        "name": "Helensburgh Upper Rail Station",
        "lng": -4.7298,
        "lat": 56.0124
    },
    {
        "code": "BOORCHY",
        "name": "Bridge of Orchy Rail Station",
        "lng": -4.763,
        "lat": 56.5159
    },
    {
        "code": "BOGSTON",
        "name": "Bogston Rail Station",
        "lng": -4.7114,
        "lat": 55.937
    },
    {
        "code": "CRGDRN",
        "name": "Craigendoran Rail Station",
        "lng": -4.7112,
        "lat": 55.9948
    },
    {
        "code": "ARCHRAT",
        "name": "Arrochar & Tarbet Rail Station",
        "lng": -4.7228,
        "lat": 56.204
    },
    {
        "code": "IRVN",
        "name": "Irvine Rail Station",
        "lng": -4.6751,
        "lat": 55.6109
    },
    {
        "code": "ARDLUI",
        "name": "Ardlui Rail Station",
        "lng": -4.7217,
        "lat": 56.302
    },
    {
        "code": "PTGLSGW",
        "name": "Port Glasgow Rail Station",
        "lng": -4.6898,
        "lat": 55.9335
    },
    {
        "code": "GLGN",
        "name": "Glengarnock Rail Station",
        "lng": -4.6745,
        "lat": 55.7389
    },
    {
        "code": "LCHLCHR",
        "name": "Lochluichart Rail Station",
        "lng": -4.809,
        "lat": 57.6218
    },
    {
        "code": "TROON",
        "name": "Troon Rail Station",
        "lng": -4.6553,
        "lat": 55.5428
    },
    {
        "code": "TYNDRML",
        "name": "Tyndrum Lower Rail Station",
        "lng": -4.7148,
        "lat": 56.4333
    },
    {
        "code": "RHOSNGR",
        "name": "Rhosneigr Rail Station",
        "lng": -4.5066,
        "lat": 53.2348
    },
    {
        "code": "BARASIE",
        "name": "Barassie Rail Station",
        "lng": -4.6511,
        "lat": 55.5611
    },
    {
        "code": "TYNDRMU",
        "name": "Upper Tyndrum Rail Station",
        "lng": -4.7037,
        "lat": 56.4347
    },
    {
        "code": "AYRR",
        "name": "Ayr Rail Station",
        "lng": -4.6259,
        "lat": 55.4581
    },
    {
        "code": "NWTOA",
        "name": "Newton-on-Ayr Rail Station",
        "lng": -4.6258,
        "lat": 55.4741
    },
    {
        "code": "WHHL",
        "name": "Woodhall Rail Station",
        "lng": -4.6554,
        "lat": 55.9312
    },
    {
        "code": "CDRS",
        "name": "Cardross Rail Station",
        "lng": -4.6531,
        "lat": 55.9604
    },
    {
        "code": "TYCROES",
        "name": "Ty Croes Rail Station",
        "lng": -4.4747,
        "lat": 53.2226
    },
    {
        "code": "PWCK",
        "name": "Prestwick Rail Station",
        "lng": -4.6152,
        "lat": 55.5017
    },
    {
        "code": "PWCKAPT",
        "name": "Prestwick Intl Airport Rail Station",
        "lng": -4.6142,
        "lat": 55.509
    },
    {
        "code": "TULLOCH",
        "name": "Tulloch Rail Station",
        "lng": -4.7013,
        "lat": 56.8843
    },
    {
        "code": "CORROUR",
        "name": "Corrour Rail Station",
        "lng": -4.6906,
        "lat": 56.7602
    },
    {
        "code": "STGRMNS",
        "name": "St Germans Rail Station",
        "lng": -4.3084,
        "lat": 50.3943
    },
    {
        "code": "LCHWNCH",
        "name": "Lochwinnoch Rail Station",
        "lng": -4.6161,
        "lat": 55.7872
    },
    {
        "code": "FYSD",
        "name": "Ferryside Rail Station",
        "lng": -4.3695,
        "lat": 51.7684
    },
    {
        "code": "PWLHELI",
        "name": "Pwllheli Rail Station",
        "lng": -4.4167,
        "lat": 52.8878
    },
    {
        "code": "CRNLRCH",
        "name": "Crianlarich Rail Station",
        "lng": -4.6184,
        "lat": 56.3905
    },
    {
        "code": "LGBK",
        "name": "Langbank Rail Station",
        "lng": -4.5853,
        "lat": 55.9245
    },
    {
        "code": "BODORGN",
        "name": "Bodorgan Rail Station",
        "lng": -4.418,
        "lat": 53.2043
    },
    {
        "code": "RENTON",
        "name": "Renton Rail Station",
        "lng": -4.5861,
        "lat": 55.9704
    },
    {
        "code": "BALLOCH",
        "name": "Balloch Rail Station",
        "lng": -4.5835,
        "lat": 56.0029
    },
    {
        "code": "DLREOCH",
        "name": "Dalreoch Rail Station",
        "lng": -4.5779,
        "lat": 55.9474
    },
    {
        "code": "ALXANDR",
        "name": "Alexandria Rail Station",
        "lng": -4.5775,
        "lat": 55.9851
    },
    {
        "code": "HOWOOD",
        "name": "Howwood (Renfrewshire) Rail Station",
        "lng": -4.5631,
        "lat": 55.8106
    },
    {
        "code": "GARVE",
        "name": "Garve Rail Station",
        "lng": -4.6884,
        "lat": 57.613
    },
    {
        "code": "DMBRTNC",
        "name": "Dumbarton Central Rail Station",
        "lng": -4.5669,
        "lat": 55.9467
    },
    {
        "code": "KIDWELY",
        "name": "Kidwelly Rail Station",
        "lng": -4.317,
        "lat": 51.7343
    },
    {
        "code": "ABRE",
        "name": "Abererch Rail Station",
        "lng": -4.3742,
        "lat": 52.8986
    },
    {
        "code": "DMBRTNE",
        "name": "Dumbarton East Rail Station",
        "lng": -4.5541,
        "lat": 55.9422
    },
    {
        "code": "KLMAURS",
        "name": "Kilmaurs Rail Station",
        "lng": -4.5305,
        "lat": 55.6372
    },
    {
        "code": "DNLP",
        "name": "Dunlop Rail Station",
        "lng": -4.5324,
        "lat": 55.7119
    },
    {
        "code": "CMTHN",
        "name": "Carmarthen Rail Station",
        "lng": -4.306,
        "lat": 51.8534
    },
    {
        "code": "MILKNPK",
        "name": "Milliken Park Rail Station",
        "lng": -4.5334,
        "lat": 55.8251
    },
    {
        "code": "STEWRTN",
        "name": "Stewarton Rail Station",
        "lng": -4.5181,
        "lat": 55.6822
    },
    {
        "code": "RANNOCH",
        "name": "Rannoch Rail Station",
        "lng": -4.5769,
        "lat": 56.686
    },
    {
        "code": "KILMRNK",
        "name": "Kilmarnock Rail Station",
        "lng": -4.4987,
        "lat": 55.6121
    },
    {
        "code": "GUNISLK",
        "name": "Gunnislake Rail Station",
        "lng": -4.2194,
        "lat": 50.5161
    },
    {
        "code": "PENYCHN",
        "name": "Penychain Rail Station",
        "lng": -4.3387,
        "lat": 52.9029
    },
    {
        "code": "SASH",
        "name": "Saltash Rail Station",
        "lng": -4.2091,
        "lat": 50.4074
    },
    {
        "code": "JOHNSTN",
        "name": "Johnstone Rail Station",
        "lng": -4.5036,
        "lat": 55.8347
    },
    {
        "code": "CALSTCK",
        "name": "Calstock Rail Station",
        "lng": -4.209,
        "lat": 50.4978
    },
    {
        "code": "BISHPTN",
        "name": "Bishopton Rail Station",
        "lng": -4.5005,
        "lat": 55.9023
    },
    {
        "code": "BEREALS",
        "name": "Bere Alston Rail Station",
        "lng": -4.2004,
        "lat": 50.4856
    },
    {
        "code": "BOWLING",
        "name": "Bowling Rail Station",
        "lng": -4.4938,
        "lat": 55.9311
    },
    {
        "code": "STBDXVR",
        "name": "St Budeaux Victoria Road Rail Station",
        "lng": -4.1874,
        "lat": 50.402
    },
    {
        "code": "STBDXFR",
        "name": "St Budeaux Ferry Road Rail Station",
        "lng": -4.1868,
        "lat": 50.4014
    },
    {
        "code": "PMBRYBP",
        "name": "Pembrey & Burry Port Rail Station",
        "lng": -4.2478,
        "lat": 51.6835
    },
    {
        "code": "KEYHAM",
        "name": "Keyham Rail Station",
        "lng": -4.1796,
        "lat": 50.3899
    },
    {
        "code": "BEREFRS",
        "name": "Bere Ferrers Rail Station",
        "lng": -4.1814,
        "lat": 50.4513
    },
    {
        "code": "DOCKYDP",
        "name": "Dockyard (Plymouth) Rail Station",
        "lng": -4.1759,
        "lat": 50.3822
    },
    {
        "code": "DEVNPRT",
        "name": "Devonport Rail Station",
        "lng": -4.1707,
        "lat": 50.3785
    },
    {
        "code": "KLPTRCK",
        "name": "Kilpatrick Rail Station",
        "lng": -4.4534,
        "lat": 55.9247
    },
    {
        "code": "PSLYSTJ",
        "name": "Paisley St James Rail Station",
        "lng": -4.4424,
        "lat": 55.8521
    },
    {
        "code": "PLYMTH",
        "name": "Plymouth Rail Station",
        "lng": -4.1433,
        "lat": 50.3778
    },
    {
        "code": "NEILSTN",
        "name": "Neilston Rail Station",
        "lng": -4.427,
        "lat": 55.783
    },
    {
        "code": "PSLYCAN",
        "name": "Paisley Canal Rail Station",
        "lng": -4.4241,
        "lat": 55.8401
    },
    {
        "code": "PSLYGST",
        "name": "Paisley Gilmour Street Rail Station",
        "lng": -4.4245,
        "lat": 55.8473
    },
    {
        "code": "DALMUIR",
        "name": "Dalmuir Rail Station",
        "lng": -4.4267,
        "lat": 55.9119
    },
    {
        "code": "CRICCTH",
        "name": "Criccieth Rail Station",
        "lng": -4.2375,
        "lat": 52.9184
    },
    {
        "code": "SINGER",
        "name": "Singer Rail Station",
        "lng": -4.4055,
        "lat": 55.9077
    },
    {
        "code": "CLYBANK",
        "name": "Clydebank Rail Station",
        "lng": -4.4044,
        "lat": 55.9007
    },
    {
        "code": "BRHD",
        "name": "Barrhead Rail Station",
        "lng": -4.3973,
        "lat": 55.8038
    },
    {
        "code": "HWKHEAD",
        "name": "Hawkhead Rail Station",
        "lng": -4.3989,
        "lat": 55.8422
    },
    {
        "code": "LLNLLI",
        "name": "Llanelli Rail Station",
        "lng": -4.1613,
        "lat": 51.6739
    },
    {
        "code": "YOKER",
        "name": "Yoker Rail Station",
        "lng": -4.3863,
        "lat": 55.8926
    },
    {
        "code": "DRUMRY",
        "name": "Drumry Rail Station",
        "lng": -4.3855,
        "lat": 55.9046
    },
    {
        "code": "HLNGTNW",
        "name": "Hillington West Rail Station",
        "lng": -4.3716,
        "lat": 55.856
    },
    {
        "code": "BEAULY",
        "name": "Beauly Rail Station",
        "lng": -4.4699,
        "lat": 57.4783
    },
    {
        "code": "CROKSTN",
        "name": "Crookston Rail Station",
        "lng": -4.3647,
        "lat": 55.8423
    },
    {
        "code": "GSCD",
        "name": "Garscadden Rail Station",
        "lng": -4.365,
        "lat": 55.8877
    },
    {
        "code": "NITSH",
        "name": "Nitshill Rail Station",
        "lng": -4.36,
        "lat": 55.8119
    },
    {
        "code": "DRMCHPL",
        "name": "Drumchapel Rail Station",
        "lng": -4.3629,
        "lat": 55.9048
    },
    {
        "code": "LFPW",
        "name": "Llanfairpwll Rail Station",
        "lng": -4.2092,
        "lat": 53.2209
    },
    {
        "code": "HLNGTNE",
        "name": "Hillington East Rail Station",
        "lng": -4.355,
        "lat": 55.8542
    },
    {
        "code": "MUROORD",
        "name": "Muir of Ord Rail Station",
        "lng": -4.4602,
        "lat": 57.5178
    },
    {
        "code": "SCTSTNH",
        "name": "Scotstounhill Rail Station",
        "lng": -4.3529,
        "lat": 55.8851
    },
    {
        "code": "MSSPARK",
        "name": "Mosspark Rail Station",
        "lng": -4.3483,
        "lat": 55.8408
    },
    {
        "code": "PHLD",
        "name": "Priesthill & Darnley Rail Station",
        "lng": -4.3429,
        "lat": 55.8122
    },
    {
        "code": "CDNL",
        "name": "Cardonald Rail Station",
        "lng": -4.3407,
        "lat": 55.8526
    },
    {
        "code": "PATERTN",
        "name": "Patterton Rail Station",
        "lng": -4.3353,
        "lat": 55.7906
    },
    {
        "code": "CKHL",
        "name": "Corkerhill Rail Station",
        "lng": -4.3343,
        "lat": 55.8375
    },
    {
        "code": "CONONBR",
        "name": "Conon Bridge Rail Station",
        "lng": -4.4404,
        "lat": 57.5618
    },
    {
        "code": "WESTRTN",
        "name": "Westerton Rail Station",
        "lng": -4.3349,
        "lat": 55.9048
    },
    {
        "code": "BSDN",
        "name": "Bearsden Rail Station",
        "lng": -4.332,
        "lat": 55.9171
    },
    {
        "code": "KENISHD",
        "name": "Kennishead Rail Station",
        "lng": -4.3252,
        "lat": 55.8133
    },
    {
        "code": "JORDANH",
        "name": "Jordanhill Rail Station",
        "lng": -4.3249,
        "lat": 55.8827
    },
    {
        "code": "ANSL",
        "name": "Anniesland Rail Station",
        "lng": -4.322,
        "lat": 55.8893
    },
    {
        "code": "BYNEA",
        "name": "Bynea Rail Station",
        "lng": -4.0989,
        "lat": 51.672
    },
    {
        "code": "ACHILCK",
        "name": "Auchinleck Rail Station",
        "lng": -4.2953,
        "lat": 55.4703
    },
    {
        "code": "HLFT",
        "name": "Hillfoot Rail Station",
        "lng": -4.3203,
        "lat": 55.9201
    },
    {
        "code": "THLB",
        "name": "Thornliebank Rail Station",
        "lng": -4.3117,
        "lat": 55.8111
    },
    {
        "code": "WTCR",
        "name": "Whitecraigs Rail Station",
        "lng": -4.3102,
        "lat": 55.7903
    },
    {
        "code": "HYNDLND",
        "name": "Hyndland Rail Station",
        "lng": -4.3147,
        "lat": 55.8798
    },
    {
        "code": "DINGWAL",
        "name": "Dingwall Rail Station",
        "lng": -4.4222,
        "lat": 57.5942
    },
    {
        "code": "MLGV",
        "name": "Milngavie Rail Station",
        "lng": -4.3146,
        "lat": 55.9414
    },
    {
        "code": "BRNSTPL",
        "name": "Barnstaple Rail Station",
        "lng": -4.0631,
        "lat": 51.074
    },
    {
        "code": "PTCK",
        "name": "Partick Rail Station",
        "lng": -4.3088,
        "lat": 55.8699
    },
    {
        "code": "DAWSHLM",
        "name": "Kelvindale Rail Station",
        "lng": -4.3096,
        "lat": 55.8936
    },
    {
        "code": "PLKSHWW",
        "name": "Pollokshaws West Rail Station",
        "lng": -4.3016,
        "lat": 55.8238
    },
    {
        "code": "DUMBRCK",
        "name": "Dumbreck Rail Station",
        "lng": -4.3012,
        "lat": 55.8446
    },
    {
        "code": "MRYHILL",
        "name": "Maryhill Rail Station",
        "lng": -4.3007,
        "lat": 55.8976
    },
    {
        "code": "TONFNAU",
        "name": "Tonfanau Rail Station",
        "lng": -4.1237,
        "lat": 52.6135
    },
    {
        "code": "GIFNOCK",
        "name": "Giffnock Rail Station",
        "lng": -4.293,
        "lat": 55.804
    },
    {
        "code": "LLGNNCH",
        "name": "Llangennech Rail Station",
        "lng": -4.0789,
        "lat": 51.6911
    },
    {
        "code": "WMWD",
        "name": "Williamwood Rail Station",
        "lng": -4.2903,
        "lat": 55.7937
    },
    {
        "code": "SHWLNDS",
        "name": "Shawlands Rail Station",
        "lng": -4.2923,
        "lat": 55.8292
    },
    {
        "code": "PRTHMDG",
        "name": "Porthmadog Rail Station",
        "lng": -4.1344,
        "lat": 52.9309
    },
    {
        "code": "MAXWLPK",
        "name": "Maxwell Park Rail Station",
        "lng": -4.2887,
        "lat": 55.8377
    },
    {
        "code": "SUMRSTN",
        "name": "Summerston Rail Station",
        "lng": -4.2915,
        "lat": 55.8988
    },
    {
        "code": "PLKSHWE",
        "name": "Pollokshaws East Rail Station",
        "lng": -4.2869,
        "lat": 55.8246
    },
    {
        "code": "CRSMYLF",
        "name": "Crossmyloof Rail Station",
        "lng": -4.2843,
        "lat": 55.8339
    },
    {
        "code": "LNDW",
        "name": "Llandanwg Rail Station",
        "lng": -4.1239,
        "lat": 52.8362
    },
    {
        "code": "PRTHHBR",
        "name": "Porthmadog Harbour Ffestiniog Railway Station",
        "lng": -4.1268,
        "lat": 52.924
    },
    {
        "code": "EXHIBTC",
        "name": "Exhibition Centre (Glasgow) Rail Station",
        "lng": -4.2836,
        "lat": 55.8615
    },
    {
        "code": "LAMBH",
        "name": "Gilshochill Rail Station",
        "lng": -4.2827,
        "lat": 55.8973
    },
    {
        "code": "CLRKSTN",
        "name": "Clarkston Rail Station",
        "lng": -4.2756,
        "lat": 55.7893
    },
    {
        "code": "LNSD",
        "name": "Langside Rail Station",
        "lng": -4.2773,
        "lat": 55.8211
    },
    {
        "code": "BANGOR",
        "name": "Bangor (Gwynedd) Rail Station",
        "lng": -4.1359,
        "lat": 53.2223
    },
    {
        "code": "MUIREND",
        "name": "Muirend Rail Station",
        "lng": -4.2744,
        "lat": 55.8095
    },
    {
        "code": "PLKLHDW",
        "name": "Pollokshields West Rail Station",
        "lng": -4.2758,
        "lat": 55.8377
    },
    {
        "code": "CULRAIN",
        "name": "Culrain Rail Station",
        "lng": -4.4043,
        "lat": 57.9195
    },
    {
        "code": "PSRN",
        "name": "Pensarn (Gwynedd) Rail Station",
        "lng": -4.1122,
        "lat": 52.8307
    },
    {
        "code": "LBDR",
        "name": "Llanbedr Rail Station",
        "lng": -4.1102,
        "lat": 52.8208
    },
    {
        "code": "ANDRSTN",
        "name": "Anderston Rail Station",
        "lng": -4.271,
        "lat": 55.8599
    },
    {
        "code": "INVRSHN",
        "name": "Invershin Rail Station",
        "lng": -4.3995,
        "lat": 57.9249
    },
    {
        "code": "PLKLHDE",
        "name": "Pollokshields East Rail Station",
        "lng": -4.2686,
        "lat": 55.8411
    },
    {
        "code": "CHRNGXG",
        "name": "Charing Cross (Glasgow) Rail Station",
        "lng": -4.2698,
        "lat": 55.8647
    },
    {
        "code": "CHAPLTN",
        "name": "Chapelton (Devon) Rail Station",
        "lng": -4.0247,
        "lat": 51.0165
    },
    {
        "code": "HRLC",
        "name": "Harlech Rail Station",
        "lng": -4.1092,
        "lat": 52.8613
    },
    {
        "code": "QUNPARK",
        "name": "Queens Park (Glasgow) Rail Station",
        "lng": -4.2667,
        "lat": 55.8353
    },
    {
        "code": "DYFRYNA",
        "name": "Dyffryn Ardudwy Rail Station",
        "lng": -4.1046,
        "lat": 52.7888
    },
    {
        "code": "BUSBY",
        "name": "Busby Rail Station",
        "lng": -4.2622,
        "lat": 55.7803
    },
    {
        "code": "TYWYN",
        "name": "Tywyn Rail Station",
        "lng": -4.0936,
        "lat": 52.5856
    },
    {
        "code": "LAIRG",
        "name": "Lairg Rail Station",
        "lng": -4.3999,
        "lat": 58.0018
    },
    {
        "code": "MTFL",
        "name": "Mount Florida Rail Station",
        "lng": -4.2611,
        "lat": 55.8266
    },
    {
        "code": "CCRT",
        "name": "Cathcart Rail Station",
        "lng": -4.2605,
        "lat": 55.8177
    },
    {
        "code": "ABRYSTH",
        "name": "Aberystwyth Rail Station",
        "lng": -4.0819,
        "lat": 52.414
    },
    {
        "code": "TALB",
        "name": "Talybont Rail Station",
        "lng": -4.0966,
        "lat": 52.7726
    },
    {
        "code": "GLGCLL",
        "name": "Glasgow Central Low Level Rail Station",
        "lng": -4.2585,
        "lat": 55.8587
    },
    {
        "code": "CROSSHL",
        "name": "Crosshill Rail Station",
        "lng": -4.2568,
        "lat": 55.8333
    },
    {
        "code": "PNTADLS",
        "name": "Pontarddulais Rail Station",
        "lng": -4.0455,
        "lat": 51.7176
    },
    {
        "code": "GLGC",
        "name": "Glasgow Central Rail Station",
        "lng": -4.2576,
        "lat": 55.8598
    },
    {
        "code": "POSILPK",
        "name": "Possilpark & Parkhouse Rail Station",
        "lng": -4.2585,
        "lat": 55.8901
    },
    {
        "code": "THAL",
        "name": "Thorntonhall Rail Station",
        "lng": -4.2512,
        "lat": 55.7687
    },
    {
        "code": "LYNGRIL",
        "name": "Llwyngwril Rail Station",
        "lng": -4.0877,
        "lat": 52.6668
    },
    {
        "code": "GLGQHL",
        "name": "Glasgow Queen Street Rail Station",
        "lng": -4.2515,
        "lat": 55.8622
    },
    {
        "code": "ARGYLST",
        "name": "Argyle Street Rail Station",
        "lng": -4.2507,
        "lat": 55.8573
    },
    {
        "code": "OKHMPTN",
        "name": "Okehampton Rail Station",
        "lng": -3.9962,
        "lat": 50.7324
    },
    {
        "code": "GOWERTN",
        "name": "Gowerton Rail Station",
        "lng": -4.0359,
        "lat": 51.6487
    },
    {
        "code": "GLGQLL",
        "name": "Glasgow Queen Street Low Level Rail Station",
        "lng": -4.2506,
        "lat": 55.8623
    },
    {
        "code": "KGPK",
        "name": "Kings Park Rail Station",
        "lng": -4.2465,
        "lat": 55.8195
    },
    {
        "code": "ASFIELD",
        "name": "Ashfield Rail Station",
        "lng": -4.2492,
        "lat": 55.8889
    },
    {
        "code": "LNAB",
        "name": "Llanaber Rail Station",
        "lng": -4.0772,
        "lat": 52.7415
    },
    {
        "code": "GLGHST",
        "name": "High Street (Glasgow) Rail Station",
        "lng": -4.2401,
        "lat": 55.8596
    },
    {
        "code": "MINFORD",
        "name": "Minffordd Rail Station",
        "lng": -4.085,
        "lat": 52.9261
    },
    {
        "code": "MINFFR",
        "name": "Minffordd Ffestiniog Railway Station",
        "lng": -4.0842,
        "lat": 52.9259
    },
    {
        "code": "ARDGAY",
        "name": "Ardgay Rail Station",
        "lng": -4.3621,
        "lat": 57.8815
    },
    {
        "code": "TYGWYN",
        "name": "Tygwyn Rail Station",
        "lng": -4.0787,
        "lat": 52.8938
    },
    {
        "code": "CFFT",
        "name": "Croftfoot Rail Station",
        "lng": -4.2283,
        "lat": 55.8183
    },
    {
        "code": "SPRNGBN",
        "name": "Springburn Rail Station",
        "lng": -4.2305,
        "lat": 55.8819
    },
    {
        "code": "ABDVY",
        "name": "Aberdovey Rail Station",
        "lng": -4.0571,
        "lat": 52.544
    },
    {
        "code": "BRIDGTN",
        "name": "Bridgeton Rail Station",
        "lng": -4.2261,
        "lat": 55.849
    },
    {
        "code": "HARMYRS",
        "name": "Hairmyres Rail Station",
        "lng": -4.22,
        "lat": 55.762
    },
    {
        "code": "BLGRVE",
        "name": "Bellgrove Rail Station",
        "lng": -4.2244,
        "lat": 55.8567
    },
    {
        "code": "BORTH",
        "name": "Borth Rail Station",
        "lng": -4.0502,
        "lat": 52.491
    },
    {
        "code": "UMBRLGH",
        "name": "Umberleigh Rail Station",
        "lng": -3.9829,
        "lat": 50.9967
    },
    {
        "code": "BSHB",
        "name": "Bishopbriggs Rail Station",
        "lng": -4.2249,
        "lat": 55.9039
    },
    {
        "code": "TLSRNAU",
        "name": "Talsarnau Rail Station",
        "lng": -4.0682,
        "lat": 52.9043
    },
    {
        "code": "BNHL",
        "name": "Barnhill Rail Station",
        "lng": -4.223,
        "lat": 55.8775
    },
    {
        "code": "BRMOUTH",
        "name": "Barmouth Rail Station",
        "lng": -4.0566,
        "lat": 52.7229
    },
    {
        "code": "DLMRNOK",
        "name": "Dalmarnock Rail Station",
        "lng": -4.2177,
        "lat": 55.8421
    },
    {
        "code": "PRHN",
        "name": "Penrhyndeudraeth Rail Station",
        "lng": -4.0646,
        "lat": 52.9288
    },
    {
        "code": "RTHGLEN",
        "name": "Rutherglen Rail Station",
        "lng": -4.2121,
        "lat": 55.8306
    },
    {
        "code": "DUKEST",
        "name": "Duke Street Rail Station",
        "lng": -4.213,
        "lat": 55.8584
    },
    {
        "code": "FRBN",
        "name": "Fairbourne Rail Station",
        "lng": -4.0494,
        "lat": 52.696
    },
    {
        "code": "ALXPD",
        "name": "Alexandra Parade Rail Station",
        "lng": -4.2106,
        "lat": 55.8632
    },
    {
        "code": "NWCMNCK",
        "name": "New Cumnock Rail Station",
        "lng": -4.1843,
        "lat": 55.4027
    },
    {
        "code": "LNDC",
        "name": "Llandecwyn Rail Station",
        "lng": -4.057,
        "lat": 52.9207
    },
    {
        "code": "LLDYBIE",
        "name": "Llandybie Rail Station",
        "lng": -4.0036,
        "lat": 51.821
    },
    {
        "code": "BRSDE",
        "name": "Burnside (Strathclyde) Rail Station",
        "lng": -4.2024,
        "lat": 55.8169
    },
    {
        "code": "PENHELG",
        "name": "Penhelig Rail Station",
        "lng": -4.035,
        "lat": 52.5457
    },
    {
        "code": "PNTYFYN",
        "name": "Pantyffynnon Rail Station",
        "lng": -3.9974,
        "lat": 51.7789
    },
    {
        "code": "AMMANFD",
        "name": "Ammanford Rail Station",
        "lng": -3.9967,
        "lat": 51.796
    },
    {
        "code": "SAMPCRT",
        "name": "Sampford Courtenay Rail Station",
        "lng": -3.9489,
        "lat": 50.7701
    },
    {
        "code": "MFAM",
        "name": "Morfa Mawddach Rail Station",
        "lng": -4.0322,
        "lat": 52.7071
    },
    {
        "code": "FFAIRFC",
        "name": "Ffairfach Rail Station",
        "lng": -3.9929,
        "lat": 51.8725
    },
    {
        "code": "PRTSMTA",
        "name": "Portsmouth Arms Rail Station",
        "lng": -3.9506,
        "lat": 50.957
    },
    {
        "code": "EKILBRD",
        "name": "East Kilbride Rail Station",
        "lng": -4.1802,
        "lat": 55.766
    },
    {
        "code": "LLDEILO",
        "name": "Llandeilo Rail Station",
        "lng": -3.9869,
        "lat": 51.8853
    },
    {
        "code": "DALWHIN",
        "name": "Dalwhinnie Rail Station",
        "lng": -4.2462,
        "lat": 56.9352
    },
    {
        "code": "CNTY",
        "name": "Carntyne Rail Station",
        "lng": -4.1786,
        "lat": 55.8549
    },
    {
        "code": "CMBSLNG",
        "name": "Cambuslang Rail Station",
        "lng": -4.173,
        "lat": 55.8196
    },
    {
        "code": "KRKH",
        "name": "Kirkhill Rail Station",
        "lng": -4.1671,
        "lat": 55.8139
    },
    {
        "code": "IVYBDGE",
        "name": "Ivybridge Rail Station",
        "lng": -3.9042,
        "lat": 50.3934
    },
    {
        "code": "SHTLSTN",
        "name": "Shettleston Rail Station",
        "lng": -4.16,
        "lat": 55.8535
    },
    {
        "code": "CARMYLE",
        "name": "Carmyle Rail Station",
        "lng": -4.1582,
        "lat": 55.8343
    },
    {
        "code": "TANY",
        "name": "Tan-y-Bwlch Ffestiniog Railway Station",
        "lng": -4.0115,
        "lat": 52.9544
    },
    {
        "code": "LENZIE",
        "name": "Lenzie Rail Station",
        "lng": -4.1539,
        "lat": 55.9213
    },
    {
        "code": "SWANSEA",
        "name": "Swansea Rail Station",
        "lng": -3.9415,
        "lat": 51.6251
    },
    {
        "code": "ALNESS",
        "name": "Alness Rail Station",
        "lng": -4.2497,
        "lat": 57.6944
    },
    {
        "code": "STEPPS",
        "name": "Stepps Rail Station",
        "lng": -4.1408,
        "lat": 55.8901
    },
    {
        "code": "KNYMPTN",
        "name": "Kings Nympton Rail Station",
        "lng": -3.9054,
        "lat": 50.9361
    },
    {
        "code": "NWTL",
        "name": "Newton (S Lanarks) Rail Station",
        "lng": -4.1331,
        "lat": 55.8188
    },
    {
        "code": "MNTVRNN",
        "name": "Mount Vernon Rail Station",
        "lng": -4.1337,
        "lat": 55.8402
    },
    {
        "code": "IVRNESS",
        "name": "Inverness Rail Station",
        "lng": -4.2234,
        "lat": 57.4799
    },
    {
        "code": "GARROWH",
        "name": "Garrowhill Rail Station",
        "lng": -4.1295,
        "lat": 55.8552
    },
    {
        "code": "BALISTN",
        "name": "Baillieston Rail Station",
        "lng": -4.1137,
        "lat": 55.8445
    },
    {
        "code": "LANFRFC",
        "name": "Llanfairfechan Rail Station",
        "lng": -3.9832,
        "lat": 53.2573
    },
    {
        "code": "ESHS",
        "name": "Easterhouse Rail Station",
        "lng": -4.1072,
        "lat": 55.8598
    },
    {
        "code": "EGGESFD",
        "name": "Eggesford Rail Station",
        "lng": -3.8747,
        "lat": 50.8877
    },
    {
        "code": "BLANTYR",
        "name": "Blantyre Rail Station",
        "lng": -4.087,
        "lat": 55.7973
    },
    {
        "code": "UDNGSTN",
        "name": "Uddingston Rail Station",
        "lng": -4.0867,
        "lat": 55.8235
    },
    {
        "code": "DOVYJN",
        "name": "Dovey Junction Rail Station",
        "lng": -3.9239,
        "lat": 52.5644
    },
    {
        "code": "LLNSMLT",
        "name": "Llansamlet Rail Station",
        "lng": -3.8847,
        "lat": 51.6615
    },
    {
        "code": "LLGADOG",
        "name": "Llangadog Rail Station",
        "lng": -3.8931,
        "lat": 51.9402
    },
    {
        "code": "BLAENAU",
        "name": "Blaenau Ffestiniog Rail Station",
        "lng": -3.9386,
        "lat": 52.9945
    },
    {
        "code": "GRTCSH",
        "name": "Gartcosh Rail Station",
        "lng": -4.0795,
        "lat": 55.8857
    },
    {
        "code": "BRGDDIE",
        "name": "Bargeddie Rail Station",
        "lng": -4.0738,
        "lat": 55.8513
    },
    {
        "code": "IVRGRD",
        "name": "Invergordon Rail Station",
        "lng": -4.1748,
        "lat": 57.689
    },
    {
        "code": "HAMLTNW",
        "name": "Hamilton West Rail Station",
        "lng": -4.0548,
        "lat": 55.7789
    },
    {
        "code": "ROMANBG",
        "name": "Roman Bridge Rail Station",
        "lng": -3.9216,
        "lat": 53.0444
    },
    {
        "code": "LLWRDA",
        "name": "Llanwrda Rail Station",
        "lng": -3.8717,
        "lat": 51.9626
    },
    {
        "code": "NWTM",
        "name": "Newtonmore Rail Station",
        "lng": -4.1191,
        "lat": 57.0591
    },
    {
        "code": "PNMNMWR",
        "name": "Penmaenmawr Rail Station",
        "lng": -3.9235,
        "lat": 53.2705
    },
    {
        "code": "KRKWOOD",
        "name": "Kirkwood Rail Station",
        "lng": -4.0484,
        "lat": 55.8542
    },
    {
        "code": "HAMLTNC",
        "name": "Hamilton Central Rail Station",
        "lng": -4.0389,
        "lat": 55.7732
    },
    {
        "code": "BLAIRHL",
        "name": "Blairhill Rail Station",
        "lng": -4.0433,
        "lat": 55.8664
    },
    {
        "code": "SKEWEN",
        "name": "Skewen Rail Station",
        "lng": -3.8465,
        "lat": 51.6614
    },
    {
        "code": "ROGART",
        "name": "Rogart Rail Station",
        "lng": -4.1582,
        "lat": 57.9887
    },
    {
        "code": "LAPFORD",
        "name": "Lapford Rail Station",
        "lng": -3.8106,
        "lat": 50.857
    },
    {
        "code": "COATBDC",
        "name": "Coatbridge Central Rail Station",
        "lng": -4.0319,
        "lat": 55.8625
    },
    {
        "code": "CROY",
        "name": "Croy Rail Station",
        "lng": -4.036,
        "lat": 55.9557
    },
    {
        "code": "COATBDS",
        "name": "Coatbridge Sunnyside Rail Station",
        "lng": -4.0283,
        "lat": 55.8668
    },
    {
        "code": "BLSHL",
        "name": "Bellshill Rail Station",
        "lng": -4.0245,
        "lat": 55.8171
    },
    {
        "code": "KRKC",
        "name": "Kirkconnel Rail Station",
        "lng": -3.9985,
        "lat": 55.3883
    },
    {
        "code": "WHIFLET",
        "name": "Whifflet Rail Station",
        "lng": -4.0187,
        "lat": 55.8537
    },
    {
        "code": "DLWYDLN",
        "name": "Dolwyddelan Rail Station",
        "lng": -3.8851,
        "lat": 53.052
    },
    {
        "code": "BRITFRY",
        "name": "Briton Ferry Rail Station",
        "lng": -3.8193,
        "lat": 51.6379
    },
    {
        "code": "CHTLRT",
        "name": "Chatelherault Rail Station",
        "lng": -4.0047,
        "lat": 55.7652
    },
    {
        "code": "MCHYNLT",
        "name": "Machynlleth Rail Station",
        "lng": -3.8545,
        "lat": 52.5951
    },
    {
        "code": "COATDYK",
        "name": "Coatdyke Rail Station",
        "lng": -4.005,
        "lat": 55.8643
    },
    {
        "code": "BGLAN",
        "name": "Baglan Rail Station",
        "lng": -3.8111,
        "lat": 51.6155
    },
    {
        "code": "MOCHARD",
        "name": "Morchard Road Rail Station",
        "lng": -3.7764,
        "lat": 50.8319
    },
    {
        "code": "AIRBLES",
        "name": "Airbles Rail Station",
        "lng": -3.9942,
        "lat": 55.7828
    },
    {
        "code": "MOTHRWL",
        "name": "Motherwell Rail Station",
        "lng": -3.9943,
        "lat": 55.7917
    },
    {
        "code": "NEATH",
        "name": "Neath Rail Station",
        "lng": -3.8072,
        "lat": 51.6624
    },
    {
        "code": "PNYPANT",
        "name": "Pont-y-Pant Rail Station",
        "lng": -3.8627,
        "lat": 53.0651
    },
    {
        "code": "GRNFLDS",
        "name": "Greenfaulds Rail Station",
        "lng": -3.9931,
        "lat": 55.9352
    },
    {
        "code": "KGUSSIE",
        "name": "Kingussie Rail Station",
        "lng": -4.0522,
        "lat": 57.0778
    },
    {
        "code": "MRRYTON",
        "name": "Merryton Rail Station",
        "lng": -3.9783,
        "lat": 55.7487
    },
    {
        "code": "AIRDRIE",
        "name": "Airdrie Rail Station",
        "lng": -3.9829,
        "lat": 55.864
    },
    {
        "code": "LARKHAL",
        "name": "Larkhall Rail Station",
        "lng": -3.9755,
        "lat": 55.7386
    },
    {
        "code": "LLDVERY",
        "name": "Llandovery Rail Station",
        "lng": -3.8028,
        "lat": 51.9953
    },
    {
        "code": "HOLYTWN",
        "name": "Holytown Rail Station",
        "lng": -3.9739,
        "lat": 55.8129
    },
    {
        "code": "CMBRNLD",
        "name": "Cumbernauld Rail Station",
        "lng": -3.9803,
        "lat": 55.942
    },
    {
        "code": "COPLSTN",
        "name": "Copplestone Rail Station",
        "lng": -3.7516,
        "lat": 50.8145
    },
    {
        "code": "PTALBOT",
        "name": "Port Talbot Parkway Rail Station",
        "lng": -3.7813,
        "lat": 51.5917
    },
    {
        "code": "SHILDMR",
        "name": "Shieldmuir Rail Station",
        "lng": -3.957,
        "lat": 55.7775
    },
    {
        "code": "CARFIN",
        "name": "Carfin Rail Station",
        "lng": -3.9563,
        "lat": 55.8073
    },
    {
        "code": "DEGANWY",
        "name": "Deganwy Rail Station",
        "lng": -3.8334,
        "lat": 53.2947
    },
    {
        "code": "CONWY",
        "name": "Conwy Rail Station",
        "lng": -3.8305,
        "lat": 53.2801
    },
    {
        "code": "DUNANE",
        "name": "Dunblane Rail Station",
        "lng": -3.9655,
        "lat": 56.1859
    },
    {
        "code": "SANQHAR",
        "name": "Sanquhar Rail Station",
        "lng": -3.9245,
        "lat": 55.3702
    },
    {
        "code": "DRMGLCH",
        "name": "Drumgelloch Rail Station",
        "lng": -3.9489,
        "lat": 55.8674
    },
    {
        "code": "TAIN",
        "name": "Tain Rail Station",
        "lng": -4.052,
        "lat": 57.8144
    },
    {
        "code": "DOLGARG",
        "name": "Dolgarrog Rail Station",
        "lng": -3.8226,
        "lat": 53.1863
    },
    {
        "code": "YEOFORD",
        "name": "Yeoford Rail Station",
        "lng": -3.7271,
        "lat": 50.7769
    },
    {
        "code": "LUDO",
        "name": "Llandudno Rail Station",
        "lng": -3.827,
        "lat": 53.3209
    },
    {
        "code": "BGOALAN",
        "name": "Bridge of Allan Rail Station",
        "lng": -3.9572,
        "lat": 56.1566
    },
    {
        "code": "TALYCFN",
        "name": "Tal-y-Cafn Rail Station",
        "lng": -3.8183,
        "lat": 53.2284
    },
    {
        "code": "WISHAW",
        "name": "Wishaw Rail Station",
        "lng": -3.9264,
        "lat": 55.772
    },
    {
        "code": "LANDUDJ",
        "name": "Llandudno Junction Rail Station",
        "lng": -3.8091,
        "lat": 53.2839
    },
    {
        "code": "BETSYCD",
        "name": "Betws-y-Coed Rail Station",
        "lng": -3.8009,
        "lat": 53.0921
    },
    {
        "code": "NLANRST",
        "name": "North Llanrwst Rail Station",
        "lng": -3.8027,
        "lat": 53.1438
    },
    {
        "code": "STIRLNG",
        "name": "Stirling Rail Station",
        "lng": -3.9356,
        "lat": 56.1198
    },
    {
        "code": "LNRWST",
        "name": "Llanrwst Rail Station",
        "lng": -3.7944,
        "lat": 53.1388
    },
    {
        "code": "TOTNES",
        "name": "Totnes Rail Station",
        "lng": -3.6887,
        "lat": 50.4359
    },
    {
        "code": "GLNCNWY",
        "name": "Glan Conwy Rail Station",
        "lng": -3.7977,
        "lat": 53.2674
    },
    {
        "code": "CYNGHRD",
        "name": "Cynghordy Rail Station",
        "lng": -3.7482,
        "lat": 52.0515
    },
    {
        "code": "CLELAND",
        "name": "Cleland Rail Station",
        "lng": -3.9102,
        "lat": 55.8046
    },
    {
        "code": "FEARN",
        "name": "Fearn Rail Station",
        "lng": -3.9939,
        "lat": 57.7781
    },
    {
        "code": "CLDRCRX",
        "name": "Caldercruix Rail Station",
        "lng": -3.8877,
        "lat": 55.8879
    },
    {
        "code": "PYLE",
        "name": "Pyle Rail Station",
        "lng": -3.6981,
        "lat": 51.5257
    },
    {
        "code": "GOLSPIE",
        "name": "Golspie Rail Station",
        "lng": -3.9872,
        "lat": 57.9715
    },
    {
        "code": "CRLK",
        "name": "Carluke Rail Station",
        "lng": -3.8489,
        "lat": 55.7313
    },
    {
        "code": "CREDITN",
        "name": "Crediton Rail Station",
        "lng": -3.6468,
        "lat": 50.7833
    },
    {
        "code": "SGRLOAF",
        "name": "Sugar Loaf Rail Station",
        "lng": -3.6869,
        "lat": 52.0823
    },
    {
        "code": "HRTW",
        "name": "Hartwood Rail Station",
        "lng": -3.8393,
        "lat": 55.8115
    },
    {
        "code": "DNROBIN",
        "name": "Dunrobin Castle Rail Station",
        "lng": -3.9489,
        "lat": 57.9855
    },
    {
        "code": "CBAY",
        "name": "Colwyn Bay Rail Station",
        "lng": -3.7254,
        "lat": 53.2964
    },
    {
        "code": "MAESTGW",
        "name": "Maesteg Rail Station",
        "lng": -3.6546,
        "lat": 51.6099
    },
    {
        "code": "MAESTER",
        "name": "Maesteg (Ewenny Road) Rail Station",
        "lng": -3.649,
        "lat": 51.6053
    },
    {
        "code": "LARBERT",
        "name": "Larbert Rail Station",
        "lng": -3.8306,
        "lat": 56.0227
    },
    {
        "code": "KINBRAC",
        "name": "Kinbrace Rail Station",
        "lng": -3.9412,
        "lat": 58.2583
    },
    {
        "code": "GRTHMG",
        "name": "Garth (Bridgend) Rail Station",
        "lng": -3.6414,
        "lat": 51.5965
    },
    {
        "code": "NABT",
        "name": "Newton Abbot Rail Station",
        "lng": -3.5992,
        "lat": 50.5296
    },
    {
        "code": "CAMELON",
        "name": "Camelon Rail Station",
        "lng": -3.8176,
        "lat": 56.0061
    },
    {
        "code": "BLARATH",
        "name": "Blair Atholl Rail Station",
        "lng": -3.8502,
        "lat": 56.7655
    },
    {
        "code": "SHTT",
        "name": "Shotts Rail Station",
        "lng": -3.7983,
        "lat": 55.8186
    },
    {
        "code": "NSTCYRE",
        "name": "Newton St Cyres Rail Station",
        "lng": -3.5894,
        "lat": 50.7789
    },
    {
        "code": "NAIRN",
        "name": "Nairn Rail Station",
        "lng": -3.872,
        "lat": 57.5802
    },
    {
        "code": "FALKRKH",
        "name": "Falkirk High Rail Station",
        "lng": -3.7922,
        "lat": 55.9918
    },
    {
        "code": "LLWRTYW",
        "name": "Llanwrtyd Rail Station",
        "lng": -3.6322,
        "lat": 52.1047
    },
    {
        "code": "LANARK",
        "name": "Lanark Rail Station",
        "lng": -3.7733,
        "lat": 55.6736
    },
    {
        "code": "FALKRKG",
        "name": "Falkirk Grahamston Rail Station",
        "lng": -3.785,
        "lat": 56.0026
    },
    {
        "code": "ALLOA",
        "name": "Alloa Rail Station",
        "lng": -3.7901,
        "lat": 56.1178
    },
    {
        "code": "PAIGNTN",
        "name": "Paignton Rail Station",
        "lng": -3.5649,
        "lat": 50.4347
    },
    {
        "code": "FORSNRD",
        "name": "Forsinard Rail Station",
        "lng": -3.8969,
        "lat": 58.3569
    },
    {
        "code": "TONDU",
        "name": "Tondu Rail Station",
        "lng": -3.5955,
        "lat": 51.5474
    },
    {
        "code": "AVIEMRE",
        "name": "Aviemore Rail Station",
        "lng": -3.8289,
        "lat": 57.1885
    },
    {
        "code": "SARN",
        "name": "Sarn Rail Station",
        "lng": -3.5899,
        "lat": 51.5387
    },
    {
        "code": "CARRBDG",
        "name": "Carrbridge Rail Station",
        "lng": -3.8282,
        "lat": 57.2795
    },
    {
        "code": "KILDONN",
        "name": "Kildonan Rail Station",
        "lng": -3.8691,
        "lat": 58.1708
    },
    {
        "code": "TORRE",
        "name": "Torre Rail Station",
        "lng": -3.5464,
        "lat": 50.4732
    },
    {
        "code": "WLDMILL",
        "name": "Wildmill Rail Station",
        "lng": -3.5796,
        "lat": 51.5209
    },
    {
        "code": "TORQUAY",
        "name": "Torquay Rail Station",
        "lng": -3.5433,
        "lat": 50.4611
    },
    {
        "code": "BLKRDGE",
        "name": "Blackridge Rail Station",
        "lng": -3.7508,
        "lat": 55.8842
    },
    {
        "code": "BRORA",
        "name": "Brora Rail Station",
        "lng": -3.8523,
        "lat": 58.0129
    },
    {
        "code": "BRGEND",
        "name": "Bridgend Rail Station",
        "lng": -3.5753,
        "lat": 51.507
    },
    {
        "code": "EXETRSD",
        "name": "Exeter St Davids Rail Station",
        "lng": -3.5433,
        "lat": 50.7293
    },
    {
        "code": "EXETRST",
        "name": "Exeter St Thomas Rail Station",
        "lng": -3.5388,
        "lat": 50.7171
    },
    {
        "code": "EXETERC",
        "name": "Exeter Central Rail Station",
        "lng": -3.5333,
        "lat": 50.7265
    },
    {
        "code": "FAULDHS",
        "name": "Fauldhouse Rail Station",
        "lng": -3.7193,
        "lat": 55.8225
    },
    {
        "code": "STJAMSP",
        "name": "St James Park (Devon) Rail Station",
        "lng": -3.522,
        "lat": 50.7312
    },
    {
        "code": "GLNEGLS",
        "name": "Gleneagles Rail Station",
        "lng": -3.7312,
        "lat": 56.2748
    },
    {
        "code": "POLMONT",
        "name": "Polmont Rail Station",
        "lng": -3.715,
        "lat": 55.9847
    },
    {
        "code": "LLGMMRW",
        "name": "Llangammarch Rail Station",
        "lng": -3.5548,
        "lat": 52.1143
    },
    {
        "code": "PTLCHRY",
        "name": "Pitlochry Rail Station",
        "lng": -3.7356,
        "lat": 56.7025
    },
    {
        "code": "TREHRBT",
        "name": "Treherbert Rail Station",
        "lng": -3.5363,
        "lat": 51.6722
    },
    {
        "code": "ARMDALE",
        "name": "Armadale (W Lothian) Rail Station",
        "lng": -3.6954,
        "lat": 55.8857
    },
    {
        "code": "POLSBDG",
        "name": "Polsloe Bridge Rail Station",
        "lng": -3.5019,
        "lat": 50.7313
    },
    {
        "code": "TEINMTH",
        "name": "Teignmouth Rail Station",
        "lng": -3.4947,
        "lat": 50.5481
    },
    {
        "code": "ABGLELE",
        "name": "Abergele & Pensarn Rail Station",
        "lng": -3.5826,
        "lat": 53.2946
    },
    {
        "code": "YNYSWEN",
        "name": "Ynyswen Rail Station",
        "lng": -3.5216,
        "lat": 51.665
    },
    {
        "code": "CRSTRS",
        "name": "Carstairs Rail Station",
        "lng": -3.6685,
        "lat": 55.691
    },
    {
        "code": "GARTH",
        "name": "Garth (Powys) Rail Station",
        "lng": -3.5299,
        "lat": 52.1332
    },
    {
        "code": "BREICH",
        "name": "Breich Rail Station",
        "lng": -3.6681,
        "lat": 55.8273
    },
    {
        "code": "TREORCY",
        "name": "Treorchy Rail Station",
        "lng": -3.5057,
        "lat": 51.6575
    },
    {
        "code": "PENCOED",
        "name": "Pencoed Rail Station",
        "lng": -3.5005,
        "lat": 51.5246
    },
    {
        "code": "DIGBY",
        "name": "Digby & Sowton Rail Station",
        "lng": -3.4736,
        "lat": 50.714
    },
    {
        "code": "NWCOURT",
        "name": "Newcourt Rail Station",
        "lng": -3.4728,
        "lat": 50.705
    },
    {
        "code": "DAWLISH",
        "name": "Dawlish Rail Station",
        "lng": -3.4646,
        "lat": 50.5808
    },
    {
        "code": "PINHOE",
        "name": "Pinhoe Rail Station",
        "lng": -3.4693,
        "lat": 50.7378
    },
    {
        "code": "TOPSHAM",
        "name": "Topsham Rail Station",
        "lng": -3.4644,
        "lat": 50.6862
    },
    {
        "code": "STBEES",
        "name": "St Bees Rail Station",
        "lng": -3.5911,
        "lat": 54.4925
    },
    {
        "code": "LLNWTMR",
        "name": "Llantwit Major Rail Station",
        "lng": -3.4816,
        "lat": 51.4097
    },
    {
        "code": "TONPNTR",
        "name": "Ton Pentre Rail Station",
        "lng": -3.4862,
        "lat": 51.6478
    },
    {
        "code": "WHITHVN",
        "name": "Whitehaven Rail Station",
        "lng": -3.5869,
        "lat": 54.553
    },
    {
        "code": "DUMFRES",
        "name": "Dumfries Rail Station",
        "lng": -3.6043,
        "lat": 55.0726
    },
    {
        "code": "STRCROS",
        "name": "Starcross Rail Station",
        "lng": -3.4477,
        "lat": 50.6278
    },
    {
        "code": "CRCK",
        "name": "Corkickle Rail Station",
        "lng": -3.5822,
        "lat": 54.5417
    },
    {
        "code": "BTHGATE",
        "name": "Bathgate Rail Station",
        "lng": -3.6361,
        "lat": 55.8972
    },
    {
        "code": "PARTON",
        "name": "Parton Rail Station",
        "lng": -3.5808,
        "lat": 54.5704
    },
    {
        "code": "DAWLSHW",
        "name": "Dawlish Warren Rail Station",
        "lng": -3.4436,
        "lat": 50.5987
    },
    {
        "code": "EXTON",
        "name": "Exton Rail Station",
        "lng": -3.4441,
        "lat": 50.6683
    },
    {
        "code": "LYMPSTC",
        "name": "Lympstone Commando Rail Station",
        "lng": -3.4408,
        "lat": 50.6622
    },
    {
        "code": "NETHRTN",
        "name": "Nethertown Rail Station",
        "lng": -3.5658,
        "lat": 54.4564
    },
    {
        "code": "YTRHOND",
        "name": "Ystrad Rhondda Rail Station",
        "lng": -3.4667,
        "lat": 51.6436
    },
    {
        "code": "LYMPSTN",
        "name": "Lympstone Village Rail Station",
        "lng": -3.431,
        "lat": 50.6483
    },
    {
        "code": "HNGT",
        "name": "Harrington Rail Station",
        "lng": -3.5655,
        "lat": 54.6135
    },
    {
        "code": "ADIEWEL",
        "name": "Addiewell Rail Station",
        "lng": -3.6065,
        "lat": 55.8434
    },
    {
        "code": "LLWYNYP",
        "name": "Llwynypia Rail Station",
        "lng": -3.4535,
        "lat": 51.634
    },
    {
        "code": "WKNT",
        "name": "Workington Rail Station",
        "lng": -3.5585,
        "lat": 54.6451
    },
    {
        "code": "TNYPNDY",
        "name": "Tonypandy Rail Station",
        "lng": -3.4489,
        "lat": 51.6198
    },
    {
        "code": "CBRK",
        "name": "Cranbrook Rail Station",
        "lng": -3.4204,
        "lat": 50.7501
    },
    {
        "code": "EXMOUTH",
        "name": "Exmouth Rail Station",
        "lng": -3.415,
        "lat": 50.6216
    },
    {
        "code": "BRYSTNS",
        "name": "Braystones Rail Station",
        "lng": -3.5418,
        "lat": 54.4394
    },
    {
        "code": "LLHARAN",
        "name": "Llanharan Rail Station",
        "lng": -3.4408,
        "lat": 51.5376
    },
    {
        "code": "ALTNBRC",
        "name": "Altnabreac Rail Station",
        "lng": -3.7063,
        "lat": 58.3881
    },
    {
        "code": "ABDARE",
        "name": "Aberdare Rail Station",
        "lng": -3.4431,
        "lat": 51.7151
    },
    {
        "code": "CILMERY",
        "name": "Cilmeri Rail Station",
        "lng": -3.4565,
        "lat": 52.1505
    },
    {
        "code": "LNLTHGW",
        "name": "Linlithgow Rail Station",
        "lng": -3.5959,
        "lat": 55.9765
    },
    {
        "code": "DINASR",
        "name": "Dinas (Rhondda) Rail Station",
        "lng": -3.4375,
        "lat": 51.6178
    },
    {
        "code": "RHYL",
        "name": "Rhyl Rail Station",
        "lng": -3.4891,
        "lat": 53.3184
    },
    {
        "code": "WCALDER",
        "name": "West Calder Rail Station",
        "lng": -3.567,
        "lat": 55.8538
    },
    {
        "code": "FLIMBY",
        "name": "Flimby Rail Station",
        "lng": -3.5207,
        "lat": 54.6897
    },
    {
        "code": "SELAFLD",
        "name": "Sellafield Rail Station",
        "lng": -3.5105,
        "lat": 54.4166
    },
    {
        "code": "HELMSDL",
        "name": "Helmsdale Rail Station",
        "lng": -3.6587,
        "lat": 58.1174
    },
    {
        "code": "CMBH",
        "name": "Cwmbach Rail Station",
        "lng": -3.4137,
        "lat": 51.7019
    },
    {
        "code": "BUILTHR",
        "name": "Builth Road Rail Station",
        "lng": -3.427,
        "lat": 52.1693
    },
    {
        "code": "PORH",
        "name": "Porth Rail Station",
        "lng": -3.4072,
        "lat": 51.6125
    },
    {
        "code": "CARSWS",
        "name": "Caersws Rail Station",
        "lng": -3.4325,
        "lat": 52.5161
    },
    {
        "code": "FORRES",
        "name": "Forres Rail Station",
        "lng": -3.6249,
        "lat": 57.6112
    },
    {
        "code": "DUNKELD",
        "name": "Dunkeld & Birnam Rail Station",
        "lng": -3.5784,
        "lat": 56.5571
    },
    {
        "code": "PONYCLN",
        "name": "Pontyclun Rail Station",
        "lng": -3.3929,
        "lat": 51.5238
    },
    {
        "code": "LVNSTNN",
        "name": "Livingston North Rail Station",
        "lng": -3.5444,
        "lat": 55.9014
    },
    {
        "code": "FERNHIL",
        "name": "Fernhill Rail Station",
        "lng": -3.3959,
        "lat": 51.6865
    },
    {
        "code": "SEASCAL",
        "name": "Seascale Rail Station",
        "lng": -3.4845,
        "lat": 54.3959
    },
    {
        "code": "MPRT",
        "name": "Maryport Rail Station",
        "lng": -3.4941,
        "lat": 54.7113
    },
    {
        "code": "TREHAFD",
        "name": "Trehafod Rail Station",
        "lng": -3.381,
        "lat": 51.6101
    },
    {
        "code": "TIVIPW",
        "name": "Tiverton Parkway Rail Station",
        "lng": -3.3596,
        "lat": 50.9172
    },
    {
        "code": "WHIMPLE",
        "name": "Whimple Rail Station",
        "lng": -3.3543,
        "lat": 50.768
    },
    {
        "code": "MASH",
        "name": "Mountain Ash Rail Station",
        "lng": -3.3763,
        "lat": 51.6813
    },
    {
        "code": "MERTHYR",
        "name": "Merthyr Tydfil Rail Station",
        "lng": -3.3773,
        "lat": 51.7446
    },
    {
        "code": "LLDODW",
        "name": "Llandrindod Rail Station",
        "lng": -3.3791,
        "lat": 52.2424
    },
    {
        "code": "PNTRBCH",
        "name": "Pentre-Bach Rail Station",
        "lng": -3.3623,
        "lat": 51.725
    },
    {
        "code": "PNRHCBR",
        "name": "Penrhiwceiber Rail Station",
        "lng": -3.3599,
        "lat": 51.6699
    },
    {
        "code": "LVNSTNS",
        "name": "Livingston South Rail Station",
        "lng": -3.5016,
        "lat": 55.8717
    },
    {
        "code": "RHOOSE",
        "name": "Rhoose Rail Station",
        "lng": -3.3494,
        "lat": 51.3871
    },
    {
        "code": "UPHALL",
        "name": "Uphall Rail Station",
        "lng": -3.5021,
        "lat": 55.919
    },
    {
        "code": "DRIGG",
        "name": "Drigg Rail Station",
        "lng": -3.4434,
        "lat": 54.377
    },
    {
        "code": "PSTA",
        "name": "Prestatyn Rail Station",
        "lng": -3.4071,
        "lat": 53.3365
    },
    {
        "code": "TRDYRHW",
        "name": "Troed-y-Rhiw Rail Station",
        "lng": -3.3467,
        "lat": 51.7124
    },
    {
        "code": "PTYPRID",
        "name": "Pontypridd Rail Station",
        "lng": -3.3414,
        "lat": 51.5994
    },
    {
        "code": "MERTHRV",
        "name": "Merthyr Vale Rail Station",
        "lng": -3.3366,
        "lat": 51.6866
    },
    {
        "code": "ABRCYNS",
        "name": "Abercynon Rail Station",
        "lng": -3.327,
        "lat": 51.6447
    },
    {
        "code": "TREFRST",
        "name": "Trefforest Rail Station",
        "lng": -3.3251,
        "lat": 51.5915
    },
    {
        "code": "RGLS",
        "name": "Ravenglass Rail Station",
        "lng": -3.4088,
        "lat": 54.3557
    },
    {
        "code": "QUAKRSY",
        "name": "Quakers Yard Rail Station",
        "lng": -3.3228,
        "lat": 51.6607
    },
    {
        "code": "BOOTLE",
        "name": "Bootle (Cumbria) Rail Station",
        "lng": -3.3939,
        "lat": 54.2913
    },
    {
        "code": "FENITON",
        "name": "Feniton Rail Station",
        "lng": -3.2854,
        "lat": 50.7867
    },
    {
        "code": "SCSCLDR",
        "name": "Scotscalder Rail Station",
        "lng": -3.552,
        "lat": 58.483
    },
    {
        "code": "DNFRMLE",
        "name": "Dunfermline Town Rail Station",
        "lng": -3.4525,
        "lat": 56.0682
    },
    {
        "code": "PYBONT",
        "name": "Pen-y-Bont Rail Station",
        "lng": -3.3219,
        "lat": 52.2739
    },
    {
        "code": "KRKNWTN",
        "name": "Kirknewton Rail Station",
        "lng": -3.4325,
        "lat": 55.8887
    },
    {
        "code": "TRFRSTE",
        "name": "Trefforest Estate Rail Station",
        "lng": -3.2902,
        "lat": 51.5683
    },
    {
        "code": "BARRY",
        "name": "Barry Rail Station",
        "lng": -3.285,
        "lat": 51.3968
    },
    {
        "code": "NWTP",
        "name": "Newtown (Powys) Rail Station",
        "lng": -3.3114,
        "lat": 52.5123
    },
    {
        "code": "RHYMNEY",
        "name": "Rhymney Rail Station",
        "lng": -3.2893,
        "lat": 51.7588
    },
    {
        "code": "ROSYTH",
        "name": "Rosyth Rail Station",
        "lng": -3.4273,
        "lat": 56.0455
    },
    {
        "code": "PERTH",
        "name": "Perth Rail Station",
        "lng": -3.4397,
        "lat": 56.3921
    },
    {
        "code": "THURSO",
        "name": "Thurso Rail Station",
        "lng": -3.5275,
        "lat": 58.5902
    },
    {
        "code": "BARRYIS",
        "name": "Barry Island Rail Station",
        "lng": -3.2734,
        "lat": 51.3924
    },
    {
        "code": "DNFRMQM",
        "name": "Dunfermline Queen Margaret Rail Station",
        "lng": -3.4215,
        "lat": 56.0806
    },
    {
        "code": "PNTLTYN",
        "name": "Pontlottyn Rail Station",
        "lng": -3.279,
        "lat": 51.7466
    },
    {
        "code": "BARRYDK",
        "name": "Barry Docks Rail Station",
        "lng": -3.2607,
        "lat": 51.4024
    },
    {
        "code": "TAFFSWL",
        "name": "Taffs Well Rail Station",
        "lng": -3.2629,
        "lat": 51.5408
    },
    {
        "code": "IVRKTHG",
        "name": "Inverkeithing Rail Station",
        "lng": -3.3962,
        "lat": 56.0347
    },
    {
        "code": "SILCRFT",
        "name": "Silecroft Rail Station",
        "lng": -3.3344,
        "lat": 54.226
    },
    {
        "code": "NQNSFRY",
        "name": "North Queensferry Rail Station",
        "lng": -3.3946,
        "lat": 56.0125
    },
    {
        "code": "CADOXTN",
        "name": "Cadoxton Rail Station",
        "lng": -3.2489,
        "lat": 51.4123
    },
    {
        "code": "RADYR",
        "name": "Radyr Rail Station",
        "lng": -3.2484,
        "lat": 51.5163
    },
    {
        "code": "LCKRBIE",
        "name": "Lockerbie Rail Station",
        "lng": -3.3535,
        "lat": 55.1231
    },
    {
        "code": "DLMY",
        "name": "Dalmeny Rail Station",
        "lng": -3.3816,
        "lat": 55.9863
    },
    {
        "code": "DOLAU",
        "name": "Dolau Rail Station",
        "lng": -3.2636,
        "lat": 52.2953
    },
    {
        "code": "TIRPHIL",
        "name": "Tir-phil Rail Station",
        "lng": -3.2464,
        "lat": 51.7209
    },
    {
        "code": "YSTRADM",
        "name": "Ystrad Mynach Rail Station",
        "lng": -3.2413,
        "lat": 51.6409
    },
    {
        "code": "ASPTRIA",
        "name": "Aspatria Rail Station",
        "lng": -3.3319,
        "lat": 54.759
    },
    {
        "code": "FRWATER",
        "name": "Fairwater Rail Station",
        "lng": -3.2338,
        "lat": 51.4939
    },
    {
        "code": "DANESCT",
        "name": "Danescourt Rail Station",
        "lng": -3.2339,
        "lat": 51.5005
    },
    {
        "code": "CORYTON",
        "name": "Coryton Rail Station",
        "lng": -3.2318,
        "lat": 51.5204
    },
    {
        "code": "LLBRDCH",
        "name": "Llanbradach Rail Station",
        "lng": -3.233,
        "lat": 51.6033
    },
    {
        "code": "WAUNGRN",
        "name": "Waun-gron Park Rail Station",
        "lng": -3.2297,
        "lat": 51.4882
    },
    {
        "code": "LLANDAF",
        "name": "Llandaf Rail Station",
        "lng": -3.2286,
        "lat": 51.5084
    },
    {
        "code": "ABER",
        "name": "Aber Rail Station",
        "lng": -3.2298,
        "lat": 51.575
    },
    {
        "code": "DALGETY",
        "name": "Dalgety Bay Rail Station",
        "lng": -3.3677,
        "lat": 56.0421
    },
    {
        "code": "ERGNCHP",
        "name": "Energlyn & Churchill Park Rail Station",
        "lng": -3.2288,
        "lat": 51.5832
    },
    {
        "code": "PENGAM",
        "name": "Pengam Rail Station",
        "lng": -3.2301,
        "lat": 51.6705
    },
    {
        "code": "BARGOED",
        "name": "Bargoed Rail Station",
        "lng": -3.2297,
        "lat": 51.6923
    },
    {
        "code": "BRITHDR",
        "name": "Brithdir Rail Station",
        "lng": -3.2287,
        "lat": 51.7103
    },
    {
        "code": "WHCH",
        "name": "Whitchurch (Cardiff) Rail Station",
        "lng": -3.2233,
        "lat": 51.5207
    },
    {
        "code": "GLFCHFR",
        "name": "Gilfach Fargoed Rail Station",
        "lng": -3.2266,
        "lat": 51.6842
    },
    {
        "code": "DINASP",
        "name": "Dinas Powys Rail Station",
        "lng": -3.2184,
        "lat": 51.4317
    },
    {
        "code": "HENGOED",
        "name": "Hengoed Rail Station",
        "lng": -3.2241,
        "lat": 51.6474
    },
    {
        "code": "GRGMASJ",
        "name": "Georgemas Junction Rail Station",
        "lng": -3.4521,
        "lat": 58.5136
    },
    {
        "code": "CRPHLY",
        "name": "Caerphilly Rail Station",
        "lng": -3.2185,
        "lat": 51.5716
    },
    {
        "code": "RHIWBNA",
        "name": "Rhiwbina Rail Station",
        "lng": -3.214,
        "lat": 51.5212
    },
    {
        "code": "EASTBRK",
        "name": "Eastbrook Rail Station",
        "lng": -3.2061,
        "lat": 51.4376
    },
    {
        "code": "BSPSLYD",
        "name": "Bishop's Lydeard",
        "lng": -3.1943,
        "lat": 51.0546
    },
    {
        "code": "HONITON",
        "name": "Honiton Rail Station",
        "lng": -3.1867,
        "lat": 50.7966
    },
    {
        "code": "CWDNBTH",
        "name": "Cowdenbeath Rail Station",
        "lng": -3.3432,
        "lat": 56.1121
    },
    {
        "code": "NINIANP",
        "name": "Ninian Park Rail Station",
        "lng": -3.2017,
        "lat": 51.4766
    },
    {
        "code": "BCHGRV",
        "name": "Birchgrove Rail Station",
        "lng": -3.2019,
        "lat": 51.5216
    },
    {
        "code": "TYGLAS",
        "name": "Ty Glas Rail Station",
        "lng": -3.1965,
        "lat": 51.5215
    },
    {
        "code": "EBWVTN",
        "name": "Ebbw Vale Town Rail Station",
        "lng": -3.2026,
        "lat": 51.7767
    },
    {
        "code": "MLLM",
        "name": "Millom Rail Station",
        "lng": -3.2711,
        "lat": 54.2108
    },
    {
        "code": "LLBSTRD",
        "name": "Llanbister Road Rail Station",
        "lng": -3.2134,
        "lat": 52.3364
    },
    {
        "code": "GNTN",
        "name": "Grangetown (Cardiff) Rail Station",
        "lng": -3.1897,
        "lat": 51.4676
    },
    {
        "code": "COGAN",
        "name": "Cogan Rail Station",
        "lng": -3.1891,
        "lat": 51.446
    },
    {
        "code": "EBWVPWY",
        "name": "Ebbw Vale Parkway Rail Station",
        "lng": -3.1961,
        "lat": 51.7571
    },
    {
        "code": "EDINGWY",
        "name": "Edinburgh Gateway Rail Station",
        "lng": -3.3203,
        "lat": 55.9409
    },
    {
        "code": "CURRIEH",
        "name": "Curriehill Rail Station",
        "lng": -3.3188,
        "lat": 55.9006
    },
    {
        "code": "LTHH",
        "name": "Lisvane & Thornhill Rail Station",
        "lng": -3.1856,
        "lat": 51.5446
    },
    {
        "code": "DGLROAD",
        "name": "Dingle Road Rail Station",
        "lng": -3.1806,
        "lat": 51.4401
    },
    {
        "code": "HEATHLL",
        "name": "Heath Low Level Rail Station",
        "lng": -3.182,
        "lat": 51.5157
    },
    {
        "code": "LLISHEN",
        "name": "Llanishen Rail Station",
        "lng": -3.182,
        "lat": 51.5327
    },
    {
        "code": "HEATHHL",
        "name": "Heath High Level Rail Station",
        "lng": -3.1815,
        "lat": 51.5164
    },
    {
        "code": "CRDFCEN",
        "name": "Cardiff Central Rail Station",
        "lng": -3.1793,
        "lat": 51.476
    },
    {
        "code": "CATHAYS",
        "name": "Cathays Rail Station",
        "lng": -3.1787,
        "lat": 51.4889
    },
    {
        "code": "EDINPRK",
        "name": "Edinburgh Park Rail Station",
        "lng": -3.3077,
        "lat": 55.9275
    },
    {
        "code": "PENARTH",
        "name": "Penarth Rail Station",
        "lng": -3.1744,
        "lat": 51.4359
    },
    {
        "code": "LCHGLLY",
        "name": "Lochgelly Rail Station",
        "lng": -3.3129,
        "lat": 56.1353
    },
    {
        "code": "CARDFQS",
        "name": "Cardiff Queen Street Rail Station",
        "lng": -3.1702,
        "lat": 51.482
    },
    {
        "code": "STHGYLE",
        "name": "South Gyle Rail Station",
        "lng": -3.2995,
        "lat": 55.9364
    },
    {
        "code": "GREENRD",
        "name": "Green Road Rail Station",
        "lng": -3.2456,
        "lat": 54.2445
    },
    {
        "code": "CARDFBR",
        "name": "Cardiff Bay Rail Station",
        "lng": -3.1664,
        "lat": 51.4671
    },
    {
        "code": "ABDO",
        "name": "Aberdour Rail Station",
        "lng": -3.3006,
        "lat": 56.0546
    },
    {
        "code": "ANNAN",
        "name": "Annan Rail Station",
        "lng": -3.2626,
        "lat": 54.9838
    },
    {
        "code": "WHAILES",
        "name": "Wester Hailes Rail Station",
        "lng": -3.2843,
        "lat": 55.9143
    },
    {
        "code": "BAROW",
        "name": "Barrow-in-Furness Rail Station",
        "lng": -3.2261,
        "lat": 54.119
    },
    {
        "code": "FOXFILD",
        "name": "Foxfield Rail Station",
        "lng": -3.2161,
        "lat": 54.2587
    },
    {
        "code": "LLGUNLO",
        "name": "Llangynllo Rail Station",
        "lng": -3.1614,
        "lat": 52.3496
    },
    {
        "code": "KNGW",
        "name": "Kingsknowe Rail Station",
        "lng": -3.265,
        "lat": 55.9188
    },
    {
        "code": "NBRWGE",
        "name": "Newbridge Rail Station",
        "lng": -3.1429,
        "lat": 51.6658
    },
    {
        "code": "WKIRBY",
        "name": "West Kirby Rail Station",
        "lng": -3.1838,
        "lat": 53.3732
    },
    {
        "code": "ASKAM",
        "name": "Askam Rail Station",
        "lng": -3.2045,
        "lat": 54.1889
    },
    {
        "code": "LLHLETH",
        "name": "Llanhilleth Rail Station",
        "lng": -3.1352,
        "lat": 51.7003
    },
    {
        "code": "CDND",
        "name": "Cardenden Rail Station",
        "lng": -3.2616,
        "lat": 56.1413
    },
    {
        "code": "HOYLAKE",
        "name": "Hoylake Rail Station",
        "lng": -3.1788,
        "lat": 53.3902
    },
    {
        "code": "ELGIN",
        "name": "Elgin Rail Station",
        "lng": -3.3112,
        "lat": 57.6429
    },
    {
        "code": "ROOSE",
        "name": "Roose Rail Station",
        "lng": -3.1946,
        "lat": 54.1152
    },
    {
        "code": "CRSKEYS",
        "name": "Crosskeys Rail Station",
        "lng": -3.1262,
        "lat": 51.6209
    },
    {
        "code": "MNRD",
        "name": "Manor Road Rail Station",
        "lng": -3.1714,
        "lat": 53.3948
    },
    {
        "code": "SLATEFD",
        "name": "Slateford Rail Station",
        "lng": -3.2435,
        "lat": 55.9267
    },
    {
        "code": "KRKBYIF",
        "name": "Kirkby-in-Furness Rail Station",
        "lng": -3.1874,
        "lat": 54.2327
    },
    {
        "code": "TAUNTON",
        "name": "Taunton Rail Station",
        "lng": -3.1027,
        "lat": 51.0233
    },
    {
        "code": "WELSHPL",
        "name": "Welshpool Rail Station",
        "lng": -3.1399,
        "lat": 52.6575
    },
    {
        "code": "DALTON",
        "name": "Dalton Rail Station",
        "lng": -3.179,
        "lat": 54.1542
    },
    {
        "code": "BISLND",
        "name": "Burntisland Rail Station",
        "lng": -3.2332,
        "lat": 56.0571
    },
    {
        "code": "MELS",
        "name": "Meols Rail Station",
        "lng": -3.1543,
        "lat": 53.3994
    },
    {
        "code": "HAYMRKT",
        "name": "Haymarket Rail Station",
        "lng": -3.2184,
        "lat": 55.9458
    },
    {
        "code": "RISCA",
        "name": "Risca & Pontymister Rail Station",
        "lng": -3.0922,
        "lat": 51.6058
    },
    {
        "code": "FLINT",
        "name": "Flint Rail Station",
        "lng": -3.133,
        "lat": 53.2495
    },
    {
        "code": "WIGTON",
        "name": "Wigton Rail Station",
        "lng": -3.1643,
        "lat": 54.8291
    },
    {
        "code": "KNUCKLS",
        "name": "Knucklas Rail Station",
        "lng": -3.0969,
        "lat": 52.3599
    },
    {
        "code": "EDINBUR",
        "name": "Edinburgh Rail Station",
        "lng": -3.1882,
        "lat": 55.9524
    },
    {
        "code": "MOTO",
        "name": "Moreton (Merseyside) Rail Station",
        "lng": -3.1135,
        "lat": 53.4072
    },
    {
        "code": "ROGRSTN",
        "name": "Rogerstone Rail Station",
        "lng": -3.0666,
        "lat": 51.5956
    },
    {
        "code": "KGHN",
        "name": "Kinghorn Rail Station",
        "lng": -3.1742,
        "lat": 56.0693
    },
    {
        "code": "LEASOWE",
        "name": "Leasowe Rail Station",
        "lng": -3.0996,
        "lat": 53.408
    },
    {
        "code": "KCLD",
        "name": "Kirkcaldy Rail Station",
        "lng": -3.167,
        "lat": 56.1121
    },
    {
        "code": "PYECRNR",
        "name": "Pye Corner Rail Station",
        "lng": -3.0412,
        "lat": 51.5815
    },
    {
        "code": "UPTON",
        "name": "Upton Rail Station",
        "lng": -3.0842,
        "lat": 53.3865
    },
    {
        "code": "BDSTON",
        "name": "Bidston Rail Station",
        "lng": -3.0786,
        "lat": 53.4091
    },
    {
        "code": "ULVRSTN",
        "name": "Ulverston Rail Station",
        "lng": -3.0979,
        "lat": 54.1916
    },
    {
        "code": "CHIRK",
        "name": "Chirk Rail Station",
        "lng": -3.0656,
        "lat": 52.9331
    },
    {
        "code": "HESWALL",
        "name": "Heswall Rail Station",
        "lng": -3.0737,
        "lat": 53.3297
    },
    {
        "code": "WALAGRD",
        "name": "Wallasey Grove Road Rail Station",
        "lng": -3.0697,
        "lat": 53.428
    },
    {
        "code": "WALASYV",
        "name": "Wallasey Village Rail Station",
        "lng": -3.0691,
        "lat": 53.4229
    },
    {
        "code": "KNIGHTN",
        "name": "Knighton Rail Station",
        "lng": -3.0422,
        "lat": 52.3451
    },
    {
        "code": "FRSHFLD",
        "name": "Freshfield Rail Station",
        "lng": -3.0718,
        "lat": 53.5661
    },
    {
        "code": "GLNRTHS",
        "name": "Glenrothes with Thornton Rail Station",
        "lng": -3.143,
        "lat": 56.1624
    },
    {
        "code": "FORMBY",
        "name": "Formby Rail Station",
        "lng": -3.0709,
        "lat": 53.5535
    },
    {
        "code": "NESTON",
        "name": "Neston Rail Station",
        "lng": -3.0631,
        "lat": 53.2918
    },
    {
        "code": "AXMNSTR",
        "name": "Axminster Rail Station",
        "lng": -3.0047,
        "lat": 50.7793
    },
    {
        "code": "BCKY",
        "name": "Buckley Rail Station",
        "lng": -3.0559,
        "lat": 53.163
    },
    {
        "code": "PNYF",
        "name": "Penyffordd Rail Station",
        "lng": -3.0548,
        "lat": 53.1431
    },
    {
        "code": "BRKNHDN",
        "name": "Birkenhead North Rail Station",
        "lng": -3.0575,
        "lat": 53.4044
    },
    {
        "code": "CWMBRAN",
        "name": "Cwmbran Rail Station",
        "lng": -3.0162,
        "lat": 51.6566
    },
    {
        "code": "MKIN",
        "name": "Markinch Rail Station",
        "lng": -3.1308,
        "lat": 56.201
    },
    {
        "code": "PONTYPL",
        "name": "Pontypool & New Inn Rail Station",
        "lng": -3.0142,
        "lat": 51.698
    },
    {
        "code": "HITN",
        "name": "Hightown Rail Station",
        "lng": -3.0571,
        "lat": 53.5251
    },
    {
        "code": "RUABON",
        "name": "Ruabon Rail Station",
        "lng": -3.0431,
        "lat": 52.9871
    },
    {
        "code": "GOBOWEN",
        "name": "Gobowen Rail Station",
        "lng": -3.0372,
        "lat": 52.8935
    },
    {
        "code": "HALLRD",
        "name": "Hall Road Rail Station",
        "lng": -3.0496,
        "lat": 53.4975
    },
    {
        "code": "NBTN",
        "name": "New Brighton Rail Station",
        "lng": -3.048,
        "lat": 53.4374
    },
    {
        "code": "ABRGVNY",
        "name": "Abergavenny Rail Station",
        "lng": -3.0096,
        "lat": 51.8167
    },
    {
        "code": "LADYBNK",
        "name": "Ladybank Rail Station",
        "lng": -3.1223,
        "lat": 56.2738
    },
    {
        "code": "BLCKPB",
        "name": "Blackpool Pleasure Beach Rail Station",
        "lng": -3.0539,
        "lat": 53.788
    },
    {
        "code": "HOPC",
        "name": "Hope (Flintshire) Rail Station",
        "lng": -3.0369,
        "lat": 53.1174
    },
    {
        "code": "SHOTTON",
        "name": "Shotton Rail Station",
        "lng": -3.0384,
        "lat": 53.2125
    },
    {
        "code": "NWPTRTG",
        "name": "Newport (S Wales) Rail Station",
        "lng": -3.0005,
        "lat": 51.5888
    },
    {
        "code": "BRDGWTR",
        "name": "Bridgwater Rail Station",
        "lng": -2.9904,
        "lat": 51.1279
    },
    {
        "code": "SHOTTHL",
        "name": "Shotton High Level Rail Station",
        "lng": -3.0377,
        "lat": 53.2135
    },
    {
        "code": "SQUIRES",
        "name": "Squires Gate Rail Station",
        "lng": -3.0503,
        "lat": 53.7773
    },
    {
        "code": "CAERGWL",
        "name": "Caergwrle Rail Station",
        "lng": -3.0329,
        "lat": 53.1079
    },
    {
        "code": "BRKNHDP",
        "name": "Birkenhead Park Rail Station",
        "lng": -3.0391,
        "lat": 53.3974
    },
    {
        "code": "BLCKS",
        "name": "Blackpool South Rail Station",
        "lng": -3.0489,
        "lat": 53.7987
    },
    {
        "code": "BLCKPLN",
        "name": "Blackpool North Rail Station",
        "lng": -3.0493,
        "lat": 53.8219
    },
    {
        "code": "CEFNYBD",
        "name": "Cefn-y-Bedd Rail Station",
        "lng": -3.0311,
        "lat": 53.0988
    },
    {
        "code": "BLNDLAC",
        "name": "Blundellsands & Crosby Rail Station",
        "lng": -3.0399,
        "lat": 53.4877
    },
    {
        "code": "AINSDAL",
        "name": "Ainsdale Rail Station",
        "lng": -3.0427,
        "lat": 53.602
    },
    {
        "code": "HAWARDN",
        "name": "Hawarden Rail Station",
        "lng": -3.0321,
        "lat": 53.1854
    },
    {
        "code": "HAWDNBG",
        "name": "Hawarden Bridge Rail Station",
        "lng": -3.0327,
        "lat": 53.2181
    },
    {
        "code": "BRUSTAN",
        "name": "Brunstane Rail Station",
        "lng": -3.101,
        "lat": 55.9425
    },
    {
        "code": "GWRSYLT",
        "name": "Gwersyllt Rail Station",
        "lng": -3.0179,
        "lat": 53.0726
    },
    {
        "code": "NCRAGHA",
        "name": "Newcraighall Rail Station",
        "lng": -3.0908,
        "lat": 55.9331
    },
    {
        "code": "GRETGRN",
        "name": "Gretna Green Rail Station",
        "lng": -3.0652,
        "lat": 55.001
    },
    {
        "code": "WLOO",
        "name": "Waterloo (Merseyside) Rail Station",
        "lng": -3.0255,
        "lat": 53.475
    },
    {
        "code": "BRKNCPK",
        "name": "Conway Park Rail Station",
        "lng": -3.0227,
        "lat": 53.3934
    },
    {
        "code": "HGHBRDG",
        "name": "Highbridge & Burnham-on-Sea Rail Station",
        "lng": -2.9722,
        "lat": 51.2182
    },
    {
        "code": "BRKNHDC",
        "name": "Birkenhead Central Rail Station",
        "lng": -3.0208,
        "lat": 53.3883
    },
    {
        "code": "STAS",
        "name": "St Annes-on-the-Sea Rail Station",
        "lng": -3.0291,
        "lat": 53.753
    },
    {
        "code": "LAYTON",
        "name": "Layton (Lancs) Rail Station",
        "lng": -3.03,
        "lat": 53.8353
    },
    {
        "code": "HILLSID",
        "name": "Hillside Rail Station",
        "lng": -3.0247,
        "lat": 53.6221
    },
    {
        "code": "ESKBANK",
        "name": "Eskbank Rail Station",
        "lng": -3.0831,
        "lat": 55.8818
    },
    {
        "code": "WSMARE",
        "name": "Weston-super-Mare Rail Station",
        "lng": -2.9717,
        "lat": 51.3443
    },
    {
        "code": "GNLN",
        "name": "Green Lane Rail Station",
        "lng": -3.0164,
        "lat": 53.3833
    },
    {
        "code": "SHWFAIR",
        "name": "Shawfair Rail Station",
        "lng": -3.0787,
        "lat": 55.9199
    },
    {
        "code": "HAMTSQ",
        "name": "Birkenhead Hamilton Square Rail Station",
        "lng": -3.0137,
        "lat": 53.3947
    },
    {
        "code": "ROCKFRY",
        "name": "Rock Ferry Rail Station",
        "lng": -3.0108,
        "lat": 53.3726
    },
    {
        "code": "WREXHMG",
        "name": "Wrexham General Rail Station",
        "lng": -3.0024,
        "lat": 53.0502
    },
    {
        "code": "BKDLE",
        "name": "Birkdale Rail Station",
        "lng": -3.0144,
        "lat": 53.634
    },
    {
        "code": "MSELBGH",
        "name": "Musselburgh Rail Station",
        "lng": -3.0732,
        "lat": 55.9336
    },
    {
        "code": "WREXHMC",
        "name": "Wrexham Central Rail Station",
        "lng": -2.9991,
        "lat": 53.0462
    },
    {
        "code": "NWTGRNG",
        "name": "Newtongrange Rail Station",
        "lng": -3.0694,
        "lat": 55.867
    },
    {
        "code": "BEBNGTN",
        "name": "Bebington Rail Station",
        "lng": -3.0036,
        "lat": 53.3577
    },
    {
        "code": "SFRTHAL",
        "name": "Seaforth & Litherland Rail Station",
        "lng": -3.0056,
        "lat": 53.4663
    },
    {
        "code": "PSLT",
        "name": "Port Sunlight Rail Station",
        "lng": -2.998,
        "lat": 53.3492
    },
    {
        "code": "SOUTHPT",
        "name": "Southport Rail Station",
        "lng": -3.0024,
        "lat": 53.6465
    },
    {
        "code": "SPITAL",
        "name": "Spital Rail Station",
        "lng": -2.9939,
        "lat": 53.3399
    },
    {
        "code": "BOOTLOR",
        "name": "Bootle Oriel Road Rail Station",
        "lng": -2.9957,
        "lat": 53.4466
    },
    {
        "code": "BOOTLNS",
        "name": "Bootle New Strand Rail Station",
        "lng": -2.9947,
        "lat": 53.4534
    },
    {
        "code": "JAMESST",
        "name": "Liverpool James Street Rail Station",
        "lng": -2.992,
        "lat": 53.4048
    },
    {
        "code": "BRMBRK",
        "name": "Bromborough Rake Rail Station",
        "lng": -2.9895,
        "lat": 53.3299
    },
    {
        "code": "SANDH",
        "name": "Sandhills Rail Station",
        "lng": -2.9915,
        "lat": 53.4299
    },
    {
        "code": "MORFLDS",
        "name": "Moorfields Rail Station",
        "lng": -2.9892,
        "lat": 53.4086
    },
    {
        "code": "MORFNL",
        "name": "Moorfields Rail Station",
        "lng": -2.9892,
        "lat": 53.4086
    },
    {
        "code": "BRMB",
        "name": "Bromborough Rail Station",
        "lng": -2.9869,
        "lat": 53.3218
    },
    {
        "code": "WMILTON",
        "name": "Weston Milton Rail Station",
        "lng": -2.9424,
        "lat": 51.3485
    },
    {
        "code": "BNKHALL",
        "name": "Bank Hall Rail Station",
        "lng": -2.9875,
        "lat": 53.4375
    },
    {
        "code": "GOREBRG",
        "name": "Gorebridge Rail Station",
        "lng": -3.0465,
        "lat": 55.8403
    },
    {
        "code": "ANSDELL",
        "name": "Ansdell & Fairhaven Rail Station",
        "lng": -2.993,
        "lat": 53.7415
    },
    {
        "code": "ESTHRAK",
        "name": "Eastham Rake Rail Station",
        "lng": -2.9811,
        "lat": 53.3075
    },
    {
        "code": "KRKDALE",
        "name": "Kirkdale Rail Station",
        "lng": -2.9811,
        "lat": 53.4409
    },
    {
        "code": "PLTNLFY",
        "name": "Poulton-le-Fylde Rail Station",
        "lng": -2.9906,
        "lat": 53.8484
    },
    {
        "code": "INVGWRE",
        "name": "Invergowrie Rail Station",
        "lng": -3.0574,
        "lat": 56.4565
    },
    {
        "code": "SPFD",
        "name": "Springfield Rail Station",
        "lng": -3.0524,
        "lat": 56.295
    },
    {
        "code": "HOOTON",
        "name": "Hooton Rail Station",
        "lng": -2.977,
        "lat": 53.2972
    },
    {
        "code": "LVRPLCH",
        "name": "Liverpool Central Rail Station",
        "lng": -2.9792,
        "lat": 53.4046
    },
    {
        "code": "LVRPLCL",
        "name": "Liverpool Central Loop Line",
        "lng": -2.9792,
        "lat": 53.4046
    },
    {
        "code": "LVRPLSH",
        "name": "Liverpool Lime Street Rail Station",
        "lng": -2.9777,
        "lat": 53.4073
    },
    {
        "code": "LVRPLSL",
        "name": "Liverpool Lime Street Low Level Rail Station",
        "lng": -2.9777,
        "lat": 53.4082
    },
    {
        "code": "BNWK",
        "name": "Brunswick Rail Station",
        "lng": -2.9761,
        "lat": 53.3832
    },
    {
        "code": "BKNELL",
        "name": "Bucknell Rail Station",
        "lng": -2.9474,
        "lat": 52.3574
    },
    {
        "code": "MEOLSCP",
        "name": "Meols Cop Rail Station",
        "lng": -2.9758,
        "lat": 53.6463
    },
    {
        "code": "WALTONM",
        "name": "Walton (Merseyside) Rail Station",
        "lng": -2.9657,
        "lat": 53.4562
    },
    {
        "code": "WICK",
        "name": "Wick Rail Station",
        "lng": -3.0969,
        "lat": 58.4416
    },
    {
        "code": "ORELPKH",
        "name": "Orrell Park Rail Station",
        "lng": -2.9633,
        "lat": 53.4619
    },
    {
        "code": "RICELA",
        "name": "Rice Lane Rail Station",
        "lng": -2.9623,
        "lat": 53.4578
    },
    {
        "code": "LYTHAM",
        "name": "Lytham Rail Station",
        "lng": -2.964,
        "lat": 53.7393
    },
    {
        "code": "CARK",
        "name": "Cark Rail Station",
        "lng": -2.9741,
        "lat": 54.178
    },
    {
        "code": "DALSTON",
        "name": "Dalston (Cumbria) Rail Station",
        "lng": -2.9889,
        "lat": 54.8462
    },
    {
        "code": "AINTREE",
        "name": "Aintree Rail Station",
        "lng": -2.9563,
        "lat": 53.4739
    },
    {
        "code": "WALLYFD",
        "name": "Wallyford Rail Station",
        "lng": -3.015,
        "lat": 55.9403
    },
    {
        "code": "STMCHLS",
        "name": "St Michaels Rail Station",
        "lng": -2.9528,
        "lat": 53.3756
    },
    {
        "code": "WORLE",
        "name": "Worle Rail Station",
        "lng": -2.9096,
        "lat": 51.358
    },
    {
        "code": "OLDROAN",
        "name": "Old Roan Rail Station",
        "lng": -2.9511,
        "lat": 53.4869
    },
    {
        "code": "EDGH",
        "name": "Edge Hill Rail Station",
        "lng": -2.9465,
        "lat": 53.4026
    },
    {
        "code": "LTLSUTN",
        "name": "Little Sutton Rail Station",
        "lng": -2.9433,
        "lat": 53.2855
    },
    {
        "code": "CPNHRST",
        "name": "Capenhurst Rail Station",
        "lng": -2.9423,
        "lat": 53.2602
    },
    {
        "code": "CUPAR",
        "name": "Cupar Rail Station",
        "lng": -3.0088,
        "lat": 56.317
    },
    {
        "code": "FAZKRLY",
        "name": "Fazakerley Rail Station",
        "lng": -2.9367,
        "lat": 53.4691
    },
    {
        "code": "MSSD",
        "name": "Moss Side Rail Station",
        "lng": -2.9429,
        "lat": 53.765
    },
    {
        "code": "HOPTONH",
        "name": "Hopton Heath Rail Station",
        "lng": -2.9121,
        "lat": 52.3914
    },
    {
        "code": "MAGHULL",
        "name": "Maghull Rail Station",
        "lng": -2.9309,
        "lat": 53.5065
    },
    {
        "code": "AIGBURT",
        "name": "Aigburth Rail Station",
        "lng": -2.9272,
        "lat": 53.3646
    },
    {
        "code": "OPOL",
        "name": "Overpool Rail Station",
        "lng": -2.9241,
        "lat": 53.284
    },
    {
        "code": "WVRTTEC",
        "name": "Wavertree Technology Park Rail Station",
        "lng": -2.9229,
        "lat": 53.4052
    },
    {
        "code": "MSLH",
        "name": "Mossley Hill Rail Station",
        "lng": -2.9154,
        "lat": 53.379
    },
    {
        "code": "PPAN",
        "name": "Prestonpans Rail Station",
        "lng": -2.9748,
        "lat": 55.9531
    },
    {
        "code": "CRSNGTN",
        "name": "Cressington Rail Station",
        "lng": -2.912,
        "lat": 53.3587
    },
    {
        "code": "BESCRLA",
        "name": "Bescar Lane Rail Station",
        "lng": -2.9146,
        "lat": 53.6239
    },
    {
        "code": "KTBK",
        "name": "Kents Bank Rail Station",
        "lng": -2.9252,
        "lat": 54.1729
    },
    {
        "code": "WALERTN",
        "name": "West Allerton Rail Station",
        "lng": -2.907,
        "lat": 53.3691
    },
    {
        "code": "BROOME",
        "name": "Broome Rail Station",
        "lng": -2.8852,
        "lat": 52.4228
    },
    {
        "code": "TOWNGRN",
        "name": "Town Green Rail Station",
        "lng": -2.9045,
        "lat": 53.5428
    },
    {
        "code": "KKBY",
        "name": "Kirkby Rail Station",
        "lng": -2.9028,
        "lat": 53.4862
    },
    {
        "code": "CARLILE",
        "name": "Carlisle Rail Station",
        "lng": -2.9332,
        "lat": 54.8907
    },
    {
        "code": "DUNDETB",
        "name": "Dundee Rail Station",
        "lng": -2.9712,
        "lat": 56.4565
    },
    {
        "code": "HEYMST",
        "name": "Heysham Port Rail Station",
        "lng": -2.9131,
        "lat": 54.0331
    },
    {
        "code": "ELSMPRT",
        "name": "Ellesmere Port Rail Station",
        "lng": -2.8964,
        "lat": 53.2822
    },
    {
        "code": "BACHE",
        "name": "Bache Rail Station",
        "lng": -2.8917,
        "lat": 53.2088
    },
    {
        "code": "BROADGR",
        "name": "Broad Green Rail Station",
        "lng": -2.8935,
        "lat": 53.4065
    },
    {
        "code": "AGHTNPH",
        "name": "Aughton Park Rail Station",
        "lng": -2.8952,
        "lat": 53.5542
    },
    {
        "code": "LVRPSPY",
        "name": "Liverpool South Parkway Rail Station",
        "lng": -2.8891,
        "lat": 53.3577
    },
    {
        "code": "ALERTN",
        "name": "Liverpool South Parkway Rail Station",
        "lng": -2.8891,
        "lat": 53.3577
    },
    {
        "code": "GOVS",
        "name": "Grange-over-Sands Rail Station",
        "lng": -2.9027,
        "lat": 54.1957
    },
    {
        "code": "CHST",
        "name": "Chester Rail Station",
        "lng": -2.8796,
        "lat": 53.1967
    },
    {
        "code": "WMER",
        "name": "Windermere Rail Station",
        "lng": -2.9034,
        "lat": 54.3796
    },
    {
        "code": "ORMSKRK",
        "name": "Ormskirk Rail Station",
        "lng": -2.8812,
        "lat": 53.5693
    },
    {
        "code": "KIRKHAM",
        "name": "Kirkham & Wesham Rail Station",
        "lng": -2.8829,
        "lat": 53.7869
    },
    {
        "code": "YATTON",
        "name": "Yatton Rail Station",
        "lng": -2.8278,
        "lat": 51.391
    },
    {
        "code": "NEWLANE",
        "name": "New Lane Rail Station",
        "lng": -2.8677,
        "lat": 53.6117
    },
    {
        "code": "KEITH",
        "name": "Keith Rail Station",
        "lng": -2.9541,
        "lat": 57.5509
    },
    {
        "code": "HUNTSX",
        "name": "Hunts Cross Rail Station",
        "lng": -2.8559,
        "lat": 53.3607
    },
    {
        "code": "CRAVENA",
        "name": "Craven Arms Rail Station",
        "lng": -2.8374,
        "lat": 52.4425
    },
    {
        "code": "ROBY",
        "name": "Roby Rail Station",
        "lng": -2.8559,
        "lat": 53.41
    },
    {
        "code": "MORCAME",
        "name": "Morecambe Rail Station",
        "lng": -2.8693,
        "lat": 54.0703
    },
    {
        "code": "STNLWAT",
        "name": "Stanlow & Thornton Rail Station",
        "lng": -2.8421,
        "lat": 53.2784
    },
    {
        "code": "HUYTON",
        "name": "Huyton Rail Station",
        "lng": -2.843,
        "lat": 53.4097
    },
    {
        "code": "BRSCGHB",
        "name": "Burscough Bridge Rail Station",
        "lng": -2.8409,
        "lat": 53.6053
    },
    {
        "code": "BRSCGHJ",
        "name": "Burscough Junction Rail Station",
        "lng": -2.8406,
        "lat": 53.5975
    },
    {
        "code": "LNGNDRY",
        "name": "Longniddry Rail Station",
        "lng": -2.8883,
        "lat": 55.9765
    },
    {
        "code": "HALW",
        "name": "Halewood Rail Station",
        "lng": -2.8301,
        "lat": 53.3645
    },
    {
        "code": "LEUCHRS",
        "name": "Leuchars Rail Station",
        "lng": -2.8937,
        "lat": 56.3751
    },
    {
        "code": "CRKRN",
        "name": "Crewkerne Rail Station",
        "lng": -2.7785,
        "lat": 50.8735
    },
    {
        "code": "BARELA",
        "name": "Bare Lane Rail Station",
        "lng": -2.8353,
        "lat": 54.0745
    },
    {
        "code": "CSTR",
        "name": "Church Stretton Rail Station",
        "lng": -2.8037,
        "lat": 52.5374
    },
    {
        "code": "INEL",
        "name": "Ince & Elton Rail Station",
        "lng": -2.8165,
        "lat": 53.2766
    },
    {
        "code": "STOW",
        "name": "Stow Rail Station",
        "lng": -2.8659,
        "lat": 55.6924
    },
    {
        "code": "ARNSIDE",
        "name": "Arnside Rail Station",
        "lng": -2.8282,
        "lat": 54.2027
    },
    {
        "code": "SEVTNLJ",
        "name": "Severn Tunnel Junction Rail Station",
        "lng": -2.7779,
        "lat": 51.5847
    },
    {
        "code": "SALWICK",
        "name": "Salwick Rail Station",
        "lng": -2.817,
        "lat": 53.7815
    },
    {
        "code": "BRFRY",
        "name": "Broughty Ferry Rail Station",
        "lng": -2.8732,
        "lat": 56.4672
    },
    {
        "code": "RUFDORD",
        "name": "Rufford Rail Station",
        "lng": -2.8078,
        "lat": 53.6345
    },
    {
        "code": "WETHERL",
        "name": "Wetheral Rail Station",
        "lng": -2.8317,
        "lat": 54.8838
    },
    {
        "code": "HOSCAR",
        "name": "Hoscar Rail Station",
        "lng": -2.8044,
        "lat": 53.5978
    },
    {
        "code": "STAVELY",
        "name": "Staveley Rail Station",
        "lng": -2.8189,
        "lat": 54.3755
    },
    {
        "code": "PRESCOT",
        "name": "Prescot Rail Station",
        "lng": -2.7992,
        "lat": 53.4236
    },
    {
        "code": "WHISTON",
        "name": "Whiston Rail Station",
        "lng": -2.7964,
        "lat": 53.4139
    },
    {
        "code": "LANCSTR",
        "name": "Lancaster Rail Station",
        "lng": -2.8075,
        "lat": 54.0487
    },
    {
        "code": "CDCOT",
        "name": "Caldicot Rail Station",
        "lng": -2.7606,
        "lat": 51.5848
    },
    {
        "code": "SDAL",
        "name": "Silverdale Rail Station",
        "lng": -2.8038,
        "lat": 54.1699
    },
    {
        "code": "RNFD",
        "name": "Rainford Rail Station",
        "lng": -2.7895,
        "lat": 53.5171
    },
    {
        "code": "NAILSEA",
        "name": "Nailsea & Backwell Rail Station",
        "lng": -2.7506,
        "lat": 51.4194
    },
    {
        "code": "ECPK",
        "name": "Eccleston Park Rail Station",
        "lng": -2.78,
        "lat": 53.4308
    },
    {
        "code": "BALMOSS",
        "name": "Balmossie Rail Station",
        "lng": -2.839,
        "lat": 56.4746
    },
    {
        "code": "HOUGHGR",
        "name": "Hough Green Rail Station",
        "lng": -2.7751,
        "lat": 53.3724
    },
    {
        "code": "HELSBY",
        "name": "Helsby Rail Station",
        "lng": -2.7712,
        "lat": 53.2752
    },
    {
        "code": "CROT",
        "name": "Croston Rail Station",
        "lng": -2.7777,
        "lat": 53.6676
    },
    {
        "code": "PARBOLD",
        "name": "Parbold Rail Station",
        "lng": -2.7707,
        "lat": 53.5908
    },
    {
        "code": "RHIL",
        "name": "Rainhill Rail Station",
        "lng": -2.7664,
        "lat": 53.4171
    },
    {
        "code": "GALASLS",
        "name": "Galashiels Rail Station",
        "lng": -2.8069,
        "lat": 55.6183
    },
    {
        "code": "SHRWBY",
        "name": "Shrewsbury Rail Station",
        "lng": -2.7498,
        "lat": 52.7119
    },
    {
        "code": "THHT",
        "name": "Thatto Heath Rail Station",
        "lng": -2.7594,
        "lat": 53.4366
    },
    {
        "code": "CRNF",
        "name": "Carnforth Rail Station",
        "lng": -2.7712,
        "lat": 54.1297
    },
    {
        "code": "MONIFTH",
        "name": "Monifieth Rail Station",
        "lng": -2.8182,
        "lat": 56.4801
    },
    {
        "code": "LEOMNST",
        "name": "Leominster Rail Station",
        "lng": -2.7303,
        "lat": 52.2257
    },
    {
        "code": "BNSD",
        "name": "Burneside (Cumbria) Rail Station",
        "lng": -2.7667,
        "lat": 54.355
    },
    {
        "code": "YORTON",
        "name": "Yorton Rail Station",
        "lng": -2.7365,
        "lat": 52.809
    },
    {
        "code": "ARMTHWT",
        "name": "Armathwaite Rail Station",
        "lng": -2.7721,
        "lat": 54.8095
    },
    {
        "code": "RUNCORN",
        "name": "Runcorn Rail Station",
        "lng": -2.7393,
        "lat": 53.3387
    },
    {
        "code": "UPHOLND",
        "name": "Upholland Rail Station",
        "lng": -2.7414,
        "lat": 53.5284
    },
    {
        "code": "DREMJ",
        "name": "Drem Rail Station",
        "lng": -2.786,
        "lat": 56.0051
    },
    {
        "code": "PNTH",
        "name": "Penrith North Lakes Rail Station",
        "lng": -2.7589,
        "lat": 54.6618
    },
    {
        "code": "MLDSWTH",
        "name": "Mouldsworth Rail Station",
        "lng": -2.7322,
        "lat": 53.2318
    },
    {
        "code": "WIDNES",
        "name": "Widnes Rail Station",
        "lng": -2.7335,
        "lat": 53.3785
    },
    {
        "code": "LUDLOW",
        "name": "Ludlow Rail Station",
        "lng": -2.7162,
        "lat": 52.3713
    },
    {
        "code": "HEREFRD",
        "name": "Hereford Rail Station",
        "lng": -2.7082,
        "lat": 52.0612
    },
    {
        "code": "AVONMTH",
        "name": "Avonmouth Rail Station",
        "lng": -2.6995,
        "lat": 51.5004
    },
    {
        "code": "STHLNSC",
        "name": "St Helens Central Rail Station",
        "lng": -2.7303,
        "lat": 53.4531
    },
    {
        "code": "WEMM",
        "name": "Wem Rail Station",
        "lng": -2.718,
        "lat": 52.8564
    },
    {
        "code": "SADWRD",
        "name": "St Andrews Road Rail Station",
        "lng": -2.6963,
        "lat": 51.5128
    },
    {
        "code": "FRDSHM",
        "name": "Frodsham Rail Station",
        "lng": -2.7236,
        "lat": 53.2958
    },
    {
        "code": "LEGR",
        "name": "Lea Green Rail Station",
        "lng": -2.725,
        "lat": 53.4268
    },
    {
        "code": "KENDAL",
        "name": "Kendal Rail Station",
        "lng": -2.7396,
        "lat": 54.3321
    },
    {
        "code": "TWDBANK",
        "name": "Tweedbank Rail Station",
        "lng": -2.7595,
        "lat": 55.6057
    },
    {
        "code": "APLYBDG",
        "name": "Appley Bridge Rail Station",
        "lng": -2.7193,
        "lat": 53.5787
    },
    {
        "code": "SHAMPTN",
        "name": "Shirehampton Rail Station",
        "lng": -2.6793,
        "lat": 51.4843
    },
    {
        "code": "ORRELL",
        "name": "Orrell Rail Station",
        "lng": -2.7088,
        "lat": 53.5303
    },
    {
        "code": "OXENHLM",
        "name": "Oxenholme Lake District Rail Station",
        "lng": -2.7219,
        "lat": 54.3049
    },
    {
        "code": "PRST",
        "name": "Preston Rail Station",
        "lng": -2.7081,
        "lat": 53.7569
    },
    {
        "code": "HNTL",
        "name": "Huntly Rail Station",
        "lng": -2.7757,
        "lat": 57.4445
    },
    {
        "code": "STHLNSJ",
        "name": "St Helens Junction Rail Station",
        "lng": -2.7003,
        "lat": 53.4337
    },
    {
        "code": "CHEPSTW",
        "name": "Chepstow Rail Station",
        "lng": -2.6719,
        "lat": 51.6402
    },
    {
        "code": "PREES",
        "name": "Prees Rail Station",
        "lng": -2.6897,
        "lat": 52.8993
    },
    {
        "code": "SVRNBCH",
        "name": "Severn Beach Rail Station",
        "lng": -2.6645,
        "lat": 51.56
    },
    {
        "code": "GATHRST",
        "name": "Gathurst Rail Station",
        "lng": -2.6944,
        "lat": 53.5594
    },
    {
        "code": "BRRYLNK",
        "name": "Barry Links Rail Station",
        "lng": -2.7454,
        "lat": 56.4931
    },
    {
        "code": "NBERWCK",
        "name": "North Berwick Rail Station",
        "lng": -2.7307,
        "lat": 56.057
    },
    {
        "code": "LEYLAND",
        "name": "Leyland Rail Station",
        "lng": -2.6871,
        "lat": 53.6989
    },
    {
        "code": "LSTH",
        "name": "Lostock Hall Rail Station",
        "lng": -2.6875,
        "lat": 53.7242
    },
    {
        "code": "LAZKRKO",
        "name": "Lazonby & Kirkoswald Rail Station",
        "lng": -2.7032,
        "lat": 54.7504
    },
    {
        "code": "SEMILLS",
        "name": "Sea Mills Rail Station",
        "lng": -2.6499,
        "lat": 51.48
    },
    {
        "code": "WCHR",
        "name": "Whitchurch (Shrops) Rail Station",
        "lng": -2.6717,
        "lat": 52.9681
    },
    {
        "code": "BRMPTNC",
        "name": "Brampton (Cumbria) Rail Station",
        "lng": -2.7029,
        "lat": 54.9324
    },
    {
        "code": "GARW",
        "name": "Garswood Rail Station",
        "lng": -2.6721,
        "lat": 53.4885
    },
    {
        "code": "DELAMER",
        "name": "Delamere Rail Station",
        "lng": -2.6666,
        "lat": 53.2288
    },
    {
        "code": "PBRT",
        "name": "Pemberton Rail Station",
        "lng": -2.6704,
        "lat": 53.5304
    },
    {
        "code": "EUXT",
        "name": "Euxton Balshaw Lane Rail Station",
        "lng": -2.672,
        "lat": 53.6605
    },
    {
        "code": "RUNCRNE",
        "name": "Runcorn East Rail Station",
        "lng": -2.6657,
        "lat": 53.3276
    },
    {
        "code": "GOLFSTR",
        "name": "Golf Street Rail Station",
        "lng": -2.7195,
        "lat": 56.4978
    },
    {
        "code": "CHORBUK",
        "name": "Buckshaw Parkway Rail Station",
        "lng": -2.6608,
        "lat": 53.6733
    },
    {
        "code": "BMBRBDG",
        "name": "Bamber Bridge Rail Station",
        "lng": -2.6608,
        "lat": 53.7269
    },
    {
        "code": "CNST",
        "name": "Carnoustie Rail Station",
        "lng": -2.7066,
        "lat": 56.5006
    },
    {
        "code": "PILNING",
        "name": "Pilning Rail Station",
        "lng": -2.6271,
        "lat": 51.5566
    },
    {
        "code": "SANKEY",
        "name": "Sankey for Penketh Rail Station",
        "lng": -2.6505,
        "lat": 53.3925
    },
    {
        "code": "YOVILPM",
        "name": "Yeovil Pen Mill Rail Station",
        "lng": -2.6134,
        "lat": 50.9445
    },
    {
        "code": "YOVILJN",
        "name": "Yeovil Junction Rail Station",
        "lng": -2.6125,
        "lat": 50.9247
    },
    {
        "code": "BRYN",
        "name": "Bryn Rail Station",
        "lng": -2.6472,
        "lat": 53.4999
    },
    {
        "code": "LWBY",
        "name": "Langwathby Rail Station",
        "lng": -2.6637,
        "lat": 54.6944
    },
    {
        "code": "CLFDOWN",
        "name": "Clifton Down Rail Station",
        "lng": -2.6117,
        "lat": 51.4645
    },
    {
        "code": "ERLSTWN",
        "name": "Earlestown Rail Station",
        "lng": -2.6377,
        "lat": 53.4511
    },
    {
        "code": "PARSNST",
        "name": "Parson Street Rail Station",
        "lng": -2.6077,
        "lat": 51.4333
    },
    {
        "code": "WIGANNW",
        "name": "Wigan North Western Rail Station",
        "lng": -2.6333,
        "lat": 53.5437
    },
    {
        "code": "WIGANWL",
        "name": "Wigan Wallgate Rail Station",
        "lng": -2.6332,
        "lat": 53.5448
    },
    {
        "code": "REDLAND",
        "name": "Redland Rail Station",
        "lng": -2.5991,
        "lat": 51.4684
    },
    {
        "code": "CHORLEY",
        "name": "Chorley Rail Station",
        "lng": -2.6268,
        "lat": 53.6525
    },
    {
        "code": "BDMNSTR",
        "name": "Bedminster Rail Station",
        "lng": -2.5941,
        "lat": 51.4401
    },
    {
        "code": "MONPELR",
        "name": "Montpelier Rail Station",
        "lng": -2.5887,
        "lat": 51.4683
    },
    {
        "code": "NWTNLW",
        "name": "Newton-le-Willows Rail Station",
        "lng": -2.6136,
        "lat": 53.4531
    },
    {
        "code": "THFORD",
        "name": "Thornford Rail Station",
        "lng": -2.579,
        "lat": 50.9106
    },
    {
        "code": "INCE",
        "name": "Ince (Manchester) Rail Station",
        "lng": -2.6115,
        "lat": 53.5389
    },
    {
        "code": "BRSTLTM",
        "name": "Bristol Temple Meads Rail Station",
        "lng": -2.5813,
        "lat": 51.4491
    },
    {
        "code": "YTMNSTR",
        "name": "Yetminster Rail Station",
        "lng": -2.5738,
        "lat": 50.8958
    },
    {
        "code": "CHETNOL",
        "name": "Chetnole Rail Station",
        "lng": -2.5729,
        "lat": 50.8664
    },
    {
        "code": "ACBG",
        "name": "Acton Bridge Rail Station",
        "lng": -2.6031,
        "lat": 53.2665
    },
    {
        "code": "MDNNWTN",
        "name": "Maiden Newton Rail Station",
        "lng": -2.5694,
        "lat": 50.78
    },
    {
        "code": "WRGTNBQ",
        "name": "Warrington Bank Quay Rail Station",
        "lng": -2.6024,
        "lat": 53.386
    },
    {
        "code": "CUDNGTN",
        "name": "Cuddington Rail Station",
        "lng": -2.5993,
        "lat": 53.2399
    },
    {
        "code": "WRENBRY",
        "name": "Wrenbury Rail Station",
        "lng": -2.5959,
        "lat": 53.0194
    },
    {
        "code": "ADNL",
        "name": "Adlington (Lancs) Rail Station",
        "lng": -2.6031,
        "lat": 53.6132
    },
    {
        "code": "WRGT",
        "name": "Warrington Central Rail Station",
        "lng": -2.5932,
        "lat": 53.3918
    },
    {
        "code": "STPLTNR",
        "name": "Stapleton Road Rail Station",
        "lng": -2.5662,
        "lat": 51.4675
    },
    {
        "code": "LAWRNCH",
        "name": "Lawrence Hill Rail Station",
        "lng": -2.5644,
        "lat": 51.458
    },
    {
        "code": "FILTNEW",
        "name": "Filton Abbey Wood Rail Station",
        "lng": -2.5624,
        "lat": 51.5049
    },
    {
        "code": "PATCHWY",
        "name": "Patchway Rail Station",
        "lng": -2.5627,
        "lat": 51.5259
    },
    {
        "code": "WENNGTN",
        "name": "Wennington Rail Station",
        "lng": -2.5875,
        "lat": 54.1237
    },
    {
        "code": "HINDLEY",
        "name": "Hindley Rail Station",
        "lng": -2.5755,
        "lat": 53.5422
    },
    {
        "code": "BLRD",
        "name": "Blackrod Rail Station",
        "lng": -2.5695,
        "lat": 53.5915
    },
    {
        "code": "BRSTPWY",
        "name": "Bristol Parkway Rail Station",
        "lng": -2.5422,
        "lat": 51.5138
    },
    {
        "code": "INSCH",
        "name": "Insch Rail Station",
        "lng": -2.6171,
        "lat": 57.3375
    },
    {
        "code": "PADGATE",
        "name": "Padgate Rail Station",
        "lng": -2.5568,
        "lat": 53.4058
    },
    {
        "code": "HARTFD",
        "name": "Hartford Rail Station",
        "lng": -2.5536,
        "lat": 53.2418
    },
    {
        "code": "LYDNEY",
        "name": "Lydney Rail Station",
        "lng": -2.5309,
        "lat": 51.7141
    },
    {
        "code": "CCARY",
        "name": "Castle Cary Rail Station",
        "lng": -2.5228,
        "lat": 51.0998
    },
    {
        "code": "ARBROTH",
        "name": "Arbroath Rail Station",
        "lng": -2.5889,
        "lat": 56.5596
    },
    {
        "code": "SHERBRN",
        "name": "Sherborne Rail Station",
        "lng": -2.5131,
        "lat": 50.944
    },
    {
        "code": "PLSNGTN",
        "name": "Pleasington Rail Station",
        "lng": -2.5441,
        "lat": 53.731
    },
    {
        "code": "HORWICH",
        "name": "Horwich Parkway Rail Station",
        "lng": -2.5397,
        "lat": 53.5781
    },
    {
        "code": "GBNK",
        "name": "Greenbank Rail Station",
        "lng": -2.5343,
        "lat": 53.2515
    },
    {
        "code": "WELNGTN",
        "name": "Wellington (Shropshire) Rail Station",
        "lng": -2.5172,
        "lat": 52.7013
    },
    {
        "code": "BIRCHWD",
        "name": "Birchwood Rail Station",
        "lng": -2.5253,
        "lat": 53.4127
    },
    {
        "code": "NANTWCH",
        "name": "Nantwich Rail Station",
        "lng": -2.519,
        "lat": 53.0636
    },
    {
        "code": "WSTHOTN",
        "name": "Westhoughton Rail Station",
        "lng": -2.5237,
        "lat": 53.5557
    },
    {
        "code": "KEYNSHM",
        "name": "Keynsham Rail Station",
        "lng": -2.4956,
        "lat": 51.418
    },
    {
        "code": "CHTR",
        "name": "Cherry Tree Rail Station",
        "lng": -2.5184,
        "lat": 53.7329
    },
    {
        "code": "DAISYH",
        "name": "Daisy Hill Rail Station",
        "lng": -2.5159,
        "lat": 53.5395
    },
    {
        "code": "BNTHAM",
        "name": "Bentham Rail Station",
        "lng": -2.5107,
        "lat": 54.1155
    },
    {
        "code": "NTHWICH",
        "name": "Northwich Rail Station",
        "lng": -2.4969,
        "lat": 53.2614
    },
    {
        "code": "MLHL",
        "name": "Mill Hill (Lancs) Rail Station",
        "lng": -2.5017,
        "lat": 53.7355
    },
    {
        "code": "WNSFD",
        "name": "Winsford Rail Station",
        "lng": -2.4946,
        "lat": 53.1905
    },
    {
        "code": "UPWEY",
        "name": "Upwey Rail Station",
        "lng": -2.4661,
        "lat": 50.6483
    },
    {
        "code": "HAGFOLD",
        "name": "Hag Fold Rail Station",
        "lng": -2.4948,
        "lat": 53.5339
    },
    {
        "code": "LOSTCKP",
        "name": "Lostock Rail Station",
        "lng": -2.4943,
        "lat": 53.5729
    },
    {
        "code": "WEYMTH",
        "name": "Weymouth Rail Station",
        "lng": -2.4542,
        "lat": 50.6153
    },
    {
        "code": "DUNBAR",
        "name": "Dunbar Rail Station",
        "lng": -2.5133,
        "lat": 55.9983
    },
    {
        "code": "ATHERTN",
        "name": "Atherton Rail Station",
        "lng": -2.479,
        "lat": 53.5291
    },
    {
        "code": "BLKB",
        "name": "Blackburn Rail Station",
        "lng": -2.4791,
        "lat": 53.7465
    },
    {
        "code": "RMSWILP",
        "name": "Ramsgreave & Wilpshire Rail Station",
        "lng": -2.4781,
        "lat": 53.7798
    },
    {
        "code": "APBY",
        "name": "Appleby Rail Station",
        "lng": -2.4867,
        "lat": 54.5803
    },
    {
        "code": "ZZTYLIN",
        "name": "Lintley Rail Station",
        "lng": -2.4883,
        "lat": 54.8536
    },
    {
        "code": "BRUTON",
        "name": "Bruton Rail Station",
        "lng": -2.4471,
        "lat": 51.1116
    },
    {
        "code": "DRCHW",
        "name": "Dorchester West Rail Station",
        "lng": -2.4425,
        "lat": 50.711
    },
    {
        "code": "LSTG",
        "name": "Lostock Gralam Rail Station",
        "lng": -2.4652,
        "lat": 53.2677
    },
    {
        "code": "DRCHS",
        "name": "Dorchester South Rail Station",
        "lng": -2.4372,
        "lat": 50.7093
    },
    {
        "code": "DARWEN",
        "name": "Darwen Rail Station",
        "lng": -2.4649,
        "lat": 53.698
    },
    {
        "code": "ZZTYKKH",
        "name": "Kirkhaugh Rail Station",
        "lng": -2.4769,
        "lat": 54.8434
    },
    {
        "code": "GLAZBRK",
        "name": "Glazebrook Rail Station",
        "lng": -2.4597,
        "lat": 53.4284
    },
    {
        "code": "OAKNGTS",
        "name": "Oakengates Rail Station",
        "lng": -2.4502,
        "lat": 52.6934
    },
    {
        "code": "YATE",
        "name": "Yate Rail Station",
        "lng": -2.4325,
        "lat": 51.5406
    },
    {
        "code": "TELFRDC",
        "name": "Telford Central Rail Station",
        "lng": -2.441,
        "lat": 52.6811
    },
    {
        "code": "HLTWHST",
        "name": "Haltwhistle Rail Station",
        "lng": -2.4636,
        "lat": 54.9678
    },
    {
        "code": "LGHO",
        "name": "Langho Rail Station",
        "lng": -2.4487,
        "lat": 53.8048
    },
    {
        "code": "TMPCMB",
        "name": "Templecombe Rail Station",
        "lng": -2.4177,
        "lat": 51.0015
    },
    {
        "code": "LDBURY",
        "name": "Ledbury Rail Station",
        "lng": -2.4259,
        "lat": 52.0452
    },
    {
        "code": "CREWE",
        "name": "Crewe Rail Station",
        "lng": -2.433,
        "lat": 53.0896
    },
    {
        "code": "MONTRSE",
        "name": "Montrose Rail Station",
        "lng": -2.4721,
        "lat": 56.7128
    },
    {
        "code": "IRLAM",
        "name": "Irlam Rail Station",
        "lng": -2.4332,
        "lat": 53.4343
    },
    {
        "code": "LRNCKRK",
        "name": "Laurencekirk Rail Station",
        "lng": -2.4659,
        "lat": 56.8363
    },
    {
        "code": "ZZTYALS",
        "name": "Alston Rail Station",
        "lng": -2.4418,
        "lat": 54.8146
    },
    {
        "code": "BOLTON",
        "name": "Bolton Rail Station",
        "lng": -2.4258,
        "lat": 53.5741
    },
    {
        "code": "PLUMLEY",
        "name": "Plumley Rail Station",
        "lng": -2.4197,
        "lat": 53.2747
    },
    {
        "code": "RISHTON",
        "name": "Rishton Rail Station",
        "lng": -2.4202,
        "lat": 53.7638
    },
    {
        "code": "ENTWISL",
        "name": "Entwistle Rail Station",
        "lng": -2.4145,
        "lat": 53.656
    },
    {
        "code": "HITW",
        "name": "Hall i' th' Wood Rail Station",
        "lng": -2.4131,
        "lat": 53.5974
    },
    {
        "code": "BRMCRSS",
        "name": "Bromley Cross Rail Station",
        "lng": -2.4109,
        "lat": 53.614
    },
    {
        "code": "WHALLEY",
        "name": "Whalley Rail Station",
        "lng": -2.4123,
        "lat": 53.824
    },
    {
        "code": "CLPM",
        "name": "Clapham (N Yorks) Rail Station",
        "lng": -2.4104,
        "lat": 54.1054
    },
    {
        "code": "MSGT",
        "name": "Moses Gate Rail Station",
        "lng": -2.4012,
        "lat": 53.556
    },
    {
        "code": "OLDFLDP",
        "name": "Oldfield Park Rail Station",
        "lng": -2.3805,
        "lat": 51.3792
    },
    {
        "code": "SBCH",
        "name": "Sandbach Rail Station",
        "lng": -2.3935,
        "lat": 53.1502
    },
    {
        "code": "WALKDEN",
        "name": "Walkden Rail Station",
        "lng": -2.3963,
        "lat": 53.5198
    },
    {
        "code": "CLITHRO",
        "name": "Clitheroe Rail Station",
        "lng": -2.3943,
        "lat": 53.8735
    },
    {
        "code": "CHOS",
        "name": "Church & Oswaldtwistle Rail Station",
        "lng": -2.3912,
        "lat": 53.7505
    },
    {
        "code": "FRNW",
        "name": "Farnworth Rail Station",
        "lng": -2.3878,
        "lat": 53.55
    },
    {
        "code": "FLIXTON",
        "name": "Flixton Rail Station",
        "lng": -2.3842,
        "lat": 53.4438
    },
    {
        "code": "SHIFNAL",
        "name": "Shifnal Rail Station",
        "lng": -2.3718,
        "lat": 52.6661
    },
    {
        "code": "KEARSLY",
        "name": "Kearsley Rail Station",
        "lng": -2.3751,
        "lat": 53.5441
    },
    {
        "code": "BATHSPA",
        "name": "Bath Spa Rail Station",
        "lng": -2.357,
        "lat": 51.3777
    },
    {
        "code": "DURSLEY",
        "name": "Cam & Dursley Rail Station",
        "lng": -2.3591,
        "lat": 51.7176
    },
    {
        "code": "KNUTSFD",
        "name": "Knutsford Rail Station",
        "lng": -2.3718,
        "lat": 53.3018
    },
    {
        "code": "CLWALL",
        "name": "Colwall Rail Station",
        "lng": -2.357,
        "lat": 52.0799
    },
    {
        "code": "CHASNRD",
        "name": "Chassen Road Rail Station",
        "lng": -2.3682,
        "lat": 53.4462
    },
    {
        "code": "ACRNGTN",
        "name": "Accrington Rail Station",
        "lng": -2.3695,
        "lat": 53.753
    },
    {
        "code": "KSTP",
        "name": "Kirkby Stephen Rail Station",
        "lng": -2.3686,
        "lat": 54.4549
    },
    {
        "code": "PTRCRFT",
        "name": "Patricroft Rail Station",
        "lng": -2.3582,
        "lat": 53.4848
    },
    {
        "code": "DENT",
        "name": "Dent Rail Station",
        "lng": -2.3636,
        "lat": 54.2824
    },
    {
        "code": "RIBLHED",
        "name": "Ribblehead Rail Station",
        "lng": -2.3609,
        "lat": 54.2058
    },
    {
        "code": "URMSTON",
        "name": "Urmston Rail Station",
        "lng": -2.3538,
        "lat": 53.4483
    },
    {
        "code": "HCHP",
        "name": "Holmes Chapel Rail Station",
        "lng": -2.3511,
        "lat": 53.1989
    },
    {
        "code": "MRSD",
        "name": "Moorside Rail Station",
        "lng": -2.3518,
        "lat": 53.5163
    },
    {
        "code": "HALE",
        "name": "Hale Rail Station",
        "lng": -2.3474,
        "lat": 53.3787
    },
    {
        "code": "ALTRNHM",
        "name": "Altrincham Rail Station",
        "lng": -2.3469,
        "lat": 53.3877
    },
    {
        "code": "HUNCOAT",
        "name": "Huncoat Rail Station",
        "lng": -2.3476,
        "lat": 53.7718
    },
    {
        "code": "NAVGTNR",
        "name": "Navigation Road Rail Station",
        "lng": -2.3434,
        "lat": 53.3954
    },
    {
        "code": "ASHLEY",
        "name": "Ashley Rail Station",
        "lng": -2.3415,
        "lat": 53.3557
    },
    {
        "code": "INVURIE",
        "name": "Inverurie Rail Station",
        "lng": -2.3736,
        "lat": 57.2863
    },
    {
        "code": "SWNT",
        "name": "Swinton (Manchester) Rail Station",
        "lng": -2.3375,
        "lat": 53.5148
    },
    {
        "code": "MOBERLY",
        "name": "Mobberley Rail Station",
        "lng": -2.3337,
        "lat": 53.3291
    },
    {
        "code": "ECCLES",
        "name": "Eccles Rail Station",
        "lng": -2.3345,
        "lat": 53.4854
    },
    {
        "code": "BRDNML",
        "name": "Bardon Mill Rail Station",
        "lng": -2.3465,
        "lat": 54.9745
    },
    {
        "code": "MORETON",
        "name": "Moreton (Dorset) Rail Station",
        "lng": -2.3134,
        "lat": 50.701
    },
    {
        "code": "MLVRNLK",
        "name": "Malvern Link Rail Station",
        "lng": -2.3195,
        "lat": 52.1255
    },
    {
        "code": "GOOSTRY",
        "name": "Goostrey Rail Station",
        "lng": -2.3265,
        "lat": 53.2226
    },
    {
        "code": "GTMLVRN",
        "name": "Great Malvern Rail Station",
        "lng": -2.3183,
        "lat": 52.1092
    },
    {
        "code": "HMPHRYP",
        "name": "Humphrey Park Rail Station",
        "lng": -2.3275,
        "lat": 53.4522
    },
    {
        "code": "FROME",
        "name": "Frome Rail Station",
        "lng": -2.31,
        "lat": 51.2273
    },
    {
        "code": "GARSDLE",
        "name": "Garsdale Rail Station",
        "lng": -2.3264,
        "lat": 54.3214
    },
    {
        "code": "FRESHFD",
        "name": "Freshford Rail Station",
        "lng": -2.301,
        "lat": 51.342
    },
    {
        "code": "HAPTON",
        "name": "Hapton Rail Station",
        "lng": -2.3169,
        "lat": 53.7816
    },
    {
        "code": "CLTN",
        "name": "Clifton (Manchester) Rail Station",
        "lng": -2.3147,
        "lat": 53.5225
    },
    {
        "code": "TRFDPK",
        "name": "Trafford Park Rail Station",
        "lng": -2.3106,
        "lat": 53.4548
    },
    {
        "code": "COSFORD",
        "name": "Cosford Rail Station",
        "lng": -2.3003,
        "lat": 52.6448
    },
    {
        "code": "ALSAGER",
        "name": "Alsager Rail Station",
        "lng": -2.2991,
        "lat": 53.093
    },
    {
        "code": "GGLSWCK",
        "name": "Giggleswick Rail Station",
        "lng": -2.3028,
        "lat": 54.0618
    },
    {
        "code": "HTNRIBL",
        "name": "Horton-in-Ribblesdale Rail Station",
        "lng": -2.302,
        "lat": 54.1494
    },
    {
        "code": "AVNCLFF",
        "name": "Avoncliff Rail Station",
        "lng": -2.2813,
        "lat": 51.3396
    },
    {
        "code": "MNCRUFG",
        "name": "Manchester United FC Rail Station",
        "lng": -2.2907,
        "lat": 53.4622
    },
    {
        "code": "STNHSE",
        "name": "Stonehouse Rail Station",
        "lng": -2.2795,
        "lat": 51.7459
    },
    {
        "code": "GLHM",
        "name": "Gillingham (Dorset) Rail Station",
        "lng": -2.2726,
        "lat": 51.034
    },
    {
        "code": "CHELFD",
        "name": "Chelford Rail Station",
        "lng": -2.2806,
        "lat": 53.2703
    },
    {
        "code": "ROSG",
        "name": "Rose Grove Rail Station",
        "lng": -2.2828,
        "lat": 53.7862
    },
    {
        "code": "SETTLE",
        "name": "Settle Rail Station",
        "lng": -2.2807,
        "lat": 54.0669
    },
    {
        "code": "SLFDCT",
        "name": "Salford Crescent Rail Station",
        "lng": -2.2757,
        "lat": 53.4866
    },
    {
        "code": "ALBRGHT",
        "name": "Albrighton Rail Station",
        "lng": -2.2689,
        "lat": 52.6379
    },
    {
        "code": "MNCRIAP",
        "name": "Manchester Airport Rail Station",
        "lng": -2.273,
        "lat": 53.365
    },
    {
        "code": "BRDFDOA",
        "name": "Bradford-on-Avon Rail Station",
        "lng": -2.2523,
        "lat": 51.3449
    },
    {
        "code": "BURNLYB",
        "name": "Burnley Barracks Rail Station",
        "lng": -2.2581,
        "lat": 53.7909
    },
    {
        "code": "SLFDORD",
        "name": "Salford Central Rail Station",
        "lng": -2.2548,
        "lat": 53.4831
    },
    {
        "code": "LPRESTN",
        "name": "Long Preston Rail Station",
        "lng": -2.2556,
        "lat": 54.0168
    },
    {
        "code": "MNCRDGT",
        "name": "Deansgate Rail Station",
        "lng": -2.2511,
        "lat": 53.4742
    },
    {
        "code": "GLOSTER",
        "name": "Gloucester Rail Station",
        "lng": -2.2385,
        "lat": 51.8656
    },
    {
        "code": "BURNMR",
        "name": "Burnley Manchester Road Rail Station",
        "lng": -2.2489,
        "lat": 53.785
    },
    {
        "code": "KIDSGRV",
        "name": "Kidsgrove Rail Station",
        "lng": -2.2448,
        "lat": 53.0866
    },
    {
        "code": "KDRMNST",
        "name": "Kidderminster Rail Station",
        "lng": -2.2385,
        "lat": 52.3845
    },
    {
        "code": "BURNLYC",
        "name": "Burnley Central Rail Station",
        "lng": -2.245,
        "lat": 53.7935
    },
    {
        "code": "MNCRVIC",
        "name": "Manchester Victoria Rail Station",
        "lng": -2.2426,
        "lat": 53.4875
    },
    {
        "code": "MNCROXR",
        "name": "Manchester Oxford Road Rail Station",
        "lng": -2.242,
        "lat": 53.474
    },
    {
        "code": "STYAL",
        "name": "Styal Rail Station",
        "lng": -2.2405,
        "lat": 53.3483
    },
    {
        "code": "HYDB",
        "name": "Haydon Bridge Rail Station",
        "lng": -2.2476,
        "lat": 54.9752
    },
    {
        "code": "ALDEDGE",
        "name": "Alderley Edge Rail Station",
        "lng": -2.2368,
        "lat": 53.3038
    },
    {
        "code": "HLDG",
        "name": "Heald Green Rail Station",
        "lng": -2.2367,
        "lat": 53.3694
    },
    {
        "code": "WOOL",
        "name": "Wool Rail Station",
        "lng": -2.2215,
        "lat": 50.6816
    },
    {
        "code": "BRIERFL",
        "name": "Brierfield Rail Station",
        "lng": -2.2365,
        "lat": 53.824
    },
    {
        "code": "GATLEY",
        "name": "Gatley Rail Station",
        "lng": -2.2312,
        "lat": 53.3929
    },
    {
        "code": "MNCRPIC",
        "name": "Manchester Piccadilly Rail Station",
        "lng": -2.2309,
        "lat": 53.4774
    },
    {
        "code": "STRUD",
        "name": "Stroud (Glos) Rail Station",
        "lng": -2.2194,
        "lat": 51.7446
    },
    {
        "code": "WORCSFS",
        "name": "Worcester Foregate Street Rail Station",
        "lng": -2.2216,
        "lat": 52.1951
    },
    {
        "code": "WLMSL",
        "name": "Wilmslow Rail Station",
        "lng": -2.2263,
        "lat": 53.3268
    },
    {
        "code": "HBRY",
        "name": "Hartlebury Rail Station",
        "lng": -2.2211,
        "lat": 52.3345
    },
    {
        "code": "TRWBRDG",
        "name": "Trowbridge Rail Station",
        "lng": -2.2143,
        "lat": 51.3198
    },
    {
        "code": "HELIFLD",
        "name": "Hellifield Rail Station",
        "lng": -2.2278,
        "lat": 54.0109
    },
    {
        "code": "EDIDBRY",
        "name": "East Didsbury Rail Station",
        "lng": -2.222,
        "lat": 53.4093
    },
    {
        "code": "DILTONM",
        "name": "Dilton Marsh Rail Station",
        "lng": -2.2079,
        "lat": 51.249
    },
    {
        "code": "LNGP",
        "name": "Longport Rail Station",
        "lng": -2.2164,
        "lat": 53.0419
    },
    {
        "code": "BAGE",
        "name": "Burnage Rail Station",
        "lng": -2.2157,
        "lat": 53.4212
    },
    {
        "code": "WORCSSH",
        "name": "Worcester Shrub Hill Rail Station",
        "lng": -2.2094,
        "lat": 52.1947
    },
    {
        "code": "HNDFRTH",
        "name": "Handforth Rail Station",
        "lng": -2.2136,
        "lat": 53.3465
    },
    {
        "code": "ARDWICK",
        "name": "Ardwick Rail Station",
        "lng": -2.2139,
        "lat": 53.4713
    },
    {
        "code": "NLSN",
        "name": "Nelson Rail Station",
        "lng": -2.2138,
        "lat": 53.835
    },
    {
        "code": "MLDTHRD",
        "name": "Mauldeth Road Rail Station",
        "lng": -2.2093,
        "lat": 53.4331
    },
    {
        "code": "WSTBRYW",
        "name": "Westbury (Wilts) Rail Station",
        "lng": -2.1992,
        "lat": 51.267
    },
    {
        "code": "SHVN",
        "name": "Stonehaven Rail Station",
        "lng": -2.2253,
        "lat": 56.9668
    },
    {
        "code": "CODSALL",
        "name": "Codsall Rail Station",
        "lng": -2.2018,
        "lat": 52.6273
    },
    {
        "code": "ASHBRYS",
        "name": "Ashburys Rail Station",
        "lng": -2.1944,
        "lat": 53.4716
    },
    {
        "code": "CONGLTN",
        "name": "Congleton Rail Station",
        "lng": -2.1926,
        "lat": 53.1579
    },
    {
        "code": "NTNB",
        "name": "Norton Bridge Rail Station",
        "lng": -2.1905,
        "lat": 52.8667
    },
    {
        "code": "LVHM",
        "name": "Levenshulme Rail Station",
        "lng": -2.1927,
        "lat": 53.4442
    },
    {
        "code": "BILBROK",
        "name": "Bilbrook Rail Station",
        "lng": -2.1861,
        "lat": 52.6237
    },
    {
        "code": "CHDH",
        "name": "Cheadle Hulme Rail Station",
        "lng": -2.1883,
        "lat": 53.3759
    },
    {
        "code": "WRMNSTR",
        "name": "Warminster Rail Station",
        "lng": -2.1767,
        "lat": 51.2068
    },
    {
        "code": "STOKEOT",
        "name": "Stoke-on-Trent Rail Station",
        "lng": -2.181,
        "lat": 53.008
    },
    {
        "code": "BLAKEDN",
        "name": "Blakedown Rail Station",
        "lng": -2.1769,
        "lat": 52.4064
    },
    {
        "code": "BLLVUE",
        "name": "Belle Vue Rail Station",
        "lng": -2.1805,
        "lat": 53.4624
    },
    {
        "code": "COLNE",
        "name": "Colne Rail Station",
        "lng": -2.1819,
        "lat": 53.8547
    },
    {
        "code": "HTCP",
        "name": "Heaton Chapel Rail Station",
        "lng": -2.179,
        "lat": 53.4256
    },
    {
        "code": "CSTL",
        "name": "Castleton (Manchester) Rail Station",
        "lng": -2.1782,
        "lat": 53.5918
    },
    {
        "code": "DYCE",
        "name": "Dyce Rail Station",
        "lng": -2.1923,
        "lat": 57.2056
    },
    {
        "code": "RYDRBRW",
        "name": "Ryder Brow Rail Station",
        "lng": -2.1731,
        "lat": 53.4566
    },
    {
        "code": "WEDGWD",
        "name": "Wedgwood Rail Station",
        "lng": -2.1708,
        "lat": 52.951
    },
    {
        "code": "MLSHILL",
        "name": "Mills Hill (Manchester) Rail Station",
        "lng": -2.1715,
        "lat": 53.5513
    },
    {
        "code": "MSTN",
        "name": "Moston Rail Station",
        "lng": -2.171,
        "lat": 53.5234
    },
    {
        "code": "BARLSTN",
        "name": "Barlaston Rail Station",
        "lng": -2.1681,
        "lat": 52.9429
    },
    {
        "code": "GORTON",
        "name": "Gorton Rail Station",
        "lng": -2.1662,
        "lat": 53.4691
    },
    {
        "code": "WORCPWY",
        "name": "Worcestershire Parkway Rail Station",
        "lng": -2.16,
        "lat": 52.156
    },
    {
        "code": "BMHL",
        "name": "Bramhall Rail Station",
        "lng": -2.1636,
        "lat": 53.3606
    },
    {
        "code": "STKP",
        "name": "Stockport Rail Station",
        "lng": -2.163,
        "lat": 53.4055
    },
    {
        "code": "DRTWCHS",
        "name": "Droitwich Spa Rail Station",
        "lng": -2.1584,
        "lat": 52.2682
    },
    {
        "code": "REDISHS",
        "name": "Reddish South Rail Station",
        "lng": -2.1588,
        "lat": 53.4359
    },
    {
        "code": "STONE",
        "name": "Stone Rail Station",
        "lng": -2.155,
        "lat": 52.9083
    },
    {
        "code": "REDISHN",
        "name": "Reddish North Rail Station",
        "lng": -2.1563,
        "lat": 53.4494
    },
    {
        "code": "DAVNPRT",
        "name": "Davenport Rail Station",
        "lng": -2.153,
        "lat": 53.3909
    },
    {
        "code": "RCHDALE",
        "name": "Rochdale Rail Station",
        "lng": -2.1535,
        "lat": 53.6103
    },
    {
        "code": "MELKSHM",
        "name": "Melksham Rail Station",
        "lng": -2.1445,
        "lat": 51.3798
    },
    {
        "code": "HAGLEY",
        "name": "Hagley Rail Station",
        "lng": -2.1464,
        "lat": 52.4225
    },
    {
        "code": "PSBY",
        "name": "Prestbury Rail Station",
        "lng": -2.1455,
        "lat": 53.2934
    },
    {
        "code": "FRFD",
        "name": "Fairfield Rail Station",
        "lng": -2.1458,
        "lat": 53.4713
    },
    {
        "code": "STRBDGT",
        "name": "Stourbridge Town Rail Station",
        "lng": -2.1418,
        "lat": 52.4556
    },
    {
        "code": "WMOR",
        "name": "Woodsmoor Rail Station",
        "lng": -2.1421,
        "lat": 53.3865
    },
    {
        "code": "LNTN",
        "name": "Longton Rail Station",
        "lng": -2.137,
        "lat": 52.99
    },
    {
        "code": "STRBDG1",
        "name": "Stourbridge Junction Rail Station",
        "lng": -2.1339,
        "lat": 52.4475
    },
    {
        "code": "STRBDGJ",
        "name": "Stourbridge Junction Rail Station",
        "lng": -2.1338,
        "lat": 52.4476
    },
    {
        "code": "BRNGTN",
        "name": "Brinnington Rail Station",
        "lng": -2.1351,
        "lat": 53.4321
    },
    {
        "code": "POYNTON",
        "name": "Poynton Rail Station",
        "lng": -2.1344,
        "lat": 53.3504
    },
    {
        "code": "ADLC",
        "name": "Adlington (Cheshire) Rail Station",
        "lng": -2.1336,
        "lat": 53.3196
    },
    {
        "code": "DNTON",
        "name": "Denton Rail Station",
        "lng": -2.1317,
        "lat": 53.4569
    },
    {
        "code": "STAFFRD",
        "name": "Stafford Rail Station",
        "lng": -2.122,
        "lat": 52.8039
    },
    {
        "code": "WARHAM",
        "name": "Wareham Rail Station",
        "lng": -2.1152,
        "lat": 50.6929
    },
    {
        "code": "MACLSFD",
        "name": "Macclesfield Rail Station",
        "lng": -2.122,
        "lat": 53.2593
    },
    {
        "code": "HAZL",
        "name": "Hazel Grove Rail Station",
        "lng": -2.122,
        "lat": 53.3775
    },
    {
        "code": "WVRMPTN",
        "name": "Wolverhampton Rail Station",
        "lng": -2.1195,
        "lat": 52.5878
    },
    {
        "code": "PNKRDG",
        "name": "Penkridge Rail Station",
        "lng": -2.1193,
        "lat": 52.7235
    },
    {
        "code": "CHIPNHM",
        "name": "Chippenham Rail Station",
        "lng": -2.1154,
        "lat": 51.4625
    },
    {
        "code": "LYEE",
        "name": "Lye (West Midlands) Rail Station",
        "lng": -2.1159,
        "lat": 52.4599
    },
    {
        "code": "PLTH",
        "name": "Portlethen Rail Station",
        "lng": -2.1266,
        "lat": 57.0614
    },
    {
        "code": "GIDB",
        "name": "Guide Bridge Rail Station",
        "lng": -2.1137,
        "lat": 53.4746
    },
    {
        "code": "SMBG",
        "name": "Smithy Bridge Rail Station",
        "lng": -2.1135,
        "lat": 53.6333
    },
    {
        "code": "ASHCHRC",
        "name": "Ashchurch for Tewkesbury Rail Station",
        "lng": -2.1088,
        "lat": 51.9989
    },
    {
        "code": "BREDBRY",
        "name": "Bredbury Rail Station",
        "lng": -2.1105,
        "lat": 53.4232
    },
    {
        "code": "GRGRAVE",
        "name": "Gargrave Rail Station",
        "lng": -2.1052,
        "lat": 53.9784
    },
    {
        "code": "WDEN",
        "name": "Walsden Rail Station",
        "lng": -2.1045,
        "lat": 53.6963
    },
    {
        "code": "CHLTNHM",
        "name": "Cheltenham Spa Rail Station",
        "lng": -2.0996,
        "lat": 51.8974
    },
    {
        "code": "TODMRDN",
        "name": "Todmorden Rail Station",
        "lng": -2.0997,
        "lat": 53.7138
    },
    {
        "code": "ASHONUL",
        "name": "Ashton-under-Lyne Rail Station",
        "lng": -2.0943,
        "lat": 53.4913
    },
    {
        "code": "LITLBRO",
        "name": "Littleborough Rail Station",
        "lng": -2.0947,
        "lat": 53.643
    },
    {
        "code": "WOODLEY",
        "name": "Woodley Rail Station",
        "lng": -2.0933,
        "lat": 53.4293
    },
    {
        "code": "CRADLYH",
        "name": "Cradley Heath Rail Station",
        "lng": -2.0905,
        "lat": 52.4697
    },
    {
        "code": "HEXHAM",
        "name": "Hexham Rail Station",
        "lng": -2.0948,
        "lat": 54.9735
    },
    {
        "code": "ABRDEEN",
        "name": "Aberdeen Rail Station",
        "lng": -2.0987,
        "lat": 57.1437
    },
    {
        "code": "ROMILEY",
        "name": "Romiley Rail Station",
        "lng": -2.0893,
        "lat": 53.414
    },
    {
        "code": "COSELEY",
        "name": "Coseley Rail Station",
        "lng": -2.0858,
        "lat": 52.5451
    },
    {
        "code": "HYDEN",
        "name": "Hyde North Rail Station",
        "lng": -2.0855,
        "lat": 53.4648
    },
    {
        "code": "HYDEC",
        "name": "Hyde Central Rail Station",
        "lng": -2.0853,
        "lat": 53.4519
    },
    {
        "code": "MDWD",
        "name": "Middlewood Rail Station",
        "lng": -2.0834,
        "lat": 53.36
    },
    {
        "code": "TISBURY",
        "name": "Tisbury Rail Station",
        "lng": -2.079,
        "lat": 51.0609
    },
    {
        "code": "HOLTONH",
        "name": "Holton Heath Rail Station",
        "lng": -2.0778,
        "lat": 50.7114
    },
    {
        "code": "FLWRYFD",
        "name": "Flowery Field Rail Station",
        "lng": -2.0811,
        "lat": 53.4619
    },
    {
        "code": "ROHL",
        "name": "Rose Hill Marple Rail Station",
        "lng": -2.0765,
        "lat": 53.3962
    },
    {
        "code": "PERSHOR",
        "name": "Pershore Rail Station",
        "lng": -2.0715,
        "lat": 52.1306
    },
    {
        "code": "BLYBDGE",
        "name": "Blythe Bridge Rail Station",
        "lng": -2.067,
        "lat": 52.9681
    },
    {
        "code": "NWTH",
        "name": "Newton for Hyde Rail Station",
        "lng": -2.0671,
        "lat": 53.4564
    },
    {
        "code": "TIPTON",
        "name": "Tipton Rail Station",
        "lng": -2.0657,
        "lat": 52.5304
    },
    {
        "code": "SBYD",
        "name": "Stalybridge Rail Station",
        "lng": -2.0627,
        "lat": 53.4846
    },
    {
        "code": "OLHL",
        "name": "Old Hill Rail Station",
        "lng": -2.0562,
        "lat": 52.4709
    },
    {
        "code": "MARPLE",
        "name": "Marple Rail Station",
        "lng": -2.0573,
        "lat": 53.4007
    },
    {
        "code": "GODLY",
        "name": "Godley Rail Station",
        "lng": -2.0548,
        "lat": 53.4517
    },
    {
        "code": "DUDLPT",
        "name": "Dudley Port Rail Station",
        "lng": -2.0495,
        "lat": 52.5246
    },
    {
        "code": "BRMSGRV",
        "name": "Bromsgrove Rail Station",
        "lng": -2.0473,
        "lat": 52.3223
    },
    {
        "code": "DISLEY",
        "name": "Disley Rail Station",
        "lng": -2.0425,
        "lat": 53.3582
    },
    {
        "code": "MOSSLEY",
        "name": "Mossley (Manchester) Rail Station",
        "lng": -2.0413,
        "lat": 53.515
    },
    {
        "code": "HATRSLY",
        "name": "Hattersley Rail Station",
        "lng": -2.0403,
        "lat": 53.4453
    },
    {
        "code": "STRINES",
        "name": "Strines Rail Station",
        "lng": -2.0339,
        "lat": 53.375
    },
    {
        "code": "ROWLEYR",
        "name": "Rowley Regis Rail Station",
        "lng": -2.0309,
        "lat": 52.4773
    },
    {
        "code": "SKPT",
        "name": "Skipton Rail Station",
        "lng": -2.0259,
        "lat": 53.9587
    },
    {
        "code": "KEMBLE",
        "name": "Kemble Rail Station",
        "lng": -2.0228,
        "lat": 51.677
    },
    {
        "code": "CNCK",
        "name": "Cannock Rail Station",
        "lng": -2.0221,
        "lat": 52.6862
    },
    {
        "code": "LNDYW",
        "name": "Landywood Rail Station",
        "lng": -2.0207,
        "lat": 52.6565
    },
    {
        "code": "HMWTHY",
        "name": "Hamworthy Rail Station",
        "lng": -2.0194,
        "lat": 50.7252
    },
    {
        "code": "BLOXN",
        "name": "Bloxwich North Rail Station",
        "lng": -2.0177,
        "lat": 52.6254
    },
    {
        "code": "CRBG",
        "name": "Corbridge Rail Station",
        "lng": -2.0184,
        "lat": 54.9663
    },
    {
        "code": "BRBM",
        "name": "Broadbottom Rail Station",
        "lng": -2.0165,
        "lat": 53.441
    },
    {
        "code": "GFLD",
        "name": "Greenfield Rail Station",
        "lng": -2.0138,
        "lat": 53.5389
    },
    {
        "code": "CONONLY",
        "name": "Cononley Rail Station",
        "lng": -2.0121,
        "lat": 53.9176
    },
    {
        "code": "SNDWDUD",
        "name": "Sandwell & Dudley Rail Station",
        "lng": -2.0116,
        "lat": 52.5087
    },
    {
        "code": "BLOXWCH",
        "name": "Bloxwich Rail Station",
        "lng": -2.0115,
        "lat": 52.6182
    },
    {
        "code": "BRWCKUT",
        "name": "Berwick-upon-Tweed Rail Station",
        "lng": -2.011,
        "lat": 55.7743
    },
    {
        "code": "HBDNBDG",
        "name": "Hebden Bridge Rail Station",
        "lng": -2.0091,
        "lat": 53.7376
    },
    {
        "code": "NWMILSN",
        "name": "New Mills Newtown Rail Station",
        "lng": -2.0085,
        "lat": 53.3596
    },
    {
        "code": "NWMILSC",
        "name": "New Mills Central Rail Station",
        "lng": -2.0057,
        "lat": 53.3648
    },
    {
        "code": "LGRN",
        "name": "Langley Green Rail Station",
        "lng": -2.005,
        "lat": 52.4939
    },
    {
        "code": "SHPE",
        "name": "Stanhope Rail Station",
        "lng": -2.0033,
        "lat": 54.7433
    },
    {
        "code": "HDNS",
        "name": "Hednesford Rail Station",
        "lng": -2.0018,
        "lat": 52.7101
    },
    {
        "code": "BGRN",
        "name": "Barnt Green Rail Station",
        "lng": -1.9925,
        "lat": 52.3611
    },
    {
        "code": "BSCTSTA",
        "name": "Bescot Stadium Rail Station",
        "lng": -1.9911,
        "lat": 52.5631
    },
    {
        "code": "FURNESV",
        "name": "Furness Vale Rail Station",
        "lng": -1.9888,
        "lat": 53.3488
    },
    {
        "code": "WHALYBG",
        "name": "Whaley Bridge Rail Station",
        "lng": -1.9846,
        "lat": 53.3302
    },
    {
        "code": "WALSALL",
        "name": "Walsall Rail Station",
        "lng": -1.9848,
        "lat": 52.5844
    },
    {
        "code": "POOLE",
        "name": "Poole Rail Station",
        "lng": -1.9833,
        "lat": 50.7194
    },
    {
        "code": "MYTHLMR",
        "name": "Mytholmroyd Rail Station",
        "lng": -1.9814,
        "lat": 53.729
    },
    {
        "code": "LONB",
        "name": "Longbridge Rail Station",
        "lng": -1.9813,
        "lat": 52.3964
    },
    {
        "code": "GALTILL",
        "name": "Smethwick Galton Bridge Rail Station",
        "lng": -1.9805,
        "lat": 52.5018
    },
    {
        "code": "GALTINT",
        "name": "Smethwick Galton Bridge High Level Rail Station",
        "lng": -1.9805,
        "lat": 52.5018
    },
    {
        "code": "TAMEBDG",
        "name": "Tame Bridge Parkway Rail Station",
        "lng": -1.9762,
        "lat": 52.5529
    },
    {
        "code": "RIDNGML",
        "name": "Riding Mill Rail Station",
        "lng": -1.9716,
        "lat": 54.9487
    },
    {
        "code": "DNTG",
        "name": "Dinting Rail Station",
        "lng": -1.9703,
        "lat": 53.4493
    },
    {
        "code": "SMTHKRS",
        "name": "Smethwick Rolfe Street Rail Station",
        "lng": -1.9706,
        "lat": 52.4964
    },
    {
        "code": "ALVCHRC",
        "name": "Alvechurch Rail Station",
        "lng": -1.9677,
        "lat": 52.3461
    },
    {
        "code": "FROSTLY",
        "name": "Frosterley Rail Station",
        "lng": -1.9644,
        "lat": 54.727
    },
    {
        "code": "HADFILD",
        "name": "Hadfield Rail Station",
        "lng": -1.9653,
        "lat": 53.4607
    },
    {
        "code": "NRTF",
        "name": "Northfield Rail Station",
        "lng": -1.9659,
        "lat": 52.4082
    },
    {
        "code": "HNDSHWT",
        "name": "The Hawthorns Rail Station",
        "lng": -1.964,
        "lat": 52.5054
    },
    {
        "code": "GLSP",
        "name": "Glossop Rail Station",
        "lng": -1.9491,
        "lat": 53.4445
    },
    {
        "code": "EVESHAM",
        "name": "Evesham Rail Station",
        "lng": -1.9473,
        "lat": 52.0984
    },
    {
        "code": "STEETON",
        "name": "Steeton & Silsden Rail Station",
        "lng": -1.9447,
        "lat": 53.9
    },
    {
        "code": "PSTONE",
        "name": "Parkstone (Dorset) Rail Station",
        "lng": -1.948,
        "lat": 50.723
    },
    {
        "code": "CHNLY",
        "name": "Chinley Rail Station",
        "lng": -1.9439,
        "lat": 53.3403
    },
    {
        "code": "RDIT",
        "name": "Redditch Rail Station",
        "lng": -1.9452,
        "lat": 52.3063
    },
    {
        "code": "RUGLTWN",
        "name": "Rugeley Town Rail Station",
        "lng": -1.9368,
        "lat": 52.7544
    },
    {
        "code": "UNVRSYB",
        "name": "University Rail Station",
        "lng": -1.9367,
        "lat": 52.4512
    },
    {
        "code": "SELYOAK",
        "name": "Selly Oak Rail Station",
        "lng": -1.9358,
        "lat": 52.442
    },
    {
        "code": "MRSN",
        "name": "Marsden Rail Station",
        "lng": -1.9307,
        "lat": 53.6032
    },
    {
        "code": "KNORTON",
        "name": "Kings Norton Rail Station",
        "lng": -1.9323,
        "lat": 52.4143
    },
    {
        "code": "RUGL",
        "name": "Rugeley Trent Valley Rail Station",
        "lng": -1.9299,
        "lat": 52.7697
    },
    {
        "code": "HAMSTED",
        "name": "Hamstead (Birmingham) Rail Station",
        "lng": -1.929,
        "lat": 52.5311
    },
    {
        "code": "BOURNVL",
        "name": "Bournville Rail Station",
        "lng": -1.9264,
        "lat": 52.427
    },
    {
        "code": "STCKSFL",
        "name": "Stocksfield Rail Station",
        "lng": -1.9168,
        "lat": 54.947
    },
    {
        "code": "CHEF",
        "name": "Chapel-en-le-Frith Rail Station",
        "lng": -1.9188,
        "lat": 53.3122
    },
    {
        "code": "BRANKSM",
        "name": "Branksome Rail Station",
        "lng": -1.9198,
        "lat": 50.727
    },
    {
        "code": "BUXTON",
        "name": "Buxton Rail Station",
        "lng": -1.9129,
        "lat": 53.2607
    },
    {
        "code": "BHAMJEW",
        "name": "Jewellery Quarter Rail Station",
        "lng": -1.9132,
        "lat": 52.4894
    },
    {
        "code": "FIVEWYS",
        "name": "Five Ways Rail Station",
        "lng": -1.913,
        "lat": 52.4711
    },
    {
        "code": "SWRBBDG",
        "name": "Sowerby Bridge Rail Station",
        "lng": -1.907,
        "lat": 53.7078
    },
    {
        "code": "KEIGHLY",
        "name": "Keighley Rail Station",
        "lng": -1.9016,
        "lat": 53.868
    },
    {
        "code": "PRYBR",
        "name": "Perry Barr Rail Station",
        "lng": -1.902,
        "lat": 52.5165
    },
    {
        "code": "BHAMNWS",
        "name": "Birmingham New Street Rail Station",
        "lng": -1.9002,
        "lat": 52.4778
    },
    {
        "code": "BHAMSNH",
        "name": "Birmingham Snow Hill Rail Station",
        "lng": -1.8991,
        "lat": 52.4834
    },
    {
        "code": "BHAMMRS",
        "name": "Birmingham Moor Street Rail Station",
        "lng": -1.8925,
        "lat": 52.4791
    },
    {
        "code": "DVHL",
        "name": "Dove Holes Rail Station",
        "lng": -1.8898,
        "lat": 53.3
    },
    {
        "code": "WOLSHAM",
        "name": "Wolsingham Rail Station",
        "lng": -1.8835,
        "lat": 54.7263
    },
    {
        "code": "SLTHWTE",
        "name": "Slaithwaite Rail Station",
        "lng": -1.8816,
        "lat": 53.6238
    },
    {
        "code": "WITTON",
        "name": "Witton (West Midlands) Rail Station",
        "lng": -1.8844,
        "lat": 52.5124
    },
    {
        "code": "BRDS",
        "name": "Bordesley Rail Station",
        "lng": -1.8778,
        "lat": 52.4719
    },
    {
        "code": "PRUDHOE",
        "name": "Prudhoe Rail Station",
        "lng": -1.8649,
        "lat": 54.9658
    },
    {
        "code": "ASTON",
        "name": "Aston Rail Station",
        "lng": -1.8719,
        "lat": 52.5042
    },
    {
        "code": "DUDESTN",
        "name": "Duddeston Rail Station",
        "lng": -1.8714,
        "lat": 52.4884
    },
    {
        "code": "WYTH",
        "name": "Wythall Rail Station",
        "lng": -1.8655,
        "lat": 52.3799
    },
    {
        "code": "ELWD",
        "name": "Earlswood (West Midlands) Rail Station",
        "lng": -1.8612,
        "lat": 52.3666
    },
    {
        "code": "SMLHTH",
        "name": "Small Heath Rail Station",
        "lng": -1.8594,
        "lat": 52.4638
    },
    {
        "code": "BOMO",
        "name": "Bournemouth Rail Station",
        "lng": -1.8645,
        "lat": 50.7273
    },
    {
        "code": "UTOXETR",
        "name": "Uttoxeter Rail Station",
        "lng": -1.8573,
        "lat": 52.8968
    },
    {
        "code": "HLFX",
        "name": "Halifax Rail Station",
        "lng": -1.8536,
        "lat": 53.721
    },
    {
        "code": "ADERLYP",
        "name": "Adderley Park Rail Station",
        "lng": -1.8559,
        "lat": 52.4831
    },
    {
        "code": "YRDLYWD",
        "name": "Yardley Wood Rail Station",
        "lng": -1.8544,
        "lat": 52.4215
    },
    {
        "code": "GRAVLYH",
        "name": "Gravelly Hill Rail Station",
        "lng": -1.8526,
        "lat": 52.515
    },
    {
        "code": "WHLE",
        "name": "Whitlocks End Rail Station",
        "lng": -1.8515,
        "lat": 52.3918
    },
    {
        "code": "CFLATTS",
        "name": "Crossflatts Rail Station",
        "lng": -1.8449,
        "lat": 53.8585
    },
    {
        "code": "HLGN",
        "name": "Hall Green Rail Station",
        "lng": -1.8457,
        "lat": 52.4369
    },
    {
        "code": "BLKST",
        "name": "Blake Street Rail Station",
        "lng": -1.8449,
        "lat": 52.6049
    },
    {
        "code": "SHIRLEY",
        "name": "Shirley Rail Station",
        "lng": -1.8452,
        "lat": 52.4034
    },
    {
        "code": "SHNS",
        "name": "Shenstone Rail Station",
        "lng": -1.8442,
        "lat": 52.6394
    },
    {
        "code": "THELAKS",
        "name": "The Lakes Rail Station",
        "lng": -1.8447,
        "lat": 52.3591
    },
    {
        "code": "WDND",
        "name": "Wood End Rail Station",
        "lng": -1.8442,
        "lat": 52.3437
    },
    {
        "code": "BNGY",
        "name": "Bingley Rail Station",
        "lng": -1.8373,
        "lat": 53.8486
    },
    {
        "code": "ERDNGTN",
        "name": "Erdington Rail Station",
        "lng": -1.8395,
        "lat": 52.5283
    },
    {
        "code": "TYSL",
        "name": "Tyseley Rail Station",
        "lng": -1.8391,
        "lat": 52.4541
    },
    {
        "code": "BTLRSLA",
        "name": "Butlers Lane Rail Station",
        "lng": -1.838,
        "lat": 52.5925
    },
    {
        "code": "SPRD",
        "name": "Spring Road Rail Station",
        "lng": -1.8374,
        "lat": 52.4434
    },
    {
        "code": "CHSRD",
        "name": "Chester Road Rail Station",
        "lng": -1.8325,
        "lat": 52.5356
    },
    {
        "code": "HONYBRN",
        "name": "Honeybourne Rail Station",
        "lng": -1.8337,
        "lat": 52.1016
    },
    {
        "code": "WYGN",
        "name": "Wylde Green Rail Station",
        "lng": -1.8314,
        "lat": 52.5457
    },
    {
        "code": "FOUROKS",
        "name": "Four Oaks Rail Station",
        "lng": -1.828,
        "lat": 52.5798
    },
    {
        "code": "ILKLEY",
        "name": "Ilkley Rail Station",
        "lng": -1.822,
        "lat": 53.9248
    },
    {
        "code": "LCHC",
        "name": "Lichfield City Rail Station",
        "lng": -1.8254,
        "lat": 52.6801
    },
    {
        "code": "SUTCO",
        "name": "Sutton Coldfield Rail Station",
        "lng": -1.8248,
        "lat": 52.5649
    },
    {
        "code": "WYLAM",
        "name": "Wylam Rail Station",
        "lng": -1.8141,
        "lat": 54.975
    },
    {
        "code": "EDALE",
        "name": "Edale Rail Station",
        "lng": -1.8166,
        "lat": 53.365
    },
    {
        "code": "DANZEY",
        "name": "Danzey Rail Station",
        "lng": -1.8209,
        "lat": 52.3248
    },
    {
        "code": "ACOCKSG",
        "name": "Acocks Green Rail Station",
        "lng": -1.819,
        "lat": 52.4493
    },
    {
        "code": "POKSDWN",
        "name": "Pokesdown Rail Station",
        "lng": -1.8251,
        "lat": 50.7311
    },
    {
        "code": "STECHFD",
        "name": "Stechford Rail Station",
        "lng": -1.811,
        "lat": 52.4848
    },
    {
        "code": "LKWD",
        "name": "Lockwood Rail Station",
        "lng": -1.8008,
        "lat": 53.6347
    },
    {
        "code": "BNRHYDN",
        "name": "Ben Rhydding Rail Station",
        "lng": -1.7974,
        "lat": 53.9257
    },
    {
        "code": "OLTON",
        "name": "Olton Rail Station",
        "lng": -1.8043,
        "lat": 52.4385
    },
    {
        "code": "LCHTTVH",
        "name": "Lichfield Trent Valley High Level Rail Station",
        "lng": -1.8002,
        "lat": 52.6869
    },
    {
        "code": "LCHTTVL",
        "name": "Lichfield Trent Valley Rail Station",
        "lng": -1.8002,
        "lat": 52.6869
    },
    {
        "code": "SLSBRY",
        "name": "Salisbury Rail Station",
        "lng": -1.8064,
        "lat": 51.0705
    },
    {
        "code": "BERRYB",
        "name": "Berry Brow Rail Station",
        "lng": -1.7934,
        "lat": 53.621
    },
    {
        "code": "SAIR",
        "name": "Saltaire Rail Station",
        "lng": -1.7905,
        "lat": 53.8385
    },
    {
        "code": "HDRSFLD",
        "name": "Huddersfield Rail Station",
        "lng": -1.7847,
        "lat": 53.6485
    },
    {
        "code": "SOLIHUL",
        "name": "Solihull Rail Station",
        "lng": -1.7884,
        "lat": 52.4144
    },
    {
        "code": "HONLEY",
        "name": "Honley Rail Station",
        "lng": -1.781,
        "lat": 53.6082
    },
    {
        "code": "LEAHALL",
        "name": "Lea Hall Rail Station",
        "lng": -1.786,
        "lat": 52.4806
    },
    {
        "code": "BRHOUSE",
        "name": "Brighouse Rail Station",
        "lng": -1.7794,
        "lat": 53.6982
    },
    {
        "code": "WOTONWN",
        "name": "Wootton Wawen Rail Station",
        "lng": -1.7847,
        "lat": 52.2669
    },
    {
        "code": "HENLYIA",
        "name": "Henley-in-Arden Rail Station",
        "lng": -1.784,
        "lat": 52.2915
    },
    {
        "code": "SDON",
        "name": "Swindon Rail Station",
        "lng": -1.7855,
        "lat": 51.5655
    },
    {
        "code": "SHPY",
        "name": "Shipley Rail Station",
        "lng": -1.7735,
        "lat": 53.833
    },
    {
        "code": "CHRISTC",
        "name": "Christchurch Rail Station",
        "lng": -1.7845,
        "lat": 50.7382
    },
    {
        "code": "FRZNGHL",
        "name": "Frizinghall Rail Station",
        "lng": -1.769,
        "lat": 53.8204
    },
    {
        "code": "BKHLS",
        "name": "Brockholes Rail Station",
        "lng": -1.7697,
        "lat": 53.597
    },
    {
        "code": "WDNYMNR",
        "name": "Widney Manor Rail Station",
        "lng": -1.7744,
        "lat": 52.3959
    },
    {
        "code": "PEWSEY",
        "name": "Pewsey Rail Station",
        "lng": -1.7707,
        "lat": 51.3422
    },
    {
        "code": "BURLYIW",
        "name": "Burley-in-Wharfedale Rail Station",
        "lng": -1.7534,
        "lat": 53.9081
    },
    {
        "code": "BAILDON",
        "name": "Baildon Rail Station",
        "lng": -1.7536,
        "lat": 53.8502
    },
    {
        "code": "LOWMOOR",
        "name": "Low Moor Rail Station",
        "lng": -1.7534,
        "lat": 53.7499
    },
    {
        "code": "BRADFS",
        "name": "Bradford Forster Square Rail Station",
        "lng": -1.753,
        "lat": 53.7969
    },
    {
        "code": "DEIGHTN",
        "name": "Deighton Rail Station",
        "lng": -1.7519,
        "lat": 53.6685
    },
    {
        "code": "BRADIN",
        "name": "Bradford Interchange Rail Station",
        "lng": -1.7496,
        "lat": 53.7911
    },
    {
        "code": "MRSTNGR",
        "name": "Marston Green Rail Station",
        "lng": -1.7556,
        "lat": 52.4672
    },
    {
        "code": "WILMCOT",
        "name": "Wilmcote Rail Station",
        "lng": -1.756,
        "lat": 52.223
    },
    {
        "code": "DORIDGE",
        "name": "Dorridge Rail Station",
        "lng": -1.7529,
        "lat": 52.3721
    },
    {
        "code": "BEARLEY",
        "name": "Bearley Rail Station",
        "lng": -1.7503,
        "lat": 52.2444
    },
    {
        "code": "MENSTON",
        "name": "Menston Rail Station",
        "lng": -1.7355,
        "lat": 53.8923
    },
    {
        "code": "WTRORTN",
        "name": "Water Orton Rail Station",
        "lng": -1.7431,
        "lat": 52.5186
    },
    {
        "code": "HOPD",
        "name": "Hope (Derbyshire) Rail Station",
        "lng": -1.7299,
        "lat": 53.3461
    },
    {
        "code": "STKSMR",
        "name": "Stocksmoor Rail Station",
        "lng": -1.7232,
        "lat": 53.5941
    },
    {
        "code": "SOAVPWY",
        "name": "Stratford-upon-Avon Parkway Rail Station",
        "lng": -1.7308,
        "lat": 52.2068
    },
    {
        "code": "BLAYDON",
        "name": "Blaydon Rail Station",
        "lng": -1.7126,
        "lat": 54.9658
    },
    {
        "code": "AIRP",
        "name": "Newcastle Airport Metro",
        "lng": -1.711,
        "lat": 55.0359
    },
    {
        "code": "CHHL",
        "name": "Chathill Rail Station",
        "lng": -1.7064,
        "lat": 55.5367
    },
    {
        "code": "BHAMINT",
        "name": "Birmingham International Rail Station",
        "lng": -1.7259,
        "lat": 52.4508
    },
    {
        "code": "LAPWRTH",
        "name": "Lapworth Rail Station",
        "lng": -1.7257,
        "lat": 52.3422
    },
    {
        "code": "GUISELY",
        "name": "Guiseley Rail Station",
        "lng": -1.7151,
        "lat": 53.8759
    },
    {
        "code": "APERLYB",
        "name": "Apperley Bridge Rail Station",
        "lng": -1.7058,
        "lat": 53.8417
    },
    {
        "code": "SOAV",
        "name": "Stratford-upon-Avon Rail Station",
        "lng": -1.7163,
        "lat": 52.1942
    },
    {
        "code": "SPLY",
        "name": "Shepley Rail Station",
        "lng": -1.7049,
        "lat": 53.5887
    },
    {
        "code": "COLESHL",
        "name": "Coleshill Parkway Rail Station",
        "lng": -1.7082,
        "lat": 52.5165
    },
    {
        "code": "HINTONA",
        "name": "Hinton Admiral Rail Station",
        "lng": -1.7141,
        "lat": 50.7526
    },
    {
        "code": "MRPTHRP",
        "name": "Morpeth Rail Station",
        "lng": -1.6831,
        "lat": 55.1624
    },
    {
        "code": "MIRFILD",
        "name": "Mirfield Rail Station",
        "lng": -1.6925,
        "lat": 53.6714
    },
    {
        "code": "HMPTNIA",
        "name": "Hampton-in-Arden Rail Station",
        "lng": -1.6999,
        "lat": 52.429
    },
    {
        "code": "MINMARS",
        "name": "Moreton-in-Marsh Rail Station",
        "lng": -1.7004,
        "lat": 51.9923
    },
    {
        "code": "BAMFORD",
        "name": "Bamford Rail Station",
        "lng": -1.6891,
        "lat": 53.339
    },
    {
        "code": "CLAVRDN",
        "name": "Claverdon Rail Station",
        "lng": -1.6966,
        "lat": 52.2771
    },
    {
        "code": "BSAUKLD",
        "name": "Bishop Auckland Rail Station",
        "lng": -1.6777,
        "lat": 54.6572
    },
    {
        "code": "BSAUWEA",
        "name": "Bishop Auckland Rail Station",
        "lng": -1.6777,
        "lat": 54.6572
    },
    {
        "code": "NPUD",
        "name": "New Pudsey Rail Station",
        "lng": -1.6808,
        "lat": 53.8045
    },
    {
        "code": "TMWTHLL",
        "name": "Tamworth Rail Station",
        "lng": -1.6865,
        "lat": 52.6375
    },
    {
        "code": "TMWTHHL",
        "name": "Tamworth High Level Rail Station",
        "lng": -1.6864,
        "lat": 52.6375
    },
    {
        "code": "TUTBURY",
        "name": "Tutbury & Hatton Rail Station",
        "lng": -1.6822,
        "lat": 52.8641
    },
    {
        "code": "GTSHDMC",
        "name": "Metrocentre Rail Station",
        "lng": -1.6656,
        "lat": 54.9587
    },
    {
        "code": "WILNECT",
        "name": "Wilnecote (Staffs) Rail Station",
        "lng": -1.6797,
        "lat": 52.6107
    },
    {
        "code": "ACKLNGT",
        "name": "Acklington Rail Station",
        "lng": -1.6518,
        "lat": 55.3071
    },
    {
        "code": "DNDL",
        "name": "Denby Dale Rail Station",
        "lng": -1.6632,
        "lat": 53.5726
    },
    {
        "code": "HATTON",
        "name": "Hatton (Warks) Rail Station",
        "lng": -1.673,
        "lat": 52.2953
    },
    {
        "code": "PEGSWD",
        "name": "Pegswood Rail Station",
        "lng": -1.6442,
        "lat": 55.1781
    },
    {
        "code": "RTHP",
        "name": "Ravensthorpe Rail Station",
        "lng": -1.6556,
        "lat": 53.6755
    },
    {
        "code": "DNSN",
        "name": "Dunston Rail Station",
        "lng": -1.642,
        "lat": 54.9501
    },
    {
        "code": "ALNMOTH",
        "name": "Alnmouth Rail Station",
        "lng": -1.6366,
        "lat": 55.3928
    },
    {
        "code": "HATHRSG",
        "name": "Hathersage Rail Station",
        "lng": -1.6517,
        "lat": 53.3258
    },
    {
        "code": "SHDN",
        "name": "Shildon Rail Station",
        "lng": -1.6366,
        "lat": 54.6262
    },
    {
        "code": "BRMLYSR",
        "name": "Bramley (West Yorks) Rail Station",
        "lng": -1.6372,
        "lat": 53.8053
    },
    {
        "code": "BURTNOT",
        "name": "Burton-on-Trent Rail Station",
        "lng": -1.6425,
        "lat": 52.8058
    },
    {
        "code": "NMILTON",
        "name": "New Milton Rail Station",
        "lng": -1.6578,
        "lat": 50.7558
    },
    {
        "code": "DWBY",
        "name": "Dewsbury Rail Station",
        "lng": -1.6331,
        "lat": 53.6921
    },
    {
        "code": "BKSWELL",
        "name": "Berkswell Rail Station",
        "lng": -1.6428,
        "lat": 52.3959
    },
    {
        "code": "HSFT",
        "name": "Horsforth Rail Station",
        "lng": -1.6302,
        "lat": 53.8477
    },
    {
        "code": "WDRNGTN",
        "name": "Widdrington Rail Station",
        "lng": -1.6165,
        "lat": 55.2413
    },
    {
        "code": "NWCSTLE",
        "name": "Newcastle Rail Station",
        "lng": -1.6173,
        "lat": 54.9684
    },
    {
        "code": "KRKSLFR",
        "name": "Kirkstall Forge Rail Station",
        "lng": -1.6225,
        "lat": 53.8237
    },
    {
        "code": "BATLEY",
        "name": "Batley Rail Station",
        "lng": -1.623,
        "lat": 53.7099
    },
    {
        "code": "GRNDLFD",
        "name": "Grindleford Rail Station",
        "lng": -1.6263,
        "lat": 53.3056
    },
    {
        "code": "PENISTN",
        "name": "Penistone Rail Station",
        "lng": -1.6228,
        "lat": 53.5255
    },
    {
        "code": "MANORS",
        "name": "Manors Rail Station",
        "lng": -1.6047,
        "lat": 54.9728
    },
    {
        "code": "KINGHAM",
        "name": "Kingham Rail Station",
        "lng": -1.6288,
        "lat": 51.9022
    },
    {
        "code": "DEAN",
        "name": "Dean Rail Station",
        "lng": -1.6349,
        "lat": 51.0425
    },
    {
        "code": "CRMLNGT",
        "name": "Cramlington Rail Station",
        "lng": -1.5986,
        "lat": 55.0878
    },
    {
        "code": "PWTH",
        "name": "Polesworth Rail Station",
        "lng": -1.6105,
        "lat": 52.6258
    },
    {
        "code": "WARWPWY",
        "name": "Warwick Parkway Rail Station",
        "lng": -1.6121,
        "lat": 52.2861
    },
    {
        "code": "NWTA",
        "name": "Newton Aycliffe Rail Station",
        "lng": -1.5896,
        "lat": 54.6137
    },
    {
        "code": "GRATELY",
        "name": "Grateley Rail Station",
        "lng": -1.6208,
        "lat": 51.1701
    },
    {
        "code": "HEDNGLY",
        "name": "Headingley Rail Station",
        "lng": -1.5942,
        "lat": 53.818
    },
    {
        "code": "DRHM",
        "name": "Durham Rail Station",
        "lng": -1.5818,
        "lat": 54.7794
    },
    {
        "code": "MRLY",
        "name": "Morley Rail Station",
        "lng": -1.591,
        "lat": 53.7499
    },
    {
        "code": "HGHNGTN",
        "name": "Heighington Rail Station",
        "lng": -1.5818,
        "lat": 54.597
    },
    {
        "code": "CLST",
        "name": "Chester-le-Street Rail Station",
        "lng": -1.578,
        "lat": 54.8546
    },
    {
        "code": "COTNGLY",
        "name": "Cottingley Rail Station",
        "lng": -1.5877,
        "lat": 53.7678
    },
    {
        "code": "TILEH",
        "name": "Tile Hill Rail Station",
        "lng": -1.5968,
        "lat": 52.3951
    },
    {
        "code": "SWAY",
        "name": "Sway Rail Station",
        "lng": -1.61,
        "lat": 50.7847
    },
    {
        "code": "WEETON",
        "name": "Weeton Rail Station",
        "lng": -1.5812,
        "lat": 53.9232
    },
    {
        "code": "BRLEYPK",
        "name": "Burley Park Rail Station",
        "lng": -1.5778,
        "lat": 53.812
    },
    {
        "code": "BEDYN",
        "name": "Bedwyn Rail Station",
        "lng": -1.5988,
        "lat": 51.3796
    },
    {
        "code": "SPTN",
        "name": "Shipton Rail Station",
        "lng": -1.5927,
        "lat": 51.8657
    },
    {
        "code": "HEWORTH",
        "name": "Heworth Rail Station",
        "lng": -1.5558,
        "lat": 54.9516
    },
    {
        "code": "WARWICK",
        "name": "Warwick Rail Station",
        "lng": -1.5819,
        "lat": 52.2865
    },
    {
        "code": "NTRD",
        "name": "North Road Rail Station",
        "lng": -1.5539,
        "lat": 54.5362
    },
    {
        "code": "SKSCMN",
        "name": "Silkstone Common Rail Station",
        "lng": -1.5635,
        "lat": 53.5349
    },
    {
        "code": "KENLSTN",
        "name": "Kenilworth Rail Station",
        "lng": -1.5727,
        "lat": 52.3427
    },
    {
        "code": "DLTN",
        "name": "Darlington Rail Station",
        "lng": -1.5473,
        "lat": 54.5204
    },
    {
        "code": "WLNTNON",
        "name": "Willington Rail Station",
        "lng": -1.5634,
        "lat": 52.8536
    },
    {
        "code": "MATLOCK",
        "name": "Matlock Rail Station",
        "lng": -1.5589,
        "lat": 53.1384
    },
    {
        "code": "MATLCKB",
        "name": "Matlock Bath Rail Station",
        "lng": -1.5568,
        "lat": 53.1224
    },
    {
        "code": "LEEDS",
        "name": "Leeds Rail Station",
        "lng": -1.548,
        "lat": 53.7956
    },
    {
        "code": "ASCTUWD",
        "name": "Ascott-under-Wychwood Rail Station",
        "lng": -1.5641,
        "lat": 51.8673
    },
    {
        "code": "BKNHRST",
        "name": "Brockenhurst Rail Station",
        "lng": -1.5735,
        "lat": 50.8168
    },
    {
        "code": "CROMFD",
        "name": "Cromford Rail Station",
        "lng": -1.5492,
        "lat": 53.1129
    },
    {
        "code": "ATHRSTN",
        "name": "Atherstone Rail Station",
        "lng": -1.5528,
        "lat": 52.579
    },
    {
        "code": "HAGT",
        "name": "Harrogate Rail Station",
        "lng": -1.5376,
        "lat": 53.9932
    },
    {
        "code": "PANNAL",
        "name": "Pannal Rail Station",
        "lng": -1.5335,
        "lat": 53.9583
    },
    {
        "code": "CANLEY",
        "name": "Canley Rail Station",
        "lng": -1.5476,
        "lat": 52.3992
    },
    {
        "code": "DRTN",
        "name": "Darton Rail Station",
        "lng": -1.5317,
        "lat": 53.5884
    },
    {
        "code": "DODWRTH",
        "name": "Dodworth Rail Station",
        "lng": -1.5317,
        "lat": 53.5443
    },
    {
        "code": "HRNBPK",
        "name": "Hornbeam Park Rail Station",
        "lng": -1.5268,
        "lat": 53.9799
    },
    {
        "code": "LMNGTNS",
        "name": "Leamington Spa Rail Station",
        "lng": -1.5362,
        "lat": 52.2845
    },
    {
        "code": "MOTFONT",
        "name": "Mottisfont & Dunbridge Rail Station",
        "lng": -1.5471,
        "lat": 51.0339
    },
    {
        "code": "DORE",
        "name": "Dore & Totley Rail Station",
        "lng": -1.5153,
        "lat": 53.3276
    },
    {
        "code": "OUTWOOD",
        "name": "Outwood Rail Station",
        "lng": -1.5104,
        "lat": 53.7153
    },
    {
        "code": "WKFLDWG",
        "name": "Wakefield Westgate Rail Station",
        "lng": -1.5061,
        "lat": 53.6831
    },
    {
        "code": "LMTNTWN",
        "name": "Lymington Town Rail Station",
        "lng": -1.5372,
        "lat": 50.7609
    },
    {
        "code": "STARBCK",
        "name": "Starbeck Rail Station",
        "lng": -1.5011,
        "lat": 53.999
    },
    {
        "code": "COVNTRY",
        "name": "Coventry Rail Station",
        "lng": -1.5135,
        "lat": 52.4008
    },
    {
        "code": "LMTNPIR",
        "name": "Lymington Pier Rail Station",
        "lng": -1.5294,
        "lat": 50.7583
    },
    {
        "code": "WATSTND",
        "name": "Whatstandwell Rail Station",
        "lng": -1.5041,
        "lat": 53.0833
    },
    {
        "code": "LYNDHRD",
        "name": "Ashurst New Forest Rail Station",
        "lng": -1.5266,
        "lat": 50.8898
    },
    {
        "code": "WKFLDKG",
        "name": "Wakefield Kirkgate Rail Station",
        "lng": -1.4886,
        "lat": 53.6787
    },
    {
        "code": "HUNGRFD",
        "name": "Hungerford Rail Station",
        "lng": -1.5123,
        "lat": 51.4149
    },
    {
        "code": "SABR",
        "name": "Sandal & Agbrigg Rail Station",
        "lng": -1.4814,
        "lat": 53.6631
    },
    {
        "code": "COVAREN",
        "name": "Coventry Arena Rail Station",
        "lng": -1.4941,
        "lat": 52.4477
    },
    {
        "code": "BRWHINS",
        "name": "Brockley Whins Rail Station",
        "lng": -1.4614,
        "lat": 54.9595
    },
    {
        "code": "DINSDAL",
        "name": "Dinsdale Rail Station",
        "lng": -1.4671,
        "lat": 54.5147
    },
    {
        "code": "DUFIELD",
        "name": "Duffield Rail Station",
        "lng": -1.486,
        "lat": 52.9884
    },
    {
        "code": "BNSLY",
        "name": "Barnsley Rail Station",
        "lng": -1.4772,
        "lat": 53.5543
    },
    {
        "code": "KNRSBGH",
        "name": "Knaresborough Rail Station",
        "lng": -1.4704,
        "lat": 54.009
    },
    {
        "code": "BELPER",
        "name": "Belper Rail Station",
        "lng": -1.4825,
        "lat": 53.0238
    },
    {
        "code": "AMBERGT",
        "name": "Ambergate Rail Station",
        "lng": -1.4807,
        "lat": 53.0605
    },
    {
        "code": "BLIEURD",
        "name": "Beaulieu Road Rail Station",
        "lng": -1.5047,
        "lat": 50.855
    },
    {
        "code": "CHBURY",
        "name": "Charlbury Rail Station",
        "lng": -1.4897,
        "lat": 51.8724
    },
    {
        "code": "DRONFLD",
        "name": "Dronfield Rail Station",
        "lng": -1.4688,
        "lat": 53.3014
    },
    {
        "code": "CHPLTWN",
        "name": "Chapeltown Rail Station",
        "lng": -1.4663,
        "lat": 53.4623
    },
    {
        "code": "PEARTRE",
        "name": "Peartree Rail Station",
        "lng": -1.4732,
        "lat": 52.897
    },
    {
        "code": "ANDOVER",
        "name": "Andover Rail Station",
        "lng": -1.4922,
        "lat": 51.2115
    },
    {
        "code": "ROMSEY",
        "name": "Romsey Rail Station",
        "lng": -1.4931,
        "lat": 50.9925
    },
    {
        "code": "SHEFFLD",
        "name": "Sheffield Rail Station",
        "lng": -1.4621,
        "lat": 53.3782
    },
    {
        "code": "BERMPRK",
        "name": "Bermuda Park Rail Station",
        "lng": -1.4722,
        "lat": 52.5014
    },
    {
        "code": "DRBY",
        "name": "Derby Rail Station",
        "lng": -1.4634,
        "lat": 52.9165
    },
    {
        "code": "CSGT",
        "name": "Cross Gates Rail Station",
        "lng": -1.4516,
        "lat": 53.8049
    },
    {
        "code": "BEDWRTH",
        "name": "Bedworth Rail Station",
        "lng": -1.4674,
        "lat": 52.4793
    },
    {
        "code": "NLRTN",
        "name": "Northallerton Rail Station",
        "lng": -1.4413,
        "lat": 54.3331
    },
    {
        "code": "NNTN",
        "name": "Nuneaton Rail Station",
        "lng": -1.4639,
        "lat": 52.5264
    },
    {
        "code": "TOTTON",
        "name": "Totton Rail Station",
        "lng": -1.4824,
        "lat": 50.9179
    },
    {
        "code": "FINSTCK",
        "name": "Finstock Rail Station",
        "lng": -1.4693,
        "lat": 51.8528
    },
    {
        "code": "WDLESFD",
        "name": "Woodlesford Rail Station",
        "lng": -1.4429,
        "lat": 53.7568
    },
    {
        "code": "EBOLDON",
        "name": "East Boldon Rail Station",
        "lng": -1.4203,
        "lat": 54.9464
    },
    {
        "code": "TSDARPR",
        "name": "Tees-side Airport Rail Station",
        "lng": -1.4253,
        "lat": 54.5181
    },
    {
        "code": "REDBDGE",
        "name": "Redbridge (Hants) Rail Station",
        "lng": -1.4702,
        "lat": 50.9199
    },
    {
        "code": "ELSC",
        "name": "Elsecar Rail Station",
        "lng": -1.4274,
        "lat": 53.4987
    },
    {
        "code": "NORMNTN",
        "name": "Normanton Rail Station",
        "lng": -1.4234,
        "lat": 53.7005
    },
    {
        "code": "KNTBRY",
        "name": "Kintbury Rail Station",
        "lng": -1.446,
        "lat": 51.4025
    },
    {
        "code": "CHFD",
        "name": "Chesterfield Rail Station",
        "lng": -1.4201,
        "lat": 53.2382
    },
    {
        "code": "WOMBWEL",
        "name": "Wombwell Rail Station",
        "lng": -1.4162,
        "lat": 53.5173
    },
    {
        "code": "MEADWHL",
        "name": "Meadowhall Rail Station",
        "lng": -1.4129,
        "lat": 53.4175
    },
    {
        "code": "DARNALL",
        "name": "Darnall Rail Station",
        "lng": -1.4126,
        "lat": 53.3846
    },
    {
        "code": "SEABURN",
        "name": "Seaburn Rail Station",
        "lng": -1.3867,
        "lat": 54.9295
    },
    {
        "code": "SNDRMNK",
        "name": "St Peters Rail Station",
        "lng": -1.3838,
        "lat": 54.9114
    },
    {
        "code": "SPDN",
        "name": "Spondon Rail Station",
        "lng": -1.4111,
        "lat": 52.9122
    },
    {
        "code": "SNDRLND",
        "name": "Sunderland Rail Station",
        "lng": -1.3823,
        "lat": 54.9053
    },
    {
        "code": "STHS",
        "name": "Streethouse Rail Station",
        "lng": -1.4001,
        "lat": 53.6762
    },
    {
        "code": "MBRK",
        "name": "Millbrook (Hants) Rail Station",
        "lng": -1.4338,
        "lat": 50.9115
    },
    {
        "code": "GARFRTH",
        "name": "Garforth Rail Station",
        "lng": -1.3823,
        "lat": 53.7966
    },
    {
        "code": "THIRSK",
        "name": "Thirsk Rail Station",
        "lng": -1.3726,
        "lat": 54.2282
    },
    {
        "code": "SOTON",
        "name": "Southampton Central Rail Station",
        "lng": -1.4136,
        "lat": 50.9074
    },
    {
        "code": "ALLENSW",
        "name": "Allens West Rail Station",
        "lng": -1.3611,
        "lat": 54.5246
    },
    {
        "code": "FITZWLM",
        "name": "Fitzwilliam Rail Station",
        "lng": -1.3743,
        "lat": 53.6325
    },
    {
        "code": "EGRFRTH",
        "name": "East Garforth Rail Station",
        "lng": -1.3705,
        "lat": 53.792
    },
    {
        "code": "COMBE",
        "name": "Combe (Oxon) Rail Station",
        "lng": -1.3941,
        "lat": 51.8326
    },
    {
        "code": "SOTNTQ",
        "name": "Southampton Town Quay",
        "lng": -1.4058,
        "lat": 50.8952
    },
    {
        "code": "SEAHAM",
        "name": "Seaham Rail Station",
        "lng": -1.3463,
        "lat": 54.8391
    },
    {
        "code": "YAAM",
        "name": "Yarm Rail Station",
        "lng": -1.3515,
        "lat": 54.4939
    },
    {
        "code": "EGLSCLF",
        "name": "Eaglescliffe Rail Station",
        "lng": -1.3494,
        "lat": 54.5294
    },
    {
        "code": "ALFRETN",
        "name": "Alfreton Rail Station",
        "lng": -1.3697,
        "lat": 53.1004
    },
    {
        "code": "FTHRSTN",
        "name": "Featherstone Rail Station",
        "lng": -1.3584,
        "lat": 53.6791
    },
    {
        "code": "ROTHCEN",
        "name": "Rotherham Central Rail Station",
        "lng": -1.3604,
        "lat": 53.4323
    },
    {
        "code": "CASTLFD",
        "name": "Castleford Rail Station",
        "lng": -1.3547,
        "lat": 53.7241
    },
    {
        "code": "HINCKLY",
        "name": "Hinckley Rail Station",
        "lng": -1.3719,
        "lat": 52.535
    },
    {
        "code": "WDHOUSE",
        "name": "Woodhouse Rail Station",
        "lng": -1.3576,
        "lat": 53.3637
    },
    {
        "code": "STDENYS",
        "name": "St Denys Rail Station",
        "lng": -1.3878,
        "lat": 50.9222
    },
    {
        "code": "CSFD",
        "name": "Chandlers Ford Rail Station",
        "lng": -1.3852,
        "lat": 50.9837
    },
    {
        "code": "HANDBRO",
        "name": "Hanborough Rail Station",
        "lng": -1.3735,
        "lat": 51.8252
    },
    {
        "code": "GLASHTN",
        "name": "Glasshoughton Rail Station",
        "lng": -1.342,
        "lat": 53.709
    },
    {
        "code": "BITERNE",
        "name": "Bitterne Rail Station",
        "lng": -1.377,
        "lat": 50.9182
    },
    {
        "code": "WOLSTON",
        "name": "Woolston Rail Station",
        "lng": -1.3771,
        "lat": 50.8989
    },
    {
        "code": "SWYTHLN",
        "name": "Swaythling Rail Station",
        "lng": -1.3764,
        "lat": 50.9411
    },
    {
        "code": "STOCTON",
        "name": "Stockton Rail Station",
        "lng": -1.3185,
        "lat": 54.5696
    },
    {
        "code": "MCKLFLD",
        "name": "Micklefield Rail Station",
        "lng": -1.3268,
        "lat": 53.7888
    },
    {
        "code": "CATTAL",
        "name": "Cattal Rail Station",
        "lng": -1.3205,
        "lat": 53.9974
    },
    {
        "code": "SHOLING",
        "name": "Sholing Rail Station",
        "lng": -1.3649,
        "lat": 50.8968
    },
    {
        "code": "SOTPKWY",
        "name": "Southampton Airport Parkway Rail Station",
        "lng": -1.3631,
        "lat": 50.9508
    },
    {
        "code": "LGML",
        "name": "Langley Mill Rail Station",
        "lng": -1.3312,
        "lat": 53.0181
    },
    {
        "code": "PTFTTSF",
        "name": "Pontefract Tanshelf Rail Station",
        "lng": -1.3189,
        "lat": 53.6941
    },
    {
        "code": "TABY",
        "name": "Thornaby Rail Station",
        "lng": -1.3014,
        "lat": 54.5593
    },
    {
        "code": "GLDTHRP",
        "name": "Goldthorpe Rail Station",
        "lng": -1.3128,
        "lat": 53.5342
    },
    {
        "code": "ELGH",
        "name": "Eastleigh Rail Station",
        "lng": -1.3501,
        "lat": 50.9692
    },
    {
        "code": "BLTNODR",
        "name": "Bolton-Upon-Dearne Rail Station",
        "lng": -1.3115,
        "lat": 53.5189
    },
    {
        "code": "TRNO",
        "name": "Thurnscoe Rail Station",
        "lng": -1.3088,
        "lat": 53.545
    },
    {
        "code": "PTFTMHL",
        "name": "Pontefract Monkhill Rail Station",
        "lng": -1.3037,
        "lat": 53.699
    },
    {
        "code": "MORTHRP",
        "name": "Moorthorpe Rail Station",
        "lng": -1.3049,
        "lat": 53.595
    },
    {
        "code": "PTFTBHL",
        "name": "Pontefract Baghill Rail Station",
        "lng": -1.3034,
        "lat": 53.6919
    },
    {
        "code": "BNBR",
        "name": "Banbury Rail Station",
        "lng": -1.3281,
        "lat": 52.0603
    },
    {
        "code": "SWINTN",
        "name": "Swinton (South Yorks) Rail Station",
        "lng": -1.3058,
        "lat": 53.4862
    },
    {
        "code": "WHTCHRH",
        "name": "Whitchurch (Hants) Rail Station",
        "lng": -1.3377,
        "lat": 51.2375
    },
    {
        "code": "NETLEY",
        "name": "Netley Rail Station",
        "lng": -1.3419,
        "lat": 50.8749
    },
    {
        "code": "BLNGHM",
        "name": "Billingham Rail Station",
        "lng": -1.2797,
        "lat": 54.6056
    },
    {
        "code": "HAMERTN",
        "name": "Hammerton Rail Station",
        "lng": -1.2841,
        "lat": 53.9963
    },
    {
        "code": "NEWBURY",
        "name": "Newbury Rail Station",
        "lng": -1.3229,
        "lat": 51.3976
    },
    {
        "code": "SHAWFD",
        "name": "Shawford Rail Station",
        "lng": -1.3278,
        "lat": 51.0221
    },
    {
        "code": "HMBLE",
        "name": "Hamble Rail Station",
        "lng": -1.3292,
        "lat": 50.8714
    },
    {
        "code": "MEXBRGH",
        "name": "Mexborough Rail Station",
        "lng": -1.2886,
        "lat": 53.491
    },
    {
        "code": "SELMSAL",
        "name": "South Elmsall Rail Station",
        "lng": -1.2849,
        "lat": 53.5946
    },
    {
        "code": "ILKES",
        "name": "Ilkeston Rail Station",
        "lng": -1.2949,
        "lat": 52.9796
    },
    {
        "code": "WNCHSTR",
        "name": "Winchester Rail Station",
        "lng": -1.3197,
        "lat": 51.0672
    },
    {
        "code": "LNGEATN",
        "name": "Long Eaton Rail Station",
        "lng": -1.2875,
        "lat": 52.885
    },
    {
        "code": "NEWBRYR",
        "name": "Newbury Racecourse Rail Station",
        "lng": -1.3078,
        "lat": 51.3985
    },
    {
        "code": "HEYFORD",
        "name": "Heyford Rail Station",
        "lng": -1.2993,
        "lat": 51.9192
    },
    {
        "code": "TACKLEY",
        "name": "Tackley Rail Station",
        "lng": -1.2975,
        "lat": 51.8812
    },
    {
        "code": "KVTNBDG",
        "name": "Kiveton Bridge Rail Station",
        "lng": -1.2672,
        "lat": 53.341
    },
    {
        "code": "BURSLDN",
        "name": "Bursledon Rail Station",
        "lng": -1.305,
        "lat": 50.8837
    },
    {
        "code": "KNTNGLY",
        "name": "Knottingley Rail Station",
        "lng": -1.2592,
        "lat": 53.7065
    },
    {
        "code": "KINSSTN",
        "name": "Kings Sutton Rail Station",
        "lng": -1.2809,
        "lat": 52.0213
    },
    {
        "code": "SMILFD",
        "name": "South Milford Rail Station",
        "lng": -1.2505,
        "lat": 53.7823
    },
    {
        "code": "MDLSBRO",
        "name": "Middlesbrough Rail Station",
        "lng": -1.2347,
        "lat": 54.5791
    },
    {
        "code": "HEDGEND",
        "name": "Hedge End Rail Station",
        "lng": -1.2945,
        "lat": 50.9323
    },
    {
        "code": "EMPKWAY",
        "name": "East Midlands Parkway Rail Station",
        "lng": -1.2632,
        "lat": 52.8625
    },
    {
        "code": "KRKYCEN",
        "name": "Kirkby in Ashfield Rail Station",
        "lng": -1.2531,
        "lat": 53.1001
    },
    {
        "code": "OXFPWAY",
        "name": "Oxford Parkway Rail Station",
        "lng": -1.2745,
        "lat": 51.8041
    },
    {
        "code": "OXFD",
        "name": "Oxford Rail Station",
        "lng": -1.2702,
        "lat": 51.7535
    },
    {
        "code": "STTNPWY",
        "name": "Sutton Parkway Rail Station",
        "lng": -1.2456,
        "lat": 53.1141
    },
    {
        "code": "SHBN",
        "name": "Sherburn-in-Elmet Rail Station",
        "lng": -1.2327,
        "lat": 53.7972
    },
    {
        "code": "KVTNPK",
        "name": "Kiveton Park Rail Station",
        "lng": -1.2398,
        "lat": 53.3367
    },
    {
        "code": "CONBRGH",
        "name": "Conisbrough Rail Station",
        "lng": -1.2343,
        "lat": 53.4893
    },
    {
        "code": "CHFN",
        "name": "Church Fenton Rail Station",
        "lng": -1.2276,
        "lat": 53.8266
    },
    {
        "code": "RUGBY",
        "name": "Rugby Rail Station",
        "lng": -1.2505,
        "lat": 52.3791
    },
    {
        "code": "HRTLEPL",
        "name": "Hartlepool Rail Station",
        "lng": -1.2073,
        "lat": 54.6868
    },
    {
        "code": "JAMCOK",
        "name": "James Cook University Hospital Rail Station",
        "lng": -1.2086,
        "lat": 54.552
    },
    {
        "code": "SETNCRW",
        "name": "Seaton Carew Rail Station",
        "lng": -1.2004,
        "lat": 54.6583
    },
    {
        "code": "SWNWICK",
        "name": "Swanwick Rail Station",
        "lng": -1.2659,
        "lat": 50.8757
    },
    {
        "code": "MCHLDVR",
        "name": "Micheldever Rail Station",
        "lng": -1.2607,
        "lat": 51.1824
    },
    {
        "code": "ATNBRO",
        "name": "Attenborough Rail Station",
        "lng": -1.2314,
        "lat": 52.9062
    },
    {
        "code": "OVTN",
        "name": "Overton Rail Station",
        "lng": -1.2593,
        "lat": 51.2543
    },
    {
        "code": "ULESKLF",
        "name": "Ulleskelf Rail Station",
        "lng": -1.214,
        "lat": 53.8536
    },
    {
        "code": "MARTON",
        "name": "Marton Rail Station",
        "lng": -1.1985,
        "lat": 54.5443
    },
    {
        "code": "BOTLEY",
        "name": "Botley Rail Station",
        "lng": -1.2592,
        "lat": 50.9165
    },
    {
        "code": "NWSTEAD",
        "name": "Newstead Rail Station",
        "lng": -1.2218,
        "lat": 53.07
    },
    {
        "code": "CRWLL",
        "name": "Creswell (Derbys) Rail Station",
        "lng": -1.2164,
        "lat": 53.2641
    },
    {
        "code": "DIDCOTP",
        "name": "Didcot Parkway Rail Station",
        "lng": -1.2429,
        "lat": 51.611
    },
    {
        "code": "APPLEFD",
        "name": "Appleford Rail Station",
        "lng": -1.2421,
        "lat": 51.6396
    },
    {
        "code": "ISLIP",
        "name": "Islip Rail Station",
        "lng": -1.2382,
        "lat": 51.8258
    },
    {
        "code": "RDLEY",
        "name": "Radley Rail Station",
        "lng": -1.2405,
        "lat": 51.6862
    },
    {
        "code": "THATCHM",
        "name": "Thatcham Rail Station",
        "lng": -1.2432,
        "lat": 51.3938
    },
    {
        "code": "LGWITH",
        "name": "Langwith - Whaley Thorns Rail Station",
        "lng": -1.2093,
        "lat": 53.2318
    },
    {
        "code": "CULHAM",
        "name": "Culham Rail Station",
        "lng": -1.2365,
        "lat": 51.6538
    },
    {
        "code": "GYPSYLA",
        "name": "Gypsy Lane Rail Station",
        "lng": -1.1794,
        "lat": 54.5329
    },
    {
        "code": "STHBANK",
        "name": "South Bank Rail Station",
        "lng": -1.1767,
        "lat": 54.5838
    },
    {
        "code": "BESTON",
        "name": "Beeston Rail Station",
        "lng": -1.2077,
        "lat": 52.9208
    },
    {
        "code": "SHRBROK",
        "name": "Shirebrook Rail Station",
        "lng": -1.2024,
        "lat": 53.2042
    },
    {
        "code": "WHWLL",
        "name": "Whitwell (Derbys) Rail Station",
        "lng": -1.2002,
        "lat": 53.28
    },
    {
        "code": "MFLDWSE",
        "name": "Mansfield Woodhouse Rail Station",
        "lng": -1.2018,
        "lat": 53.1636
    },
    {
        "code": "MFLDTWN",
        "name": "Mansfield Rail Station",
        "lng": -1.1984,
        "lat": 53.1421
    },
    {
        "code": "NUNTHRP",
        "name": "Nunthorpe Rail Station",
        "lng": -1.1694,
        "lat": 54.5279
    },
    {
        "code": "HUCKNAL",
        "name": "Hucknall Rail Station",
        "lng": -1.1958,
        "lat": 53.0383
    },
    {
        "code": "BULWELL",
        "name": "Bulwell Rail Station",
        "lng": -1.1962,
        "lat": 52.9997
    },
    {
        "code": "NARBRO",
        "name": "Narborough Rail Station",
        "lng": -1.2033,
        "lat": 52.5713
    },
    {
        "code": "LOGHBRO",
        "name": "Loughborough (Leics) Rail Station",
        "lng": -1.1959,
        "lat": 52.779
    },
    {
        "code": "ADWICK",
        "name": "Adwick Rail Station",
        "lng": -1.1804,
        "lat": 53.5723
    },
    {
        "code": "SHRKSKS",
        "name": "Shireoaks Rail Station",
        "lng": -1.168,
        "lat": 53.3248
    },
    {
        "code": "WHTBDGE",
        "name": "Whitley Bridge Rail Station",
        "lng": -1.1583,
        "lat": 53.6991
    },
    {
        "code": "POPLTON",
        "name": "Poppleton Rail Station",
        "lng": -1.1486,
        "lat": 53.9759
    },
    {
        "code": "BTLYSY",
        "name": "Bentley (S Yorks) Rail Station",
        "lng": -1.1509,
        "lat": 53.5439
    },
    {
        "code": "FAREHAM",
        "name": "Fareham Rail Station",
        "lng": -1.192,
        "lat": 50.853
    },
    {
        "code": "DONC",
        "name": "Doncaster Rail Station",
        "lng": -1.1398,
        "lat": 53.5221
    },
    {
        "code": "MIDGHAM",
        "name": "Midgham Rail Station",
        "lng": -1.1777,
        "lat": 51.396
    },
    {
        "code": "GTAYTON",
        "name": "Great Ayton Rail Station",
        "lng": -1.1153,
        "lat": 54.4896
    },
    {
        "code": "REDCBSC",
        "name": "British Steel Redcar Rail Station",
        "lng": -1.1127,
        "lat": 54.6099
    },
    {
        "code": "NTNG",
        "name": "Nottingham Rail Station",
        "lng": -1.1464,
        "lat": 52.9471
    },
    {
        "code": "BAROWOS",
        "name": "Barrow upon Soar Rail Station",
        "lng": -1.1448,
        "lat": 52.7493
    },
    {
        "code": "SHANKLN",
        "name": "Shanklin Rail Station",
        "lng": -1.1798,
        "lat": 50.6339
    },
    {
        "code": "CHOLSEY",
        "name": "Cholsey Rail Station",
        "lng": -1.158,
        "lat": 51.5702
    },
    {
        "code": "WORKSOP",
        "name": "Worksop Rail Station",
        "lng": -1.1228,
        "lat": 53.3115
    },
    {
        "code": "BCSTN",
        "name": "Bicester North Rail Station",
        "lng": -1.1504,
        "lat": 51.9035
    },
    {
        "code": "HENSALL",
        "name": "Hensall Rail Station",
        "lng": -1.1145,
        "lat": 53.6985
    },
    {
        "code": "BCSTRTN",
        "name": "Bicester Village Rail Station",
        "lng": -1.1488,
        "lat": 51.893
    },
    {
        "code": "WGSTS",
        "name": "South Wigston Rail Station",
        "lng": -1.1341,
        "lat": 52.5822
    },
    {
        "code": "BTRSBY",
        "name": "Battersby Rail Station",
        "lng": -1.093,
        "lat": 54.4577
    },
    {
        "code": "LAKEIOW",
        "name": "Lake (Isle of Wight) Rail Station",
        "lng": -1.1663,
        "lat": 50.6465
    },
    {
        "code": "LESTER",
        "name": "Leicester Rail Station",
        "lng": -1.1253,
        "lat": 52.6314
    },
    {
        "code": "SNDOWN",
        "name": "Sandown Rail Station",
        "lng": -1.1624,
        "lat": 50.6569
    },
    {
        "code": "RYDP",
        "name": "Ryde Pier Head Rail Station",
        "lng": -1.1601,
        "lat": 50.7392
    },
    {
        "code": "RYDE",
        "name": "Ryde Esplanade Rail Station",
        "lng": -1.1596,
        "lat": 50.7329
    },
    {
        "code": "YORK",
        "name": "York Rail Station",
        "lng": -1.0932,
        "lat": 53.958
    },
    {
        "code": "RYDS",
        "name": "Ryde St Johns Road Rail Station",
        "lng": -1.1566,
        "lat": 50.7244
    },
    {
        "code": "SMALBRK",
        "name": "Smallbrook Junction Rail Station",
        "lng": -1.1542,
        "lat": 50.7111
    },
    {
        "code": "ALDMSTN",
        "name": "Aldermaston Rail Station",
        "lng": -1.1374,
        "lat": 51.402
    },
    {
        "code": "REDCARC",
        "name": "Redcar Central Rail Station",
        "lng": -1.0709,
        "lat": 54.6162
    },
    {
        "code": "SILEBY",
        "name": "Sileby Rail Station",
        "lng": -1.11,
        "lat": 52.7316
    },
    {
        "code": "GORASTR",
        "name": "Goring & Streatley Rail Station",
        "lng": -1.133,
        "lat": 51.5215
    },
    {
        "code": "KLDL",
        "name": "Kildale Rail Station",
        "lng": -1.0681,
        "lat": 54.4778
    },
    {
        "code": "BRDING",
        "name": "Brading Rail Station",
        "lng": -1.1387,
        "lat": 50.6784
    },
    {
        "code": "REDCARE",
        "name": "Redcar East Rail Station",
        "lng": -1.0523,
        "lat": 54.6093
    },
    {
        "code": "KKSNDAL",
        "name": "Kirk Sandall Rail Station",
        "lng": -1.0741,
        "lat": 53.5639
    },
    {
        "code": "PCHESTR",
        "name": "Portchester Rail Station",
        "lng": -1.1242,
        "lat": 50.8487
    },
    {
        "code": "SELBY",
        "name": "Selby Rail Station",
        "lng": -1.0638,
        "lat": 53.7828
    },
    {
        "code": "NTHRFLD",
        "name": "Netherfield Rail Station",
        "lng": -1.0798,
        "lat": 52.9614
    },
    {
        "code": "CRTN",
        "name": "Carlton Rail Station",
        "lng": -1.0787,
        "lat": 52.9651
    },
    {
        "code": "SYSTON",
        "name": "Syston Rail Station",
        "lng": -1.0824,
        "lat": 52.6942
    },
    {
        "code": "LNGBKBY",
        "name": "Long Buckby Rail Station",
        "lng": -1.0865,
        "lat": 52.2947
    },
    {
        "code": "LONGBCK",
        "name": "Longbeck Rail Station",
        "lng": -1.0305,
        "lat": 54.5892
    },
    {
        "code": "PHBR",
        "name": "Portsmouth Harbour Rail Station",
        "lng": -1.1078,
        "lat": 50.797
    },
    {
        "code": "PANGBRN",
        "name": "Pangbourne Rail Station",
        "lng": -1.0905,
        "lat": 51.4854
    },
    {
        "code": "MRSK",
        "name": "Marske Rail Station",
        "lng": -1.0189,
        "lat": 54.5874
    },
    {
        "code": "SSEACLE",
        "name": "Southsea Hoverport",
        "lng": -1.1,
        "lat": 50.7853
    },
    {
        "code": "BSNGSTK",
        "name": "Basingstoke Rail Station",
        "lng": -1.0873,
        "lat": 51.2684
    },
    {
        "code": "PSEA",
        "name": "Portsmouth & Southsea Rail Station",
        "lng": -1.0909,
        "lat": 50.7985
    },
    {
        "code": "SNAITH",
        "name": "Snaith Rail Station",
        "lng": -1.0285,
        "lat": 53.6931
    },
    {
        "code": "THEALE",
        "name": "Theale Rail Station",
        "lng": -1.075,
        "lat": 51.4334
    },
    {
        "code": "BRTJYC",
        "name": "Burton Joyce Rail Station",
        "lng": -1.0409,
        "lat": 52.9834
    },
    {
        "code": "HTFLASF",
        "name": "Hatfield & Stainforth Rail Station",
        "lng": -1.0234,
        "lat": 53.5887
    },
    {
        "code": "RADNOT",
        "name": "Radcliffe (Notts) Rail Station",
        "lng": -1.0373,
        "lat": 52.9488
    },
    {
        "code": "FRATTON",
        "name": "Fratton Rail Station",
        "lng": -1.074,
        "lat": 50.7963
    },
    {
        "code": "BMLY",
        "name": "Bramley (Hants) Rail Station",
        "lng": -1.061,
        "lat": 51.3303
    },
    {
        "code": "COSHAM",
        "name": "Cosham Rail Station",
        "lng": -1.0673,
        "lat": 50.8419
    },
    {
        "code": "HILSEA",
        "name": "Hilsea Rail Station",
        "lng": -1.0588,
        "lat": 50.8283
    },
    {
        "code": "SBRN",
        "name": "Saltburn Rail Station",
        "lng": -0.9741,
        "lat": 54.5834
    },
    {
        "code": "COMONDL",
        "name": "Commondale Rail Station",
        "lng": -0.9751,
        "lat": 54.4813
    },
    {
        "code": "MTIMER",
        "name": "Mortimer Rail Station",
        "lng": -1.0355,
        "lat": 51.3721
    },
    {
        "code": "LOWDHAM",
        "name": "Lowdham Rail Station",
        "lng": -0.9984,
        "lat": 53.0063
    },
    {
        "code": "TILHRST",
        "name": "Tilehurst Rail Station",
        "lng": -1.0298,
        "lat": 51.4715
    },
    {
        "code": "THORNEN",
        "name": "Thorne North Rail Station",
        "lng": -0.9723,
        "lat": 53.6161
    },
    {
        "code": "CTNM",
        "name": "Castleton Moor Rail Station",
        "lng": -0.9466,
        "lat": 54.4671
    },
    {
        "code": "RAWCLIF",
        "name": "Rawcliffe Rail Station",
        "lng": -0.9609,
        "lat": 53.689
    },
    {
        "code": "THORNES",
        "name": "Thorne South Rail Station",
        "lng": -0.9551,
        "lat": 53.6033
    },
    {
        "code": "THRGRTN",
        "name": "Thurgarton Rail Station",
        "lng": -0.9623,
        "lat": 53.0289
    },
    {
        "code": "RTFD",
        "name": "Retford Rail Station",
        "lng": -0.9479,
        "lat": 53.3152
    },
    {
        "code": "REDGWST",
        "name": "Reading West Rail Station",
        "lng": -0.9901,
        "lat": 51.4555
    },
    {
        "code": "RTFDLL",
        "name": "Retford Low Level Rail Station",
        "lng": -0.9448,
        "lat": 53.3141
    },
    {
        "code": "BINGHAM",
        "name": "Bingham Rail Station",
        "lng": -0.9515,
        "lat": 52.9542
    },
    {
        "code": "DANBY",
        "name": "Danby Rail Station",
        "lng": -0.911,
        "lat": 54.4662
    },
    {
        "code": "BDHMPTN",
        "name": "Bedhampton Rail Station",
        "lng": -0.9958,
        "lat": 50.854
    },
    {
        "code": "BLEASBY",
        "name": "Bleasby Rail Station",
        "lng": -0.9437,
        "lat": 53.0414
    },
    {
        "code": "WRESSLE",
        "name": "Wressle Rail Station",
        "lng": -0.9243,
        "lat": 53.7729
    },
    {
        "code": "RDNG4AB",
        "name": "Reading Rail Station",
        "lng": -0.9719,
        "lat": 51.4588
    },
    {
        "code": "RDNGSTN",
        "name": "Reading Rail Station",
        "lng": -0.9718,
        "lat": 51.4588
    },
    {
        "code": "RDNGBUS",
        "name": "Reading Rail Station",
        "lng": -0.9717,
        "lat": 51.4581
    },
    {
        "code": "HAVANT",
        "name": "Havant Rail Station",
        "lng": -0.9816,
        "lat": 50.8544
    },
    {
        "code": "ALTON",
        "name": "Alton Rail Station",
        "lng": -0.9669,
        "lat": 51.152
    },
    {
        "code": "HOOK",
        "name": "Hook Rail Station",
        "lng": -0.9616,
        "lat": 51.28
    },
    {
        "code": "WRBLNGT",
        "name": "Warblington Rail Station",
        "lng": -0.9672,
        "lat": 50.8534
    },
    {
        "code": "FISKRTN",
        "name": "Fiskerton Rail Station",
        "lng": -0.9122,
        "lat": 53.0603
    },
    {
        "code": "HADMATP",
        "name": "Haddenham & Thame Parkway Rail Station",
        "lng": -0.9421,
        "lat": 51.7709
    },
    {
        "code": "RWLNDSC",
        "name": "Rowlands Castle Rail Station",
        "lng": -0.9575,
        "lat": 50.8922
    },
    {
        "code": "ROLSTN",
        "name": "Rolleston Rail Station",
        "lng": -0.8997,
        "lat": 53.0653
    },
    {
        "code": "ASLCKTN",
        "name": "Aslockton Rail Station",
        "lng": -0.8981,
        "lat": 52.9515
    },
    {
        "code": "MRKTHRB",
        "name": "Market Harborough Rail Station",
        "lng": -0.9093,
        "lat": 52.4797
    },
    {
        "code": "PTRSFLD",
        "name": "Petersfield Rail Station",
        "lng": -0.9411,
        "lat": 51.0067
    },
    {
        "code": "GOOLE",
        "name": "Goole Rail Station",
        "lng": -0.8742,
        "lat": 53.7049
    },
    {
        "code": "NMPTN",
        "name": "Northampton Rail Station",
        "lng": -0.9067,
        "lat": 52.2375
    },
    {
        "code": "EMSWTH",
        "name": "Emsworth Rail Station",
        "lng": -0.9384,
        "lat": 50.8516
    },
    {
        "code": "HOWDEN",
        "name": "Howden Rail Station",
        "lng": -0.8605,
        "lat": 53.7647
    },
    {
        "code": "MLTNSDG",
        "name": "Melton Mowbray Rail Station",
        "lng": -0.8859,
        "lat": 52.761
    },
    {
        "code": "ERLY",
        "name": "Earley Rail Station",
        "lng": -0.918,
        "lat": 51.4411
    },
    {
        "code": "LEALHLM",
        "name": "Lealholm Rail Station",
        "lng": -0.8257,
        "lat": 54.4606
    },
    {
        "code": "WNCFILD",
        "name": "Winchfield Rail Station",
        "lng": -0.907,
        "lat": 51.2849
    },
    {
        "code": "HNLYOT",
        "name": "Henley-on-Thames Rail Station",
        "lng": -0.9002,
        "lat": 51.5342
    },
    {
        "code": "SBOURNE",
        "name": "Southbourne Rail Station",
        "lng": -0.9081,
        "lat": 50.8483
    },
    {
        "code": "ELTON",
        "name": "Elton & Orston Rail Station",
        "lng": -0.8555,
        "lat": 52.9521
    },
    {
        "code": "WINETGL",
        "name": "Winnersh Triangle Rail Station",
        "lng": -0.8913,
        "lat": 51.4367
    },
    {
        "code": "SHPLAKE",
        "name": "Shiplake Rail Station",
        "lng": -0.8826,
        "lat": 51.5115
    },
    {
        "code": "LISS",
        "name": "Liss Rail Station",
        "lng": -0.8929,
        "lat": 51.0436
    },
    {
        "code": "WARGRAV",
        "name": "Wargrave Rail Station",
        "lng": -0.8765,
        "lat": 51.4982
    },
    {
        "code": "WINERSH",
        "name": "Winnersh Rail Station",
        "lng": -0.8769,
        "lat": 51.4303
    },
    {
        "code": "GLAISDL",
        "name": "Glaisdale Rail Station",
        "lng": -0.7938,
        "lat": 54.4394
    },
    {
        "code": "CROWLE",
        "name": "Crowle Rail Station",
        "lng": -0.8174,
        "lat": 53.5897
    },
    {
        "code": "AYLSPWY",
        "name": "Aylesbury Vale Parkway Rail Station",
        "lng": -0.8602,
        "lat": 51.8312
    },
    {
        "code": "SLTMRSH",
        "name": "Saltmarshe Rail Station",
        "lng": -0.8095,
        "lat": 53.7219
    },
    {
        "code": "MALTON",
        "name": "Malton Rail Station",
        "lng": -0.7972,
        "lat": 54.1321
    },
    {
        "code": "NUTBORN",
        "name": "Nutbourne Rail Station",
        "lng": -0.8829,
        "lat": 50.8461
    },
    {
        "code": "TWYFORD",
        "name": "Twyford Rail Station",
        "lng": -0.8633,
        "lat": 51.4755
    },
    {
        "code": "BNTEY",
        "name": "Bentley (Hants) Rail Station",
        "lng": -0.8681,
        "lat": 51.1812
    },
    {
        "code": "NWRKCAS",
        "name": "Newark Castle Rail Station",
        "lng": -0.8132,
        "lat": 53.08
    },
    {
        "code": "PRINRIS",
        "name": "Princes Risborough Rail Station",
        "lng": -0.8439,
        "lat": 51.7179
    },
    {
        "code": "ESTRNGT",
        "name": "Eastrington Rail Station",
        "lng": -0.7876,
        "lat": 53.7552
    },
    {
        "code": "EGTON",
        "name": "Egton Rail Station",
        "lng": -0.7615,
        "lat": 54.4375
    },
    {
        "code": "NEWANG",
        "name": "Newark North Gate Rail Station",
        "lng": -0.7999,
        "lat": 53.0818
    },
    {
        "code": "WOKNGHM",
        "name": "Wokingham Rail Station",
        "lng": -0.8425,
        "lat": 51.4112
    },
    {
        "code": "MNKRISB",
        "name": "Monks Risborough Rail Station",
        "lng": -0.8293,
        "lat": 51.7358
    },
    {
        "code": "BOTESFD",
        "name": "Bottesford Rail Station",
        "lng": -0.7948,
        "lat": 52.9446
    },
    {
        "code": "BOSHAM",
        "name": "Bosham Rail Station",
        "lng": -0.8474,
        "lat": 50.8427
    },
    {
        "code": "SUNDRTN",
        "name": "Saunderton Rail Station",
        "lng": -0.8255,
        "lat": 51.6759
    },
    {
        "code": "FLEET",
        "name": "Fleet Rail Station",
        "lng": -0.8308,
        "lat": 51.2906
    },
    {
        "code": "AYLSBRY",
        "name": "Aylesbury Rail Station",
        "lng": -0.8151,
        "lat": 51.8139
    },
    {
        "code": "GBROC",
        "name": "Gainsborough Central Rail Station",
        "lng": -0.7697,
        "lat": 53.3996
    },
    {
        "code": "GBGHLRD",
        "name": "Gainsborough Lea Road Rail Station",
        "lng": -0.7686,
        "lat": 53.3861
    },
    {
        "code": "WLVR",
        "name": "Wolverton Rail Station",
        "lng": -0.8043,
        "lat": 52.0659
    },
    {
        "code": "CRWTHRN",
        "name": "Crowthorne Rail Station",
        "lng": -0.8193,
        "lat": 51.3667
    },
    {
        "code": "LTLKMBL",
        "name": "Little Kimble Rail Station",
        "lng": -0.8085,
        "lat": 51.7522
    },
    {
        "code": "GROSMNT",
        "name": "Grosmont Rail Station",
        "lng": -0.725,
        "lat": 54.4361
    },
    {
        "code": "SNDHRST",
        "name": "Sandhurst Rail Station",
        "lng": -0.8046,
        "lat": 51.3469
    },
    {
        "code": "FSHBORN",
        "name": "Fishbourne Rail Station",
        "lng": -0.8151,
        "lat": 50.839
    },
    {
        "code": "CLHM",
        "name": "Collingham Rail Station",
        "lng": -0.7504,
        "lat": 53.1441
    },
    {
        "code": "GLBRDYK",
        "name": "Gilberdyke Rail Station",
        "lng": -0.7322,
        "lat": 53.748
    },
    {
        "code": "ALTPE",
        "name": "Althorpe Rail Station",
        "lng": -0.7332,
        "lat": 53.5855
    },
    {
        "code": "STKM",
        "name": "Stoke Mandeville Rail Station",
        "lng": -0.7841,
        "lat": 51.7878
    },
    {
        "code": "LIPHOOK",
        "name": "Liphook Rail Station",
        "lng": -0.8002,
        "lat": 51.0713
    },
    {
        "code": "MKNSCEN",
        "name": "Milton Keynes Central Rail Station",
        "lng": -0.7741,
        "lat": 52.0343
    },
    {
        "code": "FARNHAM",
        "name": "Farnham Rail Station",
        "lng": -0.7924,
        "lat": 51.2119
    },
    {
        "code": "BCKWATR",
        "name": "Blackwater Rail Station",
        "lng": -0.7767,
        "lat": 51.3316
    },
    {
        "code": "MARLOW",
        "name": "Marlow Rail Station",
        "lng": -0.7664,
        "lat": 51.571
    },
    {
        "code": "OAKHAM",
        "name": "Oakham Rail Station",
        "lng": -0.7342,
        "lat": 52.6722
    },
    {
        "code": "CHCHSTR",
        "name": "Chichester Rail Station",
        "lng": -0.7817,
        "lat": 50.8321
    },
    {
        "code": "KETR",
        "name": "Kettering Rail Station",
        "lng": -0.7316,
        "lat": 52.3936
    },
    {
        "code": "WENDOVR",
        "name": "Wendover Rail Station",
        "lng": -0.7474,
        "lat": 51.7618
    },
    {
        "code": "ALDRSHT",
        "name": "Aldershot Rail Station",
        "lng": -0.7599,
        "lat": 51.2464
    },
    {
        "code": "SLEGHTS",
        "name": "Sleights Rail Station",
        "lng": -0.6625,
        "lat": 54.4611
    },
    {
        "code": "SWNDRBY",
        "name": "Swinderby Rail Station",
        "lng": -0.7027,
        "lat": 53.1696
    },
    {
        "code": "FRBRMN",
        "name": "Farnborough (Main) Rail Station",
        "lng": -0.7557,
        "lat": 51.2966
    },
    {
        "code": "BLTCHLY",
        "name": "Bletchley Rail Station",
        "lng": -0.7363,
        "lat": 51.9953
    },
    {
        "code": "BRACKNL",
        "name": "Bracknell Rail Station",
        "lng": -0.7517,
        "lat": 51.4131
    },
    {
        "code": "HWYCOMB",
        "name": "High Wycombe Rail Station",
        "lng": -0.7454,
        "lat": 51.6296
    },
    {
        "code": "FRIMLEY",
        "name": "Frimley Rail Station",
        "lng": -0.747,
        "lat": 51.3119
    },
    {
        "code": "CMBLEY",
        "name": "Camberley Rail Station",
        "lng": -0.7443,
        "lat": 51.3363
    },
    {
        "code": "BRFT",
        "name": "Broomfleet Rail Station",
        "lng": -0.6718,
        "lat": 53.7402
    },
    {
        "code": "FRBRNTH",
        "name": "Farnborough North Rail Station",
        "lng": -0.743,
        "lat": 51.302
    },
    {
        "code": "FSTR",
        "name": "Fenny Stratford Rail Station",
        "lng": -0.716,
        "lat": 52.0001
    },
    {
        "code": "FURZEP",
        "name": "Furze Platt Rail Station",
        "lng": -0.7285,
        "lat": 51.533
    },
    {
        "code": "NTHCAMP",
        "name": "North Camp Rail Station",
        "lng": -0.7312,
        "lat": 51.2758
    },
    {
        "code": "COOKHAM",
        "name": "Cookham Rail Station",
        "lng": -0.7221,
        "lat": 51.5575
    },
    {
        "code": "MDNHEAD",
        "name": "Maidenhead Rail Station",
        "lng": -0.7227,
        "lat": 51.5187
    },
    {
        "code": "MHERON",
        "name": "Martins Heron Rail Station",
        "lng": -0.7244,
        "lat": 51.4074
    },
    {
        "code": "RUSWARP",
        "name": "Ruswarp Rail Station",
        "lng": -0.6278,
        "lat": 54.4702
    },
    {
        "code": "CORBY",
        "name": "Corby Rail Station",
        "lng": -0.6883,
        "lat": 52.4888
    },
    {
        "code": "SAXILBY",
        "name": "Saxilby Rail Station",
        "lng": -0.664,
        "lat": 53.2672
    },
    {
        "code": "ASHVALE",
        "name": "Ash Vale Rail Station",
        "lng": -0.7216,
        "lat": 51.2722
    },
    {
        "code": "GTMSNDN",
        "name": "Great Missenden Rail Station",
        "lng": -0.7091,
        "lat": 51.7035
    },
    {
        "code": "SCNTHRP",
        "name": "Scunthorpe Rail Station",
        "lng": -0.651,
        "lat": 53.5862
    },
    {
        "code": "BORNEND",
        "name": "Bourne End Rail Station",
        "lng": -0.7105,
        "lat": 51.5771
    },
    {
        "code": "BOWBRKH",
        "name": "Bow Brickhill Rail Station",
        "lng": -0.6961,
        "lat": 52.0043
    },
    {
        "code": "WTBY",
        "name": "Whitby Rail Station",
        "lng": -0.6154,
        "lat": 54.4846
    },
    {
        "code": "HASLEMR",
        "name": "Haslemere Rail Station",
        "lng": -0.7192,
        "lat": 51.0886
    },
    {
        "code": "ASHH",
        "name": "Ash Rail Station",
        "lng": -0.7128,
        "lat": 51.2496
    },
    {
        "code": "WLNGBRO",
        "name": "Wellingborough Rail Station",
        "lng": -0.6767,
        "lat": 52.3038
    },
    {
        "code": "LTNBZRD",
        "name": "Leighton Buzzard Rail Station",
        "lng": -0.677,
        "lat": 51.9163
    },
    {
        "code": "BAGSHOT",
        "name": "Bagshot Rail Station",
        "lng": -0.6887,
        "lat": 51.3644
    },
    {
        "code": "GTHM",
        "name": "Grantham Rail Station",
        "lng": -0.6425,
        "lat": 52.9065
    },
    {
        "code": "TAPLOW",
        "name": "Taplow Rail Station",
        "lng": -0.6814,
        "lat": 51.5236
    },
    {
        "code": "ASCOT",
        "name": "Ascot Rail Station",
        "lng": -0.6758,
        "lat": 51.4062
    },
    {
        "code": "CHDNGTN",
        "name": "Cheddington Rail Station",
        "lng": -0.6622,
        "lat": 51.8579
    },
    {
        "code": "WOBURNS",
        "name": "Woburn Sands Rail Station",
        "lng": -0.6541,
        "lat": 52.0181
    },
    {
        "code": "WANBRO",
        "name": "Wanborough Rail Station",
        "lng": -0.6676,
        "lat": 51.2445
    },
    {
        "code": "KRTNLND",
        "name": "Kirton Lindsey Rail Station",
        "lng": -0.5939,
        "lat": 53.4848
    },
    {
        "code": "BOGNORR",
        "name": "Bognor Regis Rail Station",
        "lng": -0.6762,
        "lat": 50.7866
    },
    {
        "code": "HYKEHAM",
        "name": "Hykeham Rail Station",
        "lng": -0.6002,
        "lat": 53.195
    },
    {
        "code": "BROUGH",
        "name": "Brough Rail Station",
        "lng": -0.5787,
        "lat": 53.727
    },
    {
        "code": "ASPLEYG",
        "name": "Aspley Guise Rail Station",
        "lng": -0.6323,
        "lat": 52.0212
    },
    {
        "code": "BCNSFLD",
        "name": "Beaconsfield Rail Station",
        "lng": -0.6438,
        "lat": 51.6113
    },
    {
        "code": "BNHAM",
        "name": "Burnham (Berks) Rail Station",
        "lng": -0.6464,
        "lat": 51.5235
    },
    {
        "code": "WITLEY",
        "name": "Witley Rail Station",
        "lng": -0.6458,
        "lat": 51.1332
    },
    {
        "code": "TRING",
        "name": "Tring Rail Station",
        "lng": -0.6224,
        "lat": 51.8007
    },
    {
        "code": "BRKWOOD",
        "name": "Brookwood Rail Station",
        "lng": -0.6357,
        "lat": 51.3038
    },
    {
        "code": "SUNNGDL",
        "name": "Sunningdale Rail Station",
        "lng": -0.633,
        "lat": 51.3919
    },
    {
        "code": "MLFORD",
        "name": "Milford (Surrey) Rail Station",
        "lng": -0.6369,
        "lat": 51.1633
    },
    {
        "code": "BRHM",
        "name": "Barnham Rail Station",
        "lng": -0.6397,
        "lat": 50.8309
    },
    {
        "code": "AMERSHM",
        "name": "Amersham Rail Station",
        "lng": -0.6076,
        "lat": 51.6742
    },
    {
        "code": "SEERGRN",
        "name": "Seer Green Rail Station",
        "lng": -0.6078,
        "lat": 51.6098
    },
    {
        "code": "RIDGMNT",
        "name": "Ridgmont Rail Station",
        "lng": -0.5946,
        "lat": 52.0264
    },
    {
        "code": "WINDSEC",
        "name": "Windsor & Eton Central Rail Station",
        "lng": -0.6104,
        "lat": 51.4833
    },
    {
        "code": "GDLMING",
        "name": "Godalming Rail Station",
        "lng": -0.6189,
        "lat": 51.1866
    },
    {
        "code": "WSORAER",
        "name": "Windsor & Eton Riverside Rail Station",
        "lng": -0.6065,
        "lat": 51.4856
    },
    {
        "code": "LINCLNC",
        "name": "Lincoln Central Rail Station",
        "lng": -0.5399,
        "lat": 53.2261
    },
    {
        "code": "FRNCMB",
        "name": "Farncombe Rail Station",
        "lng": -0.6045,
        "lat": 51.1972
    },
    {
        "code": "SLOUGH",
        "name": "Slough Rail Station",
        "lng": -0.5915,
        "lat": 51.5119
    },
    {
        "code": "LNGCROS",
        "name": "Longcross Rail Station",
        "lng": -0.5946,
        "lat": 51.3852
    },
    {
        "code": "ANCASTR",
        "name": "Ancaster Rail Station",
        "lng": -0.5356,
        "lat": 52.9877
    },
    {
        "code": "FERRIBY",
        "name": "Ferriby Rail Station",
        "lng": -0.5078,
        "lat": 53.7172
    },
    {
        "code": "DATCHET",
        "name": "Datchet Rail Station",
        "lng": -0.5794,
        "lat": 51.4831
    },
    {
        "code": "LDLNGTN",
        "name": "Lidlington Rail Station",
        "lng": -0.5589,
        "lat": 52.0415
    },
    {
        "code": "WRPLSDN",
        "name": "Worplesdon Rail Station",
        "lng": -0.5826,
        "lat": 51.289
    },
    {
        "code": "GUILDFD",
        "name": "Guildford Rail Station",
        "lng": -0.5804,
        "lat": 51.237
    },
    {
        "code": "BERKHMD",
        "name": "Berkhamsted Rail Station",
        "lng": -0.562,
        "lat": 51.7631
    },
    {
        "code": "CHLFNAL",
        "name": "Chalfont & Latimer Rail Station",
        "lng": -0.5605,
        "lat": 51.6681
    },
    {
        "code": "VRGNWTR",
        "name": "Virginia Water Rail Station",
        "lng": -0.5622,
        "lat": 51.4018
    },
    {
        "code": "SUNYMDS",
        "name": "Sunnymeads Rail Station",
        "lng": -0.5594,
        "lat": 51.4703
    },
    {
        "code": "GERRDSX",
        "name": "Gerrards Cross Rail Station",
        "lng": -0.5553,
        "lat": 51.589
    },
    {
        "code": "SHALFD",
        "name": "Shalford (Surrey) Rail Station",
        "lng": -0.5668,
        "lat": 51.2143
    },
    {
        "code": "FORD",
        "name": "Ford Rail Station",
        "lng": -0.5784,
        "lat": 50.8294
    },
    {
        "code": "LRDGFD",
        "name": "London Road (Guildford) Rail Station",
        "lng": -0.5651,
        "lat": 51.2406
    },
    {
        "code": "BRGG",
        "name": "Brigg Rail Station",
        "lng": -0.4861,
        "lat": 53.5491
    },
    {
        "code": "WOKING",
        "name": "Woking Rail Station",
        "lng": -0.557,
        "lat": 51.3185
    },
    {
        "code": "MLBRKB",
        "name": "Millbrook (Beds) Rail Station",
        "lng": -0.5327,
        "lat": 52.0538
    },
    {
        "code": "EGHAM",
        "name": "Egham Rail Station",
        "lng": -0.5465,
        "lat": 51.4296
    },
    {
        "code": "LANGLEY",
        "name": "Langley (Berks) Rail Station",
        "lng": -0.5418,
        "lat": 51.5081
    },
    {
        "code": "WRYSBRY",
        "name": "Wraysbury Rail Station",
        "lng": -0.5419,
        "lat": 51.4577
    },
    {
        "code": "STWRTBY",
        "name": "Stewartby Rail Station",
        "lng": -0.5207,
        "lat": 52.0691
    },
    {
        "code": "ARUNDEL",
        "name": "Arundel Rail Station",
        "lng": -0.5462,
        "lat": 50.8482
    },
    {
        "code": "LTLHMPT",
        "name": "Littlehampton Rail Station",
        "lng": -0.546,
        "lat": 50.8101
    },
    {
        "code": "KMPSTNH",
        "name": "Kempston Hardwick Rail Station",
        "lng": -0.5039,
        "lat": 52.0922
    },
    {
        "code": "CHRW",
        "name": "Chorleywood Rail Station",
        "lng": -0.5183,
        "lat": 51.6542
    },
    {
        "code": "AMLY",
        "name": "Amberley Rail Station",
        "lng": -0.542,
        "lat": 50.8967
    },
    {
        "code": "DRIFILD",
        "name": "Driffield Rail Station",
        "lng": -0.4347,
        "lat": 54.0015
    },
    {
        "code": "DENHMGC",
        "name": "Denham Golf Club Rail Station",
        "lng": -0.5178,
        "lat": 51.5806
    },
    {
        "code": "HTNCRNS",
        "name": "Hutton Cranswick Rail Station",
        "lng": -0.4339,
        "lat": 53.9559
    },
    {
        "code": "BRTHMBR",
        "name": "Barton-on-Humber Rail Station",
        "lng": -0.4434,
        "lat": 53.6889
    },
    {
        "code": "HESSLE",
        "name": "Hessle Rail Station",
        "lng": -0.4418,
        "lat": 53.7174
    },
    {
        "code": "STAMFD",
        "name": "Stamford Rail Station",
        "lng": -0.4801,
        "lat": 52.6478
    },
    {
        "code": "CHLWTH",
        "name": "Chilworth Rail Station",
        "lng": -0.5248,
        "lat": 51.2152
    },
    {
        "code": "SEAMER",
        "name": "Seamer Rail Station",
        "lng": -0.417,
        "lat": 54.2408
    },
    {
        "code": "FLITWCK",
        "name": "Flitwick Rail Station",
        "lng": -0.4953,
        "lat": 52.0036
    },
    {
        "code": "HRLG",
        "name": "Harlington (Beds) Rail Station",
        "lng": -0.4957,
        "lat": 51.9621
    },
    {
        "code": "ARRAM",
        "name": "Arram Rail Station",
        "lng": -0.4266,
        "lat": 53.8843
    },
    {
        "code": "RAUCEBY",
        "name": "Rauceby Rail Station",
        "lng": -0.4566,
        "lat": 52.9852
    },
    {
        "code": "IVER",
        "name": "Iver Rail Station",
        "lng": -0.5067,
        "lat": 51.5085
    },
    {
        "code": "CHTSEY",
        "name": "Chertsey Rail Station",
        "lng": -0.5093,
        "lat": 51.3871
    },
    {
        "code": "BEVERLY",
        "name": "Beverley Rail Station",
        "lng": -0.423,
        "lat": 53.8423
    },
    {
        "code": "SCARBRO",
        "name": "Scarborough Rail Station",
        "lng": -0.4057,
        "lat": 54.2798
    },
    {
        "code": "STAINES",
        "name": "Staines Rail Station",
        "lng": -0.5032,
        "lat": 51.4325
    },
    {
        "code": "BEDFDM",
        "name": "Bedford Rail Station",
        "lng": -0.4794,
        "lat": 52.1362
    },
    {
        "code": "WBYFLET",
        "name": "West Byfleet Rail Station",
        "lng": -0.5055,
        "lat": 51.3392
    },
    {
        "code": "DENHAM",
        "name": "Denham Rail Station",
        "lng": -0.4974,
        "lat": 51.5788
    },
    {
        "code": "PULBRO",
        "name": "Pulborough Rail Station",
        "lng": -0.5166,
        "lat": 50.9574
    },
    {
        "code": "HEMLHMP",
        "name": "Hemel Hempstead Rail Station",
        "lng": -0.4908,
        "lat": 51.7423
    },
    {
        "code": "CLANDON",
        "name": "Clandon Rail Station",
        "lng": -0.5028,
        "lat": 51.264
    },
    {
        "code": "HTRWTM5",
        "name": "Heathrow Terminal 5 Rail Station",
        "lng": -0.4906,
        "lat": 51.4701
    },
    {
        "code": "BESJOHN",
        "name": "Bedford St Johns Rail Station",
        "lng": -0.4675,
        "lat": 52.1295
    },
    {
        "code": "HTRBUS5",
        "name": "Heathrow Airport Terminal 5",
        "lng": -0.4894,
        "lat": 51.4712
    },
    {
        "code": "CTTGHM",
        "name": "Cottingham Rail Station",
        "lng": -0.4064,
        "lat": 53.7816
    },
    {
        "code": "BNTBY",
        "name": "Barnetby Rail Station",
        "lng": -0.4097,
        "lat": 53.5751
    },
    {
        "code": "ADLESTN",
        "name": "Addlestone Rail Station",
        "lng": -0.4845,
        "lat": 51.373
    },
    {
        "code": "RCKMNSW",
        "name": "Rickmansworth Rail Station",
        "lng": -0.4733,
        "lat": 51.6402
    },
    {
        "code": "BYFLANH",
        "name": "Byfleet & New Haw Rail Station",
        "lng": -0.4814,
        "lat": 51.3498
    },
    {
        "code": "NAFERTN",
        "name": "Nafferton Rail Station",
        "lng": -0.3861,
        "lat": 54.0112
    },
    {
        "code": "WDRYTON",
        "name": "West Drayton Rail Station",
        "lng": -0.4722,
        "lat": 51.5101
    },
    {
        "code": "LEAGRVE",
        "name": "Leagrave Rail Station",
        "lng": -0.4585,
        "lat": 51.9052
    },
    {
        "code": "BARWHVN",
        "name": "Barrow Haven Rail Station",
        "lng": -0.393,
        "lat": 53.6974
    },
    {
        "code": "APSLEY",
        "name": "Apsley Rail Station",
        "lng": -0.4629,
        "lat": 51.7325
    },
    {
        "code": "ANGMRNG",
        "name": "Angmering Rail Station",
        "lng": -0.4894,
        "lat": 50.8166
    },
    {
        "code": "ASFDMSX",
        "name": "Ashford (Surrey) Rail Station",
        "lng": -0.4681,
        "lat": 51.4365
    },
    {
        "code": "SLEFD",
        "name": "Sleaford Rail Station",
        "lng": -0.4103,
        "lat": 52.9955
    },
    {
        "code": "HTRWAPT",
        "name": "Heathrow Terminals 1-3 Rail Station",
        "lng": -0.4543,
        "lat": 51.4714
    },
    {
        "code": "WEYBDGB",
        "name": "Weybridge Rail Station",
        "lng": -0.4577,
        "lat": 51.3618
    },
    {
        "code": "WEYBDGE",
        "name": "Weybridge Rail Station",
        "lng": -0.4577,
        "lat": 51.3618
    },
    {
        "code": "HTRWCBS",
        "name": "Heathrow Airport Central Bus Stn (Rail-Air)",
        "lng": -0.4533,
        "lat": 51.4711
    },
    {
        "code": "MTHRNGH",
        "name": "Metheringham Rail Station",
        "lng": -0.3915,
        "lat": 53.1389
    },
    {
        "code": "HTRWTE4",
        "name": "Heathrow Terminal 4 (Rail-Air)",
        "lng": -0.447,
        "lat": 51.4593
    },
    {
        "code": "KLGL",
        "name": "Kings Langley Rail Station",
        "lng": -0.4384,
        "lat": 51.7064
    },
    {
        "code": "HTRWTM4",
        "name": "Heathrow Terminal 4 Rail Station",
        "lng": -0.4455,
        "lat": 51.4583
    },
    {
        "code": "SHEPRTN",
        "name": "Shepperton Rail Station",
        "lng": -0.4468,
        "lat": 51.3968
    },
    {
        "code": "NHOL",
        "name": "New Holland Rail Station",
        "lng": -0.3602,
        "lat": 53.7019
    },
    {
        "code": "WRUISLP",
        "name": "West Ruislip Rail Station",
        "lng": -0.4378,
        "lat": 51.5698
    },
    {
        "code": "RSKNGTN",
        "name": "Ruskington Rail Station",
        "lng": -0.3808,
        "lat": 53.0415
    },
    {
        "code": "BILSHST",
        "name": "Billingshurst Rail Station",
        "lng": -0.4503,
        "lat": 51.0152
    },
    {
        "code": "GOMSHAL",
        "name": "Gomshall Rail Station",
        "lng": -0.4419,
        "lat": 51.2194
    },
    {
        "code": "HULL",
        "name": "Hull Rail Station",
        "lng": -0.3457,
        "lat": 53.7441
    },
    {
        "code": "UHALIFD",
        "name": "Upper Halliford Rail Station",
        "lng": -0.4309,
        "lat": 51.4131
    },
    {
        "code": "HRSLEY",
        "name": "Horsley Rail Station",
        "lng": -0.4354,
        "lat": 51.2793
    },
    {
        "code": "LUTON",
        "name": "Luton Rail Station",
        "lng": -0.414,
        "lat": 51.8823
    },
    {
        "code": "HAYESAH",
        "name": "Hayes & Harlington Rail Station",
        "lng": -0.4207,
        "lat": 51.5031
    },
    {
        "code": "GOXHILL",
        "name": "Goxhill Rail Station",
        "lng": -0.3371,
        "lat": 53.6767
    },
    {
        "code": "HUNMNBY",
        "name": "Hunmanby Rail Station",
        "lng": -0.3146,
        "lat": 54.1739
    },
    {
        "code": "SUNBURY",
        "name": "Sunbury Rail Station",
        "lng": -0.4178,
        "lat": 51.4183
    },
    {
        "code": "EFNGHMJ",
        "name": "Effingham Junction Rail Station",
        "lng": -0.42,
        "lat": 51.2915
    },
    {
        "code": "WONT",
        "name": "Walton-on-Thames Rail Station",
        "lng": -0.4146,
        "lat": 51.3729
    },
    {
        "code": "GORNGBS",
        "name": "Goring-by-Sea Rail Station",
        "lng": -0.4331,
        "lat": 50.8177
    },
    {
        "code": "LUTOAPY",
        "name": "Luton Airport Parkway Rail Station",
        "lng": -0.3959,
        "lat": 51.8724
    },
    {
        "code": "FELTHAM",
        "name": "Feltham Rail Station",
        "lng": -0.4098,
        "lat": 51.4479
    },
    {
        "code": "KMPTNPK",
        "name": "Kempton Park Rail Station",
        "lng": -0.4098,
        "lat": 51.421
    },
    {
        "code": "MKTR",
        "name": "Market Rasen Rail Station",
        "lng": -0.3369,
        "lat": 53.3839
    },
    {
        "code": "THABBEY",
        "name": "Thornton Abbey Rail Station",
        "lng": -0.323,
        "lat": 53.6543
    },
    {
        "code": "WATFJDC",
        "name": "Watford Junction Rail Station",
        "lng": -0.3965,
        "lat": 51.6635
    },
    {
        "code": "WATFDJ",
        "name": "Watford Junction Rail Station",
        "lng": -0.3959,
        "lat": 51.6639
    },
    {
        "code": "SRUISLP",
        "name": "South Ruislip Rail Station",
        "lng": -0.3993,
        "lat": 51.5569
    },
    {
        "code": "WATFDHS",
        "name": "Watford High Street Rail Station",
        "lng": -0.3917,
        "lat": 51.6527
    },
    {
        "code": "FILEY",
        "name": "Filey Rail Station",
        "lng": -0.2938,
        "lat": 54.2099
    },
    {
        "code": "WATFDN",
        "name": "Watford North Rail Station",
        "lng": -0.3899,
        "lat": 51.6757
    },
    {
        "code": "BUSHYDC",
        "name": "Bushey Rail Station",
        "lng": -0.3853,
        "lat": 51.6457
    },
    {
        "code": "CRPNDPK",
        "name": "Carpenders Park Rail Station",
        "lng": -0.3859,
        "lat": 51.6283
    },
    {
        "code": "BUSHEY",
        "name": "Bushey Rail Station",
        "lng": -0.3847,
        "lat": 51.6456
    },
    {
        "code": "GRSTH",
        "name": "Garston (Herts) Rail Station",
        "lng": -0.3817,
        "lat": 51.6866
    },
    {
        "code": "DRNGTOS",
        "name": "Durrington-on-Sea Rail Station",
        "lng": -0.4115,
        "lat": 50.8175
    },
    {
        "code": "HERSHAM",
        "name": "Hersham Rail Station",
        "lng": -0.39,
        "lat": 51.3768
    },
    {
        "code": "CBHMSDA",
        "name": "Cobham & Stoke d'Abernon Rail Station",
        "lng": -0.3893,
        "lat": 51.3181
    },
    {
        "code": "ULCEBY",
        "name": "Ulceby Rail Station",
        "lng": -0.3008,
        "lat": 53.6192
    },
    {
        "code": "STHALL",
        "name": "Southall Rail Station",
        "lng": -0.3786,
        "lat": 51.506
    },
    {
        "code": "BOOKHAM",
        "name": "Bookham Rail Station",
        "lng": -0.384,
        "lat": 51.2887
    },
    {
        "code": "HTCHEND",
        "name": "Hatch End Rail Station",
        "lng": -0.3686,
        "lat": 51.6094
    },
    {
        "code": "HAMPTON",
        "name": "Hampton (London) Rail Station",
        "lng": -0.3721,
        "lat": 51.4159
    },
    {
        "code": "WWRTHNG",
        "name": "West Worthing Rail Station",
        "lng": -0.393,
        "lat": 50.8184
    },
    {
        "code": "BCWD",
        "name": "Bricket Wood Rail Station",
        "lng": -0.3591,
        "lat": 51.7054
    },
    {
        "code": "HRPNDN",
        "name": "Harpenden Rail Station",
        "lng": -0.3515,
        "lat": 51.8146
    },
    {
        "code": "NTHOLTP",
        "name": "Northolt Park Rail Station",
        "lng": -0.3595,
        "lat": 51.5575
    },
    {
        "code": "HEDSTNL",
        "name": "Headstone Lane Rail Station",
        "lng": -0.3572,
        "lat": 51.6026
    },
    {
        "code": "HOUNSLW",
        "name": "Hounslow Rail Station",
        "lng": -0.3623,
        "lat": 51.4619
    },
    {
        "code": "OXSHOTT",
        "name": "Oxshott Rail Station",
        "lng": -0.3624,
        "lat": 51.3364
    },
    {
        "code": "WHTTON",
        "name": "Whitton Rail Station",
        "lng": -0.3577,
        "lat": 51.4496
    },
    {
        "code": "HOWWOOD",
        "name": "How Wood (Herts) Rail Station",
        "lng": -0.3447,
        "lat": 51.7177
    },
    {
        "code": "WORTHNG",
        "name": "Worthing Rail Station",
        "lng": -0.3762,
        "lat": 50.8185
    },
    {
        "code": "STALBNA",
        "name": "St Albans Abbey Rail Station",
        "lng": -0.3426,
        "lat": 51.7447
    },
    {
        "code": "HABRO",
        "name": "Habrough Rail Station",
        "lng": -0.2695,
        "lat": 53.6061
    },
    {
        "code": "HCKNGTN",
        "name": "Heckington Rail Station",
        "lng": -0.2939,
        "lat": 52.9773
    },
    {
        "code": "ESHER",
        "name": "Esher Rail Station",
        "lng": -0.3533,
        "lat": 51.3799
    },
    {
        "code": "PKST",
        "name": "Park Street Rail Station",
        "lng": -0.3403,
        "lat": 51.7255
    },
    {
        "code": "CHRSTSH",
        "name": "Christs Hospital Rail Station",
        "lng": -0.3636,
        "lat": 51.0507
    },
    {
        "code": "GFORD",
        "name": "Greenford Rail Station",
        "lng": -0.3458,
        "lat": 51.5423
    },
    {
        "code": "FULWELL",
        "name": "Fulwell Rail Station",
        "lng": -0.3495,
        "lat": 51.4339
    },
    {
        "code": "CLYGATE",
        "name": "Claygate Rail Station",
        "lng": -0.3482,
        "lat": 51.3612
    },
    {
        "code": "HAROOTH",
        "name": "Harrow-on-the-Hill Rail Station",
        "lng": -0.3372,
        "lat": 51.5792
    },
    {
        "code": "HCRT",
        "name": "Hampton Court Rail Station",
        "lng": -0.3427,
        "lat": 51.4026
    },
    {
        "code": "HANWELL",
        "name": "Hanwell Rail Station",
        "lng": -0.3386,
        "lat": 51.5118
    },
    {
        "code": "HROW",
        "name": "Harrow & Wealdstone Rail Station",
        "lng": -0.3346,
        "lat": 51.5922
    },
    {
        "code": "HROWDC",
        "name": "Harrow & Wealdstone Rail Station",
        "lng": -0.3346,
        "lat": 51.5922
    },
    {
        "code": "SDBRYHH",
        "name": "Sudbury Hill Harrow Rail Station",
        "lng": -0.3358,
        "lat": 51.5585
    },
    {
        "code": "SGFORD",
        "name": "South Greenford Rail Station",
        "lng": -0.3367,
        "lat": 51.5337
    },
    {
        "code": "STRWBYH",
        "name": "Strawberry Hill Rail Station",
        "lng": -0.3394,
        "lat": 51.439
    },
    {
        "code": "STALBCY",
        "name": "St Albans City Rail Station",
        "lng": -0.3275,
        "lat": 51.7505
    },
    {
        "code": "HNCHLYW",
        "name": "Hinchley Wood Rail Station",
        "lng": -0.3405,
        "lat": 51.375
    },
    {
        "code": "ISLEWTH",
        "name": "Isleworth Rail Station",
        "lng": -0.3369,
        "lat": 51.4748
    },
    {
        "code": "TDITTON",
        "name": "Thames Ditton Rail Station",
        "lng": -0.3392,
        "lat": 51.3891
    },
    {
        "code": "CBARPAR",
        "name": "Castle Bar Park Rail Station",
        "lng": -0.3315,
        "lat": 51.5229
    },
    {
        "code": "DRAYGRN",
        "name": "Drayton Green Rail Station",
        "lng": -0.3302,
        "lat": 51.5166
    },
    {
        "code": "EWRTHNG",
        "name": "East Worthing Rail Station",
        "lng": -0.3549,
        "lat": 50.8216
    },
    {
        "code": "DRKGW",
        "name": "Dorking West Rail Station",
        "lng": -0.34,
        "lat": 51.2362
    },
    {
        "code": "TEDNGTN",
        "name": "Teddington Rail Station",
        "lng": -0.3327,
        "lat": 51.4245
    },
    {
        "code": "TWCKNHM",
        "name": "Twickenham Rail Station",
        "lng": -0.3304,
        "lat": 51.45
    },
    {
        "code": "LETHRHD",
        "name": "Leatherhead Rail Station",
        "lng": -0.3332,
        "lat": 51.2988
    },
    {
        "code": "SYONLA",
        "name": "Syon Lane Rail Station",
        "lng": -0.3248,
        "lat": 51.4818
    },
    {
        "code": "RADLETT",
        "name": "Radlett Rail Station",
        "lng": -0.3172,
        "lat": 51.6852
    },
    {
        "code": "OCKLYAC",
        "name": "Ockley Rail Station",
        "lng": -0.336,
        "lat": 51.1515
    },
    {
        "code": "WEALING",
        "name": "West Ealing Rail Station",
        "lng": -0.3201,
        "lat": 51.5135
    },
    {
        "code": "KTON",
        "name": "Kenton Rail Station",
        "lng": -0.317,
        "lat": 51.5818
    },
    {
        "code": "BOXHAWH",
        "name": "Box Hill & Westhumble Rail Station",
        "lng": -0.3285,
        "lat": 51.254
    },
    {
        "code": "STMGTS",
        "name": "St Margarets (London) Rail Station",
        "lng": -0.3202,
        "lat": 51.4552
    },
    {
        "code": "SDBRYHR",
        "name": "Sudbury & Harrow Road Rail Station",
        "lng": -0.3155,
        "lat": 51.5544
    },
    {
        "code": "DEPDENE",
        "name": "Dorking Deepdene Rail Station",
        "lng": -0.3246,
        "lat": 51.2388
    },
    {
        "code": "DORKING",
        "name": "Dorking Rail Station",
        "lng": -0.3243,
        "lat": 51.2409
    },
    {
        "code": "WARNHAM",
        "name": "Warnham Rail Station",
        "lng": -0.3295,
        "lat": 51.0929
    },
    {
        "code": "SKENTON",
        "name": "South Kenton Rail Station",
        "lng": -0.3085,
        "lat": 51.5702
    },
    {
        "code": "HAMWICK",
        "name": "Hampton Wick Rail Station",
        "lng": -0.3125,
        "lat": 51.4145
    },
    {
        "code": "BNTFORD",
        "name": "Brentford Rail Station",
        "lng": -0.3097,
        "lat": 51.4875
    },
    {
        "code": "HLMW",
        "name": "Holmwood Rail Station",
        "lng": -0.3208,
        "lat": 51.1812
    },
    {
        "code": "NWEMBLY",
        "name": "North Wembley Rail Station",
        "lng": -0.304,
        "lat": 51.5626
    },
    {
        "code": "SNDY",
        "name": "Sandy Rail Station",
        "lng": -0.2812,
        "lat": 52.1247
    },
    {
        "code": "HORSHAM",
        "name": "Horsham Rail Station",
        "lng": -0.3193,
        "lat": 51.0661
    },
    {
        "code": "CHSSS",
        "name": "Chessington South Rail Station",
        "lng": -0.3082,
        "lat": 51.3565
    },
    {
        "code": "BRDLNGT",
        "name": "Bridlington Rail Station",
        "lng": -0.1987,
        "lat": 54.0841
    },
    {
        "code": "EALINGB",
        "name": "Ealing Broadway Rail Station",
        "lng": -0.3018,
        "lat": 51.5148
    },
    {
        "code": "ASHD",
        "name": "Ashtead Rail Station",
        "lng": -0.3076,
        "lat": 51.3179
    },
    {
        "code": "RICHMND",
        "name": "Richmond (London) Rail Station",
        "lng": -0.3016,
        "lat": 51.4631
    },
    {
        "code": "RICHNLL",
        "name": "Richmond NLL Rail Station",
        "lng": -0.3014,
        "lat": 51.4631
    },
    {
        "code": "SURBITN",
        "name": "Surbiton Rail Station",
        "lng": -0.304,
        "lat": 51.3925
    },
    {
        "code": "LNCG",
        "name": "Lancing Rail Station",
        "lng": -0.3231,
        "lat": 50.8271
    },
    {
        "code": "WMBY",
        "name": "Wembley Central Rail Station",
        "lng": -0.2964,
        "lat": 51.5523
    },
    {
        "code": "WMBYDC",
        "name": "Wembley Central Rail Station",
        "lng": -0.2964,
        "lat": 51.5523
    },
    {
        "code": "KGSTON",
        "name": "Kingston Rail Station",
        "lng": -0.3012,
        "lat": 51.4127
    },
    {
        "code": "CHSSN",
        "name": "Chessington North Rail Station",
        "lng": -0.3007,
        "lat": 51.364
    },
    {
        "code": "LHVN",
        "name": "Littlehaven Rail Station",
        "lng": -0.308,
        "lat": 51.0797
    },
    {
        "code": "PBRO",
        "name": "Peterborough Rail Station",
        "lng": -0.2498,
        "lat": 52.575
    },
    {
        "code": "WEMBLSM",
        "name": "Wembley Stadium Rail Station",
        "lng": -0.2856,
        "lat": 51.5544
    },
    {
        "code": "BEMPTON",
        "name": "Bempton Rail Station",
        "lng": -0.1805,
        "lat": 54.1277
    },
    {
        "code": "KEWBDGE",
        "name": "Kew Bridge Rail Station",
        "lng": -0.2871,
        "lat": 51.4895
    },
    {
        "code": "NSHEEN",
        "name": "North Sheen Rail Station",
        "lng": -0.2879,
        "lat": 51.4652
    },
    {
        "code": "ARLSEY",
        "name": "Arlesey Rail Station",
        "lng": -0.2663,
        "lat": 52.026
    },
    {
        "code": "ELTR",
        "name": "Elstree & Borehamwood Rail Station",
        "lng": -0.2801,
        "lat": 51.6531
    },
    {
        "code": "KEWGRDN",
        "name": "Kew Gardens Rail Station",
        "lng": -0.2851,
        "lat": 51.4771
    },
    {
        "code": "BIGLSWD",
        "name": "Biggleswade Rail Station",
        "lng": -0.2612,
        "lat": 52.0847
    },
    {
        "code": "HITCHIN",
        "name": "Hitchin Rail Station",
        "lng": -0.2635,
        "lat": 51.9533
    },
    {
        "code": "NRBITON",
        "name": "Norbiton Rail Station",
        "lng": -0.284,
        "lat": 51.4124
    },
    {
        "code": "STNBGPK",
        "name": "Stonebridge Park Rail Station",
        "lng": -0.2758,
        "lat": 51.5441
    },
    {
        "code": "BRLANDS",
        "name": "Berrylands Rail Station",
        "lng": -0.2807,
        "lat": 51.399
    },
    {
        "code": "STNEOTS",
        "name": "St Neots Rail Station",
        "lng": -0.2474,
        "lat": 52.2316
    },
    {
        "code": "GNRSBRY",
        "name": "Gunnersbury Rail Station",
        "lng": -0.2753,
        "lat": 51.4917
    },
    {
        "code": "TOLWTH",
        "name": "Tolworth Rail Station",
        "lng": -0.2795,
        "lat": 51.3769
    },
    {
        "code": "SACTON",
        "name": "South Acton Rail Station",
        "lng": -0.2702,
        "lat": 51.4997
    },
    {
        "code": "SBROUGH",
        "name": "Stallingborough Rail Station",
        "lng": -0.1837,
        "lat": 53.5871
    },
    {
        "code": "ACTONML",
        "name": "Acton Main Line Rail Station",
        "lng": -0.2668,
        "lat": 51.5172
    },
    {
        "code": "CHISWCK",
        "name": "Chiswick Rail Station",
        "lng": -0.2678,
        "lat": 51.4811
    },
    {
        "code": "MRTLKE",
        "name": "Mortlake Rail Station",
        "lng": -0.2671,
        "lat": 51.4681
    },
    {
        "code": "ACTNCTL",
        "name": "Acton Central Rail Station",
        "lng": -0.263,
        "lat": 51.5087
    },
    {
        "code": "EPSM",
        "name": "Epsom Rail Station",
        "lng": -0.2688,
        "lat": 51.3344
    },
    {
        "code": "HARLSDN",
        "name": "Harlesden Rail Station",
        "lng": -0.2577,
        "lat": 51.5363
    },
    {
        "code": "BTCHWTH",
        "name": "Betchworth Rail Station",
        "lng": -0.267,
        "lat": 51.2482
    },
    {
        "code": "MALDENM",
        "name": "Malden Manor Rail Station",
        "lng": -0.2613,
        "lat": 51.3847
    },
    {
        "code": "MLHB",
        "name": "Mill Hill Broadway Rail Station",
        "lng": -0.2492,
        "lat": 51.6131
    },
    {
        "code": "NEWMLDN",
        "name": "New Malden Rail Station",
        "lng": -0.2559,
        "lat": 51.4041
    },
    {
        "code": "BNSBDGE",
        "name": "Barnes Bridge Rail Station",
        "lng": -0.2526,
        "lat": 51.472
    },
    {
        "code": "EWELW",
        "name": "Ewell West Rail Station",
        "lng": -0.257,
        "lat": 51.35
    },
    {
        "code": "LTCE",
        "name": "Letchworth Rail Station",
        "lng": -0.2293,
        "lat": 51.98
    },
    {
        "code": "FAYGATE",
        "name": "Faygate Rail Station",
        "lng": -0.263,
        "lat": 51.0959
    },
    {
        "code": "SHRHMBS",
        "name": "Shoreham-by-Sea (Sussex) Rail Station",
        "lng": -0.2717,
        "lat": 50.8344
    },
    {
        "code": "SWSHEAD",
        "name": "Swineshead Rail Station",
        "lng": -0.1872,
        "lat": 52.9698
    },
    {
        "code": "WLSDJHL",
        "name": "Willesden Junction Rail Station",
        "lng": -0.2445,
        "lat": 51.5325
    },
    {
        "code": "HEALING",
        "name": "Healing Rail Station",
        "lng": -0.1606,
        "lat": 53.5818
    },
    {
        "code": "WLSDNJL",
        "name": "Willesden Junction Low Level Rail Station",
        "lng": -0.2433,
        "lat": 51.532
    },
    {
        "code": "STLEIGH",
        "name": "Stoneleigh Rail Station",
        "lng": -0.2487,
        "lat": 51.3634
    },
    {
        "code": "HDON",
        "name": "Hendon Rail Station",
        "lng": -0.2387,
        "lat": 51.5801
    },
    {
        "code": "BARNES",
        "name": "Barnes Rail Station",
        "lng": -0.2422,
        "lat": 51.4671
    },
    {
        "code": "WRCSTRP",
        "name": "Worcester Park Rail Station",
        "lng": -0.2452,
        "lat": 51.3813
    },
    {
        "code": "EWELLE",
        "name": "Ewell East Rail Station",
        "lng": -0.2415,
        "lat": 51.3453
    },
    {
        "code": "MOTSPRP",
        "name": "Motspur Park Rail Station",
        "lng": -0.2395,
        "lat": 51.3952
    },
    {
        "code": "TATNHMC",
        "name": "Tattenham Corner Rail Station",
        "lng": -0.2426,
        "lat": 51.3092
    },
    {
        "code": "EPSDNS",
        "name": "Epsom Downs Rail Station",
        "lng": -0.239,
        "lat": 51.3237
    },
    {
        "code": "TADWTH",
        "name": "Tadworth Rail Station",
        "lng": -0.236,
        "lat": 51.2916
    },
    {
        "code": "RAYNSPK",
        "name": "Raynes Park Rail Station",
        "lng": -0.2302,
        "lat": 51.4092
    },
    {
        "code": "KENSLG",
        "name": "Kensal Green Rail Station",
        "lng": -0.2251,
        "lat": 51.5305
    },
    {
        "code": "HATFILD",
        "name": "Hatfield (Herts) Rail Station",
        "lng": -0.2156,
        "lat": 51.7639
    },
    {
        "code": "HNTNGDN",
        "name": "Huntingdon Rail Station",
        "lng": -0.1921,
        "lat": 52.3286
    },
    {
        "code": "STEVNGE",
        "name": "Stevenage Rail Station",
        "lng": -0.2071,
        "lat": 51.9017
    },
    {
        "code": "KENR",
        "name": "Kensal Rise Rail Station",
        "lng": -0.22,
        "lat": 51.5346
    },
    {
        "code": "WELHAMG",
        "name": "Welham Green Rail Station",
        "lng": -0.2107,
        "lat": 51.7364
    },
    {
        "code": "SHPDSB",
        "name": "Shepherds Bush Rail Station",
        "lng": -0.2177,
        "lat": 51.5053
    },
    {
        "code": "GTCOATS",
        "name": "Great Coates Rail Station",
        "lng": -0.1302,
        "lat": 53.5758
    },
    {
        "code": "WLWYNGC",
        "name": "Welwyn Garden City Rail Station",
        "lng": -0.2041,
        "lat": 51.801
    },
    {
        "code": "CRKLWD",
        "name": "Cricklewood Rail Station",
        "lng": -0.2127,
        "lat": 51.5585
    },
    {
        "code": "PUTNEY",
        "name": "Putney Rail Station",
        "lng": -0.2165,
        "lat": 51.4613
    },
    {
        "code": "BRKMNPK",
        "name": "Brookmans Park Rail Station",
        "lng": -0.2045,
        "lat": 51.7211
    },
    {
        "code": "BRBYPK",
        "name": "Brondesbury Park Rail Station",
        "lng": -0.2101,
        "lat": 51.5407
    },
    {
        "code": "WIMLCHS",
        "name": "Wimbledon Chase Rail Station",
        "lng": -0.214,
        "lat": 51.4096
    },
    {
        "code": "STHWICK",
        "name": "Southwick Rail Station",
        "lng": -0.236,
        "lat": 50.8325
    },
    {
        "code": "KENOLYM",
        "name": "Kensington (Olympia) Rail Station",
        "lng": -0.2104,
        "lat": 51.4979
    },
    {
        "code": "SPALDNG",
        "name": "Spalding Rail Station",
        "lng": -0.1569,
        "lat": 52.7888
    },
    {
        "code": "CHEAM",
        "name": "Cheam Rail Station",
        "lng": -0.2142,
        "lat": 51.3555
    },
    {
        "code": "BALDOCK",
        "name": "Baldock Rail Station",
        "lng": -0.1876,
        "lat": 51.9929
    },
    {
        "code": "BANSTED",
        "name": "Banstead Rail Station",
        "lng": -0.2132,
        "lat": 51.3293
    },
    {
        "code": "QPRK",
        "name": "Queens Park (London) Rail Station",
        "lng": -0.205,
        "lat": 51.534
    },
    {
        "code": "WLWYNN",
        "name": "Welwyn North Rail Station",
        "lng": -0.1921,
        "lat": 51.8235
    },
    {
        "code": "BRBY",
        "name": "Brondesbury Rail Station",
        "lng": -0.2023,
        "lat": 51.5452
    },
    {
        "code": "WIMBLDN",
        "name": "Wimbledon Rail Station",
        "lng": -0.2064,
        "lat": 51.4213
    },
    {
        "code": "WDON",
        "name": "Wimbledon Rail Station",
        "lng": -0.2064,
        "lat": 51.4213
    },
    {
        "code": "KGWD",
        "name": "Kingswood Rail Station",
        "lng": -0.2112,
        "lat": 51.2947
    },
    {
        "code": "KNEBWTH",
        "name": "Knebworth Rail Station",
        "lng": -0.1873,
        "lat": 51.8669
    },
    {
        "code": "SMERTON",
        "name": "South Merton Rail Station",
        "lng": -0.2052,
        "lat": 51.403
    },
    {
        "code": "POTRSBR",
        "name": "Potters Bar Rail Station",
        "lng": -0.1926,
        "lat": 51.6971
    },
    {
        "code": "WSUTTON",
        "name": "West Sutton Rail Station",
        "lng": -0.2052,
        "lat": 51.3659
    },
    {
        "code": "IFIELD",
        "name": "Ifield Rail Station",
        "lng": -0.2148,
        "lat": 51.1156
    },
    {
        "code": "MORDENS",
        "name": "Morden South Rail Station",
        "lng": -0.1995,
        "lat": 51.3961
    },
    {
        "code": "WBRMPTN",
        "name": "West Brompton Rail Station",
        "lng": -0.1956,
        "lat": 51.4871
    },
    {
        "code": "SHLIER",
        "name": "St Helier (London) Rail Station",
        "lng": -0.1988,
        "lat": 51.3899
    },
    {
        "code": "WHMPSTM",
        "name": "West Hampstead Thameslink Rail Station",
        "lng": -0.1918,
        "lat": 51.5485
    },
    {
        "code": "KLBRNHR",
        "name": "Kilburn High Road Rail Station",
        "lng": -0.1922,
        "lat": 51.5373
    },
    {
        "code": "REIGATE",
        "name": "Reigate Rail Station",
        "lng": -0.2038,
        "lat": 51.242
    },
    {
        "code": "FSHRSGT",
        "name": "Fishersgate Rail Station",
        "lng": -0.2194,
        "lat": 50.8342
    },
    {
        "code": "WHMDSTD",
        "name": "West Hampstead Rail Station",
        "lng": -0.1912,
        "lat": 51.5475
    },
    {
        "code": "BELM",
        "name": "Belmont Rail Station",
        "lng": -0.1989,
        "lat": 51.3438
    },
    {
        "code": "SUTTONC",
        "name": "Sutton Common Rail Station",
        "lng": -0.1963,
        "lat": 51.3749
    },
    {
        "code": "WDWTOWN",
        "name": "Wandsworth Town Rail Station",
        "lng": -0.1881,
        "lat": 51.461
    },
    {
        "code": "HYDNSRD",
        "name": "Haydons Road Rail Station",
        "lng": -0.1888,
        "lat": 51.4254
    },
    {
        "code": "SUTTON",
        "name": "Sutton (London) Rail Station",
        "lng": -0.1912,
        "lat": 51.3595
    },
    {
        "code": "ERLFLD",
        "name": "Earlsfield Rail Station",
        "lng": -0.1877,
        "lat": 51.4423
    },
    {
        "code": "FNCHLYR",
        "name": "Finchley Road & Frognal Rail Station",
        "lng": -0.1831,
        "lat": 51.5503
    },
    {
        "code": "HADLYWD",
        "name": "Hadley Wood Rail Station",
        "lng": -0.1762,
        "lat": 51.6685
    },
    {
        "code": "CSEAH",
        "name": "Imperial Wharf Rail Station",
        "lng": -0.1828,
        "lat": 51.4749
    },
    {
        "code": "SHMPSTD",
        "name": "South Hampstead Rail Station",
        "lng": -0.1789,
        "lat": 51.5414
    },
    {
        "code": "PSLDAWH",
        "name": "Portslade Rail Station",
        "lng": -0.2053,
        "lat": 50.8357
    },
    {
        "code": "NBARNET",
        "name": "New Barnet Rail Station",
        "lng": -0.173,
        "lat": 51.6486
    },
    {
        "code": "PADTON",
        "name": "London Paddington Rail Station",
        "lng": -0.1762,
        "lat": 51.516
    },
    {
        "code": "GRMSBYT",
        "name": "Grimsby Town Rail Station",
        "lng": -0.087,
        "lat": 53.5634
    },
    {
        "code": "HBRTBDG",
        "name": "Hubberts Bridge Rail Station",
        "lng": -0.1105,
        "lat": 52.9754
    },
    {
        "code": "OKLGHPK",
        "name": "Oakleigh Park Rail Station",
        "lng": -0.1662,
        "lat": 51.6377
    },
    {
        "code": "CRAWLEY",
        "name": "Crawley Rail Station",
        "lng": -0.1867,
        "lat": 51.1122
    },
    {
        "code": "CLPHMJ2",
        "name": "Clapham Junction Rail Station",
        "lng": -0.1703,
        "lat": 51.4642
    },
    {
        "code": "CLPHMJC",
        "name": "Clapham Junction Rail Station",
        "lng": -0.1703,
        "lat": 51.4642
    },
    {
        "code": "CLPHMJM",
        "name": "Clapham Junction Rail Station",
        "lng": -0.1703,
        "lat": 51.4642
    },
    {
        "code": "CLPHMJW",
        "name": "Clapham Junction Rail Station",
        "lng": -0.1703,
        "lat": 51.4642
    },
    {
        "code": "CLPHMJ1",
        "name": "Clapham Junction Rail Station",
        "lng": -0.1702,
        "lat": 51.4642
    },
    {
        "code": "HMPSTDH",
        "name": "Hampstead Heath Rail Station",
        "lng": -0.1657,
        "lat": 51.5552
    },
    {
        "code": "GRMSBYD",
        "name": "Grimsby Docks Rail Station",
        "lng": -0.0756,
        "lat": 53.5743
    },
    {
        "code": "CRSHLTB",
        "name": "Carshalton Beeches Rail Station",
        "lng": -0.1698,
        "lat": 51.3574
    },
    {
        "code": "MARYLBN",
        "name": "London Marylebone Rail Station",
        "lng": -0.1629,
        "lat": 51.5225
    },
    {
        "code": "WHTLSEA",
        "name": "Whittlesea Rail Station",
        "lng": -0.119,
        "lat": 52.5495
    },
    {
        "code": "CHSD",
        "name": "Chipstead Rail Station",
        "lng": -0.1695,
        "lat": 51.3093
    },
    {
        "code": "WANDCMN",
        "name": "Wandsworth Common Rail Station",
        "lng": -0.1634,
        "lat": 51.4462
    },
    {
        "code": "CRSHLTN",
        "name": "Carshalton Rail Station",
        "lng": -0.1664,
        "lat": 51.3685
    },
    {
        "code": "EARLSWD",
        "name": "Earlswood (Surrey) Rail Station",
        "lng": -0.1708,
        "lat": 51.2273
    },
    {
        "code": "TOOTING",
        "name": "Tooting Rail Station",
        "lng": -0.1613,
        "lat": 51.4198
    },
    {
        "code": "ALDTON",
        "name": "Aldrington Rail Station",
        "lng": -0.1838,
        "lat": 50.8364
    },
    {
        "code": "REDHILL",
        "name": "Redhill Rail Station",
        "lng": -0.1659,
        "lat": 51.2402
    },
    {
        "code": "MITCHMJ",
        "name": "Mitcham Junction Rail Station",
        "lng": -0.1578,
        "lat": 51.3929
    },
    {
        "code": "GOSPLOK",
        "name": "Gospel Oak Rail Station",
        "lng": -0.1508,
        "lat": 51.5553
    },
    {
        "code": "ESTFLDS",
        "name": "Mitcham Eastfields Rail Station",
        "lng": -0.1546,
        "lat": 51.4077
    },
    {
        "code": "SALFDS",
        "name": "Salfords (Surrey) Rail Station",
        "lng": -0.1625,
        "lat": 51.2017
    },
    {
        "code": "BALHAM",
        "name": "Balham Rail Station",
        "lng": -0.1524,
        "lat": 51.4432
    },
    {
        "code": "NEWCLEE",
        "name": "New Clee Rail Station",
        "lng": -0.0608,
        "lat": 53.5744
    },
    {
        "code": "HKBG",
        "name": "Hackbridge Rail Station",
        "lng": -0.1539,
        "lat": 51.3779
    },
    {
        "code": "KNTSHTW",
        "name": "Kentish Town West Rail Station",
        "lng": -0.1467,
        "lat": 51.5465
    },
    {
        "code": "HORLEY",
        "name": "Horley Rail Station",
        "lng": -0.1611,
        "lat": 51.1688
    },
    {
        "code": "NEWSGAT",
        "name": "New Southgate Rail Station",
        "lng": -0.143,
        "lat": 51.6141
    },
    {
        "code": "GTWK",
        "name": "Gatwick Airport Rail Station",
        "lng": -0.161,
        "lat": 51.1565
    },
    {
        "code": "WDMNSTR",
        "name": "Woodmansterne Rail Station",
        "lng": -0.1543,
        "lat": 51.319
    },
    {
        "code": "BATRSPK",
        "name": "Battersea Park Rail Station",
        "lng": -0.1475,
        "lat": 51.477
    },
    {
        "code": "THBDGS",
        "name": "Three Bridges Rail Station",
        "lng": -0.1612,
        "lat": 51.1169
    },
    {
        "code": "QTRDBAT",
        "name": "Queenstown Road (Battersea) Rail Station",
        "lng": -0.1467,
        "lat": 51.475
    },
    {
        "code": "WALNGTN",
        "name": "Wallington Rail Station",
        "lng": -0.1508,
        "lat": 51.3604
    },
    {
        "code": "VICTRIC",
        "name": "London Victoria Rail Station",
        "lng": -0.1446,
        "lat": 51.4953
    },
    {
        "code": "VICTRIE",
        "name": "London Victoria Rail Station",
        "lng": -0.1445,
        "lat": 51.4953
    },
    {
        "code": "HOVE",
        "name": "Hove Rail Station",
        "lng": -0.1707,
        "lat": 50.8352
    },
    {
        "code": "KNTSHTN",
        "name": "Kentish Town Rail Station",
        "lng": -0.1404,
        "lat": 51.5505
    },
    {
        "code": "MERSTHM",
        "name": "Merstham Rail Station",
        "lng": -0.1502,
        "lat": 51.2642
    },
    {
        "code": "CMDNRD",
        "name": "Camden Road Rail Station",
        "lng": -0.1387,
        "lat": 51.5418
    },
    {
        "code": "WNDSWRD",
        "name": "Wandsworth Road Rail Station",
        "lng": -0.1385,
        "lat": 51.4702
    },
    {
        "code": "EUSTON",
        "name": "London Euston Rail Station",
        "lng": -0.1339,
        "lat": 51.5281
    },
    {
        "code": "WATONAS",
        "name": "Watton-at-Stone Rail Station",
        "lng": -0.1194,
        "lat": 51.8564
    },
    {
        "code": "STRHCOM",
        "name": "Streatham Common Rail Station",
        "lng": -0.136,
        "lat": 51.4187
    },
    {
        "code": "UPRHLWY",
        "name": "Upper Holloway Rail Station",
        "lng": -0.1295,
        "lat": 51.5636
    },
    {
        "code": "ASHWELC",
        "name": "Ashwell & Morden Rail Station",
        "lng": -0.1098,
        "lat": 52.0308
    },
    {
        "code": "CLPHHS",
        "name": "Clapham High Street Rail Station",
        "lng": -0.1325,
        "lat": 51.4655
    },
    {
        "code": "COLSDNS",
        "name": "Coulsdon South Rail Station",
        "lng": -0.1379,
        "lat": 51.3158
    },
    {
        "code": "PRSP",
        "name": "Preston Park Rail Station",
        "lng": -0.1552,
        "lat": 50.8459
    },
    {
        "code": "STPXBOX",
        "name": "London St Pancras International LL Rail Station",
        "lng": -0.1273,
        "lat": 51.5322
    },
    {
        "code": "STPX",
        "name": "London St Pancras International Rail Station",
        "lng": -0.1272,
        "lat": 51.5324
    },
    {
        "code": "STRETHM",
        "name": "Streatham Rail Station",
        "lng": -0.1316,
        "lat": 51.4258
    },
    {
        "code": "STPADOM",
        "name": "London St Pancras International Rail Station",
        "lng": -0.1265,
        "lat": 51.5325
    },
    {
        "code": "COLSTWN",
        "name": "Coulsdon Town Rail Station",
        "lng": -0.1345,
        "lat": 51.322
    },
    {
        "code": "CHRX",
        "name": "London Charing Cross Rail Station",
        "lng": -0.1248,
        "lat": 51.508
    },
    {
        "code": "BOWESPK",
        "name": "Bowes Park Rail Station",
        "lng": -0.1206,
        "lat": 51.607
    },
    {
        "code": "STRHILL",
        "name": "Streatham Hill Rail Station",
        "lng": -0.1272,
        "lat": 51.4382
    },
    {
        "code": "ALEXNDP",
        "name": "Alexandra Palace Rail Station",
        "lng": -0.1202,
        "lat": 51.5979
    },
    {
        "code": "KNGX",
        "name": "London Kings Cross Rail Station",
        "lng": -0.1229,
        "lat": 51.5309
    },
    {
        "code": "HASOCKS",
        "name": "Hassocks Rail Station",
        "lng": -0.146,
        "lat": 50.9246
    },
    {
        "code": "VAUXHLM",
        "name": "Vauxhall Rail Station",
        "lng": -0.1229,
        "lat": 51.4862
    },
    {
        "code": "VAUXHLW",
        "name": "Vauxhall Rail Station",
        "lng": -0.1229,
        "lat": 51.4862
    },
    {
        "code": "NUTFILD",
        "name": "Nutfield Rail Station",
        "lng": -0.1325,
        "lat": 51.2268
    },
    {
        "code": "CROUCHH",
        "name": "Crouch Hill Rail Station",
        "lng": -0.1171,
        "lat": 51.5713
    },
    {
        "code": "CLTHRPS",
        "name": "Cleethorpes Rail Station",
        "lng": -0.0292,
        "lat": 53.5619
    },
    {
        "code": "BALCOMB",
        "name": "Balcombe Rail Station",
        "lng": -0.1369,
        "lat": 51.0555
    },
    {
        "code": "CLDNNRB",
        "name": "Caledonian Road & Barnsbury Rail Station",
        "lng": -0.1167,
        "lat": 51.543
    },
    {
        "code": "CUFFLEY",
        "name": "Cuffley Rail Station",
        "lng": -0.1098,
        "lat": 51.7087
    },
    {
        "code": "NORBURY",
        "name": "Norbury Rail Station",
        "lng": -0.1219,
        "lat": 51.4114
    },
    {
        "code": "REEDHMS",
        "name": "Reedham (Surrey) Rail Station",
        "lng": -0.1234,
        "lat": 51.3311
    },
    {
        "code": "HRNSY",
        "name": "Hornsey Rail Station",
        "lng": -0.112,
        "lat": 51.5865
    },
    {
        "code": "PALMRSG",
        "name": "Palmers Green Rail Station",
        "lng": -0.1104,
        "lat": 51.6183
    },
    {
        "code": "CRHL",
        "name": "Crews Hill Rail Station",
        "lng": -0.1069,
        "lat": 51.6845
    },
    {
        "code": "BRGHTN",
        "name": "Brighton Rail Station",
        "lng": -0.1413,
        "lat": 50.829
    },
    {
        "code": "WATRLMN",
        "name": "London Waterloo Rail Station",
        "lng": -0.1131,
        "lat": 51.5033
    },
    {
        "code": "BRIXTON",
        "name": "Brixton Rail Station",
        "lng": -0.1142,
        "lat": 51.4633
    },
    {
        "code": "WADDON",
        "name": "Waddon Rail Station",
        "lng": -0.1173,
        "lat": 51.3674
    },
    {
        "code": "BRGHLRD",
        "name": "London Road (Brighton) Rail Station",
        "lng": -0.1365,
        "lat": 50.8367
    },
    {
        "code": "WLOE",
        "name": "London Waterloo East Rail Station",
        "lng": -0.1089,
        "lat": 51.5041
    },
    {
        "code": "FNPK",
        "name": "Finsbury Park Rail Station",
        "lng": -0.1063,
        "lat": 51.5643
    },
    {
        "code": "HRGY",
        "name": "Harringay Rail Station",
        "lng": -0.1051,
        "lat": 51.5774
    },
    {
        "code": "DRYP",
        "name": "Drayton Park Rail Station",
        "lng": -0.1055,
        "lat": 51.5528
    },
    {
        "code": "PURLEY",
        "name": "Purley Rail Station",
        "lng": -0.114,
        "lat": 51.3376
    },
    {
        "code": "WNMHILL",
        "name": "Winchmore Hill Rail Station",
        "lng": -0.1009,
        "lat": 51.6339
    },
    {
        "code": "BAYFORD",
        "name": "Bayford Rail Station",
        "lng": -0.0956,
        "lat": 51.7577
    },
    {
        "code": "FRNDNLT",
        "name": "Farringdon (London) Rail Station",
        "lng": -0.1052,
        "lat": 51.5202
    },
    {
        "code": "HGHI",
        "name": "Highbury & Islington Rail Station",
        "lng": -0.1038,
        "lat": 51.5462
    },
    {
        "code": "HIGHBYA",
        "name": "Highbury & Islington Rail Station",
        "lng": -0.1038,
        "lat": 51.5461
    },
    {
        "code": "BURGESH",
        "name": "Burgess Hill Rail Station",
        "lng": -0.1274,
        "lat": 50.9537
    },
    {
        "code": "HFDN",
        "name": "Hertford North Rail Station",
        "lng": -0.0918,
        "lat": 51.7989
    },
    {
        "code": "CTMSLNK",
        "name": "City Thameslink Rail Station",
        "lng": -0.1036,
        "lat": 51.5139
    },
    {
        "code": "BLFR",
        "name": "London Blackfriars Rail Station",
        "lng": -0.1033,
        "lat": 51.5118
    },
    {
        "code": "GRPK",
        "name": "Grange Park Rail Station",
        "lng": -0.0974,
        "lat": 51.6426
    },
    {
        "code": "TULSEH",
        "name": "Tulse Hill Rail Station",
        "lng": -0.1051,
        "lat": 51.4399
    },
    {
        "code": "GORDONH",
        "name": "Gordon Hill Rail Station",
        "lng": -0.0946,
        "lat": 51.6633
    },
    {
        "code": "HRGYGL",
        "name": "Harringay Green Lanes Rail Station",
        "lng": -0.0981,
        "lat": 51.5772
    },
    {
        "code": "WNORWOD",
        "name": "West Norwood Rail Station",
        "lng": -0.1038,
        "lat": 51.4317
    },
    {
        "code": "LBGHJN",
        "name": "Loughborough Junction Rail Station",
        "lng": -0.1022,
        "lat": 51.4663
    },
    {
        "code": "HERNEH",
        "name": "Herne Hill Rail Station",
        "lng": -0.1023,
        "lat": 51.4533
    },
    {
        "code": "WVLSFLD",
        "name": "Wivelsfield Rail Station",
        "lng": -0.1208,
        "lat": 50.9643
    },
    {
        "code": "ELPHNAC",
        "name": "Elephant & Castle Rail Station",
        "lng": -0.0987,
        "lat": 51.494
    },
    {
        "code": "ESSEXRD",
        "name": "Essex Road Rail Station",
        "lng": -0.0963,
        "lat": 51.5407
    },
    {
        "code": "WCROYDN",
        "name": "West Croydon Rail Station",
        "lng": -0.1026,
        "lat": 51.3784
    },
    {
        "code": "ENFC",
        "name": "Enfield Chase Rail Station",
        "lng": -0.0907,
        "lat": 51.6533
    },
    {
        "code": "THTH",
        "name": "Thornton Heath Rail Station",
        "lng": -0.1003,
        "lat": 51.3988
    },
    {
        "code": "BOSTON",
        "name": "Boston Rail Station",
        "lng": -0.031,
        "lat": 52.9781
    },
    {
        "code": "CNNB",
        "name": "Canonbury Rail Station",
        "lng": -0.0922,
        "lat": 51.5487
    },
    {
        "code": "KNLY",
        "name": "Kenley Rail Station",
        "lng": -0.1009,
        "lat": 51.3248
    },
    {
        "code": "PURLEYO",
        "name": "Purley Oaks Rail Station",
        "lng": -0.0989,
        "lat": 51.347
    },
    {
        "code": "RDLSDWN",
        "name": "Riddlesdown Rail Station",
        "lng": -0.0994,
        "lat": 51.3325
    },
    {
        "code": "MLSECMB",
        "name": "Moulsecoomb Rail Station",
        "lng": -0.1188,
        "lat": 50.8467
    },
    {
        "code": "CANONST",
        "name": "London Cannon Street Rail Station",
        "lng": -0.0903,
        "lat": 51.5114
    },
    {
        "code": "MRGT",
        "name": "Moorgate Rail Station",
        "lng": -0.0889,
        "lat": 51.5185
    },
    {
        "code": "OLDST",
        "name": "Old Street Rail Station",
        "lng": -0.0885,
        "lat": 51.5258
    },
    {
        "code": "WDULWCH",
        "name": "West Dulwich Rail Station",
        "lng": -0.0914,
        "lat": 51.4407
    },
    {
        "code": "DENMRKH",
        "name": "Denmark Hill Rail Station",
        "lng": -0.0894,
        "lat": 51.4682
    },
    {
        "code": "SCROYDN",
        "name": "South Croydon Rail Station",
        "lng": -0.0935,
        "lat": 51.363
    },
    {
        "code": "ECROYDN",
        "name": "East Croydon Rail Station",
        "lng": -0.0928,
        "lat": 51.3755
    },
    {
        "code": "SDSD",
        "name": "Sanderstead Rail Station",
        "lng": -0.0937,
        "lat": 51.3483
    },
    {
        "code": "LNDNBDC",
        "name": "London Bridge Rail Station",
        "lng": -0.0861,
        "lat": 51.505
    },
    {
        "code": "LNDNBDE",
        "name": "London Bridge Rail Station",
        "lng": -0.0861,
        "lat": 51.5051
    },
    {
        "code": "NDULWCH",
        "name": "North Dulwich Rail Station",
        "lng": -0.0879,
        "lat": 51.4545
    },
    {
        "code": "ENFLDTN",
        "name": "Enfield Town Rail Station",
        "lng": -0.0793,
        "lat": 51.652
    },
    {
        "code": "HERTFDE",
        "name": "Hertford East Rail Station",
        "lng": -0.0729,
        "lat": 51.799
    },
    {
        "code": "HYWRDSH",
        "name": "Haywards Heath Rail Station",
        "lng": -0.1051,
        "lat": 51.0057
    },
    {
        "code": "SELHRST",
        "name": "Selhurst Rail Station",
        "lng": -0.0883,
        "lat": 51.3919
    },
    {
        "code": "LIVST",
        "name": "London Liverpool Street Rail Station",
        "lng": -0.0814,
        "lat": 51.518
    },
    {
        "code": "GIPSYH",
        "name": "Gipsy Hill Rail Station",
        "lng": -0.0838,
        "lat": 51.4245
    },
    {
        "code": "STMFDHL",
        "name": "Stamford Hill Rail Station",
        "lng": -0.0767,
        "lat": 51.5745
    },
    {
        "code": "FENCHRS",
        "name": "London Fenchurch Street Rail Station",
        "lng": -0.0789,
        "lat": 51.5116
    },
    {
        "code": "EDULWCH",
        "name": "East Dulwich Rail Station",
        "lng": -0.0806,
        "lat": 51.4615
    },
    {
        "code": "SEVNSIS",
        "name": "Seven Sisters Rail Station",
        "lng": -0.0753,
        "lat": 51.5823
    },
    {
        "code": "DALSKLD",
        "name": "Dalston Kingsland Rail Station",
        "lng": -0.0757,
        "lat": 51.5481
    },
    {
        "code": "SYDNHMH",
        "name": "Sydenham Hill Rail Station",
        "lng": -0.0803,
        "lat": 51.4327
    },
    {
        "code": "HAGGERS",
        "name": "Haggerston Rail Station",
        "lng": -0.0757,
        "lat": 51.5387
    },
    {
        "code": "DALS",
        "name": "Dalston Junction Rail Station",
        "lng": -0.0751,
        "lat": 51.5461
    },
    {
        "code": "HOXTON",
        "name": "Hoxton Rail Station",
        "lng": -0.0757,
        "lat": 51.5315
    },
    {
        "code": "SHRDHST",
        "name": "Shoreditch High Street Rail Station",
        "lng": -0.0752,
        "lat": 51.5234
    },
    {
        "code": "STKNWNG",
        "name": "Stoke Newington Rail Station",
        "lng": -0.0729,
        "lat": 51.5652
    },
    {
        "code": "STOTNHM",
        "name": "South Tottenham Rail Station",
        "lng": -0.0721,
        "lat": 51.5804
    },
    {
        "code": "WHHRTLA",
        "name": "White Hart Lane Rail Station",
        "lng": -0.0709,
        "lat": 51.605
    },
    {
        "code": "BHILLPK",
        "name": "Bush Hill Park Rail Station",
        "lng": -0.0692,
        "lat": 51.6415
    },
    {
        "code": "BRUCGRV",
        "name": "Bruce Grove Rail Station",
        "lng": -0.0699,
        "lat": 51.594
    },
    {
        "code": "WHYTELF",
        "name": "Whyteleafe Rail Station",
        "lng": -0.0811,
        "lat": 51.31
    },
    {
        "code": "SIVRST",
        "name": "Silver Street Rail Station",
        "lng": -0.0672,
        "lat": 51.6147
    },
    {
        "code": "NORWDJ",
        "name": "Norwood Junction Rail Station",
        "lng": -0.0752,
        "lat": 51.397
    },
    {
        "code": "RCTRYRD",
        "name": "Rectory Road Rail Station",
        "lng": -0.0683,
        "lat": 51.5585
    },
    {
        "code": "UWRLNGH",
        "name": "Upper Warlingham Rail Station",
        "lng": -0.078,
        "lat": 51.3085
    },
    {
        "code": "CATERHM",
        "name": "Caterham Rail Station",
        "lng": -0.0783,
        "lat": 51.2821
    },
    {
        "code": "CRYSTLP",
        "name": "Crystal Palace Rail Station",
        "lng": -0.0726,
        "lat": 51.4181
    },
    {
        "code": "WHYTLFS",
        "name": "Whyteleafe South Rail Station",
        "lng": -0.0769,
        "lat": 51.3034
    },
    {
        "code": "PCKHMRY",
        "name": "Peckham Rye Rail Station",
        "lng": -0.0694,
        "lat": 51.47
    },
    {
        "code": "PKHMRYC",
        "name": "Peckham Rye Rail Station",
        "lng": -0.0694,
        "lat": 51.47
    },
    {
        "code": "EDMNGRN",
        "name": "Edmonton Green Rail Station",
        "lng": -0.0611,
        "lat": 51.6249
    },
    {
        "code": "TTNHMHL",
        "name": "Tottenham Hale Rail Station",
        "lng": -0.0599,
        "lat": 51.5883
    },
    {
        "code": "HAKNYNM",
        "name": "Hackney Downs Rail Station",
        "lng": -0.0608,
        "lat": 51.5488
    },
    {
        "code": "ANERLEY",
        "name": "Anerley Rail Station",
        "lng": -0.0659,
        "lat": 51.4122
    },
    {
        "code": "FAMR",
        "name": "Falmer Rail Station",
        "lng": -0.0874,
        "lat": 50.8621
    },
    {
        "code": "BTHNLGR",
        "name": "Bethnal Green Rail Station",
        "lng": -0.0596,
        "lat": 51.5239
    },
    {
        "code": "WCHAPEL",
        "name": "Whitechapel Rail Station",
        "lng": -0.0598,
        "lat": 51.5195
    },
    {
        "code": "CLAPTON",
        "name": "Clapton Rail Station",
        "lng": -0.057,
        "lat": 51.5616
    },
    {
        "code": "LONFLDS",
        "name": "London Fields Rail Station",
        "lng": -0.0578,
        "lat": 51.5412
    },
    {
        "code": "SBURY",
        "name": "Southbury Rail Station",
        "lng": -0.0524,
        "lat": 51.6487
    },
    {
        "code": "CAMHTH",
        "name": "Cambridge Heath (London) Rail Station",
        "lng": -0.0573,
        "lat": 51.532
    },
    {
        "code": "NMBRLPK",
        "name": "Northumberland Park Rail Station",
        "lng": -0.0539,
        "lat": 51.602
    },
    {
        "code": "HACKNYC",
        "name": "Hackney Central Rail Station",
        "lng": -0.0561,
        "lat": 51.5471
    },
    {
        "code": "SHADWEL",
        "name": "Shadwell Rail Station",
        "lng": -0.0569,
        "lat": 51.5113
    },
    {
        "code": "PENEW",
        "name": "Penge West Rail Station",
        "lng": -0.0608,
        "lat": 51.4176
    },
    {
        "code": "PCKHMQD",
        "name": "Queens Road Peckham Rail Station",
        "lng": -0.0573,
        "lat": 51.4736
    },
    {
        "code": "WAPPING",
        "name": "Wapping Rail Station",
        "lng": -0.0559,
        "lat": 51.5044
    },
    {
        "code": "MWRWSTN",
        "name": "Meridian Water Rail Station",
        "lng": -0.0509,
        "lat": 51.6101
    },
    {
        "code": "TURKYST",
        "name": "Turkey Street Rail Station",
        "lng": -0.0472,
        "lat": 51.6726
    },
    {
        "code": "SBRMNDS",
        "name": "South Bermondsey Rail Station",
        "lng": -0.0547,
        "lat": 51.4881
    },
    {
        "code": "ANGELRD",
        "name": "Angel Road Rail Station",
        "lng": -0.0488,
        "lat": 51.6124
    },
    {
        "code": "RTHERHI",
        "name": "Rotherhithe Rail Station",
        "lng": -0.052,
        "lat": 51.5008
    },
    {
        "code": "BIRKBCK",
        "name": "Birkbeck Rail Station",
        "lng": -0.0557,
        "lat": 51.4039
    },
    {
        "code": "SYDENHM",
        "name": "Sydenham Rail Station",
        "lng": -0.0542,
        "lat": 51.4272
    },
    {
        "code": "ROYSTON",
        "name": "Royston Rail Station",
        "lng": -0.0269,
        "lat": 52.0531
    },
    {
        "code": "NUNHEAD",
        "name": "Nunhead Rail Station",
        "lng": -0.0523,
        "lat": 51.4668
    },
    {
        "code": "PNGEE",
        "name": "Penge East Rail Station",
        "lng": -0.0542,
        "lat": 51.4193
    },
    {
        "code": "FORESTH",
        "name": "Forest Hill Rail Station",
        "lng": -0.0532,
        "lat": 51.4393
    },
    {
        "code": "CNDAW",
        "name": "Canada Water Rail Station",
        "lng": -0.0497,
        "lat": 51.498
    },
    {
        "code": "SURREYQ",
        "name": "Surrey Quays Rail Station",
        "lng": -0.0475,
        "lat": 51.4932
    },
    {
        "code": "ELMERSE",
        "name": "Elmers End Rail Station",
        "lng": -0.0496,
        "lat": 51.3985
    },
    {
        "code": "BLCHSRD",
        "name": "Blackhorse Road Rail Station",
        "lng": -0.0412,
        "lat": 51.5866
    },
    {
        "code": "HOMRTON",
        "name": "Homerton Rail Station",
        "lng": -0.0424,
        "lat": 51.547
    },
    {
        "code": "HONROPK",
        "name": "Honor Oak Park Rail Station",
        "lng": -0.0455,
        "lat": 51.45
    },
    {
        "code": "THBLDSG",
        "name": "Theobalds Grove Rail Station",
        "lng": -0.0348,
        "lat": 51.6925
    },
    {
        "code": "WLDNGHM",
        "name": "Woldingham Rail Station",
        "lng": -0.0519,
        "lat": 51.2902
    },
    {
        "code": "WARE",
        "name": "Ware Rail Station",
        "lng": -0.0288,
        "lat": 51.808
    },
    {
        "code": "KENTHOS",
        "name": "Kent House Rail Station",
        "lng": -0.0452,
        "lat": 51.4122
    },
    {
        "code": "PNDRSEN",
        "name": "Ponders End Rail Station",
        "lng": -0.0351,
        "lat": 51.6423
    },
    {
        "code": "LIMHSE",
        "name": "Limehouse Rail Station",
        "lng": -0.0398,
        "lat": 51.5125
    },
    {
        "code": "LEABDGE",
        "name": "Lea Bridge Rail Station",
        "lng": -0.0367,
        "lat": 51.5665
    },
    {
        "code": "NEWXGEL",
        "name": "New Cross Gate ELL Rail Station",
        "lng": -0.0404,
        "lat": 51.4751
    },
    {
        "code": "NEWXGTE",
        "name": "New Cross Gate Rail Station",
        "lng": -0.0404,
        "lat": 51.4751
    },
    {
        "code": "GODSTON",
        "name": "Godstone Rail Station",
        "lng": -0.0501,
        "lat": 51.2182
    },
    {
        "code": "BRIMSDN",
        "name": "Brimsdown Rail Station",
        "lng": -0.0308,
        "lat": 51.6556
    },
    {
        "code": "CLOCKHS",
        "name": "Clock House Rail Station",
        "lng": -0.0407,
        "lat": 51.4086
    },
    {
        "code": "STJMSST",
        "name": "St James Street (London) Rail Station",
        "lng": -0.0329,
        "lat": 51.581
    },
    {
        "code": "BROCKLY",
        "name": "Brockley Rail Station",
        "lng": -0.0375,
        "lat": 51.4646
    },
    {
        "code": "PLMPTON",
        "name": "Plumpton Rail Station",
        "lng": -0.0602,
        "lat": 50.9287
    },
    {
        "code": "ENFLDLK",
        "name": "Enfield Lock Rail Station",
        "lng": -0.0285,
        "lat": 51.6709
    },
    {
        "code": "CFPK",
        "name": "Crofton Park Rail Station",
        "lng": -0.0365,
        "lat": 51.4552
    },
    {
        "code": "WALHAMX",
        "name": "Waltham Cross Rail Station",
        "lng": -0.0266,
        "lat": 51.6851
    },
    {
        "code": "CHESHNT",
        "name": "Cheshunt Rail Station",
        "lng": -0.024,
        "lat": 51.7029
    },
    {
        "code": "NBCKNHM",
        "name": "New Beckenham Rail Station",
        "lng": -0.0353,
        "lat": 51.4168
    },
    {
        "code": "NWCRELL",
        "name": "New Cross ELL Rail Station",
        "lng": -0.0324,
        "lat": 51.4763
    },
    {
        "code": "NWCROSS",
        "name": "New Cross Rail Station",
        "lng": -0.0324,
        "lat": 51.4763
    },
    {
        "code": "LSYDNHM",
        "name": "Lower Sydenham Rail Station",
        "lng": -0.0333,
        "lat": 51.4248
    },
    {
        "code": "WLTHQRD",
        "name": "Walthamstow Queens Road Rail Station",
        "lng": -0.0238,
        "lat": 51.5815
    },
    {
        "code": "HACKNYW",
        "name": "Hackney Wick Rail Station",
        "lng": -0.0249,
        "lat": 51.5434
    },
    {
        "code": "DEPTFD",
        "name": "Deptford Rail Station",
        "lng": -0.0263,
        "lat": 51.4788
    },
    {
        "code": "CATFORD",
        "name": "Catford Rail Station",
        "lng": -0.0263,
        "lat": 51.4444
    },
    {
        "code": "WLTWCEN",
        "name": "Walthamstow Central Rail Station",
        "lng": -0.0198,
        "lat": 51.5829
    },
    {
        "code": "CATFBDG",
        "name": "Catford Bridge Rail Station",
        "lng": -0.0248,
        "lat": 51.4447
    },
    {
        "code": "BCKNMJC",
        "name": "Beckenham Junction Rail Station",
        "lng": -0.026,
        "lat": 51.4112
    },
    {
        "code": "BCKNHMJ",
        "name": "Beckenham Junction Rail Station",
        "lng": -0.0258,
        "lat": 51.411
    },
    {
        "code": "BROXBRN",
        "name": "Broxbourne Rail Station",
        "lng": -0.0111,
        "lat": 51.7469
    },
    {
        "code": "EDPK",
        "name": "Eden Park Rail Station",
        "lng": -0.0264,
        "lat": 51.3901
    },
    {
        "code": "STJOHNS",
        "name": "St Johns (London) Rail Station",
        "lng": -0.0227,
        "lat": 51.4694
    },
    {
        "code": "LDYW",
        "name": "Ladywell Rail Station",
        "lng": -0.019,
        "lat": 51.4562
    },
    {
        "code": "MELDRTH",
        "name": "Meldreth Rail Station",
        "lng": 0.0089,
        "lat": 52.0907
    },
    {
        "code": "BELNGHM",
        "name": "Bellingham Rail Station",
        "lng": -0.0193,
        "lat": 51.4329
    },
    {
        "code": "BCKNHMH",
        "name": "Beckenham Hill Rail Station",
        "lng": -0.016,
        "lat": 51.4246
    },
    {
        "code": "LEWISHM",
        "name": "Lewisham Rail Station",
        "lng": -0.014,
        "lat": 51.4657
    },
    {
        "code": "GNWH",
        "name": "Greenwich Rail Station",
        "lng": -0.0133,
        "lat": 51.4781
    },
    {
        "code": "SMARGRT",
        "name": "St Margarets (Herts) Rail Station",
        "lng": 0.0013,
        "lat": 51.7878
    },
    {
        "code": "LEYTNMR",
        "name": "Leyton Midland Road Rail Station",
        "lng": -0.0081,
        "lat": 51.5697
    },
    {
        "code": "STFODOM",
        "name": "Stratford International Rail Station",
        "lng": -0.0088,
        "lat": 51.5448
    },
    {
        "code": "WWICKHM",
        "name": "West Wickham Rail Station",
        "lng": -0.0144,
        "lat": 51.3813
    },
    {
        "code": "RYEHOUS",
        "name": "Rye House Rail Station",
        "lng": 0.0056,
        "lat": 51.7694
    },
    {
        "code": "WDST",
        "name": "Wood Street Rail Station",
        "lng": -0.0024,
        "lat": 51.5866
    },
    {
        "code": "STFD",
        "name": "Stratford (London) Rail Station",
        "lng": -0.0034,
        "lat": 51.5419
    },
    {
        "code": "HGHMSPK",
        "name": "Highams Park Rail Station",
        "lng": -0.0002,
        "lat": 51.6083
    },
    {
        "code": "RBRN",
        "name": "Ravensbourne Rail Station",
        "lng": -0.0076,
        "lat": 51.4142
    },
    {
        "code": "EGRNSTD",
        "name": "East Grinstead Rail Station",
        "lng": -0.0179,
        "lat": 51.1263
    },
    {
        "code": "HTHRGRN",
        "name": "Hither Green Rail Station",
        "lng": -0.0009,
        "lat": 51.452
    },
    {
        "code": "MAZEH",
        "name": "Maze Hill Rail Station",
        "lng": 0.0029,
        "lat": 51.4826
    },
    {
        "code": "MRYLAND",
        "name": "Maryland Rail Station",
        "lng": 0.0058,
        "lat": 51.5461
    },
    {
        "code": "SHPRTH",
        "name": "Shepreth Rail Station",
        "lng": 0.0313,
        "lat": 52.1142
    },
    {
        "code": "CHINGFD",
        "name": "Chingford Rail Station",
        "lng": 0.0099,
        "lat": 51.6331
    },
    {
        "code": "WHAMHL",
        "name": "West Ham Rail Station",
        "lng": 0.0054,
        "lat": 51.5285
    },
    {
        "code": "LYTNSHR",
        "name": "Leytonstone High Road Rail Station",
        "lng": 0.0084,
        "lat": 51.5636
    },
    {
        "code": "OXTED",
        "name": "Oxted Rail Station",
        "lng": -0.0048,
        "lat": 51.2579
    },
    {
        "code": "OXTEDBY",
        "name": "Oxted Rail Station",
        "lng": -0.0048,
        "lat": 51.2579
    },
    {
        "code": "SHRTLND",
        "name": "Shortlands Rail Station",
        "lng": 0.0018,
        "lat": 51.4058
    },
    {
        "code": "LINGFLD",
        "name": "Lingfield Rail Station",
        "lng": -0.0072,
        "lat": 51.1765
    },
    {
        "code": "BLKHTH",
        "name": "Blackheath Rail Station",
        "lng": 0.0089,
        "lat": 51.4658
    },
    {
        "code": "DORMANS",
        "name": "Dormans Rail Station",
        "lng": -0.0043,
        "lat": 51.1558
    },
    {
        "code": "HRSTGRN",
        "name": "Hurst Green Rail Station",
        "lng": 0.0039,
        "lat": 51.2444
    },
    {
        "code": "LEEE",
        "name": "Lee Rail Station",
        "lng": 0.0135,
        "lat": 51.4498
    },
    {
        "code": "HAYS",
        "name": "Hayes (Kent) Rail Station",
        "lng": 0.0106,
        "lat": 51.3763
    },
    {
        "code": "COKSBDG",
        "name": "Cooksbridge Rail Station",
        "lng": -0.0092,
        "lat": 50.9038
    },
    {
        "code": "WCOMBEP",
        "name": "Westcombe Park Rail Station",
        "lng": 0.0184,
        "lat": 51.4842
    },
    {
        "code": "BROMLYN",
        "name": "Bromley North Rail Station",
        "lng": 0.017,
        "lat": 51.4083
    },
    {
        "code": "BROMLYS",
        "name": "Bromley South Rail Station",
        "lng": 0.0173,
        "lat": 51.4
    },
    {
        "code": "FRSTGT",
        "name": "Forest Gate Rail Station",
        "lng": 0.0244,
        "lat": 51.5494
    },
    {
        "code": "WNSTDPK",
        "name": "Wanstead Park Rail Station",
        "lng": 0.0262,
        "lat": 51.5517
    },
    {
        "code": "ROYDON",
        "name": "Roydon Rail Station",
        "lng": 0.0363,
        "lat": 51.7755
    },
    {
        "code": "GRVPK",
        "name": "Grove Park Rail Station",
        "lng": 0.0217,
        "lat": 51.4309
    },
    {
        "code": "SNDP",
        "name": "Sundridge Park Rail Station",
        "lng": 0.0214,
        "lat": 51.4138
    },
    {
        "code": "FOXTON",
        "name": "Foxton Rail Station",
        "lng": 0.0563,
        "lat": 52.1192
    },
    {
        "code": "KIDBROK",
        "name": "Kidbrooke Rail Station",
        "lng": 0.0275,
        "lat": 51.4621
    },
    {
        "code": "CRLN",
        "name": "Charlton Rail Station",
        "lng": 0.0313,
        "lat": 51.4868
    },
    {
        "code": "LEWES",
        "name": "Lewes Rail Station",
        "lng": 0.0113,
        "lat": 50.8706
    },
    {
        "code": "WDGRNPK",
        "name": "Woodgrange Park Rail Station",
        "lng": 0.0444,
        "lat": 51.5493
    },
    {
        "code": "MRCH",
        "name": "March Rail Station",
        "lng": 0.0912,
        "lat": 52.5599
    },
    {
        "code": "MANRPK",
        "name": "Manor Park Rail Station",
        "lng": 0.0463,
        "lat": 51.5525
    },
    {
        "code": "SESABUS",
        "name": "Southease - Piddinghoe Road",
        "lng": 0.0178,
        "lat": 50.8296
    },
    {
        "code": "ELMW",
        "name": "Elmstead Woods Rail Station",
        "lng": 0.0443,
        "lat": 51.4171
    },
    {
        "code": "BICKLEY",
        "name": "Bickley Rail Station",
        "lng": 0.0452,
        "lat": 51.4001
    },
    {
        "code": "MOTNGHM",
        "name": "Mottingham Rail Station",
        "lng": 0.0501,
        "lat": 51.4402
    },
    {
        "code": "ELTHAM",
        "name": "Eltham Rail Station",
        "lng": 0.0525,
        "lat": 51.4556
    },
    {
        "code": "WOLWCDY",
        "name": "Woolwich Dockyard Rail Station",
        "lng": 0.0546,
        "lat": 51.4911
    },
    {
        "code": "SESARDM",
        "name": "Southease Rail Station",
        "lng": 0.0306,
        "lat": 50.8313
    },
    {
        "code": "CHSLHRS",
        "name": "Chislehurst Rail Station",
        "lng": 0.0574,
        "lat": 51.4056
    },
    {
        "code": "ILFORD",
        "name": "Ilford Rail Station",
        "lng": 0.0697,
        "lat": 51.5591
    },
    {
        "code": "WOLWCHA",
        "name": "Woolwich Arsenal Rail Station",
        "lng": 0.0692,
        "lat": 51.4899
    },
    {
        "code": "NWELTHM",
        "name": "New Eltham Rail Station",
        "lng": 0.0705,
        "lat": 51.4381
    },
    {
        "code": "EDNB",
        "name": "Edenbridge Rail Station",
        "lng": 0.0606,
        "lat": 51.2084
    },
    {
        "code": "BARKING",
        "name": "Barking Rail Station",
        "lng": 0.0809,
        "lat": 51.5395
    },
    {
        "code": "PETSWD",
        "name": "Petts Wood Rail Station",
        "lng": 0.0745,
        "lat": 51.3886
    },
    {
        "code": "EDNT",
        "name": "Edenbridge Town Rail Station",
        "lng": 0.0672,
        "lat": 51.2001
    },
    {
        "code": "FALCNWD",
        "name": "Falconwood Rail Station",
        "lng": 0.0793,
        "lat": 51.4592
    },
    {
        "code": "HRLWTWN",
        "name": "Harlow Town Rail Station",
        "lng": 0.0951,
        "lat": 51.7811
    },
    {
        "code": "PLMS",
        "name": "Plumstead Rail Station",
        "lng": 0.0843,
        "lat": 51.4898
    },
    {
        "code": "ILFENBP",
        "name": "Newbury Park Station",
        "lng": 0.0897,
        "lat": 51.575
    },
    {
        "code": "NEWHVNT",
        "name": "Newhaven Town Rail Station",
        "lng": 0.0549,
        "lat": 50.7949
    },
    {
        "code": "NEWHVNH",
        "name": "Newhaven Harbour Rail Station",
        "lng": 0.055,
        "lat": 50.7898
    },
    {
        "code": "SVNKNGS",
        "name": "Seven Kings Rail Station",
        "lng": 0.0971,
        "lat": 51.564
    },
    {
        "code": "ORPNGTN",
        "name": "Orpington Rail Station",
        "lng": 0.0891,
        "lat": 51.3733
    },
    {
        "code": "GLYNDE",
        "name": "Glynde Rail Station",
        "lng": 0.0701,
        "lat": 50.8592
    },
    {
        "code": "WELLING",
        "name": "Welling Rail Station",
        "lng": 0.1017,
        "lat": 51.4648
    },
    {
        "code": "CAMBDGE",
        "name": "Cambridge Rail Station",
        "lng": 0.1375,
        "lat": 52.1941
    },
    {
        "code": "SIDCUP",
        "name": "Sidcup Rail Station",
        "lng": 0.1038,
        "lat": 51.4339
    },
    {
        "code": "GODMAYS",
        "name": "Goodmayes Rail Station",
        "lng": 0.1108,
        "lat": 51.5656
    },
    {
        "code": "SHELFD",
        "name": "Shelford (Cambs) Rail Station",
        "lng": 0.14,
        "lat": 52.1488
    },
    {
        "code": "HEVER",
        "name": "Hever Rail Station",
        "lng": 0.0951,
        "lat": 51.1814
    },
    {
        "code": "STMRYC",
        "name": "St Mary Cray Rail Station",
        "lng": 0.1064,
        "lat": 51.3947
    },
    {
        "code": "BSSN",
        "name": "Bishopstone Rail Station",
        "lng": 0.0828,
        "lat": 50.7801
    },
    {
        "code": "CHLSFLD",
        "name": "Chelsfield Rail Station",
        "lng": 0.1091,
        "lat": 51.3563
    },
    {
        "code": "HRLWMIL",
        "name": "Harlow Mill Rail Station",
        "lng": 0.1323,
        "lat": 51.7904
    },
    {
        "code": "TCULVRT",
        "name": "Thorpe Culvert Rail Station",
        "lng": 0.1994,
        "lat": 53.1231
    },
    {
        "code": "UCKFILD",
        "name": "Uckfield Rail Station",
        "lng": 0.0964,
        "lat": 50.9687
    },
    {
        "code": "ABWD",
        "name": "Abbey Wood (London) Rail Station",
        "lng": 0.1214,
        "lat": 51.4911
    },
    {
        "code": "CAMBNTH",
        "name": "Cambridge North Rail Station",
        "lng": 0.1585,
        "lat": 52.2245
    },
    {
        "code": "CHDWLHT",
        "name": "Chadwell Heath Rail Station",
        "lng": 0.129,
        "lat": 51.568
    },
    {
        "code": "COWDEN",
        "name": "Cowden Rail Station",
        "lng": 0.11,
        "lat": 51.1556
    },
    {
        "code": "ALBNYPK",
        "name": "Albany Park Rail Station",
        "lng": 0.1257,
        "lat": 51.4355
    },
    {
        "code": "MANEA",
        "name": "Manea Rail Station",
        "lng": 0.1777,
        "lat": 52.4978
    },
    {
        "code": "SEAFORD",
        "name": "Seaford Rail Station",
        "lng": 0.1001,
        "lat": 50.7728
    },
    {
        "code": "BXLYHTH",
        "name": "Bexleyheath Rail Station",
        "lng": 0.1337,
        "lat": 51.4635
    },
    {
        "code": "WTLESFD",
        "name": "Whittlesford Parkway Rail Station",
        "lng": 0.1656,
        "lat": 52.1036
    },
    {
        "code": "KNCKHLT",
        "name": "Knockholt Rail Station",
        "lng": 0.1308,
        "lat": 51.3458
    },
    {
        "code": "DGNHMDC",
        "name": "Dagenham Dock Rail Station",
        "lng": 0.1461,
        "lat": 51.5261
    },
    {
        "code": "SBDGWTH",
        "name": "Sawbridgeworth Rail Station",
        "lng": 0.1604,
        "lat": 51.8143
    },
    {
        "code": "BSHPSFD",
        "name": "Bishops Stortford Rail Station",
        "lng": 0.1649,
        "lat": 51.8667
    },
    {
        "code": "BEXLEY",
        "name": "Bexley Rail Station",
        "lng": 0.1479,
        "lat": 51.4402
    },
    {
        "code": "BELVEDR",
        "name": "Belvedere Rail Station",
        "lng": 0.1523,
        "lat": 51.4921
    },
    {
        "code": "BXTD",
        "name": "Buxted Rail Station",
        "lng": 0.1314,
        "lat": 50.99
    },
    {
        "code": "WAINFLT",
        "name": "Wainfleet Rail Station",
        "lng": 0.2347,
        "lat": 53.1051
    },
    {
        "code": "WATBECH",
        "name": "Waterbeach Rail Station",
        "lng": 0.1968,
        "lat": 52.2623
    },
    {
        "code": "BRNHRST",
        "name": "Barnehurst Rail Station",
        "lng": 0.1596,
        "lat": 51.465
    },
    {
        "code": "GTCHSFD",
        "name": "Great Chesterford Rail Station",
        "lng": 0.1935,
        "lat": 52.0598
    },
    {
        "code": "ASHURST",
        "name": "Ashurst (Kent) Rail Station",
        "lng": 0.1527,
        "lat": 51.1287
    },
    {
        "code": "SWLY",
        "name": "Swanley Rail Station",
        "lng": 0.1692,
        "lat": 51.3934
    },
    {
        "code": "ERITH",
        "name": "Erith Rail Station",
        "lng": 0.1751,
        "lat": 51.4817
    },
    {
        "code": "ROMFORD",
        "name": "Romford Rail Station",
        "lng": 0.1832,
        "lat": 51.5748
    },
    {
        "code": "STANMFC",
        "name": "Stansted Mountfitchet Rail Station",
        "lng": 0.1998,
        "lat": 51.9014
    },
    {
        "code": "DTNG",
        "name": "Dunton Green Rail Station",
        "lng": 0.1709,
        "lat": 51.2965
    },
    {
        "code": "CRFD",
        "name": "Crayford Rail Station",
        "lng": 0.1789,
        "lat": 51.4483
    },
    {
        "code": "AUDLEYE",
        "name": "Audley End Rail Station",
        "lng": 0.2072,
        "lat": 52.0044
    },
    {
        "code": "PNSHRST",
        "name": "Penshurst Rail Station",
        "lng": 0.1735,
        "lat": 51.1973
    },
    {
        "code": "RNHAME",
        "name": "Rainham (London) Rail Station",
        "lng": 0.1906,
        "lat": 51.5167
    },
    {
        "code": "NEWPRTE",
        "name": "Newport (Essex) Rail Station",
        "lng": 0.2151,
        "lat": 51.9799
    },
    {
        "code": "HAVENHS",
        "name": "Havenhouse Rail Station",
        "lng": 0.2732,
        "lat": 53.1145
    },
    {
        "code": "SLADEGN",
        "name": "Slade Green Rail Station",
        "lng": 0.1905,
        "lat": 51.4678
    },
    {
        "code": "SVNOAKS",
        "name": "Sevenoaks Rail Station",
        "lng": 0.1817,
        "lat": 51.2769
    },
    {
        "code": "SHRMKT",
        "name": "Shoreham (Kent) Rail Station",
        "lng": 0.1889,
        "lat": 51.3322
    },
    {
        "code": "BERWICK",
        "name": "Berwick (Sussex) Rail Station",
        "lng": 0.166,
        "lat": 50.8404
    },
    {
        "code": "GIDEAPK",
        "name": "Gidea Park Rail Station",
        "lng": 0.206,
        "lat": 51.5819
    },
    {
        "code": "BATABAL",
        "name": "Bat & Ball Rail Station",
        "lng": 0.1942,
        "lat": 51.2898
    },
    {
        "code": "OTFORD",
        "name": "Otford Rail Station",
        "lng": 0.1968,
        "lat": 51.3132
    },
    {
        "code": "ELSENHM",
        "name": "Elsenham Rail Station",
        "lng": 0.2281,
        "lat": 51.9205
    },
    {
        "code": "CBGH",
        "name": "Crowborough Rail Station",
        "lng": 0.188,
        "lat": 51.0464
    },
    {
        "code": "EYNSFD",
        "name": "Eynsford Rail Station",
        "lng": 0.2044,
        "lat": 51.3627
    },
    {
        "code": "EMRSPKH",
        "name": "Emerson Park Rail Station",
        "lng": 0.2201,
        "lat": 51.5686
    },
    {
        "code": "ERIDGE",
        "name": "Eridge Rail Station",
        "lng": 0.2014,
        "lat": 51.089
    },
    {
        "code": "DARTFD",
        "name": "Dartford Rail Station",
        "lng": 0.2192,
        "lat": 51.4474
    },
    {
        "code": "ELYY",
        "name": "Ely Rail Station",
        "lng": 0.2668,
        "lat": 52.3912
    },
    {
        "code": "LEIGHK",
        "name": "Leigh (Kent) Rail Station",
        "lng": 0.2105,
        "lat": 51.1939
    },
    {
        "code": "HRLDWOD",
        "name": "Harold Wood Rail Station",
        "lng": 0.2331,
        "lat": 51.5928
    },
    {
        "code": "PURFLET",
        "name": "Purfleet Rail Station",
        "lng": 0.2368,
        "lat": 51.481
    },
    {
        "code": "FRNNGRD",
        "name": "Farningham Road Rail Station",
        "lng": 0.2355,
        "lat": 51.4017
    },
    {
        "code": "HLDNBRO",
        "name": "Hildenborough Rail Station",
        "lng": 0.2276,
        "lat": 51.2145
    },
    {
        "code": "STANAIR",
        "name": "Stansted Airport Rail Station",
        "lng": 0.2608,
        "lat": 51.8886
    },
    {
        "code": "UPMNSP6",
        "name": "Upminster Rail Station",
        "lng": 0.2509,
        "lat": 51.5591
    },
    {
        "code": "UPMNSTR",
        "name": "Upminster Rail Station",
        "lng": 0.2509,
        "lat": 51.559
    },
    {
        "code": "SKEGNES",
        "name": "Skegness Rail Station",
        "lng": 0.3343,
        "lat": 53.1432
    },
    {
        "code": "KEMSING",
        "name": "Kemsing Rail Station",
        "lng": 0.2474,
        "lat": 51.2972
    },
    {
        "code": "STCR",
        "name": "Stone Crossing Rail Station",
        "lng": 0.2638,
        "lat": 51.4513
    },
    {
        "code": "LTLPORT",
        "name": "Littleport Rail Station",
        "lng": 0.3166,
        "lat": 52.4624
    },
    {
        "code": "POLGATE",
        "name": "Polegate Rail Station",
        "lng": 0.2451,
        "lat": 50.8212
    },
    {
        "code": "TUNWELL",
        "name": "Tunbridge Wells Rail Station",
        "lng": 0.2628,
        "lat": 51.1302
    },
    {
        "code": "GNHT",
        "name": "Greenhithe for Bluewater Rail Station",
        "lng": 0.2803,
        "lat": 51.4504
    },
    {
        "code": "TONBDG",
        "name": "Tonbridge Rail Station",
        "lng": 0.271,
        "lat": 51.1914
    },
    {
        "code": "CHADHDD",
        "name": "Chafford Hundred Rail Station",
        "lng": 0.2874,
        "lat": 51.4856
    },
    {
        "code": "OCKENDN",
        "name": "Ockendon Rail Station",
        "lng": 0.2905,
        "lat": 51.522
    },
    {
        "code": "BRTWOOD",
        "name": "Brentwood Rail Station",
        "lng": 0.2996,
        "lat": 51.6136
    },
    {
        "code": "HBROOMS",
        "name": "High Brooms Rail Station",
        "lng": 0.2773,
        "lat": 51.1494
    },
    {
        "code": "LGFD",
        "name": "Longfield Rail Station",
        "lng": 0.3004,
        "lat": 51.3962
    },
    {
        "code": "DOWNHAM",
        "name": "Downham Market Rail Station",
        "lng": 0.3657,
        "lat": 52.6041
    },
    {
        "code": "SWNSCMB",
        "name": "Swanscombe Rail Station",
        "lng": 0.3095,
        "lat": 51.4491
    },
    {
        "code": "HMPDNPK",
        "name": "Hampden Park (Sussex) Rail Station",
        "lng": 0.2794,
        "lat": 50.7964
    },
    {
        "code": "FRANT",
        "name": "Frant Rail Station",
        "lng": 0.2945,
        "lat": 51.104
    },
    {
        "code": "BORWGAW",
        "name": "Borough Green & Wrotham Rail Station",
        "lng": 0.3062,
        "lat": 51.2932
    },
    {
        "code": "EBOURNE",
        "name": "Eastbourne Rail Station",
        "lng": 0.2812,
        "lat": 50.7694
    },
    {
        "code": "WATLGTN",
        "name": "Watlington Rail Station",
        "lng": 0.3833,
        "lat": 52.6732
    },
    {
        "code": "GRAYS",
        "name": "Grays Rail Station",
        "lng": 0.3218,
        "lat": 51.4762
    },
    {
        "code": "SHENFLD",
        "name": "Shenfield Rail Station",
        "lng": 0.3299,
        "lat": 51.6309
    },
    {
        "code": "EBSFDOM",
        "name": "Ebbsfleet International Rail Station",
        "lng": 0.3209,
        "lat": 51.443
    },
    {
        "code": "NRTHFLT",
        "name": "Northfleet Rail Station",
        "lng": 0.3243,
        "lat": 51.4458
    },
    {
        "code": "DULNGHM",
        "name": "Dullingham Rail Station",
        "lng": 0.3667,
        "lat": 52.2016
    },
    {
        "code": "WADHRST",
        "name": "Wadhurst Rail Station",
        "lng": 0.3132,
        "lat": 51.0735
    },
    {
        "code": "KLYNN",
        "name": "Kings Lynn Rail Station",
        "lng": 0.4034,
        "lat": 52.7539
    },
    {
        "code": "WHORNDN",
        "name": "West Horndon Rail Station",
        "lng": 0.3406,
        "lat": 51.5679
    },
    {
        "code": "TLBYTWN",
        "name": "Tilbury Town Rail Station",
        "lng": 0.354,
        "lat": 51.4624
    },
    {
        "code": "PVNSYAW",
        "name": "Pevensey & Westham Rail Station",
        "lng": 0.3248,
        "lat": 50.8158
    },
    {
        "code": "MEOPHAM",
        "name": "Meopham Rail Station",
        "lng": 0.357,
        "lat": 51.3864
    },
    {
        "code": "SPHL",
        "name": "Shippea Hill Rail Station",
        "lng": 0.4133,
        "lat": 52.4302
    },
    {
        "code": "NWMKET",
        "name": "Newmarket Rail Station",
        "lng": 0.4062,
        "lat": 52.2379
    },
    {
        "code": "GRVSEND",
        "name": "Gravesend Rail Station",
        "lng": 0.3666,
        "lat": 51.4413
    },
    {
        "code": "INGTSTN",
        "name": "Ingatestone Rail Station",
        "lng": 0.3842,
        "lat": 51.667
    },
    {
        "code": "PVNSYBY",
        "name": "Pevensey Bay Rail Station",
        "lng": 0.3429,
        "lat": 50.8175
    },
    {
        "code": "SOLEST",
        "name": "Sole Street Rail Station",
        "lng": 0.3781,
        "lat": 51.3831
    },
    {
        "code": "SNGT",
        "name": "Stonegate Rail Station",
        "lng": 0.3639,
        "lat": 51.02
    },
    {
        "code": "PKWD",
        "name": "Paddock Wood Rail Station",
        "lng": 0.3891,
        "lat": 51.1823
    },
    {
        "code": "BILERCY",
        "name": "Billericay Rail Station",
        "lng": 0.4186,
        "lat": 51.6289
    },
    {
        "code": "ETILBRY",
        "name": "East Tilbury Rail Station",
        "lng": 0.4129,
        "lat": 51.4848
    },
    {
        "code": "BLTRNAB",
        "name": "Beltring Rail Station",
        "lng": 0.4035,
        "lat": 51.2047
    },
    {
        "code": "LAINDON",
        "name": "Laindon Rail Station",
        "lng": 0.4243,
        "lat": 51.5675
    },
    {
        "code": "SLEHOPE",
        "name": "Stanford-le-Hope Rail Station",
        "lng": 0.423,
        "lat": 51.5144
    },
    {
        "code": "NRMNSBY",
        "name": "Normans Bay Rail Station",
        "lng": 0.3895,
        "lat": 50.8261
    },
    {
        "code": "YALDING",
        "name": "Yalding Rail Station",
        "lng": 0.4122,
        "lat": 51.2265
    },
    {
        "code": "WMALING",
        "name": "West Malling Rail Station",
        "lng": 0.4187,
        "lat": 51.292
    },
    {
        "code": "WTRNGBY",
        "name": "Wateringbury Rail Station",
        "lng": 0.4225,
        "lat": 51.2497
    },
    {
        "code": "KENNETT",
        "name": "Kennett Rail Station",
        "lng": 0.4905,
        "lat": 52.2773
    },
    {
        "code": "EMALING",
        "name": "East Malling Rail Station",
        "lng": 0.4393,
        "lat": 51.2858
    },
    {
        "code": "HALG",
        "name": "Halling Rail Station",
        "lng": 0.4449,
        "lat": 51.3525
    },
    {
        "code": "BASILDN",
        "name": "Basildon Rail Station",
        "lng": 0.4568,
        "lat": 51.5681
    },
    {
        "code": "CHLMSFD",
        "name": "Chelmsford Rail Station",
        "lng": 0.4686,
        "lat": 51.7364
    },
    {
        "code": "SNODLND",
        "name": "Snodland Rail Station",
        "lng": 0.4482,
        "lat": 51.3302
    },
    {
        "code": "CODNBCH",
        "name": "Cooden Beach Rail Station",
        "lng": 0.4269,
        "lat": 50.8334
    },
    {
        "code": "NWHYTHE",
        "name": "New Hythe Rail Station",
        "lng": 0.4549,
        "lat": 51.313
    },
    {
        "code": "ETCHNGM",
        "name": "Etchingham Rail Station",
        "lng": 0.4424,
        "lat": 51.0105
    },
    {
        "code": "CXTN",
        "name": "Cuxton Rail Station",
        "lng": 0.4617,
        "lat": 51.3739
    },
    {
        "code": "HIGM",
        "name": "Higham Rail Station",
        "lng": 0.4663,
        "lat": 51.4266
    },
    {
        "code": "AYLESFD",
        "name": "Aylesford Rail Station",
        "lng": 0.4662,
        "lat": 51.3013
    },
    {
        "code": "LAKNHTH",
        "name": "Lakenheath Rail Station",
        "lng": 0.5352,
        "lat": 52.4474
    },
    {
        "code": "BARMING",
        "name": "Barming Rail Station",
        "lng": 0.479,
        "lat": 51.2849
    },
    {
        "code": "CTNG",
        "name": "Collington Rail Station",
        "lng": 0.4579,
        "lat": 50.8393
    },
    {
        "code": "RBRTSBD",
        "name": "Robertsbridge Rail Station",
        "lng": 0.4688,
        "lat": 50.9849
    },
    {
        "code": "EFARLGH",
        "name": "East Farleigh Rail Station",
        "lng": 0.4847,
        "lat": 51.2552
    },
    {
        "code": "PITSEA",
        "name": "Pitsea Rail Station",
        "lng": 0.5063,
        "lat": 51.5604
    },
    {
        "code": "STROOD",
        "name": "Strood Rail Station",
        "lng": 0.5002,
        "lat": 51.3965
    },
    {
        "code": "MARDEN",
        "name": "Marden Rail Station",
        "lng": 0.4932,
        "lat": 51.1752
    },
    {
        "code": "BEXHILL",
        "name": "Bexhill Rail Station",
        "lng": 0.477,
        "lat": 50.841
    },
    {
        "code": "WIKFORD",
        "name": "Wickford Rail Station",
        "lng": 0.5192,
        "lat": 51.615
    },
    {
        "code": "RCHT",
        "name": "Rochester Rail Station",
        "lng": 0.5103,
        "lat": 51.3855
    },
    {
        "code": "MSTONEB",
        "name": "Maidstone Barracks Rail Station",
        "lng": 0.514,
        "lat": 51.2772
    },
    {
        "code": "BATTLE",
        "name": "Battle Rail Station",
        "lng": 0.4947,
        "lat": 50.9129
    },
    {
        "code": "CHATHAM",
        "name": "Chatham Rail Station",
        "lng": 0.5212,
        "lat": 51.3804
    },
    {
        "code": "MSTONEW",
        "name": "Maidstone West Rail Station",
        "lng": 0.5158,
        "lat": 51.2705
    },
    {
        "code": "MSTONEE",
        "name": "Maidstone East Rail Station",
        "lng": 0.5213,
        "lat": 51.2778
    },
    {
        "code": "CRWHRST",
        "name": "Crowhurst Rail Station",
        "lng": 0.5013,
        "lat": 50.8886
    },
    {
        "code": "BRAINTR",
        "name": "Braintree Rail Station",
        "lng": 0.5567,
        "lat": 51.8754
    },
    {
        "code": "BRAINFP",
        "name": "Braintree Freeport Rail Station",
        "lng": 0.5684,
        "lat": 51.8694
    },
    {
        "code": "GLNGHMK",
        "name": "Gillingham (Kent) Rail Station",
        "lng": 0.5499,
        "lat": 51.3866
    },
    {
        "code": "CRESING",
        "name": "Cressing Rail Station",
        "lng": 0.578,
        "lat": 51.8523
    },
    {
        "code": "BTLSBDG",
        "name": "Battlesbridge Rail Station",
        "lng": 0.5653,
        "lat": 51.6248
    },
    {
        "code": "BENFLET",
        "name": "Benfleet Rail Station",
        "lng": 0.5617,
        "lat": 51.5439
    },
    {
        "code": "SPHS",
        "name": "Staplehurst Rail Station",
        "lng": 0.5504,
        "lat": 51.1715
    },
    {
        "code": "BNDON",
        "name": "Brandon Rail Station",
        "lng": 0.6247,
        "lat": 52.454
    },
    {
        "code": "WSLE",
        "name": "West St Leonards Rail Station",
        "lng": 0.5399,
        "lat": 50.8532
    },
    {
        "code": "HFLPEVL",
        "name": "Hatfield Peverel Rail Station",
        "lng": 0.5921,
        "lat": 51.7799
    },
    {
        "code": "WNOTLEY",
        "name": "White Notley Rail Station",
        "lng": 0.5959,
        "lat": 51.8389
    },
    {
        "code": "BSTD",
        "name": "Bearsted Rail Station",
        "lng": 0.5776,
        "lat": 51.2758
    },
    {
        "code": "RAYLEGH",
        "name": "Rayleigh Rail Station",
        "lng": 0.6,
        "lat": 51.5893
    },
    {
        "code": "STLNRWS",
        "name": "St Leonards Warrior Square Rail Station",
        "lng": 0.5603,
        "lat": 50.8557
    },
    {
        "code": "WDHAMFR",
        "name": "South Woodham Ferrers Rail Station",
        "lng": 0.6065,
        "lat": 51.6495
    },
    {
        "code": "HASTING",
        "name": "Hastings Rail Station",
        "lng": 0.5767,
        "lat": 50.8579
    },
    {
        "code": "RAINHMK",
        "name": "Rainham (Kent) Rail Station",
        "lng": 0.6113,
        "lat": 51.3663
    },
    {
        "code": "WITHAME",
        "name": "Witham (Essex) Rail Station",
        "lng": 0.6391,
        "lat": 51.806
    },
    {
        "code": "OREE",
        "name": "Ore Rail Station",
        "lng": 0.5916,
        "lat": 50.8669
    },
    {
        "code": "LHONSEA",
        "name": "Leigh-on-Sea Rail Station",
        "lng": 0.6404,
        "lat": 51.5413
    },
    {
        "code": "HBRN",
        "name": "Hollingbourne Rail Station",
        "lng": 0.6278,
        "lat": 51.2652
    },
    {
        "code": "DOLEHAM",
        "name": "Doleham Rail Station",
        "lng": 0.61,
        "lat": 50.9186
    },
    {
        "code": "HEADCRN",
        "name": "Headcorn Rail Station",
        "lng": 0.6275,
        "lat": 51.1657
    },
    {
        "code": "THOK",
        "name": "Three Oaks Rail Station",
        "lng": 0.6131,
        "lat": 50.9011
    },
    {
        "code": "HOCKLEY",
        "name": "Hockley Rail Station",
        "lng": 0.659,
        "lat": 51.6036
    },
    {
        "code": "BSTEDMS",
        "name": "Bury St Edmunds Rail Station",
        "lng": 0.7133,
        "lat": 52.2538
    },
    {
        "code": "CHLKWEL",
        "name": "Chalkwell Rail Station",
        "lng": 0.6706,
        "lat": 51.5387
    },
    {
        "code": "FAMBDGE",
        "name": "North Fambridge Rail Station",
        "lng": 0.6817,
        "lat": 51.6486
    },
    {
        "code": "NEWNGTN",
        "name": "Newington Rail Station",
        "lng": 0.6686,
        "lat": 51.3533
    },
    {
        "code": "KELVEDN",
        "name": "Kelvedon Rail Station",
        "lng": 0.7024,
        "lat": 51.8407
    },
    {
        "code": "HRSM",
        "name": "Harrietsham Rail Station",
        "lng": 0.6724,
        "lat": 51.2448
    },
    {
        "code": "WCLIFF",
        "name": "Westcliff-on-Sea Rail Station",
        "lng": 0.6915,
        "lat": 51.5373
    },
    {
        "code": "THETFD",
        "name": "Thetford Rail Station",
        "lng": 0.7451,
        "lat": 52.4191
    },
    {
        "code": "ROCHFD",
        "name": "Rochford Rail Station",
        "lng": 0.7023,
        "lat": 51.5817
    },
    {
        "code": "STHEAIR",
        "name": "Southend Airport Rail Station",
        "lng": 0.705,
        "lat": 51.5687
    },
    {
        "code": "SUDBURY",
        "name": "Sudbury (Suffolk) Rail Station",
        "lng": 0.7354,
        "lat": 52.0363
    },
    {
        "code": "PRITLWL",
        "name": "Prittlewell Rail Station",
        "lng": 0.7107,
        "lat": 51.5507
    },
    {
        "code": "STHVIC",
        "name": "Southend Victoria Rail Station",
        "lng": 0.7115,
        "lat": 51.5415
    },
    {
        "code": "STHCENT",
        "name": "Southend Central Rail Station",
        "lng": 0.7117,
        "lat": 51.5371
    },
    {
        "code": "LENHAM",
        "name": "Lenham Rail Station",
        "lng": 0.7078,
        "lat": 51.2345
    },
    {
        "code": "STHNDE",
        "name": "Southend East Rail Station",
        "lng": 0.7318,
        "lat": 51.539
    },
    {
        "code": "CHPWKSC",
        "name": "Chappel & Wakes Colne Rail Station",
        "lng": 0.7585,
        "lat": 51.9259
    },
    {
        "code": "WINCHLS",
        "name": "Winchelsea Rail Station",
        "lng": 0.7023,
        "lat": 50.9338
    },
    {
        "code": "BURES",
        "name": "Bures Rail Station",
        "lng": 0.7691,
        "lat": 51.9712
    },
    {
        "code": "ALTHORN",
        "name": "Althorne Rail Station",
        "lng": 0.7525,
        "lat": 51.6479
    },
    {
        "code": "KMSLY",
        "name": "Kemsley Rail Station",
        "lng": 0.7354,
        "lat": 51.3624
    },
    {
        "code": "STNGBRN",
        "name": "Sittingbourne Rail Station",
        "lng": 0.7347,
        "lat": 51.342
    },
    {
        "code": "SWALE",
        "name": "Swale Rail Station",
        "lng": 0.7471,
        "lat": 51.3892
    },
    {
        "code": "QUENBRO",
        "name": "Queenborough Rail Station",
        "lng": 0.7497,
        "lat": 51.4156
    },
    {
        "code": "THOPBAY",
        "name": "Thorpe Bay Rail Station",
        "lng": 0.7617,
        "lat": 51.5376
    },
    {
        "code": "MRKSTEY",
        "name": "Marks Tey Rail Station",
        "lng": 0.7833,
        "lat": 51.8809
    },
    {
        "code": "SHRNSOS",
        "name": "Sheerness-on-Sea Rail Station",
        "lng": 0.7585,
        "lat": 51.4411
    },
    {
        "code": "THUSTON",
        "name": "Thurston Rail Station",
        "lng": 0.8087,
        "lat": 52.25
    },
    {
        "code": "RYEE",
        "name": "Rye Rail Station",
        "lng": 0.7307,
        "lat": 50.9524
    },
    {
        "code": "PLUCKLY",
        "name": "Pluckley Rail Station",
        "lng": 0.7474,
        "lat": 51.1565
    },
    {
        "code": "SHBRYNS",
        "name": "Shoeburyness Rail Station",
        "lng": 0.7953,
        "lat": 51.531
    },
    {
        "code": "BRNMONC",
        "name": "Burnham-on-Crouch Rail Station",
        "lng": 0.814,
        "lat": 51.6337
    },
    {
        "code": "CRNG",
        "name": "Charing (Kent) Rail Station",
        "lng": 0.7903,
        "lat": 51.2081
    },
    {
        "code": "TEYNHAM",
        "name": "Teynham Rail Station",
        "lng": 0.8074,
        "lat": 51.3334
    },
    {
        "code": "SMINSTR",
        "name": "Southminster Rail Station",
        "lng": 0.8352,
        "lat": 51.6606
    },
    {
        "code": "APDR",
        "name": "Appledore (Kent) Rail Station",
        "lng": 0.8163,
        "lat": 51.0332
    },
    {
        "code": "HRLNGRD",
        "name": "Harling Road Rail Station",
        "lng": 0.9091,
        "lat": 52.4537
    },
    {
        "code": "ELMSWEL",
        "name": "Elmswell Rail Station",
        "lng": 0.9126,
        "lat": 52.238
    },
    {
        "code": "CLCHSTR",
        "name": "Colchester Rail Station",
        "lng": 0.8926,
        "lat": 51.9007
    },
    {
        "code": "CLCHRTN",
        "name": "Colchester Town Rail Station",
        "lng": 0.9048,
        "lat": 51.8865
    },
    {
        "code": "HMST",
        "name": "Ham Street Rail Station",
        "lng": 0.8545,
        "lat": 51.0684
    },
    {
        "code": "ASHFKY",
        "name": "Ashford International Rail Station",
        "lng": 0.8762,
        "lat": 51.1437
    },
    {
        "code": "CLCHHYT",
        "name": "Hythe (Essex) Rail Station",
        "lng": 0.9275,
        "lat": 51.8856
    },
    {
        "code": "FAVRSHM",
        "name": "Faversham Rail Station",
        "lng": 0.891,
        "lat": 51.3117
    },
    {
        "code": "ECLR",
        "name": "Eccles Road Rail Station",
        "lng": 0.9699,
        "lat": 52.4709
    },
    {
        "code": "WIVENHO",
        "name": "Wivenhoe Rail Station",
        "lng": 0.9561,
        "lat": 51.8565
    },
    {
        "code": "WYEE",
        "name": "Wye Rail Station",
        "lng": 0.9293,
        "lat": 51.185
    },
    {
        "code": "STWMRKT",
        "name": "Stowmarket Rail Station",
        "lng": 1,
        "lat": 52.1897
    },
    {
        "code": "ATTLBON",
        "name": "Attleborough Rail Station",
        "lng": 1.0223,
        "lat": 52.5145
    },
    {
        "code": "SELLING",
        "name": "Selling Rail Station",
        "lng": 0.9409,
        "lat": 51.2774
    },
    {
        "code": "ALRESFD",
        "name": "Alresford (Essex) Rail Station",
        "lng": 0.9974,
        "lat": 51.854
    },
    {
        "code": "CLMN",
        "name": "Chilham Rail Station",
        "lng": 0.9759,
        "lat": 51.2446
    },
    {
        "code": "NEEDHAM",
        "name": "Needham Market Rail Station",
        "lng": 1.0553,
        "lat": 52.1526
    },
    {
        "code": "MANNGTR",
        "name": "Manningtree Rail Station",
        "lng": 1.0452,
        "lat": 51.949
    },
    {
        "code": "SPONRRW",
        "name": "Spooner Row Rail Station",
        "lng": 1.0865,
        "lat": 52.535
    },
    {
        "code": "CHARTHM",
        "name": "Chartham Rail Station",
        "lng": 1.018,
        "lat": 51.2573
    },
    {
        "code": "GTBNTLY",
        "name": "Great Bentley Rail Station",
        "lng": 1.0652,
        "lat": 51.8518
    },
    {
        "code": "WHSTBLE",
        "name": "Whitstable Rail Station",
        "lng": 1.0333,
        "lat": 51.3576
    },
    {
        "code": "WYMNDHM",
        "name": "Wymondham Rail Station",
        "lng": 1.118,
        "lat": 52.5654
    },
    {
        "code": "MISTLEY",
        "name": "Mistley Rail Station",
        "lng": 1.0814,
        "lat": 51.9436
    },
    {
        "code": "DISS",
        "name": "Diss Rail Station",
        "lng": 1.1237,
        "lat": 52.3737
    },
    {
        "code": "WENHNGR",
        "name": "Westenhanger Rail Station",
        "lng": 1.038,
        "lat": 51.095
    },
    {
        "code": "CHSW",
        "name": "Chestfield & Swalecliffe Rail Station",
        "lng": 1.0669,
        "lat": 51.3602
    },
    {
        "code": "CNTBW",
        "name": "Canterbury West Rail Station",
        "lng": 1.0753,
        "lat": 51.2843
    },
    {
        "code": "CNTBE",
        "name": "Canterbury East Rail Station",
        "lng": 1.076,
        "lat": 51.2743
    },
    {
        "code": "WEELEY",
        "name": "Weeley Rail Station",
        "lng": 1.1155,
        "lat": 51.8531
    },
    {
        "code": "SDLG",
        "name": "Sandling Rail Station",
        "lng": 1.066,
        "lat": 51.0904
    },
    {
        "code": "IPSWICH",
        "name": "Ipswich Rail Station",
        "lng": 1.1444,
        "lat": 52.0506
    },
    {
        "code": "SHRGHAM",
        "name": "Sheringham Rail Station",
        "lng": 1.2103,
        "lat": 52.9414
    },
    {
        "code": "WSTRFLD",
        "name": "Westerfield Rail Station",
        "lng": 1.1659,
        "lat": 52.081
    },
    {
        "code": "HRNEBAY",
        "name": "Herne Bay Rail Station",
        "lng": 1.1177,
        "lat": 51.3646
    },
    {
        "code": "CLACTON",
        "name": "Clacton-on-Sea Rail Station",
        "lng": 1.1541,
        "lat": 51.794
    },
    {
        "code": "STURRY",
        "name": "Sturry Rail Station",
        "lng": 1.1223,
        "lat": 51.3011
    },
    {
        "code": "THPLESK",
        "name": "Thorpe-le-Soken Rail Station",
        "lng": 1.1614,
        "lat": 51.8476
    },
    {
        "code": "WRABNES",
        "name": "Wrabness Rail Station",
        "lng": 1.1715,
        "lat": 51.9395
    },
    {
        "code": "WRUNTON",
        "name": "West Runton Rail Station",
        "lng": 1.2455,
        "lat": 52.9355
    },
    {
        "code": "DERBYRD",
        "name": "Derby Road (Ipswich) Rail Station",
        "lng": 1.1826,
        "lat": 52.0506
    },
    {
        "code": "BEKSBRN",
        "name": "Bekesbourne Rail Station",
        "lng": 1.1367,
        "lat": 51.2614
    },
    {
        "code": "FLKSTNW",
        "name": "Folkestone West Rail Station",
        "lng": 1.1539,
        "lat": 51.0846
    },
    {
        "code": "CMER",
        "name": "Cromer Rail Station",
        "lng": 1.2928,
        "lat": 52.9301
    },
    {
        "code": "KIRBYX",
        "name": "Kirby Cross Rail Station",
        "lng": 1.215,
        "lat": 51.8414
    },
    {
        "code": "RGHTNRD",
        "name": "Roughton Road Rail Station",
        "lng": 1.2998,
        "lat": 52.918
    },
    {
        "code": "FLKSTNC",
        "name": "Folkestone Central Rail Station",
        "lng": 1.1695,
        "lat": 51.0829
    },
    {
        "code": "ADISHAM",
        "name": "Adisham Rail Station",
        "lng": 1.1991,
        "lat": 51.2412
    },
    {
        "code": "FRINTON",
        "name": "Frinton-on-Sea Rail Station",
        "lng": 1.2432,
        "lat": 51.8377
    },
    {
        "code": "PRKSTON",
        "name": "Harwich International Rail Station",
        "lng": 1.2551,
        "lat": 51.9473
    },
    {
        "code": "NRCH",
        "name": "Norwich Rail Station",
        "lng": 1.3068,
        "lat": 52.6272
    },
    {
        "code": "ALSHAM",
        "name": "Aylesham Rail Station",
        "lng": 1.2095,
        "lat": 51.2273
    },
    {
        "code": "SNWDNAN",
        "name": "Snowdown Rail Station",
        "lng": 1.2137,
        "lat": 51.2153
    },
    {
        "code": "WONNAZE",
        "name": "Walton-on-the-Naze Rail Station",
        "lng": 1.2677,
        "lat": 51.8462
    },
    {
        "code": "GUNTON",
        "name": "Gunton Rail Station",
        "lng": 1.3491,
        "lat": 52.8663
    },
    {
        "code": "DOVRCRT",
        "name": "Dovercourt Rail Station",
        "lng": 1.2806,
        "lat": 51.9387
    },
    {
        "code": "SWELL",
        "name": "Shepherds Well Rail Station",
        "lng": 1.2299,
        "lat": 51.1884
    },
    {
        "code": "HARWICH",
        "name": "Harwich Town Rail Station",
        "lng": 1.2867,
        "lat": 51.9441
    },
    {
        "code": "WODBDGE",
        "name": "Woodbridge Rail Station",
        "lng": 1.3178,
        "lat": 52.0904
    },
    {
        "code": "TRIMLEY",
        "name": "Trimley Rail Station",
        "lng": 1.3195,
        "lat": 51.9765
    },
    {
        "code": "NWALSHM",
        "name": "North Walsham Rail Station",
        "lng": 1.3845,
        "lat": 52.8169
    },
    {
        "code": "MELTON",
        "name": "Melton (Suffolk) Rail Station",
        "lng": 1.3382,
        "lat": 52.1044
    },
    {
        "code": "KSNY",
        "name": "Kearsney Rail Station",
        "lng": 1.2721,
        "lat": 51.1494
    },
    {
        "code": "SALHOUS",
        "name": "Salhouse Rail Station",
        "lng": 1.3914,
        "lat": 52.6756
    },
    {
        "code": "WORSTED",
        "name": "Worstead Rail Station",
        "lng": 1.4041,
        "lat": 52.7774
    },
    {
        "code": "BCNGNOS",
        "name": "Birchington-on-Sea Rail Station",
        "lng": 1.3014,
        "lat": 51.3775
    },
    {
        "code": "FLXSTOW",
        "name": "Felixstowe Rail Station",
        "lng": 1.3504,
        "lat": 51.9671
    },
    {
        "code": "WROXHAM",
        "name": "Hoveton & Wroxham Rail Station",
        "lng": 1.408,
        "lat": 52.7156
    },
    {
        "code": "MINSTER",
        "name": "Minster Rail Station",
        "lng": 1.3172,
        "lat": 51.3292
    },
    {
        "code": "DOVERP",
        "name": "Dover Priory Rail Station",
        "lng": 1.3053,
        "lat": 51.1257
    },
    {
        "code": "BRUNDLG",
        "name": "Brundall Gardens Rail Station",
        "lng": 1.4184,
        "lat": 52.6234
    },
    {
        "code": "WESGTOS",
        "name": "Westgate-on-Sea Rail Station",
        "lng": 1.3384,
        "lat": 51.3814
    },
    {
        "code": "WCKHMMR",
        "name": "Wickham Market Rail Station",
        "lng": 1.3987,
        "lat": 52.1511
    },
    {
        "code": "BRUNDAL",
        "name": "Brundall Rail Station",
        "lng": 1.4393,
        "lat": 52.6195
    },
    {
        "code": "SWCH",
        "name": "Sandwich Rail Station",
        "lng": 1.3426,
        "lat": 51.2699
    },
    {
        "code": "MMIL",
        "name": "Martin Mill Rail Station",
        "lng": 1.3482,
        "lat": 51.1707
    },
    {
        "code": "MARGATE",
        "name": "Margate Rail Station",
        "lng": 1.372,
        "lat": 51.3854
    },
    {
        "code": "BUCKNHM",
        "name": "Buckenham Rail Station",
        "lng": 1.4703,
        "lat": 52.5977
    },
    {
        "code": "LGWOOD",
        "name": "Lingwood Rail Station",
        "lng": 1.4899,
        "lat": 52.6221
    },
    {
        "code": "WALMER",
        "name": "Walmer Rail Station",
        "lng": 1.3829,
        "lat": 51.2033
    },
    {
        "code": "RAMSGTE",
        "name": "Ramsgate Rail Station",
        "lng": 1.4065,
        "lat": 51.3408
    },
    {
        "code": "DEAL",
        "name": "Deal Rail Station",
        "lng": 1.3988,
        "lat": 51.223
    },
    {
        "code": "CNTLEY",
        "name": "Cantley Rail Station",
        "lng": 1.5134,
        "lat": 52.5787
    },
    {
        "code": "SXMNDHM",
        "name": "Saxmundham Rail Station",
        "lng": 1.4902,
        "lat": 52.2149
    },
    {
        "code": "DUMPTNP",
        "name": "Dumpton Park Rail Station",
        "lng": 1.4258,
        "lat": 51.3457
    },
    {
        "code": "HALSWTH",
        "name": "Halesworth Rail Station",
        "lng": 1.5057,
        "lat": 52.3468
    },
    {
        "code": "BRSR",
        "name": "Broadstairs Rail Station",
        "lng": 1.4336,
        "lat": 51.3607
    },
    {
        "code": "ACLE",
        "name": "Acle Rail Station",
        "lng": 1.5439,
        "lat": 52.6347
    },
    {
        "code": "DARSHAM",
        "name": "Darsham Rail Station",
        "lng": 1.5235,
        "lat": 52.273
    },
    {
        "code": "BRAMPTN",
        "name": "Brampton (Suffolk) Rail Station",
        "lng": 1.5438,
        "lat": 52.3954
    },
    {
        "code": "RDHAMN",
        "name": "Reedham (Norfolk) Rail Station",
        "lng": 1.5597,
        "lat": 52.5645
    },
    {
        "code": "BECCLES",
        "name": "Beccles Rail Station",
        "lng": 1.5695,
        "lat": 52.4585
    },
    {
        "code": "HADISCO",
        "name": "Haddiscoe Rail Station",
        "lng": 1.623,
        "lat": 52.5288
    },
    {
        "code": "BRNYARM",
        "name": "Berney Arms Rail Station",
        "lng": 1.6304,
        "lat": 52.5898
    },
    {
        "code": "SMRLYTN",
        "name": "Somerleyton Rail Station",
        "lng": 1.6523,
        "lat": 52.5102
    },
    {
        "code": "OULTNBS",
        "name": "Oulton Broad South Rail Station",
        "lng": 1.7077,
        "lat": 52.4696
    },
    {
        "code": "YARMTH",
        "name": "Great Yarmouth Rail Station",
        "lng": 1.7209,
        "lat": 52.6122
    },
    {
        "code": "OULTNBN",
        "name": "Oulton Broad North Rail Station",
        "lng": 1.7157,
        "lat": 52.4778
    },
    {
        "code": "LOWSTFT",
        "name": "Lowestoft Rail Station",
        "lng": 1.7497,
        "lat": 52.4744
    }
];

export const stationsLookup = _.chain(stations)
    .keyBy('code')
    .value();
