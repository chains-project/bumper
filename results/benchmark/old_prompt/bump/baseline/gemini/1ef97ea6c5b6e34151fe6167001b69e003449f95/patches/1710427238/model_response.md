```java
  public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    Date between = super.between(from, to);
    if (between != null) {
      return new Timestamp(between.getTime());
    } else {
      return null;
    }
  }
```