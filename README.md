# newsly

To get started, simply run this command:

```
./run.sh
```

It will build all the docker contianers and run all the projects. From there, open your browser to: https://localhost:5173/ and you can login to newsly.

## Stopping the project

```
docker compose down 
```

## Seeding the project 

To load data run this command: 


```
./seed.sh
```

## MacOS

If you're running on Mac, open the docker desktop application. 
Press the gear icon in the upper right to enter settings. 
Navigate to the resources tab, then network, then check "Enable host networking"


Rerun ` ./run.sh `




