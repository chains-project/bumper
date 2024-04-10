```java
  public Timestamp between(Date from, Date to) throws IllegalArgumentException {
        return new Timestamp(super.between((Timestamp) from, (Timestamp) to).getTime());
    }
```