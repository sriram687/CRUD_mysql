import mysql.connector
import streamlit as st

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="crud_new1"
)
myCursor = mydb.cursor()
print("connection established")


def main():
    st.title("CRUD Operations with mysql")

    option = st.sidebar.selectbox("Select an operation ", ("create", "read", "update", "delete"))
    if option == "create":
        st.subheader("create a record")
        name = st.text_input("enter the name")
        email = st.text_input("enter the email")
        if st.button("create"):
            sql = "insert into users(name, email) values(%s,%s)"
            val = (name, email)
            myCursor.execute(sql, val)
            mydb.commit()
            st.success("record created successfully!!")

    elif option == "update":
        st.subheader("update a record")
        sid = st.number_input("enter ID", min_value=1)
        name = st.text_input("enter new name")
        email = st.text_input("enter new email")
        if st.button("update"):
            sql = "update users set name =%s, email=%s where id =%s"
            val = (name, email, sid)
            myCursor.execute(sql, val)
            mydb.commit()
            st.success("record updated successfully!!!")

    elif option == "read":
        st.subheader("read a record")
        myCursor.execute("select * from users")
        result = myCursor.fetchall()
        for row in result:
            st.write(row)

    elif option == "delete":
        st.subheader("delete a record")
        sid = st.number_input("enter ID", min_value=1)
        if st.button("delete"):
            sql = "delete from users where id =%s"
            val = (sid,)
            myCursor.execute(sql, val)
            mydb.commit()
            st.success("record deleted successfully!!")


if __name__ == "__main__":
    main()
