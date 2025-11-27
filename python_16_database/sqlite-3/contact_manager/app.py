import streamlit as st
from db import create_table, add_contact, get_contacts, delete_contact

st.set_page_config(page_title="Contact Manager", layout="centered")

# Create table if not exists
create_table()

st.title("📒 Simple Contact Manager")

# ---- Add Contact ----
st.subheader("Add New Contact")

name = st.text_input("Name")
phone = st.text_input("Phone")

if st.button("Add Contact"):
    if name and phone:
        add_contact(name, phone)
        st.success("Contact added!")
    else:
        st.error("Please enter name and phone!")

st.write("---")

# ---- Show Contacts ----
st.subheader("All Contacts")

contacts = get_contacts()

if contacts:
    for c in contacts:
        st.write(f"### {c[1]} — {c[2]}")
        st.caption(f"ID: {c[0]}")
        st.write("---")
else:
    st.info("No contacts found.")

# ---- Delete ----
st.subheader("Delete Contact")

delete_id = st.number_input("Enter Contact ID", min_value=0)

if st.button("Delete Contact"):
    delete_contact(delete_id)
    st.warning("Contact deleted!")
