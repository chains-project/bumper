```java
  public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return new Timestamp(net.datafaker.DateAndTime.between(from, to).getTime());
  }
```