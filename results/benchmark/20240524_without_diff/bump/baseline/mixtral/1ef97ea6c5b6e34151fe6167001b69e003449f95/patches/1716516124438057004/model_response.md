Here's the proposed patch:

```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    java.sql.Timestamp sqlFrom = new Timestamp(from.getTime());
    java.sql.Timestamp sqlTo = new Timestamp(to.getTime());
    return new Timestamp(super.between(sqlFrom, sqlTo).getTime());
}
```

The changes made include creating new `java.sql.Timestamp` variables for the input `Date` objects, so that the new library method can be used. The original `Date` objects are then converted back to `Timestamp` objects for the return value.