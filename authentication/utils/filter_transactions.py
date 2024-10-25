

def filter_transactions_by_address_and_to_attr(result, address):
    data = []
    for res in result["result"]:
        if res["to"] == str(address).lower():
            data.append(
                res
            )
    result["result"] = data
    return result
