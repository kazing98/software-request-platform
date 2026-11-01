from enum import Enum

class RequestStatus(Enum):
    PENDING_MANAGER_1 = "PENDING_MANAGER_1"
    PENDING_MANAGER_2 = "PENDING_MANAGER_2"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

class SoftwareRequest:

    def __init__(self, requester, software, approver_1, approver_2, status=RequestStatus.PENDING_MANAGER_1):
        if approver_1 == approver_2:
            raise ValueError("Approvers must be different.")

        if status not in {item.value for item in RequestStatus}:
            raise ValueError("Invalid request status.")

        self.requester = requester
        self.software = software
        self.approver_1 = approver_1
        self.approver_2 = approver_2
        self.status = RequestStatus(status)

    def approve(self, actor):
        if self.status == RequestStatus.PENDING_MANAGER_1 and self.approver_1 == actor:
            self.status = RequestStatus.PENDING_MANAGER_2

        elif self.status == RequestStatus.PENDING_MANAGER_2 and self.approver_2 == actor:
            self.status = RequestStatus.APPROVED

        else:
            raise ValueError("Approval not allowed for this actor or request state")

    def reject(self, actor):
        if self.status == RequestStatus.PENDING_MANAGER_1 and self.approver_1 == actor:
            self.status = RequestStatus.REJECTED

        elif self.status == RequestStatus.PENDING_MANAGER_2 and self.approver_2 == actor:
            self.status = RequestStatus.REJECTED

        else:
            raise ValueError("Approval not allowed for this actor or request state")