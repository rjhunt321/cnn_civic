#!/usr/bin/python
#
# Copyright (c) GCI
#

import os
import requests
import json
import sys

# variables
url = 'https://www.googleapis.com/civicinfo/v2'
key = 'AIzaSyCJoI3EDt94g4Z3dZZUD00VVjhx4w1vIg8'

def test_get_representative_info_by_address(td='no'):
    """ 
    Checks response to valid representatives query using "address" parameter. 
    Verifies response code 200, and response data 'kind' & address.
    """
    test_data = [ 'Elections-201', 'Checks representatives endpoint for status 200 reps list']
    if td == 'yes':
        return test_data

    # test variables
    exp_response_kind = 'civicinfo#representativeInfoResponse'
    zip = '80517'

    print(test_data)  
    print("  sending elections query")
    URL = os.path.join(url, "representatives?address=" + zip + "&key="  + key)
    response = requests.get(url=URL, timeout=15)
    json_response = json.loads(response.content)
    print("  " + str(response))
    # print(json_response)  # [DEBUG]

    # initialize results needed for multiple asserts
    test_result = 'pass'
    error_string = 'None'
    results = []

    try:
        assert str(response.status_code) == "200"
    except AssertionError:
        test_result = 'fail'
        error_string = "expected 200 but recieved " + str(response.status_code)
        # fail and end test now!
        results.append(test_result)
        results.append(error_string)
        print(results)
        return results 
    
    print("  checking response for correct 'kind'")
    try:
        assert json_response['kind'] == exp_response_kind
    except AssertionError:
        test_result = 'fail'
        error_string = "Response 'kind' expected: " + exp_response_kind + ", but recieved: " + str(json_response['kind'])
        # fail and end test now!
        results.append(test_result)
        results.append(error_string)
        print(results)
        return results

    print("  checking response for correct address")
    try:
        assert json_response['normalizedInput']['zip'] == zip
    except AssertionError:
        test_result = 'fail'
        error_string = "Address expected: " + zip + ", but recieved: " + str(json_response['normalizedInput']['zip'])
        # [TODO] instead of zipcode, check different variable data value like city
    # fail and end test now, or continue checking other things while appending the pass/fail/warning(w/error) of each diff check before ending

    results.append(test_result)
    results.append(error_string)
    print(results)
    return results

def test_get_representative_info_by_division(td='no'):
    """ 
    Checks response to a valid representatives query using the "ocdId" route. 
    Verifies response code 200, and response key 'divisions'.
    """
    test_data = [ 'Elections-202', 'Checks representatives/ocdId endpoint for status 200 reps list']
    if td == 'yes':
        return test_data

    # test variables
    ocdId = 'ocd-division/country:us/state:co'
    ocdId_f = 'ocd-division%2Fcountry%3Aus%2Fstate%3Aco'  # formated

    print(test_data)  
    print("  sending elections query")
    URL = os.path.join(url, "representatives/" + ocdId_f + "?key="  + key)
    response = requests.get(url=URL, timeout=15)
    json_response = json.loads(response.content)
    print("  " + str(response))
    # print(json_response)  # [DEBUG]

    # initialize results needed for multiple asserts
    test_result = 'pass'
    error_string = 'None'
    results = []

    try:
        assert str(response.status_code) == "200"
    except AssertionError:
        test_result = 'fail'
        error_string = "expected 200 but recieved " + str(response.status_code)
        # fail and end test now!
        results.append(test_result)
        results.append(error_string)
        print(results)
        return results 
    
    print("  checking response for correct 'ocd-division'")
    try:
        assert ocdId in json_response['divisions']
    except AssertionError:
        test_result = 'fail'
        error_string = "Didn't recieve the expected response, recieved: " + str(json_response['divisions'])
    # fail and end test now, or continue checking other things while appending the pass/fail/warning(w/error) of each diff check before ending

    results.append(test_result)
    results.append(error_string)
    print(results)
    return results

# [TODO] incorporate important "optional" parameters
if __name__ == "__main__":
    test_get_representative_info_by_address()
    test_get_representative_info_by_division()

    



