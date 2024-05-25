```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    if (from == null || to == null) {
        throw new IllegalArgumentException("Dates cannot be null");
    }
    return new Timestamp(from.getTime());
}
```