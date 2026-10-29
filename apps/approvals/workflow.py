def approve_request(request, actor):
    if request["status"] == "PENDING_MANAGER_1" and request["approver_1"] == actor:
        request["status"] = "PENDING_MANAGER_2"

    elif request["status"] == "PENDING_MANAGER_2" and request["approver_2"] == actor:
        request["status"] = "APPROVED"

    else:
        raise ValueError("Approval not allowed for this actor or request state")

def reject_request(request, actor):
    if request["status"] == "PENDING_MANAGER_1" and request["approver_1"] == actor:
        request["status"] = "REJECTED"

    elif request["status"] == "PENDING_MANAGER_2" and request["approver_2"] == actor:
        request["status"] = "REJECTED"

    else:
        raise ValueError("Approval not allowed for this actor or request state")