Here's the proposed patch:

```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return new Timestamp(super.between(from, to).toInstant().toEpochMilli());
}
```

The patch converts the `Date` object returned by `super.between()` to an `Instant` and then to an epoch milli value before creating the `Timestamp` object. This is necessary because the new version of the library returns a `Timestamp` object from the `between()` method instead of a `Date` object.