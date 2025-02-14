# https://colab.research.google.com/drive/1BRPnhuc9dmzqvjs49FrcGv7GNT60fWUu#scrollTo=LYhJ8do_zBqy

#try out here: 
# https://www.w3schools.com/mysql/trymysql.asp?filename=trysql_select_all

# **문제1) 96년 12월의 주문데이터를 추출하여라**

# **문제2) 96년 12월에 주문한 사람 수를 세어라**

# **문제3) supplierid가 4인 공급자가 관리하는 카테고리 개수와 물건의 평균 가격을 구하라**

# **문제4)  68년생인 고용인의 데이터를 추출하여라**

# **문제5) 96년도에 주문한 건수를 추출하여라**

# **예제1) productid별, orderid별 quantity의 총 합**

# **예제2) 고객데이터 중 도시별 Unique한 고객의 수 구하기**

# **예제3) 생일연도별 employeeid의 수 구하기**

# **예제4) 생일월별 employeeid의 수**

# **예제5) supplier중 나라별 supplierid의 수**

# 예시1) 주문내역(orderdetails)에서 productid별 물품수량(quantity) 총 개수(sum(quantity)) 구해서 productid를 기준으로 정렬하기

# 예시2) 주문내역(orderdetails)에서 productid별 물품수량(quantity) 총 개수(sum(quantity)) 구해서 2번째 컬럼(=sum(quantity))을 기준으로 정렬하기

# 예시3) 고객정보를  country컬럼을 기준으로 내림차순 정렬하기

#having 
# 예제1) 주문내역(orderdetails)에서 productid별 물품수량(quantity) 총 개수(sum(quantity)) 구한 결과 중 총 물품수량(sum(quantity))이 80초과인 데이터만 조회하기

#as (new column name)
# 주문정보테이블(orders)에서 customerid가 80이상인 데이터를 employeeid별로 묶어서 유니크한 customerid 개수 구하기

# 문제1) 주문정보테이블(orders)에서 employeeid별로 유니크한 customerid 개수를 구하고, 그 중 유니크한 customerid의 개수가 3보다 큰 데이터만 조회하기

#case when (creating new columns based on conditions)
# orders테이블에서 shipperid가 3보다 크거나 같으면 “problem”, 2면 “normal” 그 외의 경우에는 “unknown”으로 정의하자

# 문제1) productid가 0~9사이면 0, 10~19면 10, 20~29면 20, 30~39면 30, 40~49면 40, 그외의 경우에는 50이상 으로 age_group이라는 새로운 컬럼을 정의하기

#substr / substring 
# customername에서 앞에서 6자리만 잘라서 name_split이라는 컬럼으로 재정의하기

#type casting: 컬럼타입 변경해주기
# productid를 string타입(원래 int타입)으로 변환해주기

# 문제1) productid를 string타입(원래 int타입)으로 변환해서 첫번째 자리만 가져오기