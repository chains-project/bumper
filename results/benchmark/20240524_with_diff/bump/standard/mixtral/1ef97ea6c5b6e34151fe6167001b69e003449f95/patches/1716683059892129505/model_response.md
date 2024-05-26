Here's a patch that you can apply to fix the error:

```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    java.sql.Timestamp sqlFrom = new Timestamp(from.getTime());
    java.sql.Timestamp sqlTo = new Timestamp(to.getTime());
    return super.between(sqlFrom, sqlTo);
}
```

This patch converts the `Date` arguments to `Timestamp` and uses the new `between` method in the superclass that takes `Timestamp` arguments.