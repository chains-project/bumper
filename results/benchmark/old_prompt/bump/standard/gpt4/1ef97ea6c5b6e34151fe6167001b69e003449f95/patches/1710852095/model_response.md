```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    Date result = super.between(from, to);
    return new Timestamp(result.getTime());
}
```