```java
  public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    Date between = super.between(from, to);
    return between == null ? null : new Timestamp(between.getTime());
  }
```