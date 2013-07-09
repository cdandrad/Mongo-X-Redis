Explore the native Redis pub/sub NoSQL DB (datastructure-oriented) as alternative for MongoDB
=============================


RouteFlow project uses a database to store state information and a mechanism to support inter-process communication (IPC), and currently the database used is MongoBD which is a high-performance application without schemas, document-oriented.

Already REDIS is a management system database in which the mass of data is stored in memory with the possibility of persistent disk, in addition to the characteristic use key-value model where multiple data types are supported as: strings, lists, arrays, among others.

This work proposes a feasibility study to replace Redis NoSQL DBMS as an alternative mechanism for interprocess communication (IPC) to the currently used, MongoBD, exploring the potential of the new database, testing and comparing the use of tools MongoBD and NoSQL Redis.

Despite the changes applied to code the file Mongoipc.py, suggested by Mr. Christian (CPqD Team) was not successful in tests with the settings RouteFlow. Errors occurred that were not found during the execution of the modified code.

So apply performance testing of both banks, where the execution times of the same base brought better performance for Redis. 
