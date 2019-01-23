Facebook Page Insights Web Crawler
==================================

Python Web Programming Study with Django Framework
--------------------------------------------------

<br/>

## 프로젝트 소개

### 개요

&nbsp;&nbsp;페이스북의 영구적인 Page Access Token을 발급 받아, 핵심적인 인사이트 데이터만 크롤링한다. 그리고 페이지 경로만 바꾸는 클릭 한번으로 그 페이지의 인사이트 데이터를 보여주고, 핵심적인 데이터를 엑셀 형태로 저장할 수 있는 웹 사이트를 제작한다.

<br/>

### 문제 정의

&nbsp;&nbsp;페이스북 페이지의 관리자 권한을 갖게 되면 '인사이트'라는 기능으로 페이지 조회, 페이지 좋아요, 게시물 도달 등의 데이터 통계를 알 수 있다. 이때 관리하는 페이지가 많을 때, 각각의 페이지마다 데이터 통계를 한 눈에 알고 싶은데 페이스북에서는 이 기능을 제공하지 않는다. 예를 들어 'A', 'B', 'C'라는 세 개의 페이지를 운영하는 관리자가 페이지 경로만 바꾸는 클릭 한번으로 A, B, C 3개의 페이지의 인사이트 데이터를 쉽게 알고 싶은데, 페이스북에서는 원하는 인사이트 데이터가 있는 페이지로 일일이 들어가야 그 페이지에 대해서만 데이터 확인이 가능하다. 물론, 창을 여러 개 띄워서 동시에 확인할 수 있겠지만, 이는 하나의 창마다 각각의 페이지로 들어가 인사이트 창을 여러개 띄워야 하는 불편함이 있다.

&nbsp;&nbsp;또한, 인사이트 항목을 들어가면 '오늘', '어제', '최근 7일', '최근 28일' 총 4가지 카테고리로 데이터를 한 눈에 볼 수 있는데 이 4가지 카테고리 뿐만이 아니라, 조회하고자 하는 기간을 직접 지정하면 그 기간에 맞춰서 데이터를 한 눈에 볼 수 있도록 하는 것이 유저 입장에서는 편하다.

&nbsp;&nbsp;마지막으로, 인사이트에서는 '데이터 다운로드' 기능이 있는데, 이는 기간을 직접 지정하고 다운로드를 진행하면 인사이트의 모든 데이터에 대한 자료를 엑셀 파일로 저장할 수 있다. 하지만 이는 영어로 되어 있고, 불필요한 정보가 많아 유저는 파일에서 필요한 데이터만 가공해야 하는 불편함이 있다.

<br/>

### 프로젝트의 의미

&nbsp;&nbsp;① 페이지 관리자는 인사이트 데이터를 필요로 할 때 Page Access Token값과 Page id값만 알면, 페이스북에 로그인 할 필요도 없이 쉽게 인사이트 데이터를 확인 가능하고, 다운로드 할 수 있다.

&nbsp;&nbsp;② 장고를 토대로, 파이썬을 공부하면서 실력을 향상시킬 수 있다.

<br/>

## 기타

### 커밋 내용

```
1. 장고 튜토리얼 학습 내용

2. 프로젝트 관련 학습 내용

3. 파이썬을 공부하면서 의미 있다고 생각하는 Source Code 
```

<br/>

### 커밋 규칙

```
1. 이해 후 커밋할 것

2. 의미없는 커밋은 하지 않는다
```
