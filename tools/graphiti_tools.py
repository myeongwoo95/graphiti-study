import datetime
from langchain_core.tools import tool

# 전역 graphiti 객체 (agent.py에서 set_graphiti_instance로 설정)
_graphiti_instance = None


def set_graphiti_instance(graphiti):
    """Graphiti 인스턴스 설정"""
    global _graphiti_instance
    _graphiti_instance = graphiti


def get_graphiti_instance():
    """Graphiti 인스턴스 반환"""
    if _graphiti_instance is None:
        raise RuntimeError("Graphiti 인스턴스가 설정되지 않았습니다. set_graphiti_instance()를 호출하세요.")
    return _graphiti_instance


# Graphiti 함수들을 LangChain tools로 래핑
@tool
async def save_to_memory(
    episode_body: str,
    name: str,
    source_description: str = "사용자 입력",
    reference_time: datetime.datetime = None,
) -> str:
    """
    Graphiti에 에피소드를 저장하는 도구입니다.
    
    Args:
        episode_body: 저장할 내용 (필수)
        name: 에피소드 식별자 (필수)
        source_description: 데이터 출처 설명 (기본값: "사용자 입력")
        reference_time: 참조 시간 (기본값: 현재 시간)
    """
    graphiti = get_graphiti_instance()
    
    try:
        result = await graphiti.add_episode(
            name=name or f"episode_{datetime.datetime.now().timestamp()}",
            episode_body=episode_body,
            source_description=source_description,
            reference_time=datetime.datetime.now(),
        )
        return f"✅ 에피소드 저장 완료: {episode_body[:50]}..."
    except Exception as e:
        return f"❌ 저장 실패: {str(e)}"


@tool
async def search_memory(
    query: str,
    num_results: int = 5,
) -> str:
    """
    Graphiti에서 정보를 검색하는 도구입니다.
    
    Args:
        query: 검색어 (필수)
        num_results: 최대 결과 수 (기본값: 5)
    """
    graphiti = get_graphiti_instance()
    
    try:
        results = await graphiti.search(
            query=query,
            num_results=num_results,
        )
        
        if not results:
            return "검색 결과가 없습니다."
        
        # 결과 포맷팅
        facts = []
        for r in results:
            if hasattr(r, 'fact'):
                facts.append(r.fact)
            elif hasattr(r, 'name'):
                facts.append(f"엔티티: {r.name}")
        
        result_text = "\n".join([f"{i+1}. {fact}" for i, fact in enumerate(facts)])
        return f"검색 결과 ({len(facts)}개):\n{result_text}"
    except Exception as e:
        return f"❌ 검색 실패: {str(e)}"
