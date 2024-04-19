```java
  @Override
  public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    Timestamp timestampFrom = new Timestamp(from.getTime());
    Timestamp timestampTo = new Timestamp(to.getTime());
    return super.between(timestampFrom, timestampTo);
  }
```