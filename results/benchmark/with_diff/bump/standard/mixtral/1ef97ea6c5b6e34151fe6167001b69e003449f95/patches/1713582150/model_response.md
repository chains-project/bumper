Here's the proposed patch:

```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    java.sql.Timestamp sqlFrom = new Timestamp(from.getTime());
    java.sql.Timestamp sqlTo = new Timestamp(to.getTime());
    return new Timestamp(super.between(sqlFrom, sqlTo).getTime());
}
```

This patch converts the `Date` objects to `Timestamp` objects before passing them to the superclass's `between` method. This ensures that the method's return type is compatible with the required `Timestamp` return type.