# -*- coding: utf-8 -*-
"""Map manufacturer ID to manufacturer name and short name."""

manufacturers = {
    # id: (name, shortname),
    1: ('Sequential Circuits',),
    4: ('Moog',),
    6: ('Lexicon',),
    7: ('Kurzweil',),
    15: ('Ensoniq',),
    16: ('Oberheim',),
    17: ('Apple',),
    24: ('Emu',),
    26: ('ART',),
    34: ('Synthaxe',),
    36: ('Hohner',),
    41: ('PPG',),
    43: ('SSL',),
    47: ('Elka / General Music', 'GEM'),
    48: ('Dynacord',),
    51: ('Clavia (Nord)', 'Clavia'),
    54: ('Cheetah',),
    62: ('Waldorf Electronics Gmbh', 'Waldorf'),
    64: ('Kawai Musical Instruments MFG. CO. Ltd', 'Kawai'),
    65: ('Roland Corporation', 'Roland'),
    66: ('Korg Inc.', 'Korg'),
    67: ('Yamaha Corporation', 'Yamaha'),
    68: ('Casio Computer Co. Ltd', 'Casio'),
    70: ('Kamiya Studio Co. Ltd', 'Kamiya'),
    71: ('Akai Electric Co. Ltd.', 'Akai'),
    72: ('Victor Company of Japan, Ltd.', 'JVC'),
    75: ('Fujitsu Limited', 'Fujitsu'),
    76: ('Sony Corporation', 'Sony'),
    78: ('Teac Corporation', 'Teac'),
    80: ('Matsushita Electric Industrial Co. , Ltd', 'M-Audio'),
    81: ('Fostex Corporation', 'Fostex'),
    82: ('Zoom Corporation', 'Zoom'),
    84: ('Matsushita Communication Industrial Co., Ltd.', 'Matsushita'),
    85: ('Suzuki Musical Instruments MFG. Co., Ltd.', 'Suzuki'),
    86: ('Fuji Sound Corporation Ltd.', 'Fuji'),
    87: ('Acoustic Technical Laboratory, Inc.', 'ATL'),
    89: ('Faith, Inc.', 'Faith'),
    90: ('Internet Corporation',),
    92: ('Seekers Co. Ltd.', 'Seekers'),
    95: ('SD Card Association',),
    0x7D: ('Non-commercial',),
    0x7E: ('Universal Non-Realtime',),
    0x7F: ('Universal Realtime',),
    (0, 0, 7): ('Digital Music Corporation',),
    (0, 0, 14): ('Alesis',),
    (0, 0, 21): ('KAT',),
    (0, 0, 22): ('Opcode',),
    (0, 0, 26): ('Allen & Heath Brenell', 'Allen & Heath'),
    (0, 0, 27): ('Peavey Electronics', 'Peavey'),
    (0, 0, 28): ('360 Systems',),
    (0, 0, 32): ('Axxes',),
    (0, 0, 116): ('Ta Horng Musical Instrument',),
    (0, 0, 117): ('e-Tek Labs (Forte Tech)', 'e-Tek Labs'),
    (0, 0, 118): ('Electro-Voice',),
    (0, 0, 119): ('Midisoft Corporation', 'Midisoft'),
    (0, 0, 120): ('QSound Labs',),
    (0, 0, 121): ('Westrex',),
    (0, 0, 122): ('Nvidia',),
    (0, 0, 123): ('ESS Technology', 'ESS'),
    (0, 0, 124): ('Media Trix Peripherals',),
    (0, 0, 125): ('Brooktree Corp',),
    (0, 0, 126): ('Otari Corp',),
    (0, 0, 127): ('Key Electronics, Inc.',),
    (0, 1, 0): ('Shure Incorporated', 'Shure'),
    (0, 1, 1): ('AuraSound',),
    (0, 1, 2): ('Crystal Semiconductor', 'Crystal'),
    (0, 1, 3): ('Conexant (Rockwell)', 'Conexant'),
    (0, 1, 4): ('Silicon Graphics', 'SGI'),
    (0, 1, 5): ('M-Audio (Midiman)', 'M-Audio'),
    (0, 1, 6): ('PreSonus',),
    (0, 1, 8): ('Topaz Enterprises', 'Topaz'),
    (0, 1, 9): ('Cast Lighting',),
    (0, 1, 10): ('Microsoft',),
    (0, 1, 11): ('Sonic Foundry',),
    (0, 1, 12): ('Line 6 (Fast Forward)', 'Line 6'),
    (0, 1, 13): ('Beatnik Inc', 'Beatnik'),
    (0, 1, 14): ('Van Koevering Company',),
    (0, 1, 15): ('Altech Systems',),
    (0, 1, 16): ('S & S Research',),
    (0, 1, 17): ('VLSI Technology',),
    (0, 1, 18): ('Chromatic Research',),
    (0, 1, 19): ('Sapphire',),
    (0, 1, 20): ('IDRC',),
    (0, 1, 21): ('Justonic Tuning',),
    (0, 1, 22): ('TorComp Research Inc.',),
    (0, 1, 23): ('Newtek Inc.',),
    (0, 1, 24): ('Sound Sculpture',),
    (0, 1, 25): ('Walker Technical',),
    (0, 1, 26): ('Digital Harmony (PAVO)',),
    (0, 1, 27): ('InVision Interactive',),
    (0, 1, 28): ('T-Square Design',),
    (0, 1, 29): ('Nemesys Music Technology',),
    (0, 1, 30): ('DBX Professional (Harman Intl)', 'DBX'),
    (0, 1, 31): ('Syndyne Corporation',),
    (0, 1, 32): ('Bitheadz',),
    (0, 1, 33): ('Cakewalk Music Software', 'Cakewalk'),
    (0, 1, 34): ('Analog Devices',),
    (0, 1, 35): ('National Semiconductor',),
    (0, 1, 36): ('Boom Theory / Adinolfi Alternative Percussion',),
    (0, 1, 37): ('Virtual DSP Corporation',),
    (0, 1, 38): ('Antares Systems',),
    (0, 1, 39): ('Angel Software',),
    (0, 1, 40): ('St Louis Music',),
    (0, 1, 41): ('Lyrrus dba G-VOX',),
    (0, 1, 42): ('Ashley Audio Inc.',),
    (0, 1, 43): ('Vari-Lite Inc.',),
    (0, 1, 44): ('Summit Audio Inc.',),
    (0, 1, 45): ('Aureal Semiconductor Inc.',),
    (0, 1, 46): ('SeaSound LLC',),
    (0, 1, 47): ('U.S. Robotics',),
    (0, 1, 48): ('Aurisis Research',),
    (0, 1, 49): ('Nearfield Research',),
    (0, 1, 50): ('FM7 Inc',),
    (0, 1, 51): ('Swivel Systems',),
    (0, 1, 52): ('Hyperactive Audio Systems',),
    (0, 1, 53): ('MidiLite (Castle Studios Productions)', 'MidiLite'),
    (0, 1, 54): ('Radikal Technologies',),
    (0, 1, 55): ('Roger Linn Design', 'LINN'),
    (0, 1, 56): ('TC-Helicon Vocal Technologies',),
    (0, 1, 57): ('Event Electronics',),
    (0, 1, 58): ('Sonic Network Inc',),
    (0, 1, 59): ('Realtime Music Solutions',),
    (0, 1, 60): ('Apogee Digital', 'Apogee'),
    (0, 1, 61): ('Classical Organs, Inc.',),
    (0, 1, 62): ('Microtools Inc.',),
    (0, 1, 63): ('Numark Industries', 'Numark'),
    (0, 1, 64): ('Frontier Design Group, LLC',),
    (0, 1, 65): ('Recordare LLC',),
    (0, 1, 66): ('Starr Labs',),
    (0, 1, 67): ('Voyager Sound Inc.',),
    (0, 1, 68): ('Manifold Labs',),
    (0, 1, 69): ('Aviom Inc.', 'Aviom'),
    (0, 1, 70): ('Mixmeister Technology',),
    (0, 1, 71): ('Notation Software',),
    (0, 1, 72): ('Mercurial Communications',),
    (0, 1, 73): ('Wave Arts',),
    (0, 1, 74): ('Logic Sequencing Devices',),
    (0, 1, 75): ('Axess Electronics', 'Axess'),
    (0, 1, 76): ('Muse Research',),
    (0, 1, 77): ('Open Labs',),
    (0, 1, 78): ('Guillemot R&D Inc',),
    (0, 1, 79): ('Samson Technologies',),
    (0, 1, 80): ('Electronic Theatre Controls',),
    (0, 1, 81): ('Blackberry (RIM)', 'Blackberry'),
    (0, 1, 82): ('Mobileer',),
    (0, 1, 83): ('Synthogy',),
    (0, 1, 84): ('Lynx Studio Technology Inc.',),
    (0, 1, 85): ('Damage Control Engineering LLC',),
    (0, 1, 86): ('Yost Engineering, Inc.',),
    (0, 1, 87): ('Brooks & Forsman Designs LLC / DrumLite',),
    (0, 1, 88): ('Infinite Response',),
    (0, 1, 89): ('Garritan Corp', 'Garritan'),
    (0, 1, 90): ('Plogue Art et Technologie, Inc',),
    (0, 1, 91): ('RJM Music Technology',),
    (0, 1, 92): ('Custom Solutions Software',),
    (0, 1, 93): ('Sonarcana LLC',),
    (0, 1, 94): ('Centrance',),
    (0, 1, 95): ('Kesumo LLC',),
    (0, 1, 96): ('Stanton (Gibson)',),
    (0, 1, 97): ('Livid Instruments',),
    (0, 1, 98): ('First Act / 745 Media',),
    (0, 1, 99): ('Pygraphics, Inc.',),
    (0, 1, 100): ('Panadigm Innovations Ltd',),
    (0, 1, 101): ('Avedis Zildjian Co',),
    (0, 1, 102): ('Auvital Music Corp',),
    (0, 1, 103): ('Inspired Instruments Inc',),
    (0, 1, 104): ('Chris Grigg Designs',),
    (0, 1, 105): ('Slate Digital LLC',),
    (0, 1, 106): ('Mixware',),
    (0, 1, 107): ('Social Entropy',),
    (0, 1, 108): ('Source Audio LLC',),
    (0, 1, 109): ('Ernie Ball / Music Man', 'Music Man'),
    (0, 1, 110): ('Fishman Transducers',),
    (0, 1, 111): ('Custom Audio Electronics',),
    (0, 1, 112): ('American Audio/DJ',),
    (0, 1, 113): ('Mega Control Systems',),
    (0, 1, 114): ('Kilpatrick Audio',),
    (0, 1, 115): ('iConnectivity',),
    (0, 1, 116): ('Fractal Audio',),
    (0, 1, 117): ('NetLogic Microsystems',),
    (0, 1, 118): ('Music Computing',),
    (0, 1, 119): ('Nektar Technology Inc',),
    (0, 1, 120): ('Zenph Sound Innovations',),
    (0, 1, 121): ('DJTechTools.com',),
    (0, 1, 122): ('Rezonance Labs',),
    (0, 1, 123): ('Decibel Eleven',),
    (0, 1, 124): ('CNMAT',),
    (0, 1, 125): ('Media Overkill',),
    (0, 1, 126): ('Confusionists LLC',),
    (0, 32, 39): ('Acorn Computer',),
    (0, 32, 41): ('Focusrite/Novation', 'Novation'),
    (0, 32, 42): ('Samkyung Mechatronics',),
    (0, 32, 43): ('Medeli Electronics Co.',),
    (0, 32, 44): ('Charlie Lab SRL',),
    (0, 32, 45): ('Blue Chip Music Technology',),
    (0, 32, 46): ('BEE OH Corp',),
    (0, 32, 47): ('LG Semicon America',),
    (0, 32, 48): ('TESI',),
    (0, 32, 49): ('EMAGIC',),
    (0, 32, 50): ('Behringer GmbH', 'Behringer'),
    (0, 32, 51): ('Access Music Electronics', 'Access'),
    (0, 32, 52): ('Synoptic',),
    (0, 32, 53): ('Hanmesoft',),
    (0, 32, 54): ('Terratec Electronic GmbH', 'Terratec'),
    (0, 32, 55): ('Proel SpA',),
    (0, 32, 56): ('IBK MIDI',),
    (0, 32, 57): ('IRCAM',),
    (0, 32, 58): ('Propellerhead Software',),
    (0, 32, 59): ('Red Sound Systems Ltd',),
    (0, 32, 60): ('Elektron ESI AB',),
    (0, 32, 61): ('Sintefex Audio',),
    (0, 32, 62): ('MAM (Music and More)', 'MAM'),
    (0, 32, 63): ('Amsaro GmbH',),
    (0, 32, 64): ('CDS Advanced Technology BV',),
    (0, 32, 65): ('Touched By Sound GmbH',),
    (0, 32, 66): ('DSP Arts',),
    (0, 32, 67): ('Phil Rees Music Tech',),
    (0, 32, 68): ('Stamer Musikanlagen GmbH',),
    (0, 32, 69): ('Musical Muntaner S.A. dba Soundart',),
    (0, 32, 70): ('C-Mexx Software', 'C-Mexx'),
    (0, 32, 71): ('Klavis Technologies',),
    (0, 32, 72): ('Noteheads AB',),
    (0, 32, 73): ('Algorithmix',),
    (0, 32, 74): ('Skrydstrup R&D',),
    (0, 32, 75): ('Professional Audio Company',),
    (0, 32, 76): ('NewWave Labs (MadWaves)',),
    (0, 32, 77): ('Vermona',),
    (0, 32, 78): ('Nokia',),
    (0, 32, 79): ('Wave Idea',),
    (0, 32, 80): ('Hartmann GmbH', 'Hartmann'),
    (0, 32, 81): ("Lion's Tracs",),
    (0, 32, 82): ('Analogue Systems',),
    (0, 32, 83): ('Focal-JMlab',),
    (0, 32, 84): ('Ringway Electronics (Chang-Zhou) Co Ltd',),
    (0, 32, 85): ('Faith Technologies (Digiplug)',),
    (0, 32, 86): ('Showworks',),
    (0, 32, 87): ('Manikin Electronic', 'Manikin'),
    (0, 32, 88): ('1 Come Tech',),
    (0, 32, 89): ('Phonic Corp',),
    (0, 32, 90): ('Dolby Australia (Lake)',),
    (0, 32, 91): ('Silansys Technologies',),
    (0, 32, 92): ('Winbond Electronics',),
    (0, 32, 93): ('Cinetix Medien und Interface GmbH',),
    (0, 32, 94): ('A&G Soluzioni Digitali',),
    (0, 32, 95): ('Sequentix Music Systems',),
    (0, 32, 96): ('Oram Pro Audio',),
    (0, 32, 97): ('Be4 Ltd',),
    (0, 32, 98): ('Infection Music',),
    (0, 32, 99): ('Central Music Co. (CME)', 'CME'),
    (0, 32, 100): ('genoQs Machines GmbH',),
    (0, 32, 101): ('Medialon',),
    (0, 32, 102): ('Waves Audio Ltd',),
    (0, 32, 103): ('Jerash Labs',),
    (0, 32, 104): ('Da Fact',),
    (0, 32, 105): ('Elby Designs',),
    (0, 32, 106): ('Spectral Audio',),
    (0, 32, 107): ('Arturia',),
    (0, 32, 108): ('Vixid',),
    (0, 32, 109): ('C-Thru Music',),
    (0, 32, 110): ('Ya Horng Electronic Co LTD',),
    (0, 32, 111): ('SM Pro Audio',),
    (0, 32, 112): ('OTO MACHINES',),
    (0, 32, 113): ('ELZAB S.A., G LAB',),
    (0, 32, 114): ('Blackstar Amplification Ltd', 'Blackstar'),
    (0, 32, 115): ('M3i Technologies GmbH',),
    (0, 32, 116): ('Gemalto (from Xiring)',),
    (0, 32, 117): ('Prostage SL',),
    (0, 32, 118): ('Teenage Engineering',),
    (0, 32, 119): ('Tobias Erichsen Consulting',),
    (0, 32, 120): ('Nixer Ltd',),
    (0, 32, 121): ('Hanpin Electron Co Ltd',),
    (0, 32, 122): ('"MIDI-hardware" R.Sowa',),
    (0, 32, 123): ('Beyond Music Industrial Ltd',),
    (0, 32, 124): ('Kiss Box B.V.',),
    (0, 32, 125): ('Misa Digital Technologies Ltd',),
    (0, 32, 126): ('AI Musics Technology Inc',),
    (0, 32, 127): ('Serato Inc LP',),
    (0, 33, 0): ('Limex Music Handles GmbH',),
    (0, 33, 1): ('Kyodday/Tokai',),
    (0, 33, 2): ('Mutable Instruments',),
    (0, 33, 3): ('PreSonus Software Ltd', 'PreSonus'),
    (0, 33, 4): ('Xiring',),
    (0, 33, 5): ('Fairlight Instruments Pty Ltd', 'Fairlight'),
    (0, 33, 6): ('Musicom Lab',),
    (0, 33, 7): ('VacoLoco',),
    (0, 33, 8): ('RWA (Hong Kong) Limited',),
    (0, 33, 9): ('Native Instruments', 'NI'),
    (0, 33, 10): ('Naonext',),
    (0, 33, 11): ('MFB',),
    (0, 33, 12): ('Teknel Research',),
    (0, 33, 13): ('Ploytec GmbH', 'Ploytec'),
    (0, 33, 14): ('Surfin Kangaroo Studio',),
    (0, 33, 15): ('Philips Electronics HK Ltd', 'Philips'),
    (0, 33, 16): ('ROLI Ltd',),
    (0, 64, 0): ('Crimson Technology Inc.',),
    (0, 64, 1): ('Softbank Mobile Corp',),
    (0, 64, 3): ('D&M Holdings Inc.',)
}
