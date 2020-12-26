from http.server import HTTPServer, BaseHTTPRequestHandler
import pymysql
from urllib import parse


# 读取学生数据表
def getStu_users():
    # 链接数据库
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        database="forum",
        user="root",
        password="123456",
        charset="utf8"
    )

    # 获取光标
    cursor = conn.cursor()
    sql = "SELECT * FROM stu_user ORDER BY id ASC"

    # 执行SQL语句
    count = cursor.execute(sql)
    result = cursor.fetchall()  # 取出所有复核条件的数据

    # 关闭光标和链接
    cursor.close()
    conn.close()
    return result


# 添加数据给学生表
def storeStu_users(content):
    # 链接数据库
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        database="forum",
        user="root",
        password="123456",
        charset="utf8"
    )

    # 获取光标
    cursor = conn.cursor()

    sql = "insert into stu_user(sname,id,sex,age,zhuanye,loudong,fangjian) VALUES (%s, %s, %s,%s, %s, %s, %s)"
    ret = cursor.execute(sql, (
        content['sname'][0], content['id'][0], content['sex'][0], content['age'][0], content['zhuanye'][0],
        content['loudong'][0], content['fangjian'][0]))
    conn.commit()  # 添加完毕数据库后需要提交一下数据

    # 关闭光标和链接
    cursor.close()
    conn.close()
    return ret

# 添加数据给管理员表
def storeAr_users(content):
    # 链接数据库
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        database="forum",
        user="root",
        password="123456",
        charset="utf8"
    )

    # 获取光标
    cursor = conn.cursor()

    sql = "insert into ar_user(aname,asex,aage,aID,password,contact) VALUES (%s, %s, %s,%s, %s, %s)"
    ret = cursor.execute(sql, (
        content['aname'][0], content['asex'][0], content['aage'][0], content['aID'][0], content['password'][0],
        content['contact'][0]))
    conn.commit()  # 添加完毕数据库后需要提交一下数据

    # 关闭光标和链接
    cursor.close()
    conn.close()
    return ret

# 学生表删除数据
def delStudent(id):
    # 链接数据库
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        database="forum",
        user="root",
        password="123456",
        charset="utf8"
    )

    # 获取光标
    cursor = conn.cursor()
    sql = 'DELETE FROM stu_user WHERE id="{}"'.format(id)

    try:
        ret = cursor.execute(sql)
        print(ret)
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(e)

    # 关闭光标和链接
    cursor.close()
    conn.close()

# 学生表修改数据
def upStudent(data):
    # 链接数据库
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        database="forum",
        user="root",
        password="123456",
        charset="utf8"
    )

    # 获取光标
    cursor = conn.cursor()
    sql = 'update stu_user set sname="{}",sex="{}",age={},zhuanye="{}",loudong={},fangjian={} where id="{}"'.format(
        data['sname'][0], data['sex'][0], data['age'][0], data['zhuanye'][0], data['loudong'][0], data['fangjian'][0],data['id'][0]
    )


    try:
        ret = cursor.execute(sql)
        print(ret)
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(e)

    # 关闭光标和链接
    cursor.close()
    conn.close()

def getStudent(whereStr):
    # 链接数据库
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        database="forum",
        user="root",
        password="123456",
        charset="utf8"
    )

    # 获取光标

    cursor = conn.cursor()
    sql = "SELECT * FROM stu_user WHERE " + whereStr

    # 执行SQL语句
    count = cursor.execute(sql)
    result = cursor.fetchone()  # 取出第一行数据

    # 关闭光标和链接
    cursor.close()
    conn.close()
    return result



def readFile(file_name):
    with open(file_name, 'rb') as f:
        return f.read(1024 * 1024)


def generateList(articles):
    html = ''
    for article in articles:
        html += '<article>'
        html += '<tr>'
        html += '<td>' + article[0] + '</td>'
        html += '<td>' + str(article[1]) + '</td>'
        html += '<td>' + article[2] + '</td>'
        html += '<td>' + str(article[3]) + '</td>'
        html += '<td>' + article[4] + '</td>'
        html += '<td>' + str(article[5]) + '</td>'
        html += '<td>' + str(article[6]) + '</td>'
        html += '<td>'
        html += '<form action="/stu_users/delete" method="post"><input type="text" name="id" value="' \
                + str(article[1]) + '" hidden><input type="submit" value="删除"></form>'
        html += '</td>'
        html += '<td>'
        html += '<a href="/edit_student?id=' + str(article[1]) + '"><button type="button">修改</button></a>'
        html += '</td>'
        html += '</tr>'
        html += '</article>'

    return html


def generateStudsOptions(studs):
    html = ''
    for stud in studs:
        html += '<article>'
        html += '<tr>'
        html += '<td>' + stud[0] + '</td>'
        html += '<td>' + str(stud[1]) + '</td>'
        html += '<td>' + stud[2] + '</td>'
        html += '<td>' + str(stud[3]) + '</td>'
        html += '<td>' + stud[4] + '</td>'
        html += '<td>' + str(stud[5]) + '</td>'
        html += '<td>' + str(stud[6]) + '</td>'
        html += '</article>'

    return html


class Resquest(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        print(path)
        if path == '/stu_users':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            content = readFile('./宿舍管理系统/static/学生宿舍登记表.html')
            content = str(content, 'utf-8')

            stu_users = getStu_users()

            articles_html = generateList(stu_users)
            content = content.replace('{{articles}}', articles_html)

            self.wfile.write(content.encode('utf-8'))


        elif path == '/select':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            content = readFile('./宿舍管理系统/static/查询显示界面.html')
            content = str(content, 'utf-8')

            stu_users = getStu_users()

            studs_html = generateStudsOptions(stu_users)
            print(studs_html)
            content = content.replace('{{studs}}', studs_html)

            self.wfile.write(content.encode('utf-8'))

        elif path == '/ar_users':
            self.send_response(302)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            content = readFile('./宿舍管理系统/static/管理员登入界面.html')
            content = str(content, 'utf-8')

            # ar_users = getAr_users()
            # print(ar_users)

            self.wfile.write(content.encode('utf-8'))

        elif path == '/ar_users/create':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            content = readFile('./宿舍管理系统/static/管理员注册界面.html')
            content = str(content, 'utf-8')

            self.wfile.write(content.encode('utf-8'))

        elif path == '/success':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            content = readFile('./宿舍管理系统/static/注册成功.html')
            content = str(content, 'utf-8')

            self.wfile.write(content.encode('utf-8'))


        elif path[0:len('/edit_student')] == '/edit_student':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            content = readFile('./宿舍管理系统/static/数据修改表.html')
            content = str(content, 'utf-8')

            params = path.split("?")[1]
            student = getStudent(params)
            print(student)

            content = content.replace('{{sname}}', student[0])
            content = content.replace('{{id}}', student[1])
            content = content.replace('{{sex}}', student[2])
            content = content.replace('{{age}}', student[3])
            content = content.replace('{{zhuanye}}', student[4])
            content = content.replace('{{loudong}}', student[5])
            content = content.replace('{{fangjian}}', student[6])

            self.wfile.write(content.encode('utf-8'))

        else:
            print(path, 'in else')
            self.send_response(300)
            if path.endswith('.css'):
                self.send_header('Content-type', 'text/css')
            elif path.endswith('.jpg'):
                self.send_header('Content-type', 'image/jpeg')
            else:
                self.send_header('Content-type', 'text/html')

            self.end_headers()
            self.wfile.write(readFile('./宿舍管理系统' + path))

    def do_POST(self):
        path = self.path
        print(self.path)
        if path == '/stu_users':
            content_length = int(self.headers['Content-Length'])
            content = self.rfile.read(content_length)
            content = str(content, "utf-8")
            content = parse.parse_qs(content)

            storeStu_users(content)

            # Respond with 200 OK
            self.send_response(302)
            self.send_header('Location', '/stu_users')
            self.end_headers()

        elif path == '/success':
            content_length = int(self.headers['Content-Length'])
            content = self.rfile.read(content_length)
            content = str(content, "utf-8")
            content = parse.parse_qs(content)

            storeAr_users(content)

            # Respond with 200 OK
            self.send_response(302)
            self.send_header('Location', '/success')
            self.end_headers()

        elif path == '/stu_users/update':
            content_length = int(self.headers['Content-Length'])
            content = self.rfile.read(content_length)
            content = str(content, "utf-8")
            content = parse.parse_qs(content)

            print(content)
            upStudent(content)

            self.send_response(302)
            self.send_header('Location', '/stu_users')
            self.end_headers()

        elif path == '/stu_users/delete':
            content_length = int(self.headers['Content-Length'])
            content = self.rfile.read(content_length)
            content = str(content, "utf-8")
            content = parse.parse_qs(content)

            print(content)
            delStudent(content['id'][0])

            self.send_response(302)
            self.send_header('Location', '/stu_users')
            self.end_headers()


if __name__ == '__main__':
    host = ('localhost', 8888)
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: {0}:{1}".format(host[0], host[1]))
    server.serve_forever()
