import streamlit as st
import sqlite3

DATABASE_PATH = "database/canteen.db"

st.set_page_config(
    page_title="University Canteen",
    page_icon="🍽️",
    layout="wide"
)

st.title("🍽️ University Canteen")
st.subheader("Digital Menu")

connection = sqlite3.connect(DATABASE_PATH)

menu = connection.execute(
    """
    SELECT id, name, category, price
    FROM menu_items
    WHERE available = 1
    ORDER BY category, name
    """
).fetchall()

connection.close()

if not menu:
    st.warning("No menu items are currently available.")
else:
    categories = sorted(set(item[2] for item in menu))

    for category in categories:
        st.header(category)

        category_items = [
            item for item in menu
            if item[2] == category
        ]

        columns = st.columns(3)

        for index, item in enumerate(category_items):
            item_id, name, item_category, price = item

            with columns[index % 3]:
                st.markdown(f"### {name}")
                st.write(f"💰 ₹{price:.2f}")

                if st.button(
                    f"Add {name}",
                    key=f"add_{item_id}"
                ):
                    st.success(f"{name} added!")