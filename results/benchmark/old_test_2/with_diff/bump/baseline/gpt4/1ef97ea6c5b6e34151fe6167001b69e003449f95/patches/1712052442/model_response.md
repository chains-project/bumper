```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
  Timestamp fromTimestamp = new Timestamp(from.getTime());
  Timestamp toTimestamp = new Timestamp(to.getTime());
  return super.between(fromTimestamp, toTimestamp);
}
```