```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return Timestamp.from(super.between(from, to).toInstant());
}
```