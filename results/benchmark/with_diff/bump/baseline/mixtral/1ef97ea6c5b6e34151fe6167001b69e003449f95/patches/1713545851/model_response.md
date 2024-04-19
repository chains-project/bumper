Here's the updated method that should fix the error:

```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    java.sql.Timestamp sqlFrom = new Timestamp(from.getTime());
    java.sql.Timestamp sqlTo = new Timestamp(to.getTime());
    return new Timestamp(super.between(sqlFrom, sqlTo).getTime());
}
```

The changes I made are:

* Create two new variables `sqlFrom` and `sqlTo` of type `java.sql.Timestamp` and initialize them with the corresponding `Date` objects converted to `Timestamp`.
* Use the new `Timestamp` variables as arguments to the `between` method of the superclass.
* Return a new `Timestamp` object initialized with the result of the `between` method of the superclass converted back to `long` using its `getTime()` method.