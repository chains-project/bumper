```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
  if (from instanceof Timestamp && to instanceof Timestamp) {
    return new Timestamp(super.between(from, to).getTime());
  } else {
    return new Timestamp(super.between(new Timestamp(from.getTime()), new Timestamp(to.getTime())).getTime());
  }
}
```