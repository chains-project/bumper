Here's the fixed version of the `between` method:

```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return new Timestamp(super.between(from, to).getTime()).toInstant().truncatedTo(ChronoUnit.MILLIS).toEpochMilli();
}
```

This version converts the `Date` to a `Timestamp`, then gets the timestamp value from the `Timestamp`, and converts it back to a `Timestamp` using the `Timestamp(long time)` constructor. This way, the returned `Timestamp` object has the same time value as the original `Date` objects.

Note that the `toInstant().truncatedTo(ChronoUnit.MILLIS).toEpochMilli()` part is used to ensure that the resulting `Timestamp` has the same precision as the original `Date` objects. This is necessary because the `Timestamp` constructor may round the input value to the nearest microsecond.