```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return new Timestamp(super.between(Timestamp.from(from.toInstant()), Timestamp.from(to.toInstant())).getTime());
}
```