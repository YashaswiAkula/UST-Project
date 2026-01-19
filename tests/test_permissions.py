from Project import permissions
from Project import database

def test_customer_cannot_update_ticket():
    ticket = database.create_ticket(
        title="Test",
        description="Test",
        created_by="customer1@example.com"
    )

    assert permissions.can_update_ticket(
        "customer1@example.com",
        ticket.id
    ) is False


def test_helper_can_update_assigned_ticket():
    ticket = database.create_ticket(
        title="Test",
        description="Test",
        created_by="customer1@example.com"
    )

    database.update_ticket(
        ticket.id,
        assigned_to="john@support.com",
        changed_by="admin@system.com"
    )

    assert permissions.can_update_ticket(
        "john@support.com",
        ticket.id
    ) is True
