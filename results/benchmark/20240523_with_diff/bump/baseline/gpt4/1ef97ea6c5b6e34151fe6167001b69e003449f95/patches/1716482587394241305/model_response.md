```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return new Timestamp(from.getTime() + (to.getTime() - from.getTime())/2);
}
```