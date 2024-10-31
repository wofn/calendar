import pathlib
import google.generativeai as genai
from dotenv import load_dotenv
import os

# .env 파일에서 환경 변수 로드
load_dotenv()

# API 키 설정
api_key = os.getenv('API_KEY')
genai.configure(api_key=api_key)

# Gemini Pro Vision 모델 생성
model = genai.GenerativeModel('gemini-1.5-flash')

# 이미지 파일 로드
image_path = '/Users/sin-yeonghyeon/Desktop/3-2/설계프로젝트/LLM/img/img01.jpg'

image = {
    'mime_type': 'image/png',
    'data': pathlib.Path(image_path).read_bytes()
}

# 프롬프트 설정
prompt = "이 사진이 무엇인지 한국말로 설명해줘"

# 컨텐츠 생성 요청
response = model.generate_content([prompt, image])

# 결과 출력
print(response.text)
