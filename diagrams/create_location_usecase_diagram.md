```mermaid
sequenceDiagram
    actor Member
    participant UI
    participant Controller
    participant User
    participant Location    

    Member->>+UI: submit new location
    UI->>+Controller: create_location()
    loop for user in User
       Controller->>+User:  get_user_by_id(user_id)
       User->>-Controller: return user
    end
    Controller->>+User: add_location()
    User->>+Location: create new location instance
    Location-->>-User: return new_location
    User-->>Controller: return new_location
    Controller-->>-UI: return new_location JSON
    UI-->>-Member: display new location