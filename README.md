# Tinder Clothes
=====================


## Tools
1. Python       3.8
2. Django       3.0.6
3. PostgresQL   10.8
4. DRF          3.11.1
# Tinder Clothes
=====================
##### Tinder the clothes is a platform for shared clothes and to interact with clothes of others users and uxchanges the clothes if two users match.

In this repository you can find the API and de backend code of this application, this API is thought as a CRUD logic for create, read, update and delete users, clothes and interactions, in this file you can see the diferents components and features of this API.  

## Index
##### 1. Tools --> Then you can see the differents tools  implemented in this project.
##### 2. Aplications and modules
##### 2.1. Users
##### 2.1.1. Users models
##### 2.1.2. Users views
##### 2.2. Clothes
##### 2.2.1. Clothes models
##### 2.2.2. Clothes views
##### 3. Integration and entry-points
##### 4. Docs
##### 5. Branches 


1. ## Tools
The next tools are implemented in the project each one with different purpouse and following good practices of development, this tools make up the diferents features of the API REST. 

- Python       3.8
- Django       3.0.6
- PostgresQL   10.8
- DRF          3.11.1

2. ## Aplications and Modules
Django is a framework of python that allow make a project based in applications with base in MTV model design, in this case you can find two principal applications, *users* and *clothes* in each application you can see the __models__ and __views__. In this section we explain the diferents features of this moduls.

### 2.1. Users
Users is the application to create, read, update and delete users if you need know why this function in this section you can see all about of this aplication, how it's based on django it countain the models module and views file.

#### 2.1.1. Users Model
Users model is an extension of User models from django, its a proxy model, the models module contain the profile and the users models, the first is an extension of the second. they works as follows:

- users: users is a proxy model based in the model of django thus it extends the *AbstractUser* of django models, but this is modified to recibe *phone number* instead of username, in the users.py you can see all abouth of this model.

- profile: It's a model that define de differents data fields about of the information of the user, this model is create to add or modify picture, city, state and reputation of the users, if you want create a proile you must send this paramethers as arguments or in the JSON format if you are consuming the API.

#### 2.1.2. Users views
Users views is a module that contain the logic of response to http petitions, the methods in this module return a response depending of the petition and http method. its module is accompanied by *serializers* module, in this module you can see the next actions methods:
- get_permissions
- login
- signup
- profile
Serializers module contain the validation data by create users.

### 2.2. Clothes
Clothes application contain *views* and *models* relationated with clothes, this application contain the logic to create, delete and update clothes, further contain the interactions module, in this module are the interactions models and view.

#### 2.2.1. Clothes Models
Clothes models contain a model based in the entity clothes and the atrubutes of this, in this module you find two files *clothes.py* and *interacions.py* that function of next form:
- clothes is a model based in the atributes of users clothes, this model have the nex atributes: (
    *owner_is=ForeingKey*, # This field is a foreing key of user model 
    *picture=ImageField*, 
    *description=TextField(max_length=500)*, 
    *size=CharField(choice)*, 
    *color=CharField*, 
    *category=CharField*, 
    *gender=CharField(choice)*, 
    *brand=CharField*, 
    *state=CharField(choice)*, 
    *public=BooleanField*, 
    *likes=PisitiveIntegerField*, 
    *dislikes=PositiveIntegerField*, 
    *super_likes=PositiveIntegerField*
    )

- Interactions is the model that contain all atributes of interaction entity, the fields of this model are: (
    *clothe=ForeignKey* # It field has foreing key clothes.ClotesModel
    *user=ForeingKey* foreing key is user.User
    *value=CharField(choice)* this value is like, superlike or dislike 
)

#### 2.2.2. Clothes views
In this views you can see the logic of the clothes interactions. Model vews of clothes is divide in three views, *clothes*, *users_clothes* and *interactions* they works as follows:

- clothes view: This view is complemented with interactions view, basics it's the view managers of return a response for each case, depending on user interaction, too is encarged of register the changes in the database, this does by interactions module.

- users_clothes: it's a view managers of creation of registers new clothes created by users, tis vew retrive the JSON with attributes of clothe and return a http response 201 if all is okey. 

#### Integrations and entry points
This API can be consumed taking into acount the nexts entry points:
- __Signup__: Retrive as paramenters *phone_number*, *first_name*, *last_name*, *password* and *password_confirmation*
- __Login__: Retrive as parameters *phone_number* and *password*, if all is okey return users data and profile, with a *token*.
- __create clothes__: *all atributes of clothe model*  
- __delete clothes__: *clothe:id_clothe* 
- __list user clothe__:*current_user*
- __update clothe__: *current_user, all atributes of clothe model*
- __match with a clothe__: *clothe:id_clothe, value:value*

#### Docs
I you want more information about of this project, you can visit this links.

Notion: https://www.notion.so/Backend-documentation-fae5f4c78df34ef9b2bf6b4bea31ccf6
Frontend Repository: https://github.com/ArzateCompany/finalProjectPlatziMaster
Backend Repository: https://github.com/marttcode/tclothes
