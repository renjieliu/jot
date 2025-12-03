# s = '5212221333223223642257233232272642637612321222242222326772231222771342132342272214328275121812237221' 
from functools import lru_cache

s='98767615212221333223223642257233232272642637612321222242222326772231222771342132342272214328275121812237221111'

with open("input.txt") as f:
    s = f.readlines()

@lru_cache
def find_max(s, n):
    
    if len(s) == n:
        return s
    elif n == 1:
        return str(max(list(s)))
    else: 
        A = s[0] + find_max(s[1:], n-1)
        B = find_max(s[1:], n)
        return str(max(int(A), int(B)))

total = 0
for curr in s:
    total += int(find_max(curr, 12))

print(total)

# print(max(list('12123198234')))

# def solve_safe_password_part2(rotations_input):
#     """
#     Calculates the total number of times the safe dial clicks onto 0 
#     (password method 0x434C49434B).
    
#     The dial has 100 positions (0 through 99).
    
#     Args:
#         rotations_input (str): A string where each line is a rotation 
#                                 (e.g., "L68\nL30\nR48\n...").
                                
#     Returns:
#         int: The total count of clicks onto 0.
#     """
#     # The dial starts at 50
#     current_position = 50
#     total_zero_clicks = 0
#     DIAL_SIZE = 100
    
#     # Split the input string into a list of individual rotation commands
#     rotation_list = rotations_input.strip().split('\n')
    
#     for rotation in rotation_list:
#         if not rotation:
#             continue
            
#         direction = rotation[0]
#         # Use abs() to ensure distance is positive, even if input guarantees it
#         distance = int(rotation[1:])
        
#         # --- 1. Calculate Clicks onto 0 during this rotation ---
        
#         # First, count the full laps (each lap hits 0 exactly once)
#         full_laps_count = distance // DIAL_SIZE
        
#         # The remaining movement for the partial lap
#         partial_distance = distance % DIAL_SIZE
        
#         partial_lap_count = 0
        
#         # We only care about a partial lap if the partial distance is greater than 0
#         if partial_distance > 0:
            
#             if direction == 'R':
#                 # Right/Clockwise rotation: 
#                 # Hits 0 if the remaining distance is large enough to cover the space 
#                 # from current_position up to 99 and wrap around to 0.
                
#                 # The distance to reach 0 is (DIAL_SIZE - current_position).
#                 # This only applies if we aren't already at 0.
#                 if current_position != 0:
#                     distance_to_zero = DIAL_SIZE - current_position
                    
#                     if partial_distance >= distance_to_zero:
#                         partial_lap_count = 1
                        
#             elif direction == 'L':
#                 # Left/Counter-Clockwise rotation:
#                 # Hits 0 if the remaining distance is large enough to cover the space 
#                 # from current_position down to 0.
                
#                 # The distance to reach 0 is (current_position).
#                 # This only applies if we aren't already at 0.
#                 if current_position != 0:
#                     distance_to_zero = current_position
                    
#                     if partial_distance >= distance_to_zero:
#                         partial_lap_count = 1
        
#         # Total clicks onto 0 for this rotation
#         zero_clicks_this_rotation = full_laps_count + partial_lap_count
#         total_zero_clicks += zero_clicks_this_rotation
        
#         # --- 2. Calculate the Final Position for the next step ---
        
#         if direction == 'R':
#             current_position = (current_position + distance) % DIAL_SIZE
#         elif direction == 'L':
#             # Python's % handles negative numbers in a way that gives the correct 
#             # circular position (e.g., -1 % 100 = 99)
#             current_position = (current_position - distance) % DIAL_SIZE
            
#     return total_zero_clicks

# # --- Example Usage (from the puzzle description) ---
# example_rotations = """
# R29
# R6
# L43
# L6
# R28
# L42
# L34
# L32
# L13
# L15
# R29
# L50
# R1
# L26
# L28
# L16
# L23
# R11
# L41
# L37
# R48
# R21
# L48
# L15
# L14
# L2
# L29
# L30
# R18
# L6
# R6
# R7
# R20
# L23
# L47
# L11
# L2
# R34
# L14
# L7
# L33
# R10
# R16
# L9
# R30
# L49
# R17
# R35
# L20
# R49
# L65
# R65
# R29
# R10
# R14
# L54
# L83
# L75
# L41
# R44
# L44
# R54
# R69
# R43
# R98
# R36
# R43
# L43
# R50
# R50
# L85
# R61
# R24
# R97
# L97
# R96
# R72
# R32
# R45
# L45
# R84
# L84
# R37
# R63
# L28
# R13
# L28
# L39
# L18
# L21
# R50
# L69
# L49
# L21
# R36
# L26
# L21
# R5
# L84
# R41
# R304
# R29
# L68
# L6
# R33
# R89
# L14
# R718
# L54
# R74
# L14
# L32
# L757
# R62
# R16
# L21
# L1
# L99
# L63
# L829
# R24
# L32
# L16
# R95
# L79
# R14
# R491
# R7
# L153
# R3
# L62
# L247
# R43
# L770
# R49
# R30
# R236
# R770
# L51
# R41
# R99
# L90
# R90
# R36
# R64
# L95
# R95
# R25
# R99
# L94
# R736
# L314
# R48
# R11
# L6
# L5
# R26
# L26
# L77
# R77
# L180
# L20
# L92
# L8
# L33
# R33
# L10
# R10
# R79
# R73
# L24
# L70
# L29
# L69
# L28
# R68
# R45
# L12
# R66
# L26
# R5
# L478
# L21
# L679
# L70
# L99
# L30
# L1
# R60
# R38
# L30
# R32
# L35
# L12
# L19
# L789
# L45
# R33
# L802
# L75
# L10
# L21
# L4
# R44
# R55
# L940
# L56
# L9
# L28
# R77
# L20
# R10
# R402
# R233
# L889
# R60
# L92
# R5
# L84
# L78
# L11
# L86
# L214
# R59
# R41
# R22
# L22
# L28
# L12
# R24
# R52
# L41
# L94
# L32
# L69
# R34
# R66
# L49
# L51
# R9
# R91
# L68
# R73
# L81
# R694
# R15
# R9
# L9
# L33
# R86
# R190
# R320
# L73
# R12
# R14
# L95
# L545
# R36
# L27
# R94
# R347
# R56
# L51
# L64
# R46
# L73
# R44
# L17
# L83
# R2
# L65
# R46
# L74
# R35
# L91
# R36
# L6
# L780
# R34
# R74
# L43
# L85
# R82
# R18
# L46
# L26
# L41
# L89
# L16
# L39
# R31
# R8
# L682
# R359
# R138
# R63
# L692
# L12
# R722
# R38
# L17
# L99
# R86
# L886
# L69
# R69
# L61
# R33
# R28
# R29
# R71
# L937
# L967
# L96
# L84
# R95
# R89
# L49
# R965
# R84
# R194
# L11
# L12
# R29
# R850
# R50
# R3
# L703
# L74
# L26
# R35
# L135
# R8
# L71
# R88
# R31
# R402
# R42
# R67
# R81
# L48
# R84
# R37
# R390
# R89
# L77
# R47
# L85
# L35
# L7
# R31
# R26
# R84
# R16
# L603
# R17
# R545
# R76
# L82
# L16
# L16
# R612
# R67
# R793
# R15
# L8
# L46
# L27
# L75
# R94
# L15
# L62
# L69
# R37
# L278
# R41
# R2
# L21
# L81
# R13
# R97
# R43
# L135
# R98
# R27
# L26
# R83
# L94
# R940
# L340
# R39
# R55
# L58
# R58
# R10
# R21
# R78
# L328
# R119
# R30
# R66
# L740
# L84
# R90
# L62
# L92
# L8
# L38
# R138
# R375
# R33
# L8
# L40
# R11
# R25
# L28
# L68
# R17
# R52
# R75
# L444
# L92
# L337
# R29
# R386
# R14
# L48
# L52
# R44
# L22
# L22
# L531
# R52
# R35
# R58
# R48
# L62
# R59
# L75
# R17
# L1
# L7
# R36
# L11
# R71
# R11
# L99
# L554
# R76
# R51
# L18
# R44
# L94
# L6
# R639
# R37
# R72
# L84
# R12
# R72
# L64
# R16
# R35
# R765
# L92
# R92
# R24
# R14
# L38
# R523
# R84
# L698
# R591
# R74
# L649
# R75
# R82
# R80
# R538
# L32
# R84
# R79
# L328
# R823
# R974
# R96
# R668
# R55
# R29
# R52
# R45
# L45
# L64
# L36
# L696
# R96
# R65
# R56
# L94
# L27
# R26
# R74
# R77
# R823
# L32
# L3
# L843
# R78
# L54
# R75
# L81
# L88
# R948
# L17
# R44
# R73
# R87
# L6
# R93
# L71
# R47
# L12
# R963
# L51
# R83
# L90
# R14
# L57
# R19
# R92
# R189
# R93
# L93
# R75
# R25
# R31
# R524
# L984
# L71
# R68
# R85
# L53
# R209
# R86
# R5
# R21
# L27
# R97
# R248
# L58
# R65
# L32
# R84
# R76
# R26
# L10
# L290
# L68
# R68
# R8
# R79
# R23
# L410
# L993
# R46
# R715
# R32
# R18
# L10
# L749
# R241
# R286
# R14
# R63
# R97
# L60
# R92
# L392
# L91
# R91
# L1
# R11
# L49
# L61
# L36
# L90
# L74
# L38
# R38
# L8
# L69
# L89
# R35
# R31
# R97
# R63
# R40
# R11
# R93
# R980
# R64
# L548
# L62
# R62
# R80
# R78
# L39
# L19
# R996
# R862
# L536
# L64
# R13
# L51
# L50
# L70
# L59
# L920
# L321
# R81
# R19
# L85
# L10
# L27
# L54
# R76
# R84
# R79
# R46
# R376
# L17
# R94
# L79
# R317
# L9
# L91
# L80
# L920
# L52
# L48
# L28
# L72
# L20
# L745
# L24
# R89
# L37
# R137
# R161
# L361
# L22
# L848
# R70
# R73
# L79
# L94
# L37
# L583
# L80
# L537
# R637
# L6
# L94
# R698
# L976
# R78
# R4
# R773
# L77
# R12
# R43
# R18
# L73
# R85
# L756
# L44
# R21
# R82
# L623
# R3
# R90
# L4
# L13
# L91
# L350
# L54
# L46
# L70
# R27
# L62
# R501
# L32
# L64
# R3
# R68
# L71
# L769
# R31
# L62
# R812
# R57
# L69
# L62
# R43
# R558
# R61
# L177
# L83
# R760
# L36
# L66
# R50
# R53
# L35
# L569
# R39
# L36
# R57
# L57
# L55
# L31
# R32
# R54
# R99
# R89
# L88
# R45
# R55
# R35
# L90
# R716
# L14
# L647
# R74
# L379
# L27
# L85
# L333
# R650
# L1
# L99
# L80
# L44
# R54
# R70
# L2
# R2
# L8
# R964
# L62
# R106
# L71
# R22
# R20
# L63
# L49
# R47
# L6
# R59
# L27
# R68
# R32
# L89
# L13
# L79
# R41
# L92
# R51
# R49
# R11
# R689
# L12
# R12
# L71
# L61
# L875
# L81
# L12
# R908
# L8
# L38
# R38
# R56
# R62
# R933
# R49
# L2
# L326
# R28
# R773
# L71
# R282
# L165
# L22
# L97
# L788
# L50
# R814
# L10
# R34
# L88
# R95
# R743
# R577
# R92
# L71
# L48
# R44
# L44
# L3
# R3
# R71
# L690
# R19
# L8
# R31
# L38
# L49
# L558
# L46
# R988
# L1
# R22
# L41
# L89
# L635
# L80
# R88
# L58
# R56
# L68
# R86
# R76
# R24
# L98
# R82
# R270
# R227
# R79
# L65
# R16
# L11
# L4
# R17
# R82
# L95
# R31
# R92
# R97
# R80
# L13
# L92
# R65
# L60
# R51
# R49
# R38
# L38
# L84
# L716
# R21
# L721
# R59
# R741
# R59
# L75
# R8
# L192
# R599
# L99
# R10
# R90
# L676
# R76
# L745
# L55
# L349
# L73
# L78
# L40
# R43
# R42
# L46
# R87
# R76
# R68
# L30
# R79
# R23
# R98
# L10
# R54
# R59
# L81
# L74
# R49
# R34
# L825
# R52
# R242
# R58
# L58
# R89
# R28
# L17
# L35
# R83
# L13
# R65
# L72
# R72
# L98
# R34
# L49
# R13
# L9
# R9
# R14
# L73
# L41
# L81
# R81
# L18
# R818
# L21
# R21
# R69
# L4
# L34
# L4
# R91
# R42
# L461
# R559
# L58
# L60
# R24
# R36
# L46
# R33
# R766
# L53
# L839
# R39
# R37
# L937
# R59
# R41
# L29
# L81
# L90
# R832
# L40
# R8
# R87
# L694
# R7
# R64
# R90
# R43
# L97
# L11
# R911
# L75
# R175
# R5
# L22
# L83
# L449
# R662
# L13
# L61
# L50
# R77
# L21
# R55
# L62
# R36
# R34
# R14
# L49
# R21
# L673
# R72
# L93
# R84
# R16
# L59
# L41
# L75
# L46
# R52
# R83
# R7
# L21
# L48
# L22
# R70
# L78
# R778
# R50
# R71
# L25
# R83
# R21
# R47
# L198
# L28
# R503
# L85
# R623
# R50
# R88
# L624
# L896
# R20
# R94
# L94
# R84
# R16
# R12
# R288
# L77
# R5
# R27
# L3
# L203
# R51
# L23
# L508
# L13
# L10
# R54
# L1
# R1
# R48
# L9
# R34
# L94
# R21
# L81
# R968
# R13
# R91
# L91
# R48
# L15
# R499
# L34
# L98
# R167
# L19
# R76
# L22
# R98
# L48
# R48
# R43
# L2
# L29
# R12
# R24
# R35
# R17
# R90
# L90
# R917
# R39
# L71
# L885
# R35
# L35
# R47
# L88
# L55
# L33
# L571
# L389
# R3
# R47
# R29
# L59
# L28
# R56
# L259
# R405
# R95
# L4
# R93
# L89
# R67
# L93
# L269
# L47
# L58
# R54
# L60
# R6
# L40
# R91
# L51
# L79
# R804
# R74
# L46
# R16
# L80
# L46
# L43
# L90
# R25
# L35
# R78
# L78
# R48
# L98
# R723
# R27
# R71
# R42
# R87
# L341
# L59
# R29
# R4
# R64
# R42
# R68
# L79
# L9
# R54
# L618
# L71
# R916
# L97
# L3
# R10
# L10
# L37
# L58
# L46
# R28
# L66
# L63
# R33
# R770
# L4
# R43
# L26
# R59
# R83
# R84
# R18
# L35
# R23
# R94
# L85
# L15
# R52
# R60
# L332
# L98
# L51
# L29
# L47
# R5
# L60
# L5
# R705
# R7
# R10
# L5
# L77
# L60
# R83
# R542
# L2
# R2
# R29
# R71
# R79
# R292
# L49
# R18
# L99
# R459
# L13
# R13
# L91
# L7
# L2
# L44
# R44
# L98
# L643
# L40
# L19
# L40
# L12
# R52
# R26
# R18
# L41
# L3
# R64
# L64
# R841
# L164
# L437
# R60
# L87
# L10
# R865
# R84
# L952
# L4
# R4
# L62
# R34
# L18
# R37
# R76
# L37
# L30
# L86
# R84
# R83
# R19
# L82
# R82
# R398
# R2
# R19
# R81
# R82
# R290
# R80
# L52
# L5
# L95
# L87
# L37
# R24
# L60
# R60
# L71
# L29
# L32
# R32
# R66
# L47
# L21
# R902
# L18
# L12
# R30
# L43
# L22
# R39
# L74
# R62
# R38
# L77
# L22
# L662
# R46
# R15
# L31
# L69
# R47
# L575
# R82
# L54
# L36
# L40
# R76
# R70
# R30
# L93
# L27
# R20
# L28
# R14
# L822
# L53
# L11
# L46
# L54
# R57
# L157
# R347
# R96
# L88
# R45
# R11
# L81
# L35
# L88
# R66
# R68
# R36
# L83
# L78
# L98
# L18
# R42
# L680
# R273
# L66
# R31
# R81
# L75
# L52
# R94
# L5
# L43
# R1
# R52
# L49
# L69
# R229
# L650
# L95
# L19
# L490
# R92
# R50
# R25
# L77
# L2
# R55
# L87
# R34
# R99
# R101
# R225
# L225
# R181
# R86
# L67
# L14
# L44
# R58
# L72
# R36
# L57
# R693
# L55
# R255
# R857
# L57
# L41
# L59
# L66
# L603
# R69
# L66
# L81
# L45
# L94
# R85
# L999
# R84
# R58
# R58
# L44
# R53
# L17
# L11
# L81
# L868
# L932
# L72
# R43
# R6
# L77
# L29
# L25
# L64
# R82
# L21
# L43
# L1
# R54
# R398
# L14
# R46
# R17
# R16
# L80
# R64
# L362
# L53
# L74
# R18
# L29
# R47
# R77
# R83
# R95
# R898
# R27
# R97
# L89
# L37
# L84
# L14
# L99
# L5
# R41
# L910
# R73
# R33
# L37
# L96
# R94
# R6
# L14
# R43
# R90
# R57
# R6
# R18
# R68
# R419
# R21
# L23
# L85
# L51
# L12
# L37
# L70
# R485
# L44
# R95
# R34
# R51
# L351
# R64
# L64
# R130
# L309
# L821
# R64
# R27
# R109
# R33
# L33
# R59
# R69
# L29
# L55
# L416
# L55
# R90
# L63
# R42
# L942
# R658
# R70
# L28
# R2
# L402
# L48
# R90
# R58
# L332
# L43
# L4
# L85
# R46
# L682
# R65
# R35
# L22
# L30
# L5
# R57
# L22
# R522
# R781
# R519
# L830
# L259
# L11
# L53
# L3
# L99
# L41
# R11
# L83
# R568
# L88
# L512
# L78
# L96
# L44
# R18
# R6
# R94
# R618
# L244
# L74
# L10
# R66
# R87
# R27
# L70
# L50
# L90
# L62
# L27
# L85
# R70
# R441
# L97
# R23
# R84
# R473
# L44
# L379
# L6
# L541
# L42
# L34
# R451
# L16
# R88
# L30
# L27
# L3
# L86
# L66
# R1
# L37
# R737
# L64
# L57
# L844
# R19
# L53
# L9
# R682
# L20
# R51
# L51
# L84
# L6
# R93
# R52
# R45
# L692
# R68
# L67
# R944
# R824
# R23
# R943
# R67
# L27
# L196
# R23
# R84
# L91
# L447
# L793
# L211
# R48
# L134
# L66
# L50
# L50
# L778
# L49
# L5
# R48
# L16
# R191
# R75
# R22
# R98
# R652
# R62
# R22
# L690
# R68
# L9
# L7
# R16
# L93
# R93
# R945
# R55
# L86
# R68
# L25
# L27
# L7
# L23
# L93
# L64
# L166
# L76
# R99
# L13
# L31
# R10
# L24
# L51
# R89
# R20
# R16
# L16
# R15
# R19
# R79
# R48
# L339
# L22
# L742
# R621
# R21
# L24
# L18
# R13
# R29
# R18
# L16
# L2
# L19
# L421
# L78
# L82
# L12
# R12
# R36
# R61
# L97
# R88
# L99
# R75
# R36
# L19
# L81
# R49
# R22
# L73
# L33
# R35
# L88
# L12
# R31
# R39
# L70
# L73
# L27
# R32
# R186
# R67
# L797
# L601
# R57
# L46
# R36
# L48
# R14
# L45
# L12
# L43
# L867
# L44
# L89
# R30
# R865
# R305
# R42
# L481
# R39
# R508
# L990
# L15
# R570
# L898
# L4
# R29
# R56
# R724
# R40
# L120
# L33
# R831
# L27
# R29
# L51
# L349
# L91
# L94
# R65
# R220
# R8
# L65
# R57
# L6
# L94
# L32
# L68
# R67
# R33
# R711
# R96
# L807
# R9
# R76
# R315
# L69
# L31
# R88
# L61
# R87
# R86
# R32
# L48
# R10
# L13
# R51
# L27
# L58
# L74
# L47
# R69
# L39
# R34
# L85
# R289
# L54
# L49
# L771
# R50
# R279
# R60
# L9
# R37
# L76
# L776
# L47
# R57
# R87
# R85
# R33
# R663
# L781
# L43
# R51
# R759
# L15
# R631
# L465
# R67
# L15
# L252
# L266
# R66
# L18
# R818
# R684
# L19
# R235
# L46
# L46
# L5
# R77
# R20
# L85
# L1
# L27
# R6
# L67
# R74
# L58
# R77
# L79
# L7
# R24
# R79
# L25
# R54
# L8
# R6
# L794
# R82
# L86
# L65
# L24
# R224
# R9
# R91
# L24
# R824
# L458
# R58
# L934
# L19
# L62
# L85
# L82
# L18
# L68
# L353
# R35
# L14
# R35
# L35
# R62
# R4
# R59
# L15
# R42
# R48
# R49
# R51
# R86
# R55
# L85
# L90
# L83
# L89
# L451
# L23
# L68
# L52
# L78
# R48
# R746
# L16
# R604
# R658
# L62
# R40
# R223
# L86
# R23
# R20
# L56
# L683
# L81
# R227
# R71
# L279
# L33
# L80
# R12
# R82
# R880
# R20
# R17
# R83
# R821
# R79
# R59
# R72
# L42
# L93
# L96
# R378
# L78
# R89
# L89
# R65
# L465
# L80
# L20
# L811
# R57
# L67
# R21
# L62
# R390
# R70
# L57
# L41
# L7
# L93
# R74
# R93
# L70
# R3
# R54
# R96
# R50
# L47
# L53
# L124
# L45
# L65
# R34
# L25
# R31
# R994
# R34
# L20
# L514
# L198
# R98
# L50
# R50
# L502
# R97
# R91
# L47
# L25
# L14
# R57
# R43
# L42
# L40
# R282
# R26
# L26
# R64
# L64
# L57
# L35
# R14
# L22
# R60
# R813
# L57
# R53
# R187
# R632
# R4
# L86
# L67
# L63
# L41
# L11
# R976
# R44
# R141
# L85
# R34
# L34
# R15
# L9
# R88
# L57
# R92
# R171
# L54
# L34
# R364
# L23
# L19
# L16
# L46
# R40
# R4
# R52
# L68
# R78
# L24
# R46
# R4
# L4
# R311
# R89
# R46
# L646
# L66
# R2
# R5
# R78
# R45
# R704
# L57
# L77
# L34
# L95
# L42
# L95
# R32
# R60
# L74
# L26
# L60
# L814
# L71
# L15
# R68
# R68
# L57
# L79
# R975
# R99
# L31
# R66
# R91
# R39
# R521
# R40
# R155
# R332
# R11
# R8
# L40
# L33
# L38
# R48
# L71
# R61
# R67
# L26
# R21
# R67
# R38
# L56
# L44
# R23
# R677
# R11
# L6
# R440
# R6
# R72
# R66
# R43
# L66
# R37
# L76
# L27
# L50
# R50
# R75
# L97
# L26
# L89
# R37
# R45
# L29
# L16
# L12
# R85
# L90
# L183
# R10
# L10
# R76
# L93
# L783
# R40
# L231
# L78
# L229
# R98
# L85
# R63
# R48
# L26
# L74
# L80
# R106
# L52
# R475
# R25
# L813
# R93
# L78
# R30
# R68
# L36
# L44
# R82
# L81
# R52
# R26
# R94
# R11
# R96
# R66
# R12
# L42
# R27
# R35
# R74
# L625
# L96
# L55
# L31
# R35
# R73
# R46
# R587
# R94
# R19
# L19
# L46
# R393
# L39
# R91
# R44
# L99
# R20
# R77
# R17
# L82
# R454
# L85
# L133
# L57
# L863
# R8
# L39
# R15
# R21
# L155
# R80
# L485
# R63
# L50
# R79
# R971
# R405
# R42
# R59
# R994
# L202
# L10
# R42
# R391
# R801
# R82
# R76
# L52
# L64
# R444
# R90
# L97
# L756
# R38
# R1
# L84
# L82
# R82
# R70
# L852
# R19
# L6
# R75
# R25
# R57
# R13
# L83
# L18
# L2
# L698
# L67
# L33
# L308
# L946
# L46
# L28
# R28
# L803
# L91
# R94
# R28
# R22
# R50
# R91
# L73
# R20
# R723
# L40
# L21
# L76
# L52
# L72
# L364
# R64
# L987
# R87
# L20
# L60
# L20
# R78
# L353
# L25
# R85
# L73
# L12
# R70
# L470
# L26
# R26
# R96
# R53
# L49
# R439
# L14
# L14
# R1
# R96
# R992
# R29
# R71
# R468
# L93
# L19
# L26
# L25
# L91
# R86
# R118
# R82
# L17
# R450
# R7
# L440
# L628
# L52
# R80
# L25
# L33
# L42
# L559
# L929
# L67
# R97
# L54
# L88
# R83
# L14
# R80
# R851
# R41
# R58
# L399
# R625
# L97
# R7
# R65
# R75
# L675
# L75
# R75
# R372
# L74
# L68
# L30
# L84
# R84
# L79
# L921
# L91
# L553
# L41
# R85
# L42
# R71
# R71
# R54
# R699
# R96
# L41
# L8
# R12
# L34
# L90
# L93
# L53
# L38
# L42
# R38
# L41
# L98
# R89
# R50
# R396
# R42
# R62
# L9
# L112
# R75
# L54
# L49
# R20
# R71
# R585
# L22
# R10
# L614
# R1
# L221
# L65
# L307
# L9
# L447
# L925
# L63
# L65
# R99
# L99
# L39
# R346
# L207
# R58
# L758
# R37
# R766
# L638
# L525
# L40
# L9
# L85
# L596
# L706
# L19
# L22
# L91
# L14
# L25
# L20
# L713
# R343
# L43
# R2
# L68
# R41
# R68
# R22
# L333
# R968
# R80
# L63
# L73
# R56
# L89
# R889
# L317
# R17
# L62
# R129
# R780
# L64
# L94
# R11
# R78
# R78
# L67
# L8
# R37
# L70
# R12
# R62
# L922
# L28
# R33
# R95
# R20
# R80
# L80
# L40
# R69
# L49
# L46
# R61
# L15
# R20
# L20
# L81
# R81
# R89
# R11
# L65
# L75
# L50
# L10
# L78
# R78
# R38
# R94
# L732
# R914
# R86
# L79
# L21
# L11
# R107
# R704
# R54
# R46
# L669
# L79
# R130
# L82
# L28
# R628
# L63
# L18
# L19
# R26
# R74
# L13
# R13
# L65
# R9
# R756
# L33
# L67
# L178
# R298
# L914
# L91
# L915
# R25
# L31
# R20
# R51
# R517
# L82
# L16
# R85
# R31
# R35
# L35
# R91
# L43
# L67
# L81
# R888
# L5
# L18
# L76
# L757
# L32
# R99
# R92
# R9
# R489
# L89
# L20
# R120
# R54
# L77
# L41
# L39
# L97
# L64
# L6
# L30
# L27
# L47
# L26
# L867
# R67
# R123
# L23
# R77
# R980
# R69
# L94
# L84
# L48
# R446
# L19
# R24
# L51
# R13
# R187
# R555
# R545
# R97
# L63
# L639
# R105
# L95
# L45
# R40
# R99
# L16
# R17
# R538
# R53
# L123
# L873
# L95
# L46
# R46
# R7
# R622
# L348
# R33
# L76
# L38
# R82
# R829
# L34
# L29
# L48
# L453
# L25
# R78
# R986
# R14
# R17
# R13
# L55
# R625
# L8
# L92
# L23
# R23
# L56
# R56
# L53
# R732
# L10
# L4
# R28
# L93
# R60
# L60
# R82
# R14
# R98
# R813
# L380
# L1
# L426
# L80
# R28
# L48
# R47
# L49
# R2
# L69
# L31
# R897
# R47
# L7
# L37
# L413
# R30
# L65
# R55
# R457
# R83
# L590
# R16
# R96
# L99
# R92
# L11
# L51
# R541
# R59
# R664
# R16
# R3
# R742
# L70
# L95
# R238
# L598
# R743
# R57
# L83
# L3
# R86
# L35
# R35
# L89
# R98
# L9
# L27
# L474
# R7
# R94
# R13
# L75
# R27
# L28
# L17
# L17
# R56
# L4
# R8
# R76
# R61
# R1
# L1
# R20
# R80
# L15
# R49
# L67
# R33
# L4
# R4
# L9
# R9
# R252
# L52
# R83
# L83
# R598
# L98
# L89
# L256
# R90
# R72
# R92
# L9
# R74
# L396
# L84
# L86
# R230
# L99
# L47
# R8
# L78
# L6
# R38
# R46
# L39
# R98
# R66
# L25
# L31
# R26
# L995
# L11
# L85
# L123
# L32
# R954
# R7
# R25
# L779
# L71
# L498
# L87
# R93
# R467
# L81
# R6
# L895
# R281
# L634
# L21
# R184
# L79
# R305
# L758
# R736
# L46
# L7
# L673
# L3
# L77
# L98
# R36
# R85
# R20
# R5
# L28
# L18
# L47
# R47
# L12
# R12
# L837
# L96
# R33
# R49
# L890
# R6
# L65
# R93
# L2
# L24
# L55
# L35
# R48
# L63
# R38
# R37
# R325
# R126
# L94
# R6
# L91
# R919
# R460
# L94
# L631
# L63
# R20
# R6
# R473
# L55
# L51
# L636
# R143
# L692
# R92
# R444
# L16
# R52
# L6
# R40
# L596
# R23
# L58
# L83
# R802
# R98
# L67
# L62
# L13
# R28
# R229
# R547
# R695
# L57
# R87
# L47
# R60
# R65
# L87
# L278
# R76
# R24
# L79
# R823
# L83
# R2
# L27
# L5
# L31
# R19
# L339
# L80
# R63
# R37
# R92
# R755
# L30
# L97
# L686
# R49
# L83
# R84
# R16
# L27
# L58
# L24
# R9
# L48
# L716
# L13
# R30
# R47
# R30
# R13
# R43
# L34
# R748
# R134
# L25
# R54
# R37
# L60
# R22
# R38
# R69
# L75
# L81
# L13
# L3
# R22
# R96
# L68
# R15
# L62
# L65
# L835
# R36
# R64
# L20
# L80
# L70
# R70
# L22
# L878
# L38
# R38
# L63
# L13
# L158
# R34
# L43
# R43
# L29
# L244
# R73
# R952
# L52
# R14
# R35
# R53
# L2
# R50
# L538
# L59
# L53
# R40
# R38
# R22
# R396
# R66
# R38
# R764
# R36
# R19
# L496
# L23
# R33
# R65
# L989
# R699
# L89
# L34
# R59
# R53
# R80
# R59
# L36
# R41
# R73
# R79
# R70
# R27
# L90
# L62
# L38
# R27
# L16
# R830
# L90
# R479
# L14
# R81
# L30
# R831
# L98
# R819
# R81
# R89
# R41
# L14
# R82
# R702
# R60
# L60
# L1
# L7
# R8
# L88
# R788
# L999
# R20
# L24
# R80
# R23
# L58
# R58
# R43
# L143
# L680
# L45
# L51
# R88
# L44
# R71
# R960
# L99
# R336
# R6
# L891
# R14
# R34
# R4
# L3
# R217
# R78
# L302
# L329
# L264
# R835
# R34
# L53
# R5
# L99
# R9
# R386
# R494
# R24
# L77
# R42
# L382
# L634
# L84
# L36
# L64
# R86
# L93
# L626
# L343
# R96
# L20
# R65
# R33
# L98
# R68
# L67
# R8
# R91
# R43
# L46
# R303
# R2
# L2
# R26
# L90
# R57
# R307
# L17
# R717
# R731
# L31
# L206
# R6
# L284
# R84
# R92
# R8
# R1
# L1
# R188
# R89
# L55
# L22
# L98
# L2
# R93
# R77
# L52
# R48
# R5
# L71
# L80
# L97
# R40
# L345
# R82
# R27
# R3
# R59
# R11
# L48
# L352
# R23
# R209
# L930
# L102
# R34
# R70
# R96
# R15
# R50
# L78
# R59
# L46
# L73
# L27
# L28
# L272
# L35
# R16
# R19
# L78
# R278
# R76
# R22
# L98
# R91
# R24
# L307
# R92
# L29
# L20
# L71
# R87
# L438
# R534
# L63
# L778
# R16
# L838
# R664
# L84
# L221
# R8
# L367
# R630
# L33
# R34
# L61
# R30
# R48
# R52
# R12
# R58
# R30
# R64
# R732
# L50
# L21
# R47
# L372
# L75
# L959
# L66
# L848
# R629
# L81
# L792
# R92
# R4
# L4
# L64
# L99
# L37
# R51
# R749
# R854
# R146
# L89
# R10
# R48
# R11
# R620
# R226
# L624
# L81
# L21
# R26
# L96
# R93
# L58
# R63
# R19
# L510
# L7
# L68
# R83
# L25
# R86
# L306
# L22
# R67
# L45
# L86
# R614
# R31
# R268
# L3
# R86
# R290
# L83
# R87
# L90
# L741
# R9
# L90
# L44
# R27
# L275
# R7
# L7
# L76
# R76
# L78
# L71
# L51
# R15
# L43
# R62
# R66
# R25
# L3
# R78
# L13
# R77
# L64
# L65
# L16
# L39
# R4
# L14
# L56
# L81
# L33
# R39
# R56
# L95
# L77
# R28
# R19
# L174
# L58
# R50
# L88
# R4
# R21
# L72
# R401
# R13
# L99
# R39
# L607
# L698
# L84
# L723
# R94
# R39
# L57
# L39
# L98
# R266
# R98
# L46
# L547
# R63
# R32
# L90
# L10
# L86
# R76
# L64
# L434
# L92
# L70
# L39
# L92
# R1
# L77
# L39
# L95
# R911
# R5
# L803
# L19
# R29
# R118
# R90
# R880
# L65
# R678
# R87
# R11
# R89
# L51
# R51
# R12
# L364
# R652
# R245
# R55
# L1
# L72
# R142
# L34
# L757
# L78
# L333
# R33
# R70
# R30
# R42
# L342
# R96
# R85
# L81
# L455
# R39
# L18
# R98
# R21
# R49
# L34
# R25
# R75
# R64
# R71
# R89
# R76
# R5
# R30
# R65
# R90
# R33
# L23
# R9
# R22
# R536
# R669
# R64
# L22
# R53
# L66
# L65
# R88
# R12
# L49
# R11
# R16
# L989
# R11
# L89
# R41
# R73
# R75
# L476
# R731
# L455
# R1
# L51
# R50
# L61
# R86
# L29
# R804
# R45
# L45
# R695
# R55
# L66
# L93
# L291
# R71
# L40
# L131
# R16
# L4
# L894
# L61
# R80
# R63
# R431
# R169
# R68
# R46
# R86
# L66
# L34
# L46
# R46
# R15
# L15
# R9
# L30
# L79
# R49
# R951
# R15
# L15
# L75
# L20
# L3
# L502
# L27
# R56
# R3
# R83
# L15
# R79
# R23
# R5
# L7
# R856
# R44
# R397
# L92
# R68
# L39
# L34
# R67
# R38
# R95
# R54
# L64
# L8
# L98
# R67
# R15
# L460
# L44
# R38
# R126
# R90
# R57
# L30
# R33
# L76
# R8
# L63
# L45
# R92
# R8
# R74
# R26
# R37
# L73
# L17
# L20
# L27
# L79
# L340
# R68
# R26
# R25
# R65
# L65
# R146
# R21
# L25
# L934
# L88
# L520
# R36
# L36
# L76
# L24
# R25
# L25
# L65
# L22
# L57
# L44
# R18
# R670
# L61
# R61
# L49
# L65
# L86
# L46
# L22
# R6
# R162
# R497
# L46
# L51
# L95
# R55
# R40
# R796
# L4
# R36
# L28
# R18
# L18
# R43
# R29
# L72
# R42
# R358
# R67
# L1
# R34
# L31
# R31
# R86
# R72
# L69
# R89
# R28
# L370
# L3
# R67
# R53
# L25
# R75
# L47
# L776
# L358
# L4
# L53
# L47
# L418
# L88
# L12
# L954
# R193
# R661
# R71
# R44
# R68
# L14
# L369
# R38
# L140
# R37
# L35
# L23
# R3
# R20
# L64
# R70
# L6
# L51
# R285
# R89
# L53
# R83
# L453
# L810
# L1
# R602
# L3
# L88
# R96
# L17
# L379
# R95
# R29
# R55
# L79
# L282
# R40
# R42
# R439
# L74
# L56
# R52
# R78
# L39
# R96
# R77
# L873
# L41
# L50
# R91
# L48
# L361
# R59
# R12
# L71
# L822
# L85
# R90
# R26
# R50
# R3
# R12
# L765
# L98
# L58
# R68
# R83
# L8
# L82
# R58
# L68
# L94
# L33
# L80
# L588
# R1
# L101
# R29
# R59
# L151
# L37
# L69
# R40
# R29
# L383
# L58
# L95
# L264
# L26
# R79
# L88
# R5
# L37
# L98
# R65
# L26
# L58
# L16
# R67
# R366
# R991
# R39
# R37
# R34
# L91
# L143
# R58
# R46
# R96
# L833
# R820
# L733
# R46
# L142
# L683
# R25
# L86
# L56
# R65
# R83
# R27
# L16
# L1
# L16
# R3
# R36
# R361
# R42
# L52
# L90
# L93
# R49
# R44
# R91
# L91
# R65
# L65
# L577
# L953
# L754
# R98
# L83
# L577
# L54
# L686
# L921
# R7
# L31
# R81
# R930
# L52
# L14
# L714
# L99
# L401
# R64
# L359
# L18
# L79
# L16
# R8
# L33
# L67
# R11
# R4
# L649
# L392
# R73
# L254
# R85
# L78
# R52
# L67
# R33
# R99
# R83
# L33
# R833
# L43
# L94
# L70
# R7
# R548
# R53
# L4
# R12
# L12
# R458
# R45
# L97
# R95
# R2
# L36
# R36
# L80
# R516
# R97
# R23
# L43
# R58
# R257
# R19
# L79
# L63
# R95
# L34
# L17
# L7
# L81
# L61
# R87
# R13
# R65
# R72
# R5
# R95
# L74
# R768
# R3
# L13
# L50
# R81
# R96
# R51
# R1
# L82
# L18
# L1
# R952
# R2
# R964
# L13
# R96
# L93
# R28
# R79
# L975
# L10
# R571
# L40
# L33
# L410
# R501
# L53
# L86
# R4
# R17
# R98
# L47
# R94
# L45
# L3
# R3
# R9
# L53
# L56
# R454
# L32
# R78
# R68
# R927
# L595
# R186
# R219
# R85
# L690
# R52
# L49
# R97
# L40
# R40
# R61
# R339
# L54
# R54
# L25
# R120
# R5
# R79
# R21
# R52
# L63
# R55
# R94
# L838
# R84
# L67
# L37
# L45
# L756
# L6
# L15
# L58
# L39
# R39
# L52
# L48
# R59
# R84
# R57
# L601
# R446
# L22
# R27
# R50
# L83
# L17
# L43
# L30
# R11
# R9
# R28
# L10
# R16
# L994
# L87
# R509
# L39
# R68
# R24
# R326
# L788
# L84
# L662
# R80
# R67
# R231
# L32
# R47
# L75
# L5
# R34
# R14
# L24
# L25
# L14
# R65
# R34
# L678
# L673
# L92
# R54
# R95
# L64
# R59
# L77
# R34
# L16
# R42
# L533
# R53
# L659
# L96
# L59
# R63
# R96
# R819
# R81
# L35
# R93
# L58
# R54
# R43
# R3
# L1
# L70
# L60
# L1
# L97
# L71
# R24
# R68
# R48
# L14
# R74
# R51
# R49
# R27
# L18
# R59
# L68
# R133
# L36
# L97
# L35
# L30
# R54
# L38
# R67
# L46
# L61
# L740
# L55
# R915
# R551
# R18
# R88
# R12
# R77
# R23
# L47
# L45
# R15
# L144
# R43
# L85
# R48
# L85
# L67
# L33
# L70
# L99
# L45
# L5
# L70
# R39
# L50
# L98
# R329
# L67
# R36
# R47
# L47
# L98
# L437
# R63
# R86
# R86
# L55
# L45
# R74
# L56
# L6
# L6
# L97
# R715
# L24
# L12
# R73
# L59
# L2
# L7
# L93
# R53
# R47
# L499
# L3
# L77
# R27
# L3
# L12
# L33
# R52
# R30
# R18
# L39
# R4
# L665
# R56
# L77
# L90
# R711
# L77
# L65
# R547
# R895
# L41
# L59
# R42
# R32
# R726
# R27
# L564
# R65
# R94
# L297
# L25
# L10
# L89
# R99
# R1
# R99
# L58
# L71
# R95
# L66
# R29
# R72
# L1
# R19
# L994
# R604
# R71
# L72
# L11
# R21
# L83
# R954
# L9
# L541
# L59
# R58
# L66
# L92
# R67
# L67
# L11
# R70
# L268
# R63
# R59
# L74
# L39
# L66
# R66
# L567
# L33
# L698
# R437
# L894
# L645
# L6
# L28
# L66
# L9
# R44
# L603
# L32
# R69
# L69
# R70
# L970
# L59
# L41
# R92
# L8
# L77
# L7
# L29
# L271
# L88
# L48
# R12
# L99
# L77
# L32
# L68
# R9
# L9
# L69
# R48
# L476
# R897
# L88
# L49
# R40
# R897
# L355
# R655
# L11
# L16
# L73
# L92
# L8
# L88
# R88
# R28
# L82
# R54
# L69
# R69
# R94
# R43
# R88
# L117
# L8
# L7
# R81
# L86
# R24
# L782
# L79
# R88
# L918
# L21
# R356
# L56
# R96
# R98
# R706
# R81
# L81
# R19
# L519
# L724
# R97
# R27
# L20
# R56
# L9
# R454
# R19
# L70
# R64
# L94
# R37
# R63
# R69
# L625
# R56
# R19
# R481
# L52
# R52
# R42
# R1
# R90
# R67
# R35
# R612
# L747
# L50
# R50
# L17
# L83
# L71
# L29
# L38
# L71
# R9
# L69
# L177
# R48
# L2
# L10
# L26
# R36
# L74
# L26
# L17
# R43
# L726
# L734
# R37
# L3
# R45
# L88
# R76
# R67
# R36
# R37
# R84
# L78
# R21
# R34
# R66
# R81
# L75
# L606
# L466
# R21
# R35
# L90
# L94
# R94
# R5
# R901
# L6
# L414
# R70
# L92
# L12
# L53
# R205
# R896
# R59
# L60
# R1
# R232
# L932
# R454
# R2
# L56
# R943
# L1
# R594
# R64
# R3
# R363
# L34
# L32
# R22
# R97
# L19
# R42
# L42
# L17
# L49
# R462
# L1
# L716
# L79
# R12
# L24
# R12
# L398
# R898
# R3
# R97
# R57
# L73
# R52
# R43
# R6
# R15
# L70
# R68
# R35
# R41
# R26
# L57
# L44
# R93
# R8
# R95
# R5
# R57
# L14
# L29
# L84
# L35
# L937
# R92
# L20
# L75
# L55
# R74
# R26
# L18
# R18
# R5
# R60
# L65
# L142
# L23
# R684
# L19
# R34
# L34
# R65
# L467
# L98
# R48
# L35
# L150
# L74
# R11
# R74
# L61
# R9
# R378
# R41
# L44
# L85
# L8
# L20
# L96
# R12
# R61
# L99
# R37
# R32
# R27
# L33
# R75
# L97
# L63
# L353
# L78
# L44
# L14
# R549
# R53
# R24
# L77
# R84
# L84
# R31
# R14
# L57
# L88
# L53
# L47
# L754
# L46
# L9
# L3
# L601
# L87
# L556
# L33
# L411
# L11
# L89
# R276
# L276
# R94
# R354
# L47
# L82
# R84
# L76
# R28
# R609
# R39
# R510
# L13
# L76
# L80
# L993
# R725
# R81
# L32
# L25
# R78
# L78
# L709
# L97
# L85
# L75
# L279
# L42
# R50
# R7
# R30
# R481
# L81
# R39
# L85
# L54
# L55
# R55
# L73
# L38
# L389
# L899
# L1
# L515
# L85
# R711
# L72
# L11
# L72
# L59
# R94
# R9
# R88
# L88
# L90
# R25
# R15
# R50
# R84
# R93
# L4
# L63
# L10
# R424
# R968
# R31
# L23
# L29
# R666
# R32
# R3
# L72
# L59
# R59
# L19
# L335
# L89
# L77
# L42
# R62
# L9
# R93
# R66
# R24
# R31
# L5
# R47
# R14
# R23
# R16
# L513
# R88
# L75
# R14
# R94
# L68
# L56
# R16
# L853
# L17
# L80
# L67
# L24
# R89
# L58
# R310
# R59
# L135
# R41
# R35
# R560
# R40
# R29
# L51
# R404
# R28
# R15
# L25
# L946
# L54
# R59
# L51
# R226
# R40
# L537
# R51
# R34
# R20
# R58
# L36
# L22
# R58
# L52
# R552
# R41
# L632
# R81
# R10
# R42
# L27
# R13
# R69
# R50
# L47
# R48
# L70
# R85
# L5
# R42
# L44
# L56
# R47
# R53
# L8
# L85
# L84
# L96
# L227
# R347
# R58
# L5
# L62
# L56
# L82
# L663
# R20
# R943
# R45
# R215
# R40
# L67
# R38
# L506
# R37
# L2
# L10
# L59
# R819
# L10
# L91
# L14
# L992
# L25
# L424
# L970
# R76
# R43
# L83
# R12
# L72
# L774
# L39
# R13
# R42
# R4
# R79
# R521
# L46
# L95
# R54
# L159
# R67
# R33
# L181
# R97
# R584
# L20
# R25
# R33
# R62
# R78
# L730
# L448
# R43
# L47
# R204
# L7
# R79
# R39
# L12
# R1
# L18
# L82
# R74
# R33
# L45
# R45
# L886
# L75
# R1
# R57
# L4
# L51
# R451
# R53
# L54
# R1
# R19
# R81
# L503
# L70
# R44
# R3
# L29
# L42
# R97
# L11
# R56
# R55
# R50
# L66
# L84
# R31
# L31
# R822
# L28
# R436
# R70
# R71
# L59
# R30
# R56
# R2
# R6
# L6
# R32
# L19
# R187
# R989
# R11
# L1
# L73
# R31
# R453
# R60
# L92
# R64
# R63
# L5
# L88
# L12
# L495
# L5
# R10
# L510
# R76
# L489
# L87
# R80
# L80
# L16
# L84
# L21
# R48
# L1
# L25
# L3
# L15
# L83
# L620
# R420
# R92
# R18
# R60
# R29
# L812
# L50
# L56
# R70
# R49
# L3
# L97
# R59
# L40
# L763
# R87
# L95
# R52
# L77
# R271
# L94
# L52
# R70
# R50
# R32
# L46
# R3
# L57
# R14
# R35
# L49
# R58
# R158
# R18
# L38
# L96
# R73
# R70
# L43
# R881
# L250
# R37
# L16
# L79
# R27
# R63
# R830
# R64
# L50
# R93
# R7
# R94
# L1
# L63
# R14
# R6
# R38
# R303
# L26
# L972
# R37
# R17
# R46
# L33
# R33
# L21
# R413
# L92
# R95
# L95
# L83
# R37
# L76
# L78
# L66
# L734
# R74
# R615
# L58
# L94
# R84
# L47
# L630
# L99
# L45
# R22
# R78
# L963
# L37
# R56
# R44
# L5
# L858
# R63
# L76
# L24
# R82
# L96
# R82
# L25
# R771
# R86
# L54
# L46
# R73
# R27
# L23
# L67
# R61
# R29
# R132
# R608
# R92
# L22
# L10
# R79
# L79
# L6
# R706
# L49
# R46
# L1
# R4
# L7
# R33
# L8
# R85
# L821
# R6
# L64
# L974
# L16
# R14
# L48
# L50
# L28
# L72
# L50
# L76
# R3
# R413
# L40
# L61
# L43
# R4
# L68
# L7
# R62
# R31
# R1
# L19
# L63
# R25
# L90
# L92
# L73
# L5
# R31
# R26
# L97
# R38
# L73
# L4
# L13
# L10
# R83
# L2
# R19
# L27
# L70
# L96
# R20
# L27
# R91
# R91
# L37
# L50
# L95
# R58
# R42
# L96
# R51
# R31
# L86
# R41
# R79
# L76
# L83
# R39
# R45
# R46
# R8
# L50
# L40
# R31
# R3
# L6
# L33
# R25
# R7
# R30
# L10
# R48
# L44
# R15
# L49
# L34
# L44
# R3
# R32
# R16
# L28
# L50
# L19
# R42
# R49
# R27
# L40
# L20
# R3
# L11
# L35
# R11
# R44
# L29
# R20
# L16
# R50
# L14
# L17
# L27
# L3
# R19
# R24
# R42
# R45
# L2
# R27
# L41
# L46
# R16
# R30
# R2
# """
# example_password = solve_safe_password_part2(example_rotations)
# print(f"Example Password (should be 6): {example_password}") # Output: 6






# def fib(n):
#     if n <= 2:
#         return 1 
#     else:
#         a = b = 1 
#         for i in range(3, n+1):
#             c = a + b 
#             a = b
#             b = c 

#         return c 

# print(fib(100))







#import heapq

# def dijkstra(graph, start):
#     """
#     Implements Dijkstra's Algorithm to find the shortest paths from the start node.
    
#     :param graph: Dictionary where keys are nodes and values are lists of (neighbor, weight) tuples.
#     :param start: The starting node.
#     :return: Dictionary with shortest distances from start to each node.
#     """
#     # Min-heap to store (distance, node)
#     min_heap = [(0, start)]
#     shortest_distances = {node: float('inf') for node in graph}
#     shortest_distances[start] = 0

#     while min_heap:
#         # print(min_heap)
#         current_distance, current_node = heapq.heappop(min_heap)

#         # Skip if we already found a shorter path
#         if current_distance > shortest_distances[current_node]:
#             continue

#         for neighbor, weight in graph[current_node]:
#             distance = current_distance + weight

#             # If found a shorter path, update
#             if distance < shortest_distances[neighbor]:
#                 shortest_distances[neighbor] = distance
#                 heapq.heappush(min_heap, (distance, neighbor))

#     return shortest_distances

# # Example usage:
# graph = {
#     'A': [('B', 2), ('C', 6)],
#     'B': [('A', 2), ('D', 5), ('E', 3)],
#     'C': [('A', 6), ('D', 8), ('F', 4)],
#     'D': [('B', 5), ('C', 8), ('G', 7), ('H', 6)],
#     'E': [('B', 3), ('I', 5), ('J', 9)],
#     'F': [('C', 4), ('J', 2), ('K', 8)],
#     'G': [('D', 7), ('L', 3), ('M', 4)],
#     'H': [('D', 6), ('M', 7), ('N', 5)],
#     'I': [('E', 5), ('O', 6)],
#     'J': [('E', 9), ('F', 2), ('O', 3), ('P', 7)],
#     'K': [('F', 8), ('P', 2), ('Q', 5)],
#     'L': [('G', 3), ('Q', 4), ('R', 6)],
#     'M': [('G', 4), ('H', 7), ('R', 5)],
#     'N': [('H', 5), ('S', 6), ('T', 8)],
#     'O': [('I', 6), ('J', 3), ('U', 4)],
#     'P': [('J', 7), ('K', 2), ('V', 6)],
#     'Q': [('K', 5), ('L', 4), ('W', 7)],
#     'R': [('L', 6), ('M', 5), ('X', 5)],
#     'S': [('N', 6), ('T', 3), ('Y', 7)],
#     'T': [('N', 8), ('S', 3), ('Z', 6)],
#     'U': [('O', 4), ('V', 2)],
#     'V': [('P', 6), ('U', 2), ('W', 4)],
#     'W': [('Q', 7), ('V', 4), ('X', 6)],
#     'X': [('R', 5), ('W', 6), ('Y', 4)],
#     'Y': [('S', 7), ('X', 4), ('Z', 3)],
#     'Z': [('T', 6), ('Y', 3)]
# }

# start_node = 'A'
# shortest_paths = dijkstra(graph, start_node)
# print(shortest_paths)






# from collections import defaultdict
# from collections import deque



# filename = 'jot.txt'
# x_bound = y_bound = 70
# time = 1024


# def print_map(b_map, b_path: list = None):
#     if b_path is None:
#         b_path = []
#     print()
#     for py in range(y_bound + 1):
#         print_line = ''
#         for px in range(x_bound + 1):
#             if (px, py) in b_path:
#                 print_line += '👠'
#             elif b_map[(px, py)] == '#':
#                 print_line += '🤖'
#             else:
#                 print_line += '◼️'
#         print(print_line)
#     print()


# def find_path(bt: int, byte_list: list):
#     # Use BFS to find a path
#     directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#     start = (0, 0)
#     goal = (x_bound, y_bound)
#     b_map = defaultdict(str)
#     # Populate the map with all the falling bytes by time t
#     for t in range(bt):
#         b_map[byte_list[t]] = '#'

#     # Queue to check the adjacent squares. This is a deque because we will be removing items from the front
#     move_queue = deque([start])
#     # If you step from square A to square B, then paths[B] = A. Helps reconstruct the path and prevent backtracking
#     paths = dict()
#     paths[start] = None
#     while move_queue:
#         # Remove the oldest item from the queue. Once the queue is empty, this will stop looking
#         current_loc = move_queue.popleft()
#         if current_loc == goal:
#             break

#         cx, cy = current_loc
#         # For each neighbor, we'll check if it's in bounds first.
#         # Then if we haven't been there already (in the paths dict) and it's not corrupted, add it to the queue
#         for this_dir in directions:
#             dx, dy = this_dir
#             nx, ny = cx + dx, cy + dy
#             if nx in range(0, x_bound + 1) and ny in range(0, y_bound + 1):
#                 if (nx, ny) not in paths and b_map[(nx, ny)] != '#':
#                     move_queue.append((cx + dx, cy + dy))
#                     paths[(cx + dx, cy + dy)] = current_loc

#     # Now we will start at the goal and walk backwards along the paths dict to find the actual path
#     current_loc = goal
#     best_path = []
#     while current_loc != start:
#         best_path.append(current_loc)
#         try:
#             current_loc = paths[current_loc]
#         except KeyError:
#             # If we never reached the goal, then paths dict will not have an entry for the goal tuple and will
#             # give a KeyError. Return an empty list
#             return []
#     # If we did reach the goal, return the path
#     return best_path


# with open(filename) as f:
#     lines = [line.rstrip() for line in f]

# falling_bytes = []
# for this_line in lines:
#     bx, by = [int(x) for x in this_line.split(',')]
#     falling_bytes.append((bx, by))

# print(f"Part 1: {len(find_path(time, falling_bytes))}")






# from collections import deque
# import heapq

# with open('jot.txt') as path_score:
#     lines = [line.rstrip() for line in path_score]

# x_bound = len(lines[0])
# y_bound = len(lines)
# maze = dict()
# solution_paths = []

# for y, this_line in enumerate(lines):
#     for x, this_char in enumerate(this_line):
#         if this_char == 'S':
#             start = (x, y)
#             maze[(x, y)] = '.'
#         elif this_char == 'E':
#             goal = (x, y)
#             maze[(x, y)] = '.'
#         else:
#             maze[(x, y)] = this_char


# def find_path(maze_map: dict, s: tuple, g: tuple):
#     d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#     direction = 0
#     score = 0
#     queue = [(score, s, direction)]
#     heapq.heapify(queue)
#     visited_from = {(s, direction): None}
#     scores = {(s, direction): 0}
#     final_score = 0
#     while queue:
#         current_score, (cx, cy), current_d = heapq.heappop(queue)
#         if (cx, cy) == g:
#             final_score = current_score
#             break
#         for nd, (dx, dy) in enumerate(d):
#             nx, ny = cx + dx, cy + dy
#             if maze_map[(nx, ny)] != '#':
#                 if nd == current_d:  # If we're going in the same direction we're facing
#                     new_score = current_score + 1
#                 elif nd == (current_d + 1) % 4:  # We are turning clockwise
#                     new_score = current_score + 1001
#                 elif nd == (current_d - 1) % 4:  # We are turning counter-clockwise
#                     new_score = current_score + 1001
#                 # else:  # We are turning around
#                 #     new_score = current_score + 2001
#                 if ((nx, ny), nd) not in visited_from or new_score < scores[((nx, ny), nd)]: 
                    
#                     # try:
#                     #     if new_score < scores[((nx, ny), nd)]:
#                     #         pass
#                     # except KeyError:
#                     #     pass
#                     visited_from[((nx, ny), nd)] = ((cx, cy), current_d)
#                     scores[((nx, ny), nd)] = new_score
#                     heapq.heappush(queue, (new_score, (nx, ny), nd))
#             else:
#                 pass

#     next_coord, next_dir = visited_from[(goal, current_d)]
#     path = [next_coord]
#     while next_coord != start:
#         next_coord, next_dir = visited_from[(next_coord, next_dir)]
#         path.append(next_coord)
#     return [path, final_score]


# optimal_path, path_score = find_path(maze, start, goal)
# print(f"Part 1: {path_score}")




# def draw_path(maze_map: dict, maze_path: list):
#     print()
#     for py in range(0, y_bound):
#         new_line = ''
#         for px in range(0, x_bound):
#             if (px, py) == start:
#                 new_line += '⭐'
#             elif (px, py) == goal:
#                 new_line += '⭐'
#             elif (px, py) in maze_path :
#                 new_line += '👠'
#             elif maze_map[(px, py)] == '#':
#                 new_line += '🪨'
#             else:
#                 new_line += '◼️'
#         print(new_line)
#     print()

# import math 
# import heapq

# heights = [[1,2,2],[3,8,2],[5,3,5]]


# def f(heights):
#     m, n = map(len, (heights, heights[0]))
#     efforts = [[math.inf] * n for _ in range(m)]
#     efforts[0][0] = 0
#     heap = [(0, 0, 0)]
#     while heap:
#         effort, x, y = heapq.heappop(heap) 
#         if (x, y) == (m - 1, n - 1):
#             return effort
#         for r, c in (x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y):
#             if m > r >= 0 <= c < n:
#                 next_effort = max(effort, abs(heights[r][c] - heights[x][y]))
#                 if efforts[r][c] > next_effort:
#                     efforts[r][c] = next_effort
#                     heapq.heappush(heap, (next_effort, r, c)) 
#         print(x, y )
# print(f(heights))



# import re

# filename = 'jot.txt'
# area_width = 101
# area_height = 103


# with open(filename) as f:
#     lines = [line.rstrip() for line in f]

# robots = []
# for this_line in lines:
#     robot_nums = [int(x) for x in re.findall('-?\d+', this_line)]
#     robots.append(robot_nums)

# def get_quadrant(x: int, y: int):
#     if x == area_width // 2 or y == area_height // 2:
#         return None
#     if x < area_width // 2 and y < area_height // 2:
#         return 0
#     if x > area_width // 2 and y < area_height // 2:
#         return 1
#     if x < area_width // 2 and y > area_height // 2:
#         return 2
#     if x > area_width // 2 and y > area_height // 2:
#         return 3


# def get_robot_position(bot: list, s: int):
#     px, py = bot[0], bot[1]
#     dx, dy = bot[2], bot[3]
#     px = (px + dx * s) % area_width
#     py = (py + dy * s) % area_height
#     return px, py


# safety_scores = []
# for i in range(10000):
#     quadrants = [0, 0, 0, 0]
#     for this_robot in robots:
#         bx, by = get_robot_position(this_robot, i)
#         q = get_quadrant(bx, by)
#         if q is not None:
#             quadrants[q] += 1
#     safety_score = 1
#     for q in quadrants:
#         safety_score *= q
#     safety_scores.append(safety_score)
#     if i == 100:
#         print(f"Part 1: {safety_score}")

# # Guess: the picture will have a minimum safety score because lots of robots will be grouped together
# min_safety = safety_scores.index(min(safety_scores))


# # Print the picture, for fun (and confirmation)
# tree_picture = set()
# for this_robot in robots:
#     tree_picture.add(get_robot_position(this_robot, min_safety))
# # print(tree_picture)


# # for this_y in range(area_height):
# #     print_line = ''
# #     for this_x in range(area_width):
# #         if (this_x, this_y) in tree_picture:
# #             print_line += '🟢'
# #         else:
# #             print_line += '⬜'
# #     print(print_line)

# print(f"Part 2: {min_safety}")


# ax = 17
# ay = 86

# bx = 84 
# by = 37

# x = 7870 
# y = 6450

# arr = []
# found = 0
# for A in range(101):
#     arr.append([])
#     arr[-1].append( [A*ax, A*ay] )
#     for B in range(101):
#         arr[-1].append([A*ax + B*bx, A*ay + B*by])
#         # if A == 80 and B == 40 :
#         #     print(arr[-1][-1])
#         if arr[-1][-1] == [x, y]:
#             found = 1
#             print("cost: ", A*3 + B*1)
#             break
#     # print(arr)       
#     if found == 1:
#         break 

 
     





# from collections import namedtuple

# with open('jot.txt') as f:
#     lines = [line.rstrip() for line in f]

# garden = dict()
# y_bound = len(lines)
# x_bound = len(lines[0])
# for y, this_line in enumerate(lines):
#     for x, this_char in enumerate(this_line):
#         garden[(x, y)] = this_char
# to_be_visited = list(garden.keys())

# Region = namedtuple('Region', ['coords', 'area', 'min_c', 'max_c'])


# def flood_fill(start_coord: tuple, g_map: dict) -> list:
#     # We will keep track of the x and y boundaries of this region to make the ray casting faster later on
#     min_x, min_y = x_bound, y_bound
#     max_x, max_y = 0, 0
#     queue = [start_coord]  # queue keeps track of coordinates we have to check
#     this_crop = g_map[start_coord]  # What letter crop are we even looking for
#     this_region = set()  # Will keep all the unique coordinates in this region of this_crop
#     checked = set()  # All the coordinates we've already checked
#     while queue:  # Keep checking the queue while it isn't empty
#         cx, cy = queue.pop()
#         if g_map[(cx, cy)] == this_crop:
#             # We've found this_crop, add it to this_region and update boundaries as needed
#             this_region.add((cx, cy))
#             if cx < min_x: min_x = cx
#             if cy < min_y: min_y = cy
#             if cx > max_x: max_x = cx
#             if cy > max_y: max_y = cy
#             # Now lets check all its neighbors
#             for diff_coord in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#                 dx, dy = diff_coord
#                 # If it is in range and we haven't checked this neighbor already, add it to the queue
#                 if cx + dx in range(0, x_bound) and cy + dy in range(0, y_bound):
#                     if (cx + dx, cy + dy) not in checked:
#                         queue.append((cx + dx, cy + dy))
#         checked.add((cx, cy))
#     return [this_region, (min_x, min_y), (max_x, max_y)]


# def ray_cast(this_region: set, mins: tuple, maxs: tuple) -> int:
#     # We will draw horizontal lines and then vertical lines across the area where this_region is located
#     # Every time we pass from outside the region to inside the region, or inside to outside, we've found a perimeter
#     perimeter = 0
#     minx, miny = mins
#     maxx, maxy = maxs
#     # Cast rays horizontally, counting every time we pass a boundary
#     for this_y in range(miny, maxy + 1):
#         in_bound = False  # Always start out of bounds
#         for this_x in range(minx, maxx + 1):
#             # If we've entered the region from outside
#             if (this_x, this_y) in this_region and not in_bound:
#                 in_bound = True
#                 perimeter += 1
#             # If we've exited the region
#             elif (this_x, this_y) not in this_region and in_bound:
#                 in_bound = False
#                 perimeter += 1
#         if in_bound:  # If we've reached the end of our checking zone and we are inside the region
#             perimeter += 1

#     # Do the same thing but vertically
#     for this_x in range(minx, maxx + 1):
#         in_bound = False
#         for this_y in range(miny, maxy + 1):
#             if (this_x, this_y) in this_region and not in_bound:
#                 in_bound = True
#                 perimeter += 1
#             elif (this_x, this_y) not in this_region and in_bound:
#                 in_bound = False
#                 perimeter += 1
#         if in_bound:
#             perimeter += 1

#     return perimeter


# def count_corners(this_region: set) -> int:
#     # Outside corners:
#     # ?.   # If (x, y-1) (up) and (x-1, y) (left) are different from A
#     # .A<  # Then A (with a caret pointed to it) is an outside corner

#     # Inside corners:
#     # VA   # if (x, y-1) and (x-1, y) are the same and (x-1, y-1) is different from A,
#     # AA<  # then A (with a caret pointed to it) is an inside corner

#     # Then check each rotation. A single coordinate can be a corner up to 4 times so we must check all ways.

#     outside_check = [
#         # different, different
#         [(0, -1), (-1, 0)],
#         [(0, -1), (1, 0)],
#         [(1, 0), (0, 1)],
#         [(-1, 0), (0, 1)]
#     ]
#     inside_check = [
#         # Same, same, different
#         [(0, -1), (-1, 0), (-1, -1)],
#         [(0, -1), (1, 0), (1, -1)],
#         [(1, 0), (0, 1), (1, 1)],
#         [(-1, 0), (0, 1), (-1, 1)]
#     ]
#     corner_count = 0
#     for coord in this_region:
#         cx, cy = coord
#         for o_coords in outside_check:
#             ox1, oy1 = o_coords[0]
#             ox2, oy2 = o_coords[1]
#             if (cx + ox1, cy + oy1) not in this_region and (cx + ox2, cy + oy2) not in this_region:
#                 corner_count += 1
#         for i_coords in inside_check:
#             ox1, oy1 = i_coords[0]
#             ox2, oy2 = i_coords[1]
#             ox3, oy3 = i_coords[2]
#             if ((cx + ox1, cy + oy1) in this_region and (cx + ox2, cy + oy2) in this_region and
#                     (cx + ox3, cy + oy3) not in this_region):
#                 corner_count += 1
#     return corner_count


# regions = []
# while to_be_visited:
#     start_c = to_be_visited.pop()
#     region_coords, min_coords, max_coords = flood_fill(start_c, garden)
#     region_size = len(region_coords)
#     regions.append(Region(region_coords, region_size, min_coords, max_coords))
#     to_be_visited = list(set(to_be_visited).difference(region_coords))

# cost = 0
# cost2 = 0
# for r in regions:
#     for s in r.coords:
#         perim = ray_cast(r.coords, r.min_c, r.max_c)
#         corners = count_corners(r.coords)
#         cost += r.area * perim
#         cost2 += r.area * corners
#         break

# print(f"Part 1: {cost}")
# print(f"Part 2: {cost2}")


# # from collections import defaultdict



# # def split(num):
# #     num = str(num) 
# #     mid = len(num)//2 
# #     return [ int(num[:mid]), int(num[mid:])  ]

# # dp = defaultdict(int)

# stones = [0, 7, 198844, 5687836, 58, 2478, 25475, 894] 
# for stone in stones: # this could be table dp
#     dp[(stone, 0)] += 1

# # blinks = 75

# # # stone, step, cnt
# # # 
# # # check the previous record = step - 1
# # # current key number += prev(step-1) 


# for blink in range(1, blinks+1):
#     nxt_dp = defaultdict(int)
#     for (stone, step), count in dp.items():
#         if blink == step+1:
#             if stone == 0:
#                 nxt_dp[(1, blink)] += count
#             elif len(str(stone)) % 2 == 0:
#                 a, b = split(stone)
#                 nxt_dp[(a, blink)] += count
#                 nxt_dp[(b, blink)] += count
#             else:
#                 nxt_dp[(stone*2024, blink)] += count
#     dp = nxt_dp
# print(len(dp))
# print(sum( count for (a, b), count in dp.items() if b == blinks))
                





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


