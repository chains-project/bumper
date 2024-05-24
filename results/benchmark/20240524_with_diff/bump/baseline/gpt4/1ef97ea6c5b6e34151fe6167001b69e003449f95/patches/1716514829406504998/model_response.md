```java
  @Override
  public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return super.between(new Timestamp(from.getTime()), new Timestamp(to.getTime()));
  }
```