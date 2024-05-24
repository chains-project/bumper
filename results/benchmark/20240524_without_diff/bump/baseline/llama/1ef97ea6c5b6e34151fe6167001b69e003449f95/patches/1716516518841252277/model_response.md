```java
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    Timestamp fromTs = new Timestamp(from.getTime());
    Timestamp toTs = new Timestamp(to.getTime());
    return new Timestamp(super.between(fromTs, toTs).getTime());
}
```