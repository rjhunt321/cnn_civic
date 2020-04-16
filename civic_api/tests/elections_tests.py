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


def test_get_election_query(td='no'):
    """ 
    Checks for proper response to /elections query. 
    Verifies response status 200. Verifies response includes the correct 'kind' & saves election ids for testing /voterinfo endpoint
    """
    test_data = [ 'Representatives-101', 'Checks elections query for status 200 representatives list']
    if td == 'yes':
        return test_data

    # test variables
    response_kind = 'civicinfo#electionsQueryResponse'

    print(test_data)  
    print("  sending elections query")
    URL = os.path.join(url, "elections?key="  + key)
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
    
    print("  saving election ids")
    if 'elections' in json_response:
        global election_ids  # make ids available to other tests
        election_ids = []
        for election in json_response['elections']:
            election_ids.append(election['id'])
        print(election_ids) 
    else:
        test_result = 'fail'
        error_string = "'elections' key missing from response"

    results.append(test_result)
    results.append(error_string)
    print(results)
    return results

def test_get_voterinfo_query(electionIds, td='no'):
    """ 
    Checks response to /voterino query.
    Argument is a list of election ids (i.e., using /elections query, or other).
    For each election, verifies response status 200. Verifies response includes correct 'kind' & address 
    """
    test_data = [ 'Elections-102', 'Checks voterinfo query for status 200 election info']
    if td == 'yes':
        return test_data

    # test variables
    response_kind_expected = 'civicinfo#voterInfoResponse'
    zip = '80517'

    # initialize results needed for multiple asserts
    test_result = 'pass'
    error_string = 'None'
    results = []

    print(test_data)  
    print("  sending voterinfo querys for address: " + zip)

    for id in electionIds:
        URL = os.path.join(url, "voterinfo?electionId=" + id + "&address=" + zip + "&key="  + key)
        response = requests.get(url=URL, timeout=15)
        json_response = json.loads(response.content)
        print("  for election id: " + id)
        print("  " + str(response))
        # print(json_response)  # [DEBUG]
    
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
            assert json_response['kind'] == response_kind_expected
        except AssertionError:
            test_result = 'fail'
            error_string = "Response 'kind' expected: " + response_kind_expected + ", but recieved: " + str(json_response['kind'])
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
            # fail and end test now, or continue checking other things while appending the pass/fail/warning (error) of each one before ending
    
        # [TODO] replace zipcode check with a different "static" value like city or disctrict name
        # [TODO] add presence checks for important "keys" in the response

    results.append(test_result)
    results.append(error_string)
    print(results)
    return results

# [TODO] incorporate important "optional" parameters
if __name__ == "__main__":
    test_get_election_query()
    test_get_voterinfo_query(election_ids)


