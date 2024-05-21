Here is a fixed version of the failing method:

```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return new Timestamp(super.between(from, to).getTime());
}

// If the above code doesn't work, try the following:

@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return new Timestamp(new Date(super.between(from, to).getTime()).getTime());
}
```
The error message you provided indicates that the `between` method in the superclass now returns a `java.sql.Timestamp` instead of a `java.util.Date`. Therefore, you can simply keep the implementation of the method unchanged. However, if the first version doesn't work, you can try the second version which explicitly converts the result of `super.between` to a `java.util.Date` before getting its time in milliseconds.