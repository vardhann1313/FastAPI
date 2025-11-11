from app.util.ragUtils import get_retriever

async def ask_service(filename: str, question: str):

    # get retriever
    retriever = get_retriever(filename)

    # Get results
    results = await retriever.ainvoke(question)

    return {
        "success": True,
        "data": results
    }