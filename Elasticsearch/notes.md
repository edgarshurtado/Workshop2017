# Elasticsearch

In a nutshell is a NoSQL database as a service


## Basic operations

* `GET /_cat/health?v`
* `GET /_cat/nodes?v`
* `GET /_cat/indices?v`

> Tags meaning:
* Green: All good
* Yellow: Some replica isn't allocated yet (it can be due to not
enough nodes in the cluster)
* Red: Data is missing (Fix ASAP)

* `PUT /customer?pretty` : add the *customer* index
> `pretty` just means that indicates elasticsearch to format the result

## CRUD operations
* `PUT /customer/external/1?pretty`
```js
{"name":"John Doe"}
```
Creates the customer index (if it wasn't already) and add a document of type
external in it with index 1. The document info is sent as the put payload

* `GET /customer/external/1?pretty`

The result will come as follows:


```js
{
  "_index" : "customer",
  "_type" : "external",
  "_id" : "1",
  "_version" : 1,
  "found" : true,
  "_source" : { "name": "John Doe" }
}
```

* `DELETE /customer?pretty`

Deletes the index

The REST patern to call Elasticsearch:

*<REST Verb> /<Index>/<Type>/<ID>*

* `POST /customer/external?v`

To add a document without specifying the ID

Some updating request

```
POST /customer/external/1/_update?pretty
{
  "doc": { "name": "Jane Doe" }
}
```

```
POST /customer/external/1/_update?pretty
{
  "doc": { "name": "Jane Doe", "age": 20 }
}
```

```
POST /customer/external/1/_update?pretty
{
  "script" : "ctx._source.age += 5"
}
```
In the above example, `ctx._source` refers to the current source document that is about to be updated.

There's no way to update several documents as a SQL would do. They have to be updated one by one.

```
DELETE /customer/external/2?pretty
```
> Note: It's posible to delete documents that match a query, however for deleting 
all documents in an index, is more efficient to remove the index instead.

## Batch processing
Multi-insert

```
POST /customer/external/_bulk?pretty
{"index":{"_id":"1"}}
{"name": "John Doe" }
{"index":{"_id":"2"}}
{"name": "Jane Doe" }
 ```

 Multi-operation
 ```
POST /customer/external/_bulk?pretty
{"update":{"_id":"1"}}
{"doc": { "name": "John Doe becomes Jane Doe" } }
{"delete":{"_id":"2"}}
 ```

### Multi-insert from a file
`curl -XPOST 'http://madwhaledev:8888/cem_cepsa/encuesta/_bulk?pretty' --data-binary "@encuesta3.json"`

The file format has to match the bulk operation format for the request body. See above.


