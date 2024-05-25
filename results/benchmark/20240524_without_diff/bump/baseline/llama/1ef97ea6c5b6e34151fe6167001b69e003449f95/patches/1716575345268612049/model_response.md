```java
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    java.util.Date date = super.between(from, to);
    return new Timestamp(date.getTime());
}
```