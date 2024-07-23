<h1 align="center"> odoo_db_extractor</h1>

In this project I created and maintained a pipeline extractor for ingesting data from the odoo api into the bronze tier of the data lake.


My folder architecture followed the Medallion Architecture Pattern:

![image](https://github.com/user-attachments/assets/469b3883-77e3-4ca4-aedd-f2696244cd9b)

<ul>
    <li>bronze: This layer is often referred to as the Raw Data Layer.</li>
    <li>Silver: This layer is known as the Cleansed or Structured Data Layer.</li>
    <li>Gold: This is the Business Level Aggregated Data Layer.</li>
</ul>

My extractor is made up of the following files:

![image](https://github.com/user-attachments/assets/5bcd74a0-bb75-446a-8857-cda752adf2cf)


Configuration files are used to set some important characteristics of the source tables and destination tables (we will use delta tables), such as:

<ul>
    <li>The increment range for each table</li>
    <li>The primary key of each table</li>
    <li>The source path and destination path for each table</li>
</ul>
