```java
  @Override
  public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    Timestamp sqlFrom = new Timestamp(from.getTime());
    Timestamp sqlTo = new Timestamp(to.getTime());
    return super.between(sqlFrom, sqlTo);
  }
```