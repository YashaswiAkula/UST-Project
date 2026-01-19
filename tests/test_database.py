from Project import database


def test_create_ticket_success():
    ticket = database.create_ticket(
        title="Login issue",
        description="Cannot login",
        priority="High",
        created_by="customer1@example.com"
    )

    assert ticket.id is not None
    assert ticket.status == "Open"
    assert ticket.priority == "High"


def test_create_ticket_invalid_priority():
    try:
        database.create_ticket(
            title="Bad",
            description="Bad",
            priority="Urgent",
            created_by="customer1@example.com"
        )
        assert False, "Should have raised ValueError"
    except ValueError:
        assert True


def test_update_ticket_status():
    ticket = database.create_ticket(
        title="Test",
        description="Test",
        created_by="customer1@example.com"
    )

    updated = database.update_ticket(
        ticket.id,
        status="Resolved",
        changed_by="john@support.com"
    )

    assert updated.status == "Resolved"
    assert updated.resolved_at is not None
