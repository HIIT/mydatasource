# Data Source

This is a part of proof-of-concept implementation of [MyData Architecture](https://github.com/HIIT/mydata-stack). More information about the POC-implementation see [DataOperator](https://github.com/dhrproject/mydataoperator)

### Repository structure
```
.
├── DataSource
│   ├── app
│   │   ├── model                              data model
│   │   │   ├── __init__.py 
│   │   │   ├── contract.py                    service's contract template
│   │   │   ├── receipt.py                     consent receipt        
│   │   │   ├── resource_set.py                customization resource set
│   │   │   ├── data.py                        service data
│   │   │   ├── link_rs_data.py                linking resource set with data
│   │   │   ├── categories.py                  data classify
│   │   │   ├── label.py                       subset of category
│   │   │   ├── units.py                       unit for each label(subset of category)
│   │   │   ├── country.py                     country table
│   │   │   ├── region.py                      region tabel
│   │   │   ├── city.py                        city table
│   │   │   ├── user_info.py                   users' information
│   │   │   ├── user_account.py                users' account
│   │   │   ├── status.py                      status list
│   │   │   └── json_type.py                   customization type inherit SQLAlchemy
│   │   ├── handler                            
│   │   │   ├── __init__.py 
│   │   │   ├── error_handler.py               customized error handler
│   │   │   └── dhHelper.py                    database handler
│   │   ├── views                              API Views
│   │   │   ├── __init__.py 
│   │   │   ├── user.py                        register, login, users' profile
│   │   │   ├── contract.py                    contract template endpoint 
│   │   │   ├── receipt.py                     consent receipt
│   │   │   ├── resource_set.py                resource set
│   │   │   ├── resource.py                    resource endpoint for sink
│   │   │   ├── category.py                    
│   │   │   ├── label.py                       
│   │   │   ├── units.py                       
│   │   │   ├── data.py                        
│   │   │   └── service.py                     service status
│   │   ├── __init__.py                        
│   │   ├── auth.py                            token decorators 
│   │   └── config.py                          app configuration
│   ├── dhr_logging                            logging module
│   │   ├── __init__.py 
│   │   ├── datetime.py
│   │   ├── formatter.py
│   │   ├── handler.py
│   │   ├── logger.py
│   │   └── setting.py
│   ├── logs                                   logging folder
│   ├── data                                   dataset sample
│   ├── create_db.sh                           script for creating database
│   ├── init.sh                                script to execute read_conf.py and init_data.py           
│   ├── read_conf.py                           read remote config
│   ├── init_data                              init service's data 
│   ├── requirements.txt                       requirements for running this server
│   └── run.py                                 app entry point
└── doc                                        API documentation
```
### Documentation
API Documentation can be found under /doc/swagger.yaml which follow standard Swagger Specification 2.0

### More information
- [MyData Architecture](https://github.com/HIIT/mydata-stack)
- [DataOperator](https://github.com/dhrproject/mydataoperator)

### Copying and License

This code is licensed under MIT
