# Here i will push small backend projects to understand FastAPI
## Getting started 
- How to create basic server using FastAPI.
## Todo App
- Basic Todo app using Pydantic to model data.
## Password Hasher
- Takes password string as input.
- Returns back hashCode of the password.
- Uses passlib modules's argon2 for hashing.
## Login Signup Authentication app
- Basic signup using name, email and password.
- Login using valid credentials
- MongoDB connection using "motor"
- Storing Hashed (using "argon2") password in DB
- On successfull Signup/Login, JWT token generation.
- One restricted resource accessible using valid token.
## SQLAlchemyDemo
- Understanding workflow of SQLAlchemy for seamless Database connection.
- Storing User detail in DB and sending back response.
## RAG Pipeline
- Implementing RAG pipeline using Langchain modules.
- Pipeline flow 
1. Upload file
2. Process file
3. Store embeddings in Chromadb
4. Ask question with unique filename
5. Get retriever for filename
6. Get answer using retriever