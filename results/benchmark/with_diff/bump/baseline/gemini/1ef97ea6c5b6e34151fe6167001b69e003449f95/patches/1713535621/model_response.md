```java
  public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    if (from instanceof Timestamp && to instanceof Timestamp) {
      return new Timestamp(((Timestamp) from).getTime() - ((Timestamp) to).getTime());
    } else {
      throw new IllegalArgumentException("Both from and to must be Timestamps");
    }
  }
```