### The difference between Exasol and Postgres
| Databases      | Pros        |Cons        | 
| -----------    | ----------- |----------- |
| Exasol         |<ul><li>Exasol to be very fast at summarizing large data sets. It is great backend for both reporting tools and data analytics/business intelligence. Combined with the fact that data import is also very fast it makes it ideal for a real-time ELT architecture.</li><br><li>Exasol is low maintenance. No indexes to maintain (The database auto-manages them) and very little tuning is required.</li><br><li>Query processing is optimized for high throughput and high parallelization. This means that even under high loads performance degrades gracefully as opposed to having "pile-ups" and "meltdowns". This has made it a very reliable database for us.</li></ul>|<li>Exasol doesn't have some of the advanced enterprise-y features found in some other large corporate database systems (e.g. native row-level and column-level security). However it's pretty customizable (SQL pre-processing, virtual schemas, powerful user-defined-function frameworks) so many of these features can be implemented manually.</li>|
|Postgres        |<UL><LI>It works well with external data sources and<BR> runs on platforms with stable performance.</LI><BR><LI>Clients can rest assured that their personal information will be safe and secure.</LI><br><LI> Many forums discuss setup and usage, and most are free.</LI><br><li>Adding tooling applications to a computer is unlimited.</li><br><li>PostgreSQL runs on many OS platforms and supports ANSI SQL, stored procedures, and triggers.</li></UL>|<li>Increasing horizontal scaling is complex, but PostgreSQL may have a solution for all replicas to accept operations.</li><br></br><li>No column re-ordering and better data compression are required.</li><br></br><li>PostgreSQL is often criticized for being slow and unsuitable for large-scale enterprise applications.</li>| 




### The differences  between stage and datawarehouse area

> The data-staging
> area is a work site. Tables are added, dropped, or modified by the ETL
> team without notifying the user community. This concept does not
> mean that the area is a free-for-all with tables being added, dropped,
> and modified by programmers at will. However, it does mean that
> the area is intended to be a workbench, not a display case.
>
> The data warehouse area is the process of collecting and managing data 
> from varied source and make it easier for end-users to understand and 
> visualize. Data warehouse is Non-volatile, which means Once data is merged there, it will not change.
> A data warehouse is optimized to store large volumes of historical data and enables fast and complex querying of that data. 



### The differences between development and production
- development area: 
Work or testplace. It's an environment where you develop, drop/delete and change your data without risks. 

- production:
Once you are done in the development area, you load or transfer the data to the production area, where they can be used to solve real work issues. 
This means you shouldn't make change there anymore. You have to be really careful. Because any mistakes done there can have severe consequences. 
