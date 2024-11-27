# Human-Rights-Demo

## Overview

This project is Assignment 2 for **Legal AI: Design and Development (LAWS90286)** at Melbourne Law School. It is an automated tool for analyzing cases related to the protection of fundamental rights. It provides a structured framework for assessing whether government actions infringe upon fundamental rights. The analysis is divided into three main stages:

1. **Scope of Protection**: Determining whether the action falls within the scope of fundamental rights protection.
2. **Intervention**: Determining whether the action constitutes an interference with the identified fundamental rights.
3. **Justification**: Assessing whether the interference can be justified. This stage employs a **proportionality principle** analysis, which is further divided into four sub-stages:
   - **Purpose**: Evaluating the legitimacy of the purpose behind the interference.
   - **Suitability**: Determining whether the interference effectively achieves its stated purpose.
   - **Necessity**: Examining whether less restrictive means could achieve the same purpose.
   - **Proportionality**: Balancing the harm caused to the right against the benefits gained.

The program provides a step-by-step process to ensure comprehensive analysis, with opportunities for user input at critical decision points.


## How to Use

1. **Input the Scenario**:
   - Begin by describing the situation in the provided input box.
   
2. **Step 1: Scope of Protection**:
   - The system will analyze whether the described action falls within the protection of fundamental rights. The results will list which rights are potentially affected.

3. **Step 2: Select Rights for Review**:
   - Based on the identified rights from Step 1, users can select which fundamental rights they wish to review further for potential interference.

4. **Step 3: Proportionality Analysis**:
   - For each selected right, the program conducts a four-stage proportionality analysis to determine if the interference is justified:
     - **Purpose**: Assessing the legitimacy of the stated aim.
     - **Suitability**: Verifying the effectiveness of the action.
     - **Necessity**: Exploring less restrictive alternatives.
     - **Proportionality**: Balancing harm and benefits.


## Demo  
To try the demo, please visit: **[Demo Link](https://human-rights-demo-2s3qsvwtxj7smci6vzg4kr.streamlit.app/)**.  


## Test Cases

### Case 1

During a public health emergency, the government imposed mandatory travel restrictions, prohibiting intercity travel without prior approval. The policy aimed to control the spread of a highly contagious virus. Citizens were required to present a government-issued pass to cross city boundaries. A commuter who relies on public transportation for work was denied a pass and arrested for attempting to bypass a checkpoint. They argue the policy infringes on their freedom of movement and personal liberty. The government defends the policy, citing the public health crisis as justification. However, critics highlight the lack of transparency in the approval process and suggest that alternative measures, such as testing or vaccination mandates, could achieve the same goals with less impact on personal freedoms.

*Expected Analysis: The application should analyze whether the restrictions fall within the scope of fundamental rights protection, whether they constitute interference, and if the justification holds under the proportionality principle.*

### Case 2

A journalist published a report exposing alleged corruption in a government defense contract. In response, the government invoked national security concerns and ordered the journalist’s detention under a newly passed law. The law criminalizes the dissemination of “sensitive information” that could harm the country’s international reputation. The journalist argues that the detention violates their freedom of speech and freedom of the press. The government claims the publication could damage relations with international allies and jeopardize national security. Advocacy groups argue that the law is overly broad, lacks clear definitions of "sensitive information," and risks being used to silence dissenting voices.

*Expected Analysis: The application should identify potential infringements on freedom of speech, determine whether the detention and law are justified under the proportionality principle, and explore alternative measures like sanctions or warnings.*

### Case 3

A city council banned street performances in a popular tourist district, citing the need to maintain pedestrian safety and prevent overcrowding. A street musician was fined for performing without a permit and claims this violates their freedom of expression and right to work. The council argues the policy is necessary to ensure public safety, but they have not provided data showing a significant increase in accidents or crowding caused by street performances. The musician argues the policy disproportionately targets artists and ignores other contributors to congestion, such as large-scale advertisements and unregulated vending. Additionally, the council has not specified criteria for obtaining a permit, creating confusion for performers.

*Expected Analysis: The application should identify the overlap between the right to work and freedom of expression, evaluate whether the justification meets proportionality standards, and account for the vagueness of the permit system.*

*Potential Limitations Exposed:*
- *Difficulty analyzing scenarios with overlapping rights.*
- *Inability to address the lack of objective data or ambiguous justifications from authorities.*


## Acknowledgements
Special thanks to **Jack Stoneman** for his guidance and support in the development of this project.
