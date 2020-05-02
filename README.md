# KyuKey Lock
Webapp to access, monitor and control KyuKey lock.<br>
https://github.com/subodhk01/kyukey<br>
And other Private repos

# Auth APIs
`BASE_URL = "kyukey-lock.herokuapp.com"`
### Login
`POST BASE_URL/api/auth/login`
Required fields : `username` and `password`
### Register
`POST BASE_URL/api/auth/signup`
Required fields : `username`, `email`, `password1` and `password2`
### Delete
`DELETE BASE_URL/api/user/delete`
Requires Auth Header :
```
{
  Authorization: "Token " + USER_TOKEN 
}
```
where USER_TOKEN is the auth token of user.
