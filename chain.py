from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.documents.base import Document

SYSTEM_PROMPT = """당신은 KBO 야구 규정을 정확하게 해석하는 수석 심판이자 데이터 전문가입니다.

규칙:
1. 반드시 아래 제공된 [참고 문서]의 내용을 바탕으로 답변하세요.
2. [인용 필수]: 답변 시 근거가 되는 규정의 'ID'와 '규정명(title)'을 명시하세요. (예: "ID 4(피치클락)에 따르면...")
3. [논리적 추론]: 복수의 규정(예: ABS, 강우콜드 등)이 겹치거나 날짜를 계산할 때는, 어떤 문서들을 조합했는지 단계별로(Step 1, Step 2...) 설명한 후 최종 결론을 내리세요.
4. 참고 문서에 없는 내용은 "규정집에서 해당 내용을 확인할 수 없습니다."라고 답변하세요.

[참고 문서]
{context}"""

def build_rag_chain(vectorstore):
    load_dotenv()

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0
    )

    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": 5 
        }
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", "{input}")
    ])

    return (
        {
            "context": retriever | RunnableLambda(format_docs),
            "input": RunnablePassthrough(),
        }
        | prompt
        | llm
        | StrOutputParser()
    )

def format_docs(docs: list[Document]) -> str:
    if not docs:
        return "관련 문서를 찾지 못했습니다."

    sections = []
    for i, doc in enumerate(docs, 1):
        doc_id = doc.metadata.get("id", "알수없음")
        title = doc.metadata.get("title", "제목없음")
        
        section = f"[{i}] 문서 ID: {doc_id} | 규정명: {title}\n{doc.page_content}"
        sections.append(section)

    return "\n\n".join(sections)