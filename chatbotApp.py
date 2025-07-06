import streamlit as st
import pandas as pd
df = pd.read_csv('finantialStatements(ms&tesla).csv')
df.head(7)
cols=['Total_Revenue', 'Net_Income', 'Total_assets', 'Total_Libilities', 'Cash_flow_opera']
for numCol in cols:
    df[numCol] = df[numCol].astype(str).str.replace(",","")
    df[numCol] = pd.to_numeric(df[numCol],errors='coerce')

def AiChatbot(Query):
    Query = Query.lower()

    if "total revenue" in Query:
        if 'tesla' in Query and '2024' in Query:
            value = df[(df['CompanyName'] == 'Tesla') & (df['Years'] == 2024)]['Total_Revenue'].values
            return f"The Tesla's Total Revenue in 2024 was: ${value[0]:,.0f} Million" if len(value) else 'Data not found.'
        elif 'microsoft' in Query and '2024' in Query:
            value = df[(df['CompanyName'] == 'Microsoft') & (df['Years'] == 2024)]['Total_Revenue'].values
            return f"The Microsoft's Total Revenue in 2024 was: ${value[0]:,.0f} Million" if len(value) else 'Data not found.'

    elif "net income" in Query:
        if "tesla" in Query and "change" in Query and "2023" in Query and "2024" in Query:
            val_23 = df[(df['CompanyName'] == 'Tesla') & (df['Years'] == 2023)]['Net_Income'].values
            val_24 = df[(df['CompanyName'] == 'Tesla') & (df['Years'] == 2024)]['Net_Income'].values
            if len(val_23) and len(val_24):
                change = val_24[0] - val_23[0]
                return f"Tesla's net income changed by ${change:,.0f} million from 2023 to 2024."
            else:
                return "Net income data for Tesla in 2023 or 2024 is missing."

        elif "tesla" in Query and "2023" in Query:
            val = df[(df['CompanyName'] == 'Tesla') & (df['Years'] == 2023)]['Net_Income'].values
            return f"The net income of Tesla in 2023 was ${val[0]:,.0f} Million" if len(val) else "Data not found."

        elif "tesla" in Query and "2024" in Query:
            val = df[(df['CompanyName'] == 'Tesla') & (df['Years'] == 2024)]['Net_Income'].values
            return f"The net income of Tesla in 2024 was ${val[0]:,.0f} Million" if len(val) else "Data not found."

        elif "microsoft" in Query and "change" in Query and "2023" in Query and "2024" in Query:
            val_23 = df[(df['CompanyName'] == 'Microsoft') & (df['Years'] == 2023)]['Net_Income'].values
            val_24 = df[(df['CompanyName'] == 'Microsoft') & (df['Years'] == 2024)]['Net_Income'].values
            if len(val_23) and len(val_24):
                change = val_24[0] - val_23[0]
                return f"Microsoft's net income changed by ${change:,.0f} million from 2023 to 2024."
            else:
                return "Net income data for Microsoft in 2023 or 2024 is missing."

        elif "microsoft" in Query and "2023" in Query:
            val = df[(df['CompanyName'] == 'Microsoft') & (df['Years'] == 2023)]['Net_Income'].values
            return f"The net income of Microsoft in 2023 was ${val[0]:,.0f} Million" if len(val) else "Data not found."

        elif "microsoft" in Query and "2024" in Query:
            val = df[(df['CompanyName'] == 'Microsoft') & (df['Years'] == 2024)]['Net_Income'].values
            return f"The net income of Microsoft in 2024 was ${val[0]:,.0f} Million" if len(val) else "Data not found."

    return "Sorry, I can only answer a few predefined financial questions."

# Streamlit UI

st.set_page_config(page_title="Financial Chatbot", layout="centered")

# Sidebar
with st.sidebar:
    st.title("💬 How to use")
    st.markdown("""
    Type questions like:
    - What is Tesla's total revenue in 2024?
    - How did Microsoft's net income change?
    - Net income of Tesla in 2023?
    """)
    st.markdown("---")
    st.info("Currently supports predefined questions about revenue and net income for Tesla and Microsoft (2022–2024).")

# Main title
st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>📊 Financial Chatbot</h1>", unsafe_allow_html=True)

# Input
user_query = st.text_input("Ask a question:", placeholder="e.g., What is Tesla's total revenue in 2024?")

# Trigger response
if st.button("Get Answer"):
    if user_query:
        response = AiChatbot(user_query)
        st.success(response)
    else:
        st.warning("Please enter a question.")

# Footer
st.markdown("<hr><small>Created by Muhammad Hanzala — Prototype version</small>", unsafe_allow_html=True)
