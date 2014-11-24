##encoding=utf8

from pyzillow import ZillowWrapper, GetDeepSearchResults, GetUpdatedPropertyDetails
from HSH.Data.pk import load_pk, dump_pk

zlid = "X1-ZWz1dyb91hllhn_6msnx"
zillow_data = ZillowWrapper(zlid)

address, zipcode = "5134 HARTWICK RD", "77093"
deep_search_response = zillow_data.get_deep_search_results(address, zipcode)
result = GetDeepSearchResults(deep_search_response)
# print(result.zillow_id) # 37253404
# dump_pk(result.zillow_id, "result_zillow_id.p")

# zillow_id = load_pk("result_zillow_id.p")
# print(zillow_id, type(zillow_id))
updated_property_details_response = zillow_data.get_updated_property_details(result.zillow_id)
result = GetUpdatedPropertyDetails(updated_property_details_response) 
dump_pk(result, "zillow.p")