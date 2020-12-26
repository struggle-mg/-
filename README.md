实训项目：学生宿舍管理信息系统

完成时间：2019.12.11
第一次修改：2020.12.24

功能描述
经过调研及分析，宿舍管理信息系统主要完成以下功能：
（1）管理员管理：提供信息的查询、修改、增加、删除，密码修改、登录管理功能，管理员对该系统用户的管理。
（2）宿舍管理：提供楼号，房间号等功能
（3）学生资料管理：提供学生基本档案，可按照姓名、年龄、性别、学号、专业、楼号、房间号统计学生信息。


第五 逻辑模型设计和优化
根据系统的总体概念设计模型、E-R图向关系模式的转化规则和数据库的范式理论，得到系统优化后的逻辑模型。
1.学生表
表名:stu-user	说明：学生信息表
字段名	类型	大小	主键	空值	缺省	描述
sname	varchar	10				学生名
id	char	15	Y			学生id
sex	char	10				学生性别
age	char	3				学生年龄
zhuanye	varchar	25				学生专业
loudong	char	3				学生楼栋
fangjian	char	4				学生房间

2.管理员表
表名：ar-user	说明：管理员信息表
字段名	类型	大小	主键	空值	缺省	描述
aname	varcahr	30		Y		管理员名
asex	char	10		Y		管理员性别
aage	char	3		Y		管理员年龄
aID	int	15	Y			管理员id
password	varchar	20				管理员密码
contact	char	12		Y		管理员联系方式


物理设计和实施
得到系统逻辑模型后，就该进行数据库的物理设计和实施数据库了，物理设计主要是要确定数据库的存储路径、存储结构以及如何建立索引等，可以采用系统的默认设置。数据库实施主要包括在具体的DBMS中创建数据库和表的过程，本设计所选用的DBMS为SQL SERVER2008，有关创建数据库和关系表的SQL语句如下所示：
1.创建数据库
/*==============================================================*/
/* DataBase: 班主任管理, 创建数据库，数据库名称为班主任管理
*/create database bzrsys;

2. 创建表
(1) 管理员表
DROP TABLE IF EXISTS `ar-user`;
CREATE TABLE `ar-user` (
  `aname` varchar(30),
  `asex` char(10),
  `aage` char(3) ,
  `aID` int(15) NOT NULL ,
  `password` varchar(20) NOT NULL ,
  `contact` char(12) ,
  PRIMARY KEY (`aID`)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8 ;

（2） 学生表
DROP TABLE IF EXISTS `stu-user`;
CREATE TABLE `stu-user` (
  `sname` varchar(10),
  `id` char(15) NOT NULL,
  `sex` char(10) ,
  `age` char(3) ,
  `zhuanye` varchar(25) ,
  `loudong` char(3),
  `fangjian` char(4),
  PRIMARY KEY (`id`)
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8; 



