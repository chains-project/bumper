```java
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    long time = super.between(from, to).getTime();
    return new Timestamp(time);
}
```