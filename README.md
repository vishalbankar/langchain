# T-shirt Store generic Q & A
This LLM project based on Google Palm and Langchain. We are building a system that can talk to MySQL database. User can asks questions in a natural language and the system generates answers by converting those questions to an SQL query and then executing that query on MySQL database.In T-shirt store they maintain their inventory, sales and discounts data in MySQL database. A store manager will may ask questions such as,

1) How many white color Adidas t shirts do we have left in the stock?
2) How much sales our store will generate if we can sell all extra-small size t shirts after applying discounts?

The system is intelligent enough to generate accurate queries for given question and execute them on MySQL database

# a short video presentation
https://github.com/vishalbankar/langchain/assets/71269939/4ac4c885-473c-46b3-a09a-56e1d953c348

# database structure
![Local Image](https://github.com/vishalbankar/langchain/blob/main/discount.png)
![Local Image](https://github.com/vishalbankar/langchain/blob/main/tees.png)
![Local Image](https://github.com/vishalbankar/langchain/blob/main/DB_tables.png)


# Project Highlights
A t shirt store that sells Adidas, Nike, Van Heusen and Levi's t shirts
Their inventory, sales and discounts data is stored in a MySQL database
I have build an LLM based question and answer system that will use following,
 * Google Palm LLM
 * Hugging face embeddings
 * Streamlit for UI
 * Langchain framework
 * Chromadb as a vector store
 * Few shot learning

In the UI, store manager will ask questions in a natural language and it will produce the answers.

# Project Structure
* main.py: The main Streamlit application script.
* langchain_helper.py: This has all the langchain code
* requirements.txt: A list of required Python packages for the project.
* few_shots.py: Contains few shot prompts
* .env: Configuration file for storing Google API key.

  # Sample Questions can be run
- How many total t shirts are left in total in stock?
- How many t-shirts do we have left for Nike in XS size and white color?
- How much is the total price of the inventory for all S-size t-shirts?
- How much sales amount will be generated if we sell all small size adidas shirts today after discounts?




