```java
  public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    long millis = super.between(from, to).getTime();
    return new Timestamp(millis);
  }
```