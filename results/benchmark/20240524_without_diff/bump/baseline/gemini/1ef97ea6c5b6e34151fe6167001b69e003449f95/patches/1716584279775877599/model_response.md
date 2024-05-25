```java
  @Override
  public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    if (from == null || to == null) {
      throw new IllegalArgumentException("From and to dates cannot be null");
    }
    long fromTime = from.getTime();
    long toTime = to.getTime();
    if (fromTime > toTime) {
      throw new IllegalArgumentException("From date cannot be after to date");
    }
    return new Timestamp(toTime - fromTime);
  }
```