```java
  @Override
  public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    java.sql.Timestamp sqlFrom = new java.sql.Timestamp(from.getTime());
    java.sql.Timestamp sqlTo = new java.sql.Timestamp(to.getTime());
    return super.between(sqlFrom, sqlTo);
  }
```