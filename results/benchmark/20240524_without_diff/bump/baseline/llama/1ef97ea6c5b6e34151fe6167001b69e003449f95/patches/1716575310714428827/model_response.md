```java
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    java.util.Date utilDate = super.between(from, to);
    java.sql.Timestamp sqlTimestamp = new java.sql.Timestamp(utilDate.getTime());
    return sqlTimestamp;
}
```