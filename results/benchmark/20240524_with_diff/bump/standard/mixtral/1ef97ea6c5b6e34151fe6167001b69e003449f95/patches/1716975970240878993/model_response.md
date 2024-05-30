Here is the proposed patch:

```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return new Timestamp(super.between(from, to).getTime());
}

private Timestamp adaptDateToTimestamp(Date date) {
    return new Timestamp(date.getTime());
}

@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return adaptDateToTimestamp(super.between(adaptDateToTimestamp(from), adaptDateToTimestamp(to)));
}
```

I created a helper method `adaptDateToTimestamp` to convert the `Date` objects returned by the superclass method `between` to `Timestamp` objects. This way, the return type of the overridden method matches the expected return type `Timestamp`.