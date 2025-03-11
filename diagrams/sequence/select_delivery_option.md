
sequenceDiagram
    actor Member
    participant UI
    participant Controller
    participant User
    participant Order

    Member->>+UI: Click change location
    UI->>+Controller: update_user_location(order_id, location_id)
    Controller->>+User: get_location_by_id(location_id)
    loop location in Location
        User->>+Location: get location
        Location->>-User: return location
    end
    User-->>-Controller: return location
    loop order in Order
        Controller->>+Order: get_order_by_id(order_id)
        Order-->>-Controller: order
    end
    Controller->>+Order: select_location(location)
    Order-->>-Controller: return None
    Controller-->>-UI: return html element with new location
    UI-->>+Member: render html element
