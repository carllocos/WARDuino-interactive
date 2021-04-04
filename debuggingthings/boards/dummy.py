
dummy_dump = {'dump':
                {'pc': '0x3ffbec62',
                 'fp': '12',
                 'start': ['0x3ffbebf0'],
                 'breakpoints': ['0x3ffbec62'],
                 'functions': [{'fidx': '0x0', 'from': '0x3ffbec44', 'to': '0x3ffbec44', 'args': 1, 'locs': 0},
                               {'fidx': '0x1', 'from': '0x3ffbec47', 'to': '0x3ffbec47', 'args': 1, 'locs': 0},
                               {'fidx': '0x2', 'from': '0x3ffbec4a', 'to': '0x3ffbec4a', 'args': 1, 'locs': 0},
                               {'fidx': '0x3', 'from': '0x3ffbec4d', 'to': '0x3ffbec4d', 'args': 1, 'locs': 0},
                               {'fidx': '0x4', 'from': '0x3ffbec50', 'to': '0x3ffbec65', 'args': 1, 'locs': 0},
                               {'fidx': '0x5', 'from': '0x3ffbec70', 'to': '0x3ffbeca6', 'args': 0, 'locs': 4}],
                 'callstack': [{'type': 0, 'fidx': '0x5', 'sp': -1, 'fp': -1, 'block_key': '0x0', 'ra': '0x3ffbec39'},
                               {'type': 3, 'fidx': '0x0', 'sp': 3, 'fp': 0, 'block_key': '0x3ffbec8b', 'ra': '0x3ffbec8d'},
                               {'type': 0, 'fidx': '0x4', 'sp': 7, 'fp': 0, 'block_key': '0x0', 'ra': '0x3ffbec99'},
                               {'type': 4, 'fidx': '0x0', 'sp': 9, 'fp': 8, 'block_key': '0x3ffbec55', 'ra': '0x3ffbec57'},
                               {'type': 0, 'fidx': '0x4', 'sp': 8, 'fp': 8, 'block_key': '0x0', 'ra': '0x3ffbec5e'},
                               {'type': 4, 'fidx': '0x0', 'sp': 10, 'fp': 9, 'block_key': '0x3ffbec55', 'ra': '0x3ffbec57'},
                               {'type': 0, 'fidx': '0x4', 'sp': 9, 'fp': 9, 'block_key': '0x0', 'ra': '0x3ffbec5e'},
                               {'type': 4, 'fidx': '0x0', 'sp': 11, 'fp': 10, 'block_key': '0x3ffbec55', 'ra': '0x3ffbec57'},
                               {'type': 0, 'fidx': '0x4', 'sp': 10, 'fp': 10, 'block_key': '0x0', 'ra': '0x3ffbec5e'},
                               {'type': 4, 'fidx': '0x0', 'sp': 12, 'fp': 11, 'block_key': '0x3ffbec55', 'ra': '0x3ffbec57'},
                               {'type': 0, 'fidx': '0x4', 'sp': 11, 'fp': 11, 'block_key': '0x0', 'ra': '0x3ffbec5e'},
                               {'type': 4, 'fidx': '0x0', 'sp': 13, 'fp': 12, 'block_key': '0x3ffbec55', 'ra': '0x3ffbec57'}],
                 'globals': [{'idx': 0, 'type': 'i32', 'value': 0}, {'idx': 1, 'type': 'i64', 'value': 64}, {'idx': 2, 'type': 'f32', 'value': 32.32, 'f64': 64.6464}],
                 'table': {'max': 5, 'init': 5, 'elements': [5, 3, 2, 1, 0]},
                 'memory': {'pages': 2,
                            'max' : 32768,
                            'init': 2,
                            'bytes': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'},
                 'br_table': {'size': 256,
                              'labels': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}},
              'bp': '0x3ffbec62'}
dummy_vals = {'local_dump': {'stack':
                             [{'idx': 0, 'type': 'f32', 'value': 32.3232002},
                              {'idx': 1, 'type': 'f64', 'value': 64.646464},
                              {'idx': 2, 'type': 'i32', 'value': 32},
                              {'idx': 3, 'type': 'i64', 'value': 64},
                              {'idx': 4, 'type': 'f32', 'value': 32.3232002},
                              {'idx': 5, 'type': 'f64', 'value': 64.646464},
                              {'idx': 6, 'type': 'i32', 'value': 32},
                              {'idx': 7, 'type': 'i64', 'value': 64},
                              {'idx': 8, 'type': 'i32', 'value': 5},
                              {'idx': 9, 'type': 'i32', 'value': 4},
                              {'idx': 10, 'type': 'i32', 'value': 3},
                              {'idx': 11, 'type': 'i32', 'value': 2},
                              {'idx': 12, 'type': 'i32', 'value': 1}]},
              'bp': '0x3ffbec62'}
