```java
  public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    if (from == null || to == null) {
      throw new IllegalArgumentException("From and to dates cannot be null");
    }
    if (from.after(to)) {
      throw new IllegalArgumentException("From date must be before or equal to to date");
    }
    long fromTime = from.getTime();
    long toTime = to.getTime();
    long difference = toTime - fromTime;
    long randomTime = fromTime + (long) (Math.random() * difference);
    return new Timestamp(randomTime);
  }
```