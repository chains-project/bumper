```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    Timestamp tsFrom = new Timestamp(from.getTime());
    Timestamp tsTo = new Timestamp(to.getTime());
    return super.between(tsFrom, tsTo);
}
```