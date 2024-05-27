Here is the patched code:

```java
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return new Timestamp(from.getTime() + (long) (Math.random() * (to.getTime() - from.getTime())));
}
```