Here's the proposed patch:

```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return new Timestamp(super.between(new Timestamp(from.getTime()), new Timestamp(to.getTime())).getTime());
}
```

This patch converts the `Date` objects to `Timestamp` before passing them to the `super.between` method, so that the return type is compatible with `java.sql.Timestamp`.