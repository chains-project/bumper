Here's the proposed patch:

```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    java.sql.Timestamp sqlFrom = new Timestamp(from.getTime());
    java.sql.Timestamp sqlTo = new Timestamp(to.getTime());
    return new Timestamp(super.between(sqlFrom, sqlTo).getTime());
}
```

This patch converts the `Date` objects to `Timestamp` objects before passing them to the superclass method, since the new version of the library requires `Timestamp` objects instead of `Date` objects.