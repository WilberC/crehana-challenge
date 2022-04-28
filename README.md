# Crehana-Challenge

- Requirements:
  - Have postgresql installed locally
  - The project is developed on `python 3.10.1`
  

- Steps to start the project locally: 
  - To manage package versions better I install `pipenv`
```zsh
 python3 -m venv venv #  to create the virtualenv
 source venv/bin/activate # to activate the virtualenv
 pip install pipenv # to install the package manager
 pipenv install # to install all the necessary packages
```

![image](https://user-images.githubusercontent.com/27011395/164089387-6e9c992c-b588-46d1-8c3f-29be6fd70f5f.png)


- Rest endpoints:
```zsh
GET 	/posts
GET 	/posts/1
GET 	/posts/1/comments
GET 	/comments?postId=1
POST 	/posts
PUT 	/posts/1
PATCH 	/posts/1
DELETE 	/posts/1
```
- Graphql endpoint: 
```zsh
http://127.0.0.1:8000/graphql/ 
# query filter example
# in filters you can put any field you want to filter dinamically
{
  users(filters: {id:1}) {
    id,
    name,
    address{
      street
    }
  }
}
# mutation example
mutation {
  createUser(userData: {name: "aa", username: "aa_username", email: "aa_username"}) {
    user {
      name,
      username,
      email
    }
    ok
  }
}
```
# base graphql query
![image](https://user-images.githubusercontent.com/27011395/165715918-3e368185-37c2-4699-83d4-f99f228290f3.png)
# mutation 
![image](https://user-images.githubusercontent.com/27011395/165716084-4ca4986e-e39e-46c0-b716-760093de5a98.png)


- I'm adding `.env` file as an example file that has to be modified
- you can run the server on local host by `uvicorn main:app --reload`
- Optimal testing env should be made by -> faker, factory_boy, pytest and coverage, but for this case I will use only fastapi testing env
- to make testing more efficient we should put pre-commits and something like Github actions to validate tests pass in each PR