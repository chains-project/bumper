Here's a fixed version of the `between` method that resolves the error:

```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return new Timestamp(super.between(from, to).getTime()).toInstant().truncatedTo(ChronoUnit.MILLIS).toEpochMilli();
}
```

This version of the method converts the `Date` objects returned by `super.between` to `Timestamp` objects and then converts them to `Instant` objects. By truncating the `Instant` to milliseconds and then converting it back to an epoch milli, we ensure that we have a `Timestamp` object with the same value as the `Date` objects.