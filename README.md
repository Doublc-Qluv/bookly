# Bookly API

一个基于 FastAPI 构建的现代化书籍管理 RESTful API 服务。

学习项目 [来源:jod35](https://github.com/jod35/fastapi-beyond-CRUD)
## 功能特性

- **用户认证**: 用户注册、邮箱验证、登录、密码重置
- **书籍管理**: 书籍的 CRUD 操作，支持用户关联
- **评论系统**: 为书籍添加评论和评分
- **标签系统**: 为书籍添加标签，支持多对多关系
- **JWT 认证**: 使用 JWT 进行身份验证，支持访问令牌和刷新令牌
- **异步任务**: 使用 Celery 处理异步邮件发送任务
- **缓存支持**: 使用 Redis 进行缓存和 JWT 黑名单管理

## 技术栈

- **语言**: Python 3.10+
- **框架**: FastAPI 0.135+
- **数据库**: PostgreSQL 14+
- **ORM**: SQLModel
- **缓存**: Redis 7+
- **任务队列**: Celery 5+
- **数据库迁移**: Alembic
- **认证**: JWT (PyJWT)
- **邮件服务**: FastAPI-Mail

## 项目结构
```
bookly/
├── src/                    # 源代码目录
│   ├── auth/               # 认证模块
│   │   ├── __init__.py
│   │   ├── dependencies.py # 依赖注入（JWT验证等）
│   │   ├── routes.py       # 认证路由
│   │   ├── schemas.py      # Pydantic 模型
│   │   ├── service.py      # 业务逻辑
│   │   └── utils.py        # 工具函数（密码哈希、JWT处理）
│   ├── books/              # 书籍模块
│   │   ├── __init__.py
│   │   ├── book_data.py    # 示例书籍数据
│   │   ├── models.py       # SQLModel 模型
│   │   ├── routes.py       # 书籍路由
│   │   ├── schemas.py      # Pydantic 模型
│   │   └── service.py      # 业务逻辑
│   ├── db/                 # 数据库模块
│   │   ├── __init__.py
│   │   ├── main.py         # 数据库连接配置
│   │   ├── models.py       # 全局 SQLModel 模型
│   │   └── redis.py        # Redis 连接配置
│   ├── reviews/            # 评论模块
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── schemas.py
│   │   └── service.py
│   ├── tags/               # 标签模块
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── schemas.py
│   │   └── service.py
│   ├── tests/              # 测试模块
│   │   ├── __init__.py
│   │   ├── conftest.py     # 测试配置
│   │   ├── test_auth.py    # 认证测试
│   │   └── test_book.py    # 书籍测试
│   ├── __init__.py         # 项目入口
│   ├── .env.example        # 环境变量示例
│   ├── celery_tasks.py     # Celery 任务定义
│   ├── config.py           # 配置管理
│   ├── errors.py           # 自定义异常
│   ├── mail.py             # 邮件服务配置
│   └── middleware.py       # 中间件
├── migrations/             # Alembic 数据库迁移
│   ├── versions/           # 迁移脚本
│   ├── README
│   ├── env.py
│   └── script.py.mako
├── alembic.ini            # Alembic 配置
├── install.sh             # 安装脚本
├── requirements.txt       # Python 依赖
└── README.md              # 项目说明
```



## 快速开始

### 环境要求

- Python 3.10+
- PostgreSQL 14+
- Redis 7+

### 安装步骤

1. **克隆项目**

```bash
git clone https://github.com/yourusername/bookly.git
cd bookly
```

2. **安装依赖**

```bash
pip install -r requirements.txt
```

3. **配置环境变量**

复制 `.env.example` 并修改配置：

```bash
cp src/.env.example src/.env
```

编辑 `src/.env` 文件：

```env
# 数据库配置
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/bookly_db

# JWT 配置
JWT_SECRET=your-secret-key-here
JWT_ALGORITHM=HS256

# Redis 配置
REDIS_URL=redis://localhost:6379/0

# 邮件配置
MAIL_USERNAME=your-email@example.com
MAIL_PASSWORD=your-email-password
MAIL_SERVER=smtp.example.com
MAIL_PORT=465
MAIL_FROM=your-email@example.com
MAIL_FROM_NAME=BooklyAdmin

# 域名配置
DOMAIN=http://localhost:8000
```

4. **数据库迁移**

```bash
cd src
alembic upgrade head
```

5. **启动服务**

```bash
# 启动 Redis（如果尚未运行）
redis-server

# 启动 Celery 工作器
celery -A celery_tasks worker --loglevel=info

# 启动 FastAPI 服务
uvicorn src:app --reload --host 0.0.0.0 --port 8000
```

### 访问 API 文档

启动服务后，访问以下地址查看 API 文档：

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API 端点

### 认证模块

| 端点 | 方法 | 描述 |
|------|------|------|
| `/api/v1/auth/signup` | POST | 用户注册 |
| `/api/v1/auth/login` | POST | 用户登录 |
| `/api/v1/auth/verify/{token}` | GET | 邮箱验证 |
| `/api/v1/auth/me` | GET | 获取当前用户 |
| `/api/v1/auth/logout` | GET | 用户登出 |
| `/api/v1/auth/refresh_token` | GET | 刷新访问令牌 |
| `/api/v1/auth/password-reset-request` | POST | 请求重置密码 |
| `/api/v1/auth/password-reset-confirm/{token}` | POST | 确认重置密码 |

### 书籍模块

| 端点 | 方法 | 描述 |
|------|------|------|
| `/api/v1/books/` | GET | 获取所有书籍 |
| `/api/v1/books/{book_uid}` | GET | 获取单本书籍 |
| `/api/v1/books/user/{user_uid}` | GET | 获取用户提交的书籍 |
| `/api/v1/books/` | POST | 创建书籍 |
| `/api/v1/books/{book_uid}` | PATCH | 更新书籍 |
| `/api/v1/books/{book_uid}` | DELETE | 删除书籍 |

### 评论模块

| 端点 | 方法 | 描述 |
|------|------|------|
| `/api/v1/reviews/` | GET | 获取所有评论 |
| `/api/v1/reviews/{review_uid}` | GET | 获取单个评论 |
| `/api/v1/reviews/book/{book_uid}` | GET | 获取书籍的评论 |
| `/api/v1/reviews/` | POST | 创建评论 |
| `/api/v1/reviews/{review_uid}` | PATCH | 更新评论 |
| `/api/v1/reviews/{review_uid}` | DELETE | 删除评论 |

### 标签模块

| 端点 | 方法 | 描述 |
|------|------|------|
| `/api/v1/tags/` | GET | 获取所有标签 |
| `/api/v1/tags/{tag_uid}` | GET | 获取单个标签 |
| `/api/v1/tags/` | POST | 创建标签 |
| `/api/v1/tags/{tag_uid}` | PATCH | 更新标签 |
| `/api/v1/tags/{tag_uid}` | DELETE | 删除标签 |

## 使用示例

### 注册用户

```bash
curl -X POST "http://localhost:8000/api/v1/auth/signup" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "email": "john@example.com",
    "password": "securepassword",
    "first_name": "John",
    "last_name": "Doe"
  }'
```

### 登录

```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "password": "securepassword"
  }'
```

### 创建书籍

```bash
curl -X POST "http://localhost:8000/api/v1/books/" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "publisher": "Scribner",
    "published_date": "1925-04-10",
    "page_count": 180,
    "language": "English"
  }'
```

## 测试

运行测试：

```bash
cd src
pytest tests/ -v
```

## 项目配置说明

### 配置文件

`src/config.py` 使用 Pydantic Settings 管理配置，自动从 `.env` 文件加载环境变量。

### 数据库模型

数据库模型定义在 `src/db/models.py`，包括：

- **User**: 用户模型
- **Book**: 书籍模型
- **Review**: 评论模型
- **Tag**: 标签模型
- **BookTag**: 书籍-标签关联表（多对多关系）

### 认证机制

- 使用 JWT (JSON Web Token) 进行无状态认证
- 访问令牌默认过期时间较短，刷新令牌过期时间较长
- Redis 用于存储 JWT 黑名单，实现登出功能

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！