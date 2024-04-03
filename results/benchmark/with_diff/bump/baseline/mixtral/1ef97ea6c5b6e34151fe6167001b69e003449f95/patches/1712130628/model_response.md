Based on the error message and the library changes, it seems that the `super.between(from, to)` method now returns a `java.sql.Timestamp` instead of a `java.util.Date`. To fix the issue, you can simply remove the `new Timestamp` constructor call when creating the return value:

```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
  return super.between(from, to);
}
```

This should fix the incompatible types error.