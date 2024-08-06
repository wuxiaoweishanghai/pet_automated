import operator

def check_result(expected_data, code, actual_data):
    if int(code) != 200:
        raise Exception("interface status code error!\n actual code is %s" % (code))
    for key in expected_data.keys():
        if expected_data[key] == '@ignored':
            expected_data[key] = ''
            if key in actual_data.keys():
                actual_data[key] = ''
    result = operator.eq(expected_data, actual_data)
    if not result:
        raise Exception("entriely check failed！ %s ! = %s" % (expected_data, actual_data ))