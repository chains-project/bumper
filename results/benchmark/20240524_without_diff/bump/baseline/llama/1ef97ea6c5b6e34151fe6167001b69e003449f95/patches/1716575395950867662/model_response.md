```java
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    java.util.Date utilDate = super.between(from, to);
    return new Timestamp(utilDate.getTime());
}
```