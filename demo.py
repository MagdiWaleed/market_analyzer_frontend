import streamlit as st
import json
from models import MarketDetails
import time
import requests



if "data" in st.session_state.keys() and st.session_state.data_here:

    marketDetails = MarketDetails(st.session_state['data'])
    col1, col2 = st.columns([4 , 1],vertical_alignment='bottom')
    with col1:
        st.title("Analysis Results:- ")
    with col2:
        st.download_button(
                label="Download Analysis Result",
                data=json.dumps(st.session_state.data),               
                file_name="analysis result.json",        
                mime="application/json"       
            )
    st.markdown(f"The product is **{marketDetails.product}** which is in: **{marketDetails.marketType}** .")
    st.markdown(f"**Description About The Market**: {marketDetails.description}")

    st.markdown("---")
    with st.expander("**The Gap in This Market**: "):
        for i, gap in enumerate(marketDetails.finalAnswer.gapInMarket):
            st.markdown(f' {i+1}) {gap}')
    with st.expander("**The Recommendations**: "):
        for i, recommendation in enumerate(marketDetails.finalAnswer.recommendations):
            st.markdown(f'  {i}) {recommendation}')
        
    st.markdown('---')
    st.title(f"Competitors Companies :- ({len(marketDetails.companies)})")
    for i,company in enumerate(marketDetails.companies):
        with st.expander(f"{company.name}"):
            tab1, tab2 = st.tabs(["Company Overview",f"Company's Products  ({len(company.products)})"])
            with tab1:
                st.markdown(f"**Overall Advantages**:-")
                st.markdown(company.overall_advantages)
                st.markdown("---")
                st.markdown(f"**Overall Weaknesses**:- ")
                st.markdown(company.overal_weaknesses)
            with tab2:
                for t,product in enumerate(company.products):
                        st.markdown(f" {t+1}) {product.name}")
                        t1,t2 = st.tabs(['Advantage',"Weaknesses"])
                        with t1:
                            st.markdown(product.advantages)
                        
                        with t2:
                            st.markdown(product.weaknesses)
                        st.markdown('---')
            
            
        

    # for key,value in st.session_state.items():
    #     if not key.startswith("delete-") and not key.startswith("add_button-"):
    #         continue

    #     if value and key.startswith("add_button-"):
    #         company_index = int(key.split("add_button-")[-1])
    #         st.session_state.data[company_index]['products'].append({"name": st.session_state[f"add_text-company-{company_index}"]})
    #         st.rerun()
    #     if value and key.startswith("delete-"):
    #         company_index = int(key.split("delete-company-")[-1].split("-")[0])
    #         product_index = int(key.split("-product-")[-1])
    #         del st.session_state.data[company_index]['products'][product_index]
    #         print(company_index,product_index)
    #         st.rerun()
else:
    uploaded_file = st.file_uploader("Upload Analysis Result to Visualize it.", type="json")

    if prompt := st.chat_input("Type your message...") or uploaded_file:
        with st.spinner("Anaylzing"):
            if uploaded_file:
                st.session_state['data'] = json.load(uploaded_file)
                st.session_state['data_here']=True
                st.rerun()
            else:
                response = requests.post("http://127.0.0.1:5000/analyze", json={"message":prompt})
                data = response.json()['data']
                st.session_state['data'] = data
                
                with open("data.json", "w") as f:
                    json.dump(data, f, indent=4)
                
                st.session_state['data_here']=True
                st.rerun()


