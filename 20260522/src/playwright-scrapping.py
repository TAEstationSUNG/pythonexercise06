# Reference - https://wikidocs.net/231787

import asyncio
from playwright.async_api import async_playwright

async def run_playwright():                 #비동기 함수선언
    # 비동기 방식으르 playwright 시작
    async with async_playwright() as p:
        # 브라우저 실행 (headless=False 로 설정하면 실제 브라우저 창이 뜸)
        browser = await p.chromium.launch(headless=False)
        #headless=False면 실제 브라우저 창이 눈에 보임
        #headless=True면 창 없이 백그라운드에서 실행
        page = await browser.new_page() #새 탭 열기

        # Naver 로 이동
        await page.goto('https://www.naver.com')

        # 검색창에 키워드 입력 (네이버 검색창 id 는 query)
        await page.fill('#query', '인공지능')

        # 검색 버튼 클릭 (네이버 검색 버튼 class 나 id 지정)
        # await page.click('.btn_search')
        await page.click('#search-btn')

        # 페이지 로드 대기
        await page.wait_for_load_state('networkidle')

        # 제목 출력 및 스크린샷
        print(f'현재 페이지 제목: {await page.title()}')
        await page.screenshot(path='./img/naver_search_result.png')

        # 눈으로 확인할 수 있도록 10초 동안 대기 (실제 코드에서는 불필요)
        await page.wait_for_timeout(10000)

        await browser.close()

async def run_extract():
    # 비동기 방식으르 playwright 시작
    async with async_playwright() as p:
        # 브라우저 실행 (headless=False 로 설정하면 실제 브라우저 창이 뜸)
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # Naver 로 이동
        await page.goto('https://finance.naver.com/news/mainnews.naver')

        #.block1 클래스 요소들 찾기
        elements = page.locator('.block1')
        #찾은 요소들의 텍스트를 전부 리스트로 가져오기
        block1_list = await elements.all_inner_texts()

        print(block1_list)

        for block1 in block1_list:
            print(block1)

        # 터미널에서 사용자가 엔터키를 입력할 때까지 브라우저가 꺼지지 않고 무한 대기하게 하려면 다음 코드를 사용
        input('터미널에서 [Enter]를 입력하면 브라우저가 종료됩니다.')

        await browser.close()

if __name__ == '__main__':
    # asyncio.run(run_playwright())
    asyncio.run(run_extract())

#if __name__ == '__main__': 해서 run_extract()만 하니까 이 파일을 직접 실행할때만 이 코드를 실행하라는뜻
