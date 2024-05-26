Here is the updated `between` method that should fix the error:

```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return new Timestamp(super.between(from, to).getTime()).toLocalDateTime().atZone(ZoneId.systemDefault()).toInstant().toEpochMilli();
}
```

This updated implementation converts the `Date` objects to `LocalDateTime`, then to `ZonedDateTime`, and finally to `Instant` before converting it back to `Timestamp`. This should ensure that the types are compatible.