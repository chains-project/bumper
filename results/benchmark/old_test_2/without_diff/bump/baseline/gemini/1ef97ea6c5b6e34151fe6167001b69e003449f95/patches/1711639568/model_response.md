```java
  @Override
  public Timestamp between(Date from, Date to) {
    return new Timestamp(super.between(from, to).getTime() + Timestamp.TIMESTAMP_MAGIC_NANOS);
  }
```