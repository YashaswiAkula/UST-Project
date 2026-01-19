from Project import database
from Project.allocation import auto_assign_ticket, get_available_staff

def test_auto_assign_ticket():
    ticket = database.create_ticket(
        title="Assign me",
        description="Auto assign",
        created_by="customer1@example.com"
    )

    helper = auto_assign_ticket(ticket.id)

    assert helper is not None
    updated = database.get_ticket(ticket.id)
    assert updated.assigned_to == helper


def test_get_available_staff():
    staff = get_available_staff()
    assert len(staff) > 0
    assert "available_capacity" in staff[0]
