```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return new Timestamp(super.between((java.sql.Timestamp) from, (java.sql.Timestamp) to).getTime());
}
```