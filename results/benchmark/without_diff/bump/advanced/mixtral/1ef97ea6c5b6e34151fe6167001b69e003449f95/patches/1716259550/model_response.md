Here is the proposed patch:

```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return new Timestamp(super.between(from, to).getTime()).toInstant().atZone(ZoneId.systemDefault()).toLocalDateTime().atZone(ZoneId.systemDefault()).toInstant().toEpochMilli();
}
```

This patch converts the `Date` object returned by `super.between()` to a `LocalDateTime` object using the `atZone()` method, and then converts it back to an `Instant` object using `atZone()` method again. Finally, it converts the `Instant` object to an `epoch milli` value using `toEpochMilli()` method. This value is used to create a new `Timestamp` object.