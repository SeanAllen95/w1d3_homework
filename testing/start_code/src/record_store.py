def get_name(record_store):
    return record_store["name"]

def find_record_by_title(record_title, record_store):
    for record in record_store["records"]:
        if record["title"] == record_title:
            return record

def sell_record(record3, record_store):
    record_store["money"] += 8
    record_store["records"].pop(record3)
    

