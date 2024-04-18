```java
  public Timestamp between(java.sql.Date from, java.sql.Date to) throws IllegalArgumentException {
        return new Timestamp(super.between(from, to).getTime());
    }
```