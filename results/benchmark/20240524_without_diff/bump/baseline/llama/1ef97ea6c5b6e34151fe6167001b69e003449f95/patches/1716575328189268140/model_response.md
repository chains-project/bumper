```java
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    java.util.Date utilDate = super.between(from, to);
    java.sql.Date sqlDate = new java.sql.Date(utilDate.getTime());
    return new Timestamp(sqlDate.getTime());
}
```