# import streamlit as st
# import random

# st.title("🎯 Guess Computer vs Golu")

# # Initialize session state
# if "number" not in st.session_state:
#     st.session_state.number = random.randint(1, 100)
#     st.session_state.attempts = 0
#     st.session_state.game_over = False

# st.write("Computer ne **1 se 100** ke beech ek number soch liya hai 😄")

# guess = st.number_input(
#     "Apna number guess karo 👇",
#     min_value=1,
#     max_value=100,
#     step=1
# )

# if st.button("Guess"):
#     if not st.session_state.game_over:
#         st.session_state.attempts += 1

#         if guess < st.session_state.number:
#             st.warning("📉 Too Low")
#         elif guess > st.session_state.number:
#             st.warning("📈 Too High")
#         else:
#             st.success("🎉 Golu Won!")
#             st.info(f"Attempts: {st.session_state.attempts}")
#             st.session_state.game_over = True

# if st.session_state.game_over:
#     if st.button("🔄 Play Again"):
#         st.session_state.number = random.randint(1, 100)
#         st.session_state.attempts = 0
#         st.session_state.game_over = False


