```java
  @Override
  public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return super.between(new java.sql.Timestamp(from.getTime()), new java.sql.Timestamp(to.getTime()));
  }
```