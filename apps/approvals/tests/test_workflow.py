from apps.approvals.workflow import approve_request, reject_request
import pytest

def test_first_approval_moves_request_to_second_approval():
    request = {
        "status": "PENDING_MANAGER_1",
        "approver_1": "manager_b",
        "approver_2": "manager_c",
    }

    approve_request(request, actor="manager_b")

    assert request["status"] == "PENDING_MANAGER_2"

def test_wrong_employee_cannot_approve_request():
    request = {
        "status": "PENDING_MANAGER_1",
        "approver_1": "manager_b",
        "approver_2": "manager_c",
    }

    with pytest.raises(ValueError):
        approve_request(request, actor="employee_d")

    assert request["status"] == "PENDING_MANAGER_1"

def test_second_approval_completes_request():
    request = {
        "status": "PENDING_MANAGER_2",
        "approver_1": "manager_b",
        "approver_2": "manager_c",
    }

    approve_request(request, actor="manager_c")

    assert request["status"] == "APPROVED"


def test_first_approver_cannot_approve_second_stage():
    request = {
        "status": "PENDING_MANAGER_2",
        "approver_1": "manager_b",
        "approver_2": "manager_c",
    }

    with pytest.raises(ValueError):
        approve_request(request, actor="manager_b")

    assert request["status"] == "PENDING_MANAGER_2"

def test_first_approver_can_reject_request():
    request = {
        "status": "PENDING_MANAGER_1",
        "approver_1": "manager_b",
        "approver_2": "manager_c",
    }

    reject_request(request, actor="manager_b")

    assert request["status"] == "REJECTED"


def test_second_approver_can_reject_request():
    request = {
        "status": "PENDING_MANAGER_2",
        "approver_1": "manager_b",
        "approver_2": "manager_c",
    }

    reject_request(request, actor="manager_c")

    assert request["status"] == "REJECTED"

def test_first_approver_cannot_reject_second_stage():
    request = {
        "status": "PENDING_MANAGER_2",
        "approver_1": "manager_b",
        "approver_2": "manager_c",
    }

    with pytest.raises(ValueError):
        reject_request(request, actor="manager_b")

    assert request["status"] == "PENDING_MANAGER_2"

def test_wrong_employee_cannot_reject_request():
    request = {
        "status": "PENDING_MANAGER_1",
        "approver_1": "manager_b",
        "approver_2": "manager_c",
    }

    with pytest.raises(ValueError):
        reject_request(request, actor="employee_d")

    assert request["status"] == "PENDING_MANAGER_1"

def test_approved_request_cannot_be_approved_again():
    request = {
        "status": "APPROVED",
        "approver_1": "manager_b",
        "approver_2": "manager_c",
    }

    with pytest.raises(ValueError):
        approve_request(request, actor="manager_c")

    assert request["status"] == "APPROVED"

def test_rejected_request_cannot_be_approved_again():
    request = {
        "status": "REJECTED",
        "approver_1": "manager_b",
        "approver_2": "manager_c",
    }

    with pytest.raises(ValueError):
        approve_request(request, actor="manager_c")

    assert request["status"] == "REJECTED"