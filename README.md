# Todo Api Endpoint Project

- Basic CRUD operations
- Uses JWT authentication (Refresh & Access Token)
- Pep8 formatting & naming guidelines
- Django OWASP Guidelines followed
  - Scoped throttling on endpoints
  - Pagination on fetch to avoid DOS attacks
  - Avoid using certain methods for Django ORM
- Unit Testing for endpoints (Todo & Account) in tests.py

## Deployment

Deploy project using docker compose

- Download the docker-compose.yml file
- Download .env
- Put both of them in the same folder and run

```bash
  docker compose up
```

- Runs on http://0.0.0.0:8001/api/

## API Reference For Accounts

#### Register Account

```http
  POST /api/account/register
```

| Body       | Type     | Description                     |
| :--------- | :------- | :------------------------------ |
| `name`     | `string` | **Required** Your Name          |
| `email`    | `string` | **Required** Your Email Address |
| `password` | `string` | **Required** Your Password      |

#### Login Account

```http
  POST /api/account/login
```

| Body       | Type     | Description                     |
| :--------- | :------- | :------------------------------ |
| `email`    | `string` | **Required** Your Email Address |
| `password` | `string` | **Required** Your Password      |

#### Retrieve new Access Token from Refresh Token

```http
  POST /api/account/refresh
```

| Body      | Type     | Description                          |
| :-------- | :------- | :----------------------------------- |
| `refresh` | `string` | **Required** to get new access token |

## API Reference For Todos

| Authentication Header | Type     | Description                           |
| :-------------------- | :------- | :------------------------------------ |
| `access_token`        | `Bearer` | **Required** for every todos endpoint |

#### Create Todo

```http
  POST /api/todos/
```

| Body        | Type     | Description                         |
| :---------- | :------- | :---------------------------------- |
| `todo_text` | `string` | **Required** text of todo to create |

#### Fetch Todos All or with Pagination

```http
  Get /api/todos/
```

```http
  Get /api/todos?limit=5&offset=0
```

| Parameter | Type     | Description                                   |
| :-------- | :------- | :-------------------------------------------- |
| `limit`   | `number` | How many data objects you need to return      |
| `offset`  | `number` | data objects number offset you need to return |

#### Update Todos

```http
  PUT /api/todos/<int:todo_id>
```

| Parameter | Type  | Description                            |
| :-------- | :---- | :------------------------------------- |
| `todo_id` | `int` | **Required**. Id of the todo to update |

| Body           | Type      | Description                    |
| :------------- | :-------- | :----------------------------- |
| `todo_text`    | `text`    | **Required**. Text of the todo |
| `is_completed` | `Boolean` | **Required**. True or False    |

#### Delete Todo

```http
  DELETE /api/todos/<int:todo_id>
```

| Parameter | Type  | Description                            |
| :-------- | :---- | :------------------------------------- |
| `todo_id` | `int` | **Required**. Id of the todo to delete |
