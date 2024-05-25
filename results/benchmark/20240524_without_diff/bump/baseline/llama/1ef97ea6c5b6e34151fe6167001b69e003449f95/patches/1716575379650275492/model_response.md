```java
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    java.util.Date superResult = super.between(from, to);
    return new Timestamp(superResult.getTime());
}
```