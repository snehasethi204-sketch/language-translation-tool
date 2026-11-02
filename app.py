import streamlit as st
from deep_translator import MyMemoryTranslator

st.set_page_config(page_title="Language Translation Tool")

st.title("🌍 Language Translation Tool")
st.write("Translate your text into different languages.")

languages = {
    "English": "en-GB",
    "Hindi": "hi-IN"
}

text = st.text_area("Enter your text")

source = st.selectbox("Source Language", list(languages.keys()))
target = st.selectbox("Target Language", list(languages.keys()))
if st.button("Translate"):
    if text.strip():
        try:
            result = MyMemoryTranslator(
                source=languages[source],
                target=languages[target]
            ).translate(text)

            st.success("Translation Completed!")
            st.write(result)

        except Exception as e:
            st.error(f"Translation Error: {e}")
    else:
        st.warning("Please enter some text.")