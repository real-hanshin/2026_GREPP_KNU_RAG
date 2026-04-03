from vectorstore import init_vectorstore, load_vector_from_local
from chain import build_rag_chain

# 처음 한 번만 주석을 해제하여 CSV 데이터를 FAISS로 변환해 저장하세요.
init_vectorstore()

vectorstore = load_vector_from_local()
chain = build_rag_chain(vectorstore=vectorstore)

queries = [
    # 요구사항 1
    "피치클락 위반 시 타자와 투수에게 각각 어떤 페널티가 부여되나요?",
    
    # 요구사항 2
    "A선수가 3일 전 경기에 나갔고 오늘 부상으로 말소됐다면, 소급 적용을 포함해 언제 복귀 가능한가?",
    
    # 요구사항 3
    "경기 중 ABS가 고장 났고, 5회초에 비가 내려 경기가 중단된 상황입니다. 이때 현재 경기의 최종 상태(종료/일시중단)를 판정해 주세요."
]

for i, q in enumerate(queries, 1):
    print(f"================ 질문 {i} ================")
    print(f"Q: {q}\n")
    result = chain.invoke(q)
    print(f"A:\n{result}\n")