 request_info = {
                "req_id": req_id,
                "base_url": base_url,
                "entry_data": entry_json.get("CPF_CNPJ"),
                "access_token": tk_response,
                "decision_name": decision_name,
                "contract_id": entry_json.get("customerId"),
                "channel": entry_json.get("canal"),
                "operator_role": entry_json.get("Operator_role"),
                "pdv": entry_json.get("PDV"),
                "product": entry_json.get("producto"),
                "maximum_viability_customer": entry_json.get("maximum_viability_custome")
                }
