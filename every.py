import sys
from selenium import webdriver
from selenium.webdriver.common.alert import Alert

class User:
    def __init__(self, id, pw):
        self.id           = id
        self.pw           = pw
        self.boards       = {}
        self.keywords     = {}
        self.last_checked = None
    
    # 웹 드라이버 만들기
    def get_driver():
        # 웹 드라이버 옵션 만들기
        options = webdriver.ChromeOptions()
        # options.add_argument('start-maximized')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')

        # 웹 드라이버 만들기
        driver = webdriver.Chrome('chromedriver.exe', options = options)
        driver.implicitly_wait(10)

        return driver
    
    def login(self, driver):
        # 에브리타임 사이트 접속하기
        driver.get('https://hanyang.everytime.kr')

        # TODO: 로그인하기 (+ Id, Password 틀렸을 때 처리)
    
    # 게시판 이름을 번호로 바꿔주기
    def board2num(self, board):
        # 웹 드라이버 만들기
        driver = User.get_driver()

        # 로그인하기
        self.login(driver)

        # TODO: 게시판 이름을 검색해서 개시판 이름을 번호로 바꿔주기

        # 웹 드라이버 종료하기
        driver.quit()
        
        return None
    
    # 알림받을 키워드 설정하기
    def add_keyword(self, keyword):
        self.keywords.add(keyword)
    
    # 알림받을 키워드 해제하기
    def remove_keyword(self, keyword):
        self.keywords.remove(keyword)
    
    # 관찰할 게시판 추가하기
    def add_board(self, board):
        self.boards.add(self.board2num(board))

    # 관찰할 게시판 해제하기
    def remove_board(self, board):
        self.boards.remove(self.board2num(board))
    
    # TODO: self.last_checked 이후로 새로 업로드된 글 목록 가져오기
    def new_uploaded(self, driver):
        return None
    
    # TODO: 게시글 내용 가져오기
    def text(self, driver, board, post):
        return None
    
    # 알림할 글 목록 가져오기
    def search(self):
        # 웹 드라이버 만들기
        driver = User.get_driver()

        # 로그인하기
        self.login(driver)

        # TODO: 새로 업로드된 글 목록 가져와서,
        #       설정된 게시판의 글만 필터링하고,
        #       게시글 내용을 차례로 읽으며,
        #       설정된 키워드가 포함된 글만 필터링하기

        # 웹 드라이버 종료
        driver.quit()
        return None