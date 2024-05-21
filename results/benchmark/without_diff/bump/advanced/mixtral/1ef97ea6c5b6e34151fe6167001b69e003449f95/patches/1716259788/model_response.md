Here's the fixed version of the `between` method:

```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return new Timestamp(super.between(from, to).getTime()).toInstant().truncatedTo(ChronoUnit.MILLIS).toEpochMilli();
}
```

This version converts the `Date` object returned by `super.between` to an `Instant` and then back to a `Timestamp`, ensuring that the returned value is a `Timestamp`.