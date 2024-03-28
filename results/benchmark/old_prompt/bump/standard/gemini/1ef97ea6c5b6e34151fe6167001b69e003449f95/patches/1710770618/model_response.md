```java
public Timestamp between(Timestamp from, Timestamp to) throws IllegalArgumentException {
        return new Timestamp(super.between(from, to).getTime());
    }
```