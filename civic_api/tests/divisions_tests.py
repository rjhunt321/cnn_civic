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

def test_get_divisions_query(td='no'):
    """ 
    Checks for proper response to /elections query. 
    Verifies response status 200. Verifies response includes the correct 'kind' & saves election ids for testing /voterinfo endpoint
    """
    test_data = [ 'Representatives-101', 'Checks elections query for status 200 representatives list']
    if td == 'yes':
        return test_data

    # test variables
    response_kind = 'civicinfo#divisionSearchResponse'
    any_part_of_ocdId = 'CO'

    print(test_data)  
    print("  sending divisions query using ocdId part: " + any_part_of_ocdId)
    URL = os.path.join(url, "divisions?query=" + any_part_of_ocdId + "&key="  + key)
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
        assert json_response['kind'] == response_kind
    except AssertionError:
        test_result = 'fail'
        error_string = "Kind expected: " + response_kind + ", but recieved: " + str(json_response['kind'])
        # fail and end test now!
        results.append(test_result)
        results.append(error_string)
        print(results)
        return results 
    
    print("  checking response for the 'results' key")
    try:
        assert 'results' in json_response
    except AssertionError:
        test_result = 'fail'
        error_string = "Didn't recieve the 'results' key"
    # fail and end test now, or continue checking other things while appending the pass/fail/warning(w/error) of each diff check before ending


    results = []
    results.append(test_result)
    results.append(error_string)
    print(results)
    return results


if __name__ == "__main__":
    test_get_divisions_query()


