import streamlit as st
from utils.ai import AIAgent
from utils.prompts import PromptManager
from css.layout import set_layout, set_header

set_layout()
set_header("Human Rights Review")

prompts = PromptManager()
agent = AIAgent()

def call_gpt(prompt):
    return agent.chat([{"role": "user", "content": prompt}])

def main():
    # Initialize session state for persistent variables
    if "scene" not in st.session_state:
        st.session_state.scene = ""
    if "step_1_response" not in st.session_state:
        st.session_state.step_1_response = ""
    if "step_2_response" not in st.session_state:
        st.session_state.step_2_response = ""
    if "step_3_results" not in st.session_state:
        st.session_state.step_3_results = {}
    if "selected_rights" not in st.session_state:
        st.session_state.selected_rights = []

    # Step 1: Input the scenario
    st.header("Step 1: Input Scenario")
    st.session_state.scene = st.text_area(
        "Input the scenario to review:",
        placeholder="Describe the situation...",
        height=150,
        value=st.session_state.scene  # Persist input
    )
    if st.button("Analyze 1"):
        if not st.session_state.scene.strip():
            st.warning("Please enter a scenario to proceed.")
            return
        try:
            st.subheader("Step 1: Scope of Protection Review")
            step_1_prompt = prompts.get_prompt("step_1", scene=st.session_state.scene)
            step_1_response = agent.chat(
                [{"role": "user", "content": step_1_prompt}],
            )
            st.session_state.step_1_response = step_1_response  # Save response
            st.success("Step 1 Completed!")
        except Exception as e:
            st.error(f"An error occurred during Step 1 analysis: {str(e)}")
    
    # Display Step 1 response
    if st.session_state.step_1_response:
        st.write("### Scope of Protection Analysis:")
        st.write(st.session_state.step_1_response)
        st.markdown("***")

    # Step 2: Select Rights to Analyze
    if st.session_state.step_1_response:
        st.header("Step 2: Select Rights to Analyze")
        protected_rights = ["Personal Liberty", "Freedom of Residence", "Freedom of Religion", "Freedom of Speech"]
        
        # Display checkboxes for selecting rights
        for right in protected_rights:
            if st.checkbox(f"{right}", value=(right in st.session_state.selected_rights)):
                if right not in st.session_state.selected_rights:
                    st.session_state.selected_rights.append(right)
            else:
                if right in st.session_state.selected_rights:
                    st.session_state.selected_rights.remove(right)

        # Button for Step 2 Analysis
        if st.button("Analyze 2"):
            if not st.session_state.selected_rights:
                st.warning("Please select at least one right to analyze.")
                return
            try:
                step_2_prompt = prompts.get_prompt(
                    "step_2",
                    scene=st.session_state.scene,
                    selected_rights=", ".join(st.session_state.selected_rights)
                )
                step_2_response = agent.chat(
                    [{"role": "user", "content": step_2_prompt}],
                )
                st.session_state.step_2_response = step_2_response
                st.success("Step 2 Completed!")
                
            except Exception as e:
                st.error(f"An error occurred during Step 2 analysis: {str(e)}")
    if st.session_state.step_2_response:
        st.write(f"### Intervention Analysis:")
        st.write(st.session_state.step_2_response)
        st.markdown("***")

    # Step 3: Proportionality Analysis
    if st.session_state.step_2_response:
        st.subheader("Step 3: Proportionality Analysis")
        selected_rights_step_3 = []
        for right in st.session_state.selected_rights:
            if st.checkbox(f"{right}", value=False, key=f"proportionality_{right}"):
                selected_rights_step_3.append(right)

        if st.button("Analyze 3"):
            if not selected_rights_step_3:
                st.warning("Please select at least one right to analyze for proportionality.")
                return
            try:
                for right in selected_rights_step_3:
                    # Analyze purpose
                    step_3_purpose_prompt = prompts.get_prompt(
                        "step_3_purpose",
                        right=right,
                        scene=st.session_state.scene
                    )
                    purpose_response = agent.chat([{"role": "user", "content": step_3_purpose_prompt}])
                    st.write(f"### Purpose Analysis for {right}:")
                    st.write(purpose_response)
                    st.markdown("***")

                    # Analyze suitability
                    step_3_suitability_prompt = prompts.get_prompt(
                        "step_3_suitability",
                        right=right,
                        scene=st.session_state.scene
                    )
                    suitability_response = agent.chat([{"role": "user", "content": step_3_suitability_prompt}])
                    st.write(f"### Suitability Analysis for {right}:")
                    st.write(suitability_response)
                    st.markdown("***")

                    # Analyze necessity
                    step_3_necessity_prompt = prompts.get_prompt(
                        "step_3_necessity",
                        right=right,
                        scene=st.session_state.scene
                    )
                    necessity_response = agent.chat([{"role": "user", "content": step_3_necessity_prompt}])
                    st.write(f"### Necessity Analysis for {right}:")
                    st.write(necessity_response)
                    st.markdown("***")

                    # Analyze proportionality
                    step_3_proportionality_prompt = prompts.get_prompt(
                        "step_3_proportionality",
                        right=right,
                        scene=st.session_state.scene
                    )
                    proportionality_response = agent.chat([{"role": "user", "content": step_3_proportionality_prompt}])
                    st.write(f"### Proportionality Analysis for {right}:")
                    st.write(proportionality_response)
                    st.markdown("***")

                    conclusion_prompt = prompts.get_prompt(
                        "step_3_conclusion",
                        right=right,
                        purpose=purpose_response,
                        suitability=suitability_response,
                        necessity=necessity_response,
                        proportionality=proportionality_response
                    )
                    conclusion_response = agent.chat([{"role": "user", "content": conclusion_prompt}])
                    st.write(f"### Conclusion for {right}:")
                    st.write(conclusion_response)
                    st.markdown("***")

                    # Save results for each right
                    st.session_state.step_3_results[right] = {
                        "purpose": purpose_response,
                        "suitability": suitability_response,
                        "necessity": necessity_response,
                        "proportionality": proportionality_response,
                    }

                st.success("Proportionality Analysis Completed!")
                
            except Exception as e:
                st.error(f"An error occurred during Proportionality analysis: {str(e)}")

if __name__ == "__main__":
    main()
