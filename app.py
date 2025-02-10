import streamlit as st
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate

def main():
    # Streamlit App Title
    st.title("VSM Generator from Text")

    # User Input
    user_input = st.text_area("Describe your process or workflow:", "Enter your process description here...")

    # Initialize LLM (Hugging Face Hub)
    hf_api_key = <secret_key>
    llm = HuggingFaceHub(repo_id="meta-llama/Llama-2-7b-chat-hf", huggingfacehub_api_token=hf_api_key)

    # VSM Extraction Prompt
    prompt_template = PromptTemplate(
        input_variables=["description"],
        template="""
        Analyze the following process description and generate an optimized Value Stream Map (VSM) with detailed steps, including lead time, cycle time, and any bottlenecks.
        Return only the structured VSM output in the following format, without additional text:
        
        Optimized Value Stream Map:
        
        - **Step 1**: Description (Lead Time: X, Cycle Time: Y, Bottleneck: Z)
        - **Step 2**: Description (Lead Time: X, Cycle Time: Y, Bottleneck: Z)
        ...
        
        **Total Lead Time**: XX
        **Total Cycle Time**: YY
        **Bottlenecks**: List of bottlenecks
        
        Process Description:
        {description}
        """
    )

    # Generate VSM Steps
    if st.button("Generate VSM Steps"):
        prompt = prompt_template.format(description=user_input)
        vsm_steps = llm(prompt)
        
        # Display Output
        st.subheader("Optimized Value Stream Map:")
        st.write(vsm_steps)

if __name__ == "__main__":
    main()
