```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
  java.sql.Timestamp fromTimestamp = new java.sql.Timestamp(from.getTime());
  java.sql.Timestamp toTimestamp = new java.sql.Timestamp(to.getTime());
  return super.between(fromTimestamp, toTimestamp);
}
```