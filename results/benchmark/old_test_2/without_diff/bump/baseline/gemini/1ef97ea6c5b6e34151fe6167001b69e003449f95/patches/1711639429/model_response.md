```java
  @Override
  public Timestamp between(Date from, Date to) {
    return new Timestamp(between(from, to).getTime());
  }
```