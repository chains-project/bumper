```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    Date date = super.between(from, to);
    return new Timestamp(date.getTime());
}
```