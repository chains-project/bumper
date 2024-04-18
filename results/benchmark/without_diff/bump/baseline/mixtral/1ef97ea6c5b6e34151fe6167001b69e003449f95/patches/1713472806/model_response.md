Here's the fixed version of the `between` method:

```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    long time = super.between(from, to).getTime();
    return new Timestamp(time);
}
```

This fix ensures that the `getTime()` method from `Date` is used, which returns a `long` value representing the number of milliseconds since January 1, 1970, 00:00:00.000 GMT. The `Timestamp` constructor then uses this value to create a new `Timestamp` object.