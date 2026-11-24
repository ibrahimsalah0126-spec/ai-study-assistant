import streamlit as st
import re
from collections import Counter

st.set_page_config(page_title="AI Study Assistant", page_icon="📚", layout="wide")

st.title("📚 AI Study Assistant")
st.caption("A beginner-friendly study helper: summarize notes, extract key terms, and practice with quizzes.")

st.info(
    "This starter version works without an AI API key. Its summaries and questions are "
    "rule-based demonstrations, not a substitute for checking your course material."
)

def clean_sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.!?؟])\s+|\n+", text) if len(s.strip()) > 20]

def summarize(text, count=4):
    sentences = clean_sentences(text)
    if not sentences:
        return "Add a little more text (at least a few complete sentences) to create a summary."
    words = re.findall(r"\b[\w'-]+\b", text.lower())
    stop = set("""the a an and or but is are was were be been being of to in on for with by as at from
                  this that these those it its into than then also can may might should would could
                  و في من على إلى عن أن إن هو هي هذا هذه ذلك التي الذي مع أو ثم كما""".split())
    frequencies = Counter(w for w in words if w not in stop and len(w) > 2)
    scored = []
    for index, sentence in enumerate(sentences):
        tokens = re.findall(r"\b[\w'-]+\b", sentence.lower())
        score = sum(frequencies[t] for t in tokens) / max(len(tokens), 1)
        scored.append((score, index, sentence))
    chosen = sorted(scored, reverse=True)[:count]
    chosen = sorted(chosen, key=lambda item: item[1])
    return "\n\n".join(f"• {item[2]}" for item in chosen)

def key_terms(text, limit=12):
    words = re.findall(r"\b[\w'-]{4,}\b", text.lower())
    stop = set("this that with from have were their there which about into when what your they them then than also".split())
    return Counter(w for w in words if w not in stop).most_common(limit)

def make_flashcards(text, limit=10):
    terms = key_terms(text, limit)
    return terms

tab1, tab2, tab3 = st.tabs(["📝 Summarize", "🔑 Key terms", "🧠 Practice"])

with st.sidebar:
    st.header("Your study session")
    language = st.selectbox("Output language", ["Keep source language", "English", "Arabic"])
    st.caption("Language selection is a reminder for your own workflow in this starter build.")

with tab1:
    st.subheader("Summarize your notes")
    source = st.text_area("Paste lecture notes or study material", height=260, key="summary_text",
                          placeholder="Paste your notes here...")
    amount = st.slider("Number of key sentences", 2, 8, 4)
    if st.button("Create summary", type="primary", key="summarize"):
        if source.strip():
            st.markdown(summarize(source, amount))
        else:
            st.warning("Please paste some study material first.")

with tab2:
    st.subheader("Find frequently used terms")
    terms_source = st.text_area("Paste text to analyze", height=220, key="terms_text")
    if st.button("Extract key terms", key="terms"):
        if terms_source.strip():
            terms = key_terms(terms_source)
            if terms:
                for term, frequency in terms:
                    st.write(f"**{term}** — {frequency} occurrence(s)")
            else:
                st.write("No key terms found.")
        else:
            st.warning("Please paste some text first.")

with tab3:
    st.subheader("Build a quick revision activity")
    quiz_source = st.text_area("Paste notes for revision", height=220, key="quiz_text")
    if st.button("Generate flashcard prompts", key="flashcards"):
        if quiz_source.strip():
            terms = make_flashcards(quiz_source)
            if terms:
                st.session_state["flashcards"] = terms
            else:
                st.warning("Not enough text to identify terms.")
        else:
            st.warning("Please paste some notes first.")

    if "flashcards" in st.session_state:
        st.write("Try explaining each term without looking at your notes:")
        for i, (term, frequency) in enumerate(st.session_state["flashcards"], 1):
            with st.expander(f"Card {i}: {term}"):
                st.write(f"Appears {frequency} time(s) in your text. Write your own definition, then check your notes.")

st.divider()
st.caption("Open-source learning project • Contributions and suggestions are welcome.")
