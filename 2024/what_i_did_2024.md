# What I Did in 2024

## Q1 (January - March)

### K-water (수자원공사) - Water Resources Intelligent Video Management System
- Led backend system migration and AI module development
- Integrated SCADA system connectivity
- Developed AI-Config algorithm settings interface
- Implemented TCP/IP socket communication for event integration (replacing Webhook)
- Built ROI (Region of Interest) responsive UI
- Created offline deployment system using Docker tar files (35GB packages)
- Deployed systems to multiple water treatment facilities (Seoknam, Gumi, Sungnam)
- Contributed 149 commits (vs. 38 commits in entire 2023)
- Resolved 5 out of 10 critical issues

### Backend Technical Meetings
- Conducted 7 regular backend technical meetings
- Topics: K-water project, DNA+, Police Lab 2.0

### Infrastructure & DevOps
- Set up A100 server configuration
- Created Aloha VMS demo site
- Managed development server hard disk capacity

### Naver MyBox Tagging API
- Responded to critical issues and performed instance migration
- Analyzed disk usage growth trends (20% → 40%)

---

## Q2 (April - June)

### K-water Expansion Project
- Completed 14/14 deployments on schedule
- Implemented "Drop strategy" for frame skipping during overload conditions
- Separated algorithm processes to fix infinite wait bugs during video disconnection
- Optimized Docker layer structure, reducing update package size from 30GB to 12GB (60% reduction)
- Added batch modification and channel control features to Admin UI
- Optimized Naiz integration protocol
- Contributed 10 commits

### Backend Technical Meetings
- Conducted 8 meetings covering K-water, DNA+, Police Lab 2.0

### Field Deployments
- Completed 47 business trips to 14 K-water facilities (Soyang River Dam, expansion sites)

### Professional Development
- Attended Kakao One-Day AI Developer Bootcamp
- Topic: Simple LLM deployment using NIM

---

## Q3 (July - September)

### K-water System Enhancement
- Introduced Ansible for remote management of multiple facility servers
- Implemented rsync partial transfer for network optimization (400KB/s bandwidth environments)
- Developed Active Learning system architecture (detection DB, labeling UI)
- Created QC program for algorithm performance verification
- Contributed 32 commits
- Resolved 3 out of 4 issues

### DNA+ (Police Drone Project)
- Developed RTSP real-time video analysis and re-encoding system
- Integrated TensorRT for model inference optimization
- Implemented Multi-GPU parallel processing and C++ multi-threading
- Deployed to ETRI platform with single service modularization
- Added IR (infrared) static image analysis capabilities
- Contributed 19 commits

### Police Lab 2.0
- Deployed detection system with multiple analysis algorithm selection
- Integrated K-water model modules for project scalability
- Implemented Shared Memory-based data pipeline to minimize inter-process communication overhead
- Introduced FastAPI with configuration file polling structure
- Contributed 19 commits

### Media Cultural Enjoyment Project
- Designed backend API architecture
- Built asynchronous queue system using Django + Celery + RabbitMQ + Redis
- Implemented Docker-based scalable architecture
- Contributed 3 commits (initial phase)

### Backend Technical Meetings
- Conducted 6 meetings focused on API documentation, server monitoring, project scheduling

### Field Work
- Completed 19 business trips (16 K-water sites, 3 Soyang River Dam)

### Community Leadership
- Completed DDD 11th cohort as operations team member
- Introduced Discord for unified communication (replacing fragmented KakaoTalk)

---

## Q4 (October - December)

### Media Cultural Enjoyment Project
- Built production-ready system handling 10+ minute analysis tasks
- Implemented stable queue scheduling and load management
- Deployed message queue system for long-running asynchronous processing
- Developed monitoring and logging systems
- Contributed 66 commits
- Technologies: Django, MariaDB, Celery, RabbitMQ, Redis, Docker

### DNA+ & Police Lab 2.0 Maintenance
- Maintained simple, well-structured codebase
- Applied shared memory approach to minimize memory copying
- Contributed 1 commit (maintenance phase)

### K-water QC System
- Developed packaged execution environment
- Created test framework for performance verification
- Contributed 23 commits
- Resolved 4 out of 8 issues
- Standardized and modularized test framework for reuse across projects

### Backend Strategy Meetings
- Conducted 6 meetings including 2 dedicated strategy sessions
- Created backend roadmap
- Wrote backend job descriptions

### Infrastructure & DevOps
- Tested Triton Inference Server
- Configured JuiceFS performance measurement standards

### Field Deployments
- Completed 11 business trips (9 K-water sites: Hwangji, Goyang, Taebaek; 2 DNA+ sites: Daejeon)

### Documentation & Planning
- Prepared 2024 retrospective and 2025 KPI documentation
- Created detailed quarterly review documents
- Wrote comprehensive project timeline covering 49 weeks

---

## Technologies Used in 2024

### Programming Languages & Frameworks
- Python (Django, FastAPI, Flask)
- C++ (TensorRT, multi-threading)
- SQL (MariaDB, PostgreSQL)

### AI/ML Infrastructure
- TensorRT (model optimization)
- CLIP (detection model)
- Multi-GPU parallel processing
- Active Learning pipeline design

### Backend & DevOps
- Docker (containerization, image optimization)
- Ansible (remote server management)
- Celery + RabbitMQ + Redis (asynchronous task queue)
- GitHub Actions (CI/CD exploration)
- rsync (efficient file transfer)

### System Integration
- RTSP (real-time video streaming)
- TCP/IP socket communication
- SCADA system integration
- Naiz platform integration

### Monitoring & Operations
- Loki/Grafana (logging systems)
- Custom QC program development
- Performance benchmarking frameworks

---

## Annual Statistics

### Code Contributions
- **Q1**: 149 commits (K-water)
- **Q2**: 10 commits
- **Q3**: 54 commits (32 K-water + 19 DNA+ + 3 Media)
- **Q4**: 90 commits (66 Media + 23 QC + 1 Police Lab)
- **Total**: ~303 commits

### Project Portfolio
- **Main Projects**: 3 (K-water, Media Cultural Enjoyment, DNA+/Police Lab 2.0)
- **Supporting Projects**: Multiple (Naver MyBox, Aloha, MiniPC R&D)

### Meetings & Collaboration
- Backend technical meetings: 27 total (7 Q1 + 8 Q2 + 6 Q3 + 6 Q4)
- Weekly planning meetings: 49 weeks
- Strategy meetings: 2 dedicated sessions

### Field Operations
- Total business trips: 77+ (10 Q1 + 47 Q2 + 19 Q3 + 11 Q4)
- Primary sites: K-water facilities, SCADA installations, system maintenance
