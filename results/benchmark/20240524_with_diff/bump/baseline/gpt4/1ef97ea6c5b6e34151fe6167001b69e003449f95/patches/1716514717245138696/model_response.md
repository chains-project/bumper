```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    Timestamp fromTs = new Timestamp(from.getTime());
    Timestamp toTs = new Timestamp(to.getTime());
    return super.between(fromTs, toTs);
}
```