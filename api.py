import requests


class API:

    def get_store_details(self) -> list:
        results = "Request Failed"  # Placeholder if function fails
        url = "https://apimdev.wakefern.com/mockexample/V1/getStoreDetails"  # getStoreDetails URL
        api_key = "4ae9400a1eda4f14b3e7227f24b74b44"

        headers = {
            "User-Agent": "PostmanRuntime/7.36.3",
            "Ocp-Apim-Subscription-Key": api_key  # Update the header key
        }

        try:
            # Print the request details
            print("Request URL:", url)
            print("Request Headers:", headers)

            # Send GET request with headers
            response = requests.get(url, headers=headers)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Save response text in results variable
                results = response.json()
            else:
                # Print an error message if the request was not successful
                print("Error:", response.status_code, response.text)
        except requests.RequestException as e:
            # Handle any errors that occurred during the request
            print("Cannot send request to", url, ":", e)

        return results

    def getItemDetails(self) -> list:
        results = "Request Failed"  # Placeholder if function fails
        url = "https://apimdev.wakefern.com/mockexample/V1/getItemDetails"  # getStoreDetails URL
        api_key = "4ae9400a1eda4f14b3e7227f24b74b44"

        headers = {
            "User-Agent": "PostmanRuntime/7.36.3",
            "Ocp-Apim-Subscription-Key": api_key  # Update the header key
        }

        try:
            # Print the request details
            print("Request URL:", url)
            print("Request Headers:", headers)

            # Send GET request with headers
            response = requests.get(url, headers=headers)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Save response text in results variable
                results = response.json()
            else:
                # Print an error message if the request was not successful
                print("Error:", response.status_code, response.text)
        except requests.RequestException as e:
            # Handle any errors that occurred during the request
            print("Cannot send request to", url, ":", e)

        return results



# if __name__ == "__main__":
#     # Print results from the API
#     print(type(getItemDetails()))
#     print(getItemDetails())
