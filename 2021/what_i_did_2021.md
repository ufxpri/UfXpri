# What I Did - 2021

## Career Growth Summary
- **참여한 프로젝트 수**: 5 → 7개
- **제작한 API 수**: 4 → 11개

## Major Projects

### 1. 수자원 AI 안전관리 시스템
**기간**: 2021.03 ~ 2022.05
**역할**: 백엔드 엔지니어 (5명 팀)
**난이도**: ⭐⭐⭐⭐⭐
**기술 스택**: Python, gRPC, Docker, PyTorch, On-Premise, MSA, FFmpeg

#### 주요 업무
- **CCTV 36대 스트리밍 데이터** 처리 시스템 설계 및 개발
- 동적 스케일링이 용이한 아키텍처 설계
  - 늘어나는 현장 요구사항에 유연하게 대처
- 시스템 부하 문제 파악 및 아키텍처 개선
  - 납품일 내에 개선안 적용
- 현장 출장 및 적용 테스트
- 데이터 수집 수행
- 현장에서 딥러닝 동작 분석 및 모델 개발팀 피드백 제공
- **Fluentd**와 **InfluxDB**를 사용한 모니터링 시스템 구축

#### 기술적 성과
- gRPC 도입을 통한 아키텍처 구성
- 도커를 자유롭게 사용하여 시스템 구축
- 실제 대규모 트래픽을 처리한 첫 번째 프로젝트
- 대규모 프로젝트 문서 작성 경험

### 2. NAS 서버 구축
**기간**: 2021.04 ~ 2021.05
**역할**: 시스템 엔지니어 (단독)
**기술 스택**: OpenVPN, Network, SMB

#### 주요 업무
- **24TB 용량의 NAS 서버** 구축
- 팀원의 작업 레벨을 고려하여 친숙한 Windows GUI 환경 선택
- 네트워크 드라이브 시스템 적용 및 교육
- RDP 기능 적용하여 원격 제어 가능하도록 설정
- NAS 이외의 추가 기능 설정

### 3. DNA+ 프로젝트
**난이도**: ⭐⭐⭐⭐
**기술 스택**: RTSP, KLV, MJPEG

#### 주요 업무
- DDD(Domain-Driven Design) 적용하여 프로그래밍
- RTSP, KLV, MJPEG 방식의 스트리밍 수신 구현
- 대규모 프로젝트 문서 작성 경험

### 4. 승강기 안전공단 프로젝트
**난이도**: ⭐⭐⭐

#### 주요 업무
- FFmpeg 스트리밍 활용
- 소프트웨어 장애 대처 고려
- Pipe 통신 사용

### 5. 인천TP 프로젝트
**난이도**: ⭐

#### 주요 성과
- 문서만으로 API 연동 가능함을 깨달음

### 6. AI Hub 서버 셋팅

#### 주요 업무
- 실제 서버실에 서버 셋팅 경험
- 서버 셋팅 시간: 일주일 → 3일로 단축

### 7. 기타 프로젝트
- 병충해 프로젝트
- 한미글로벌 프로젝트
- 롯데건설 프로젝트 (난이도: ⭐⭐⭐)

## Technical Skills & Architecture

### Architecture Improvements
- **서비스 아키텍처 변경**: gRPC 버전 ReCon_API 제작 사양서 작성
- MSA (Microservices Architecture) 적용
- 동적 스케일링 가능한 시스템 설계

### Infrastructure & DevOps
- Docker 기반 컨테이너 환경 구축
- 모니터링 시스템 구축 (Fluentd + InfluxDB)
- NAS 서버 구축 및 네트워크 관리
- OpenVPN 설정

### Streaming & Media
- FFmpeg 활용한 스트리밍 처리
- RTSP, KLV, MJPEG 프로토콜 처리
- 36대 CCTV 동시 스트리밍 데이터 처리

### API Development
- gRPC 기반 API 개발
- RESTful API 개발
- 제작한 API 수: 4개 → 11개 증가

## Research & Technical Presentations

### 논문 리뷰 - 11개
1. **gRPC**: gRPC 버전 ReCon_API 제작 사양서
2. **JWT**: JSON Web Token
3. **Python Profiling**: 성능 분석
4. **File Transfer**: 파일 전송 최적화
5. **프로젝트 문서**: 문서화 방법론
6. **CI/CD**: 지속적 통합 및 배포
7. **Eventual Consistency**: 최종 일관성
8. **Torch Script**: PyTorch 모델 최적화
9. **Docker 파일 시스템**: Docker 내부 구조
10. **Docker GPU**: GPU 컨테이너 활용
11. **동영상이란**: 비디오 인코딩 기초

### CVPR 참여
- 참여 세션: 150개

## Knowledge Sharing & Writing

### 기술 블로그 글 작성 - 17개

#### 1-2분기 (9개)
1. 아키텍트란 무엇일까?
2. 비동기 Request-Reply 패턴
3. 단 한개의 App Crash 때문에 해고당한 3명의 프로그래머들
4. 5가지 파이썬 꿀팁
5. Fast API 알아보기
6. 넷플릭스 마이크로서비스화 보고 정리
7. 소프트웨어 사용권(라이센스) 조항 읽고 직접 분류해보기
8. 개발자 16시간 운동 읽고 보고하기
9. CTO의 조건

#### 3-4분기 (8개)
1. Pub-Sub 패턴
2. Eventual consistency via domain events and azure service bus
3. 비즈니스를 시작할 때 피해야 할 20가지 실수
4. 화면설계 안하는 기획자
5. Mock의 필요성에 대하여
6. DVC에 대해서 알아보자
7. 약한 추상화? 뭔지 알아보기
8. 당근마켓 서버 밋업
9. 파이썬 스핑크스 적용 알아보기
10. config 설정 적용 문서화

## Learning & Professional Development

### Books Read
1. **GoF의 디자인 패턴** (훈련소에서 정독)
2. **도메인 주도 설계 철저 입문**
3. **클라우드 네이티브 애플리케이션 개발 가이드라인**

### External Activities

#### DDD (Designer Developer Day)
- 난도착 프로젝트 참여
- DDD 안드로이드 2팀 활동

#### 군 복무
- 기간: 5월 5일 ~ 5월 26일 (훈련소)
- 훈련소에서 GoF 디자인 패턴 정독

## Technical Stack Summary

### Languages & Frameworks
- Python
- PyTorch
- FastAPI

### Communication Protocols
- gRPC
- REST API
- RTSP
- KLV
- MJPEG

### Infrastructure & DevOps
- Docker
- OpenVPN
- SMB
- RDP

### Monitoring & Logging
- Fluentd
- InfluxDB

### Architecture Patterns
- MSA (Microservices Architecture)
- DDD (Domain-Driven Design)
- Request-Reply Pattern
- Pub-Sub Pattern

### Media Processing
- FFmpeg
- Pipe Communication

### Storage & Network
- NAS Server (24TB)
- Network Drive
- On-Premise Infrastructure

## Areas of Interest

### Professional Focus
- 소프트웨어 아키텍처
- 프로젝트 기획
- 프로그래밍 기법
- 인증 (Authentication)
- 마이크로서비스 아키텍처

## Presentation & Communication
- 한미글로벌 PPT 5장 제작 및 발표
- 논문 발표 11회
- 기술 블로그 글 17개 작성
