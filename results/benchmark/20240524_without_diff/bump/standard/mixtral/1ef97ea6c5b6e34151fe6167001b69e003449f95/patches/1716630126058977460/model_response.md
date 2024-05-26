Here is the updated `between` method that resolves the error:

```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return new Timestamp(super.between(from, to).getTime()).toLocalDateTime().atZone(ZoneId.systemDefault()).toInstant().toEpochMilli();
}
```

This modification converts the `Date` objects to `LocalDateTime`, then to `ZonedDateTime`, and finally to `Instant`, before converting it back to `Timestamp`. This ensures that the type compatibility issue is resolved.