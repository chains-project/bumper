Here is a fixed version of the `between` method that should resolve the error:

```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return new Timestamp(super.between(from, to).getTime()).toInstant().truncatedTo(ChronoUnit.MILLIS).toEpochMilli();
}
```

In this version, we create a `Timestamp` object from the result of `super.between(from, to)` and then convert it to an `Instant` using the `toInstant()` method. We then truncate the `Instant` to the nearest millisecond using `truncatedTo(ChronoUnit.MILLIS)` and convert it back to an epoch millisecond value using `toEpochMilli()`. This should ensure that the resulting value is compatible with the `Timestamp` constructor.

Note that this solution assumes that the `Date` objects passed to the method are in the same time zone. If this is not the case, you may need to adjust the solution accordingly.