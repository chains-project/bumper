```java
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    java.util.Date d = super.between(from, to);
    return new Timestamp(d.getTime());
}
```