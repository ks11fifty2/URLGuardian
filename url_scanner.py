import apikeys
import requests

def scan_url(url_to_scan):
    """
    Scan a URL using the VirusTotal API and return the scan results.

    :param url_to_scan: The URL to be scanned
    :return: Number of positive flags indicating malicious URL
    """
    # Your VirusTotal API key
    API_KEY = apikeys.VT_API_KEY
    virus_total_url = "https://www.virustotal.com/api/v3/urls"

    headers = {
        "x-apikey": API_KEY,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    params = {'url': url_to_scan}

    # Send the POST request to scan the URL
    # The VirustTotal API returns an ID for given URL which can be used to retrieve further information
    response = requests.post(virus_total_url, headers=headers, data=params)

    if response.status_code == 200:
        response_json = response.json()
        # Extract the scan_id to check the results later
        scan_id = response_json["data"]["id"]

        print("----------------------------------------------------------------------------------------")
        print(url_to_scan)
        print(f"Scan ID: {scan_id}")
        

        # Retrieve the results using the scan_id
        # The GET request retrieves detailed JSON data for the corresponding ID including Malicious flags
        result_url = f"https://www.virustotal.com/api/v3/analyses/{scan_id}"
        result_response = requests.get(result_url, headers=headers)

        if result_response.status_code == 200:
            result_json = result_response.json()
            positives = result_json['data']['attributes']['stats']['malicious']

            return positives
        else:
            return {
                "error": f"Error retrieving the scan results: {result_response.status_code} - {result_response.text}"
            }
            
    else:
        return {
            "error": f"Error: {response.status_code} - {response.text}"
        }

#url = ""
#result = scan_url(url)
#print(result)
