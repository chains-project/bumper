```java
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return new Timestamp(super.between(new Timestamp(from.getTime()), new Timestamp(to.getTime())).getTime());
}
```