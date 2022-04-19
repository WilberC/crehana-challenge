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

- I'm adding `.env` file as an example file that has to be modified
- you can run the server on local host by `uvicorn main:app --reload`