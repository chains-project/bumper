Here's the proposed patch to fix the error:

```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return new Timestamp(super.between(from, to).getTime());
}

private Timestamp adaptDateToTimestamp(Date date) {
    return date != null ? new Timestamp(date.getTime()) : null;
}

@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return adaptDateToTimestamp(super.between(adaptDateToTimestamp(from), adaptDateToTimestamp(to)));
}
```

The `adaptDateToTimestamp` method converts a `Date` object to a `Timestamp` object, which is now required by the updated library. This method is used in the overridden `between` method to ensure that the input `Date` objects are converted to `Timestamp` objects before being passed to the superclass method.