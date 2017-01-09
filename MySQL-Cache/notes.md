# For knowing if the cache is enabled

1. Run `mysql> show variables like 'have_query_cache'`

The return has to be:

```
+------------------+-------+
| Variable_name    | Value |
+------------------+-------+
| have_query_cache | YES   |
+------------------+-------+
```

2. Run `mysql> show variables like 'query_cache'`

The return will be:

```
+------------------------------+---------+
| Variable_name                | Value   |
+------------------------------+---------+
| query_alloc_block_size       | 8192    |
| query_cache_limit            | 1048576 |
| query_cache_min_res_unit     | 4096    |
| query_cache_size             | 8388608 |
| query_cache_type             | ON      |
| query_cache_wlock_invalidate | OFF     |
| query_prealloc_size          | 8192    |
+------------------------------+---------+
```
For the cache being enabled is needed:
	- *query_cache_size* > 0
	- *query_cache_type* = ON
	- *query_cache_limit* > 0

# How does the MySQL cache work?

It stores the result of queries with a result bigger than *query_cache_min_res_unit* (the units are bytes).

Every time there's a modification of the data invloved in the cached queries, there's a flush of the cache to get the new values.
This makes that caching MySQL is only efficient if the writes are not done too often.


# MySQL caching recomendations

For the previous reason, is it not recomended big query cache sizes. Because as bigger the cache size the most the db spends flushing
and locking. 

Good cache sizes would be *[between 100 and 200 mb](https://haydenjames.io/mysql-query-cache-size-performance/)* top.


## What's locking?

According to [MySQL manual glosary about locking](http://dev.mysql.com/doc/refman/5.7/en/glossary.html#glos_locking):

> The system of protecting a transaction from seeing or changing data that is being queried or changed by other transactions.
The locking strategy must balance reliability and consistency of database operations (the principles of the ACID philosophy)
against the performance needed for good concurrency. Fine-tuning the locking strategy often involves choosing an isolation
level and ensuring all your database operations are safe and reliable for that isolation level.

I fund a further explanation on a [blog post](https://www.percona.com/blog/2012/09/05/write-contentions-on-the-query-cache/).

> The answer is in the way the query cache works. Simply stated, the server wants to lock
the query cache both when checking if a result is in the cache and when writing a result 
set into the cache. When writing, locking can occur several times: the server sends results
to the cache before computing the entire result set (so the total size of the result set is
not known), so the cache has to assign memory block by block. If a block is full and the 
server keeps sending rows, a new block must be assigned, requiring the cache to be locked!

Aditionally on the [MySQL documentation about query-cache-tread-states](https://dev.mysql.com/doc/refman/5.5/en/query-cache-thread-states.html):

> * Waiting for query cache lock
This state occurs while a session is waiting to take the query cache lock. This can happen for any statement that needs to perform some query cache operation, such as an INSERT or DELETE that invalidates the query cache, a SELECT that looks for a cached entry, RESET QUERY CACHE, and so forth.  

# Interest resources

* [Speed Up Your Web Site With MySQL Query Caching](http://www.howtogeek.com/howto/programming/speed-up-your-web-site-with-mysql-query-caching/)
* [Avoid This When Tuning MySQL Query Cache for Performance](https://haydenjames.io/mysql-query-cache-size-performance/)

