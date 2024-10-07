from durable.lang import *

with ruleset('fruit_rules'):

    @when_all(m.color == '빨강')
    def red_fruit(c):
        c.assert_fact({'과일': '사과', '특징': '빨간색'})

    @when_all((m.shape == '긴 타원형') & (m.color == '노랑'))
    def banana(c):
        c.assert_fact({'과일': '바나나', '특징': '길고 노란색'})

    @when_all((m.taste == '달콤함') & (m.texture == '부드러움'))
    def mango(c):
        c.assert_fact({'과일': '망고', '특징': '달콤하고 부드러운 과일'})

    @when_all((m.size == '작음') & (m.color == '빨강'))
    def strawberry(c):
        c.assert_fact({'과일': '딸기', '특징': '작고 빨간색'})

    @when_all((m.size == '크고') & (m.color == '초록'))
    def watermelon(c):
        c.assert_fact({'과일': '수박', '특징': '크고 초록색'})

    @when_all((m.taste == '새콤함') & (m.color == '노랑'))
    def lemon(c):
        c.assert_fact({'과일': '레몬', '특징': '새콤하고 노란색'})

    @when_all((m.texture == '껍질이 거칠다') & (m.color == '주황'))
    def orange(c):
        c.assert_fact({'과일': '오렌지', '특징': '껍질이 거칠고 주황색'})

    @when_all((m.taste == '상큼함') & (m.size == '작음'))
    def blueberry(c):
        c.assert_fact({'과일': '블루베리', '특징': '작고 상큼함'})

    @when_all((m.color == '보라') & (m.shape == '둥근 타원형'))
    def grape(c):
        c.assert_fact({'과일': '포도', '특징': '보라색 둥근 타원형 과일'})

    @when_all((m.color == '갈색') & (m.shape == '둥근 모양'))
    def kiwi(c):
        c.assert_fact({'과일': '키위', '특징': '갈색 껍질에 둥근 모양'})

    @when_all((m.taste == '새콤함') & (m.color == '초록'))
    def green_apple(c):
        c.assert_fact({'과일': '초록 사과', '특징': '새콤한 맛'})

    @when_all((m.size == '매우 작음') & (m.color == '빨강'))
    def cherry(c):
        c.assert_fact({'과일': '체리', '특징': '매우 작고 빨간색'})

    @when_all((m.taste == '달콤함') & (m.color == '노랑'))
    def pineapple(c):
        c.assert_fact({'과일': '파인애플', '특징': '달콤하고 노란색'})

    @when_all((m.texture == '부드러움') & (m.shape == '타원형'))
    def avocado(c):
        c.assert_fact({'과일': '아보카도', '특징': '부드럽고 타원형'})

    @when_all((m.color == '빨강') & (m.taste == '새콤달콤함'))
    def pomegranate(c):
        c.assert_fact({'과일': '석류', '특징': '빨갛고 새콤달콤한 맛'})


assert_fact('fruit_rules', {'color': '빨강'})
assert_fact('fruit_rules', {'shape': '긴 타원형', 'color': '노랑'})
assert_fact('fruit_rules', {'taste': '달콤함', 'texture': '부드러움'})
assert_fact('fruit_rules', {'size': '작음', 'color': '빨강'})
assert_fact('fruit_rules', {'size': '크고', 'color': '초록'})
assert_fact('fruit_rules', {'taste': '새콤함', 'color': '노랑'})
assert_fact('fruit_rules', {'texture': '껍질이 거칠다', 'color': '주황'})
assert_fact('fruit_rules', {'taste': '상큼함', 'size': '작음'})
assert_fact('fruit_rules', {'color': '보라', 'shape': '둥근 타원형'})
assert_fact('fruit_rules', {'color': '갈색', 'shape': '둥근 모양'})
assert_fact('fruit_rules', {'taste': '새콤함', 'color': '초록'})
assert_fact('fruit_rules', {'size': '매우 작음', 'color': '빨강'})
assert_fact('fruit_rules', {'taste': '달콤함', 'color': '노랑'})
assert_fact('fruit_rules', {'texture': '부드러움', 'shape': '타원형'})
assert_fact('fruit_rules', {'color': '빨강', 'taste': '새콤달콤함'})