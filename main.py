import sys
from models import Role, Audition
from database import Session, engine, Base

Base.metadata.create_all(engine)
session = Session()

def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Manage Roles")
        print("2. Manage Auditions")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            manage_roles()
        elif choice == '2':
            manage_auditions()
        elif choice == '3':
            print("Exiting...")
            session.close()
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

def manage_roles():
    while True:
        print("\nRole Management")
        print("1. Create Role")
        print("2. Update Role")
        print("3. Delete Role")
        print("4. View All Roles")
        print("5. Find Role by Name")
        print("6. View Auditions for Role")
        print("7. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            create_role()
        elif choice == '2':
            update_role()
        elif choice == '3':
            delete_role()
        elif choice == '4':
            view_all_roles()
        elif choice == '5':
            find_role_by_name()
        elif choice == '6':
            view_auditions_for_role()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_auditions():
    while True:
        print("\nAudition Management")
        print("1. Create Audition")
        print("2. Update Audition")
        print("3. Delete Audition")
        print("4. View All Auditions")
        print("5. Find Audition by Actor")
        print("6. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            create_audition()
        elif choice == '2':
            update_audition()
        elif choice == '3':
            delete_audition()
        elif choice == '4':
            view_all_auditions()
        elif choice == '5':
            find_audition_by_actor()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def create_role():
    name = input("Enter role name: ")
    if name:
        role = Role(name=name)
        session.add(role)
        session.commit()
        print(f"Role '{name}' created successfully.")
    else:
        print("Role name cannot be empty.")

def update_role():
    role_id = input("Enter role ID to update: ")
    role = session.query(Role).get(role_id)
    if role:
        new_name = input(f"Enter new name for role '{role.name}': ")
        if new_name:
            role.name = new_name
            session.commit()
            print(f"Role ID {role_id} updated successfully.")
        else:
            print("Role name cannot be empty.")
    else:
        print("Role not found.")

def delete_role():
    role_id = input("Enter role ID to delete: ")
    role = session.query(Role).get(role_id)
    if role:
        session.delete(role)
        session.commit()
        print(f"Role '{role.name}' deleted successfully.")
    else:
        print("Role not found.")

def view_all_roles():
    roles = session.query(Role).all()
    if roles:
        for role in roles:
            print(f"ID: {role.id}, Name: {role.name}")
    else:
        print("No roles found.")

def find_role_by_name():
    name = input("Enter role name to find: ")
    roles = session.query(Role).filter(Role.name.like(f"%{name}%")).all()
    if roles:
        for role in roles:
            print(f"ID: {role.id}, Name: {role.name}")
    else:
        print("No roles found.")

def view_auditions_for_role():
    role_id = input("Enter role ID to view auditions: ")
    role = session.query(Role).get(role_id)
    if role:
        auditions = role.auditions
        if auditions:
            for audition in auditions:
                print(f"ID: {audition.id}, Actor: {audition.actor}")
        else:
            print("No auditions found for this role.")
    else:
        print("Role not found.")

def create_audition():
    actor = input("Enter actor name: ")
    role_id = input("Enter role ID: ")
    if actor and role_id:
        role = session.query(Role).get(role_id)
        if role:
            audition = Audition(actor=actor, role=role)
            session.add(audition)
            session.commit()
            print(f"Audition for actor '{actor}' created successfully.")
        else:
            print("Role not found.")
    else:
        print("Actor name and role ID cannot be empty.")

def update_audition():
    audition_id = input("Enter audition ID to update: ")
    audition = session.query(Audition).get(audition_id)
    if audition:
        new_actor = input(f"Enter new actor name for audition ID {audition.id}: ")
        if new_actor:
            audition.actor = new_actor
            session.commit()
            print(f"Audition ID {audition.id} updated successfully.")
        else:
            print("Actor name cannot be empty.")
    else:
        print("Audition not found.")

def delete_audition():
    audition_id = input("Enter audition ID to delete: ")
    audition = session.query(Audition).get(audition_id)
    if audition:
        session.delete(audition)
        session.commit()
        print("Audition deleted successfully.")
    else:
        print("Audition not found.")

def view_all_auditions():
    auditions = session.query(Audition).all()
    if auditions:
        for audition in auditions:
            print(f"ID: {audition.id}, Actor: {audition.actor}, Role ID: {audition.role_id}")
    else:
        print("No auditions found.")

def find_audition_by_actor():
    actor = input("Enter actor name to find: ")
    auditions = session.query(Audition).filter(Audition.actor.like(f"%{actor}%")).all()
    if auditions:
        for audition in auditions:
            print(f"ID: {audition.id}, Actor: {audition.actor}, Role ID: {audition.role_id}")
    else:
        print("No auditions found.")

if __name__ == "__main__":
    main_menu()
