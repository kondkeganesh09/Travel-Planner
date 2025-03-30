```python
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from config import GOOGLE_GENAI_API_KEY

# Initialize AI Model
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key=GOOGLE_GENAI_API_KEY)

# Define prompt templates
travel_prompt = PromptTemplate(
    input_variables=["source", "destination"],
    template="""
    You are an AI travel assistant. Provide the best travel options from {source} to {destination}.
    Include different travel modes (cab, bus, train, flight) with estimated costs and travel durations.
    Format the response in a structured manner.
    """
)
travel_chain = LLMChain(llm=llm, prompt=travel_prompt)

tips_prompt = PromptTemplate(
    input_variables=["destination"],
    template="""
    Suggest 3 travel safety or planning tips for someone visiting {destination}.
    """
)
tips_chain = LLMChain(llm=llm, prompt=tips_prompt)
```
