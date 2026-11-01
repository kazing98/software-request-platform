from apps.approvals.workflow import SoftwareRequest
import pytest

def test_first_approval_moves_request_to_second_approval():
    request = SoftwareRequest(
        requester="Rohan",
        software="xyz",
        approver_1="manager_b",
        approver_2="manager_c",
        status="PENDING_MANAGER_1"
    )

    request.approve(actor="manager_b")

    assert request.status.value == "PENDING_MANAGER_2"

def test_wrong_employee_cannot_approve_request():
    request = SoftwareRequest(
        requester="Rohan",
        software="xyz",
        approver_1="manager_b",
        approver_2="manager_c",
        status="PENDING_MANAGER_1"
    )

    with pytest.raises(ValueError):
        request.approve(actor="employee_d")

    assert request.status.value == "PENDING_MANAGER_1"

def test_second_approval_completes_request():
    request = SoftwareRequest(
        requester="Rohan",
        software="xyz",
        approver_1="manager_b",
        approver_2="manager_c",
        status="PENDING_MANAGER_2"
    )

    request.approve(actor="manager_c")

    assert request.status.value == "APPROVED"


def test_first_approver_cannot_approve_second_stage():
    request = SoftwareRequest(
        requester="Rohan",
        software="xyz",
        approver_1="manager_b",
        approver_2="manager_c",
        status="PENDING_MANAGER_2"
    )

    with pytest.raises(ValueError):
        request.approve(actor="manager_b")

    assert request.status.value == "PENDING_MANAGER_2"

def test_first_approver_can_reject_request():
    request = SoftwareRequest(
        requester="Rohan",
        software="xyz",
        approver_1="manager_b",
        approver_2="manager_c",
        status="PENDING_MANAGER_1"
    )

    request.reject(actor="manager_b")

    assert request.status.value == "REJECTED"


def test_second_approver_can_reject_request():
    request = SoftwareRequest(
        requester="Rohan",
        software="xyz",
        approver_1="manager_b",
        approver_2="manager_c",
        status="PENDING_MANAGER_2"
    )

    request.reject(actor="manager_c")

    assert request.status.value == "REJECTED"

def test_first_approver_cannot_reject_second_stage():
    request = SoftwareRequest(
        requester="Rohan",
        software="xyz",
        approver_1="manager_b",
        approver_2="manager_c",
        status="PENDING_MANAGER_2"
    )

    with pytest.raises(ValueError):
        request.reject(actor="manager_b")

    assert request.status.value == "PENDING_MANAGER_2"

def test_wrong_employee_cannot_reject_request():
    request = SoftwareRequest(
        requester="Rohan",
        software="xyz",
        approver_1="manager_b",
        approver_2="manager_c",
        status="PENDING_MANAGER_1"
    )

    with pytest.raises(ValueError):
        request.reject(actor="employee_d")

    assert request.status.value == "PENDING_MANAGER_1"

def test_approved_request_cannot_be_approved_again():
    request = SoftwareRequest(
        requester="Rohan",
        software="xyz",
        approver_1="manager_b",
        approver_2="manager_c",
        status="APPROVED"
    )

    with pytest.raises(ValueError):
        request.approve(actor="manager_c")

    assert request.status.value == "APPROVED"

def test_rejected_request_cannot_be_approved_again():
    request = SoftwareRequest(
        requester="Rohan",
        software="xyz",
        approver_1="manager_b",
        approver_2="manager_c",
        status="REJECTED"
    )

    with pytest.raises(ValueError):
        request.approve(actor="manager_c")

    assert request.status.value == "REJECTED"

def test_request_with_same_approvers():
    with pytest.raises(ValueError, match="Approvers must be different."):
        SoftwareRequest(
            requester="Rohan",
            software="xyz",
            approver_1="manager_b",
            approver_2="manager_b",
        )

def test_request_with_invalid_status():
    with pytest.raises(ValueError, match="Invalid request status."):
        SoftwareRequest(
            requester="Rohan",
            software="xyz",
            approver_1="manager_b",
            approver_2="manager_c",
            status="INVALID"
        )