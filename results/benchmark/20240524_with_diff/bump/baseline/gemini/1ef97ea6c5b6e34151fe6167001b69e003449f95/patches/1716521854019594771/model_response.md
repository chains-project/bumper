```java
  public Timestamp between(Date from, Date to) {
    if (from instanceof Timestamp && to instanceof Timestamp) {
      return new Timestamp(((Timestamp) from).getTime() - ((Timestamp) to).getTime());
    } else {
      throw new IllegalArgumentException("Both arguments must be Timestamps");
    }
  }
```