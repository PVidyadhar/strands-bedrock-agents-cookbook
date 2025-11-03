import os
from datetime import datetime
from typing import Dict, Any


def apply_prompt_template(prompt_name: str, prompt_context: Dict[str, Any] = None) -> str:
    """
    프롬프트 템플릿 파일을 로드하고 컨텍스트 변수를 적용합니다.
    
    Args:
        prompt_name (str): 프롬프트 파일명 (확장자 제외)
        prompt_context (Dict[str, Any], optional): 템플릿에 적용할 추가 컨텍스트 변수들
        
    Returns:
        str: 컨텍스트가 적용된 프롬프트 문자열
        
    Example:
        >>> system_prompt = apply_prompt_template(
        ...     prompt_name="toy_agent", 
        ...     prompt_context={"AGENT_NAME": "toy_agent"}
        ... )
    """
    if prompt_context is None:
        prompt_context = {}
    
    # 프롬프트 파일 경로 구성 (prompt 디렉토리에서 찾기)
    prompt_dir = os.path.join(os.path.dirname(__file__), "prompt")
    prompt_file_path = os.path.join(prompt_dir, f"{prompt_name}.md")
    
    # 파일 존재 확인
    if not os.path.exists(prompt_file_path):
        raise FileNotFoundError(f"프롬프트 파일을 찾을 수 없습니다: {prompt_file_path}")
    
    # 프롬프트 템플릿 파일 읽기
    with open(prompt_file_path, 'r', encoding='utf-8') as f:
        system_prompts = f.read()
    
    # 기본 컨텍스트 설정 (현재 시간)
    context = {"CURRENT_TIME": datetime.now().strftime("%a %b %d %Y %H:%M:%S %z")}
    
    # 추가 컨텍스트 병합
    context.update(prompt_context)
    
    # 템플릿 변수 치환
    try:
        system_prompts = system_prompts.format(**context)
    except KeyError as e:
        raise KeyError(f"템플릿에서 정의되지 않은 변수를 참조했습니다: {e}")
    
    return system_prompts


def load_prompt_template(prompt_name: str) -> str:
    """
    프롬프트 템플릿 파일을 원본 그대로 로드합니다 (변수 치환 없음).
    
    Args:
        prompt_name (str): 프롬프트 파일명 (확장자 제외)
        
    Returns:
        str: 원본 프롬프트 템플릿 문자열
    """
    prompt_dir = os.path.join(os.path.dirname(__file__), "prompt")
    prompt_file_path = os.path.join(prompt_dir, f"{prompt_name}.md")
    
    if not os.path.exists(prompt_file_path):
        raise FileNotFoundError(f"프롬프트 파일을 찾을 수 없습니다: {prompt_file_path}")
    
    with open(prompt_file_path, 'r', encoding='utf-8') as f:
        return f.read()


def list_available_prompts() -> list:
    """
    사용 가능한 프롬프트 템플릿 목록을 반환합니다.
    
    Returns:
        list: 사용 가능한 프롬프트 파일명 목록 (확장자 제외)
    """
    prompt_dir = os.path.join(os.path.dirname(__file__), "prompt")
    
    if not os.path.exists(prompt_dir):
        return []
    
    prompt_files = []
    for filename in os.listdir(prompt_dir):
        if filename.endswith('.md'):
            prompt_files.append(filename[:-3])  # .md 확장자 제거
    
    return sorted(prompt_files)