```java
  public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    if (from == null || to == null) {
      throw new IllegalArgumentException("Both from and to dates must be non-null.");
    }
    return new Timestamp(from.getTime());
  }
```