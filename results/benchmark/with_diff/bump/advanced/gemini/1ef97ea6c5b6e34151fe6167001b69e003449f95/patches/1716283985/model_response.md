```java
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return new Timestamp(super.between(from.getTime(), to.getTime()).getTime());
}
```